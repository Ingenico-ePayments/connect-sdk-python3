import time
import uuid
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, Timeout

from ingenico.connect.sdk.communication_exception import CommunicationException
from ingenico.connect.sdk.endpoint_configuration import EndpointConfiguration
from ingenico.connect.sdk.log.request_log_message import RequestLogMessage
from ingenico.connect.sdk.log.response_log_message import ResponseLogMessage
from ingenico.connect.sdk.pooled_connection import PooledConnection
from ingenico.connect.sdk.response import Response

CHARSET = "UTF-8"


class DefaultConnection(PooledConnection):
    """Provides an HTTP request interface, threadsafe

    :param connect_timeout: timeout in seconds before a pending connection is dropped
    :param socket_timeout: timeout in seconds before dropping an established connection
            This is the time the server is allowed for a response
    :param max_connections: the maximum number of connections in the connection pool
    :param proxy_configuration: ProxyConfiguration object that contains data about proxy settings if present.
            It should be writeable as string and have a scheme attribute.

    Use the methods get, delete, post and put to perform the corresponding HTTP request.
    Alternatively you can use request with the request method as the first parameter

    URI, headers and body should be given on a per-request basis
    """

    def __init__(self, connect_timeout,
                 socket_timeout,
                 max_connections=EndpointConfiguration.DEFAULT_MAX_CONNECTIONS,
                 proxy_configuration=None):
        self.logger = None
        self.__requests_session = requests.session()
        self.__requests_session.mount("http://", HTTPAdapter(
            pool_maxsize=max_connections, pool_connections=1))
        self.__requests_session.mount("https://", HTTPAdapter(
            pool_maxsize=max_connections, pool_connections=1))
        # request timeouts are in seconds
        self.__connect_timeout = connect_timeout if connect_timeout >= 0 else None
        self.__socket_timeout = socket_timeout if socket_timeout >= 0 else None
        if proxy_configuration:
            proxy = {"http": str(proxy_configuration),
                     "https": str(proxy_configuration)}
            self.__requests_session.proxies = proxy

    @property
    def connect_timeout(self):
        """Connection timeout in seconds"""
        return self.__connect_timeout

    @property
    def socket_timeout(self):
        """Socket timeout in seconds"""
        return self.__socket_timeout

    def get(self, url, request_headers):
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a list containing RequestHeader objects
         representing the request headers
        """
        return self._request('get', url, request_headers)

    def delete(self, url, request_headers):
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a list containing RequestHeader objects
         representing the request headers
        """
        return self._request('delete', url, request_headers)

    def post(self, url, request_headers, body):
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a list containing RequestHeader objects
         representing the request headers
        :param body: the request body
        """
        return self._request('post', url, request_headers, body)

    def put(self, url, request_headers, body):
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param request_headers: a list containing RequestHeader objects
         representing the request headers
        :param body: the request body
        """
        return self._request('put', url, request_headers, body)

    def _request(self, method, url, headers, body=None):
        """Perform a request to the server given by url

        :param url: the url to the server, given as a parsed url
        :param headers: a list containing RequestHeader objects representing
         the request headers
        :param body: the request body
        """
        headers = {} if not headers else headers
        if not isinstance(url, str):
            url = url.geturl()

        # convert the list of RequestParam objects to a dictionary of key:value pairs if neccecary
        if headers and not isinstance(headers, dict):
            headers = {param.name: param.value for param in headers}

        # send request with all parameters not declared in session and with callback for logging response
        request = requests.Request(method, url, headers=headers, data=body,
                                   hooks={'response': self._log_response})
        prepped_request = self.__requests_session.prepare_request(request)
        prepped_request.timestamp = time.clock()  # add timestamp to request for later reference
        _id = str(uuid.uuid4())
        prepped_request.id = _id  # store random id in request so it can be matched with its response in logging
        self._log_request(prepped_request)
        try:
            requests_response = self.__requests_session.send(prepped_request,
                                                             timeout=(
                                                                 self.__connect_timeout,
                                                                 self.__socket_timeout))
        except Timeout as timeout:
            self._log_error(prepped_request.id, timeout,
                            prepped_request.timestamp)
            raise CommunicationException(timeout)
        except RequestException as exception:
            self._log_error(prepped_request.id, exception,
                            prepped_request.timestamp)
            raise CommunicationException(exception)
        except RuntimeError as exception:
            self._log_error(prepped_request.id, exception,
                            prepped_request.timestamp)
            raise

        # Read body in as text, if it is json it will be unmarshalled later
        ingenico_response = Response(body=requests_response.text,
                                     headers=requests_response.headers,
                                     status_code=requests_response.status_code)
        return ingenico_response

    def _log_request(self, request):
        """Log parameter request if logging is enabled at the moment of logging.
        Also adds a timestamp to the request for response logging"""
        logger = self.logger
        if logger is None:
            return
        method = request.method
        url = urlparse(request.url)
        if len(url.query):
            localpath = url.path + "?" + url.query
        else:
            localpath = url.path
        try:
            message = RequestLogMessage(request_id=request.id, method=method,
                                        uri=localpath)
            for name in request.headers:
                message.add_header(name, request.headers[name])
            body = request.body
            if body:
                content = request.headers['Content-Type']
                if content != "application/json":
                    message.set_body(body, content, CHARSET)
                else:
                    message.set_body(body, content)
            logger.log_request(message)
        except Exception as e:
            logger.log("An error occurred trying to log request '{}'".format(
                request.id), e)

    def _log_response(self, response, **kwargs):
        """Log parameter response if logging is enabled at the moment of logging"""
        logger = self.logger
        if logger is None:
            return
        request = response.request
        _id = request.id
        duration = time.clock() - request.timestamp
        status_code = response.status_code
        try:
            message = ResponseLogMessage(request_id=_id,
                                         status_code=status_code,
                                         duration=duration)
            for name in response.headers:
                message.add_header(name, response.headers[name])
            body = response.text
            if body:
                content = response.headers['Content-Type']
                # if content != "application/json":
                #     message.set_body(body, content, CHARSET)
                # else:
                message.set_body(body, content)
            logger.log_response(message)
        except Exception as e:
            logger.log(
                "An error occurred trying to log response '{}'".format(_id), e)

    def _log_error(self, request_id, error, start_time):
        """Log communication errors when logging is enabled"""
        logger = self.logger
        if logger:
            end_time = time.clock()
            duration = end_time - start_time
            logger.log(
                "Error occurred for outgoing request (requestId='{}', {} s)".format(
                    request_id, duration), error)

    def enable_logging(self, communicator_logger):
        self.logger = communicator_logger

    def disable_logging(self):
        self.logger = None

    def close_idle_connections(self, idle_time):
        """
        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        pass

    def close_expired_connections(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.__requests_session.close()
