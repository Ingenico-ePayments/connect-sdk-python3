from datetime import datetime
from urllib.parse import quote
from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

from .communication_exception import CommunicationException
from ingenico.connect.sdk.log.logging_capable import LoggingCapable
from .not_found_exception import NotFoundException
from .pooled_connection import PooledConnection
from .request_header import RequestHeader
from .response_exception import ResponseException


class Communicator(LoggingCapable):
    """
    Used to communicate with the GlobalCollect platform web services.

    It contains all the logic to transform a request object to a HTTP request
    and a HTTP response to a response object.
    """

    def __init__(self, session, marshaller):
        if session is None:
            raise ValueError("session is required")
        if marshaller is None:
            raise ValueError("marshaller is required")
        self.__session = session
        self.__marshaller = marshaller

    def close(self):
        """
        Releases any system resources associated with this object.
        """
        self.__session.connection.close()

    def get(self, relative_path, request_headers, request_parameters,
            response_type, context):
        """
        Corresponds to the HTTP GET method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating
         with the GlobalCollect platform
        :raise: ResponseException when an error response was received from the
         GlobalCollect platform
        :raise: ApiException when an error response was received from the
         GlobalCollect platform which contained a list of errors
        """
        connection = self.__session.connection
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("GET", uri, request_headers, context)
        response = connection.get(uri, request_headers)
        return self._process_response(response, response_type, relative_path,
                                      context)

    def delete(self, relative_path, request_headers, request_parameters,
               response_type, context):
        """
        Corresponds to the HTTP DELETE method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating
         with the GlobalCollect platform
        :raise: ResponseException when an error response was received from the
         GlobalCollect platform
        :raise: ApiException when an error response was received from the
         GlobalCollect platform which contained a list of errors
        """
        connection = self.__session.connection
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        self._add_generic_headers("DELETE", uri, request_headers, context)
        response = connection.delete(uri, request_headers)
        return self._process_response(response, response_type, relative_path,
                                      context)

    def post(self, relative_path, request_headers, request_parameters,
             request_body, response_type, context):
        """
        Corresponds to the HTTP POST method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating
         with the GlobalCollect platform
        :raise: ResponseException when an error response was received from the
         GlobalCollect platform
        :raise: ApiException when an error response was received from the
         GlobalCollect platform which contained a list of errors
        """
        connection = self.__session.connection
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        request_json = None
        if request_body is not None:
            request_headers.append(
                RequestHeader("Content-Type", "application/json"))
            request_json = self.__marshaller.marshal(request_body)
        self._add_generic_headers("POST", uri, request_headers, context)
        response = connection.post(uri, request_headers, request_json)
        return self._process_response(response, response_type, relative_path,
                                      context)

    def put(self, relative_path, request_headers, request_parameters,
            request_body, response_type, context):
        """
        Corresponds to the HTTP PUT method.

        :param relative_path: The path to call, relative to the base URI.
        :param request_headers: An optional list of request headers.
        :param request_parameters: An optional set of request parameters.
        :param request_body: The optional request body to send.
        :param response_type: The type of response to return.
        :param context: The optional call context to use.
        :raise: CommunicationException when an exception occurred communicating
         with the GlobalCollect platform
        :raise: ResponseException when an error response was received from the
         GlobalCollect platform
        :raise: ApiException when an error response was received from the
         GlobalCollect platform which contained a list of errors
        """
        connection = self.__session.connection
        if request_parameters is None:
            request_parameter_list = None
        else:
            request_parameter_list = request_parameters.to_request_parameters()
        uri = self._to_absolute_uri(relative_path, request_parameter_list)
        if request_headers is None:
            request_headers = []
        request_json = None
        if request_body is not None:
            request_headers.append(
                RequestHeader("Content-Type", "application/json"))
            request_json = self.__marshaller.marshal(request_body)
        self._add_generic_headers("PUT", uri, request_headers, context)
        response = connection.put(uri, request_headers, request_json)
        return self._process_response(response, response_type, relative_path,
                                      context)

    @property
    def marshaller(self):
        """
        :return: The Marshaller object associated with this communicator. Never
         None.
        """
        return self.__marshaller

    def _to_absolute_uri(self, relative_path, request_parameters):
        api_endpoint = self.__session.api_endpoint
        if api_endpoint.path:
            raise ValueError("api_endpoint should not contain a path")
        if api_endpoint.username is not None or api_endpoint.query or \
                api_endpoint.fragment:
            raise ValueError(
                "api_endpoint should not contain user info, query or fragment")
        if relative_path.startswith("/"):
            absolute_path = relative_path
        else:
            absolute_path = "/" + relative_path
        if api_endpoint.port is None:
            if api_endpoint.scheme:
                uri = api_endpoint.scheme + "://" + api_endpoint.hostname + \
                      absolute_path
            else:
                uri = api_endpoint.hostname + absolute_path
        else:
            if api_endpoint.scheme:
                uri = api_endpoint.scheme + "://" + api_endpoint.hostname + \
                      ":" + str(api_endpoint.port) + absolute_path
            else:
                uri = api_endpoint.hostname + ":" + str(api_endpoint.port) + \
                      absolute_path
        flag = False
        if request_parameters is not None:
            for nvp in request_parameters:
                if not flag:
                    uri += "?"
                    flag = True
                else:
                    uri += "&"
                uri += quote(nvp.name) + "=" + quote(nvp.value)
        try:
            URLValidator(uri)
            return urlparse(uri)
        except ValidationError as e:
            raise ValueError("Unable to construct URI", e)

    def _add_generic_headers(self, http_method, uri, request_headers, context):
        """
        Adds the necessary headers to the given list of headers. This includes
        the authorization header, which uses other headers, so when you need to
        override this method, make sure to call super.addGenericHeaders at the
        end of your overridden method.
        """
        # add server meta info header
        request_headers.extend(
            self.__session.meta_data_provider.meta_data_headers)
        # add date header
        request_headers.append(
            RequestHeader("Date", self._get_header_date_string()))
        if context is not None and context.idempotence_key is not None:
            # add context specific headers
            request_headers.append(
                RequestHeader("X-GCS-Idempotence-Key", context.idempotence_key))
        # add signature
        authenticator = self.__session.authenticator
        authentication_signature = \
            authenticator.create_simple_authentication_signature(
                http_method, uri, request_headers)
        request_headers.append(RequestHeader("Authorization",
                                             authentication_signature))

    def _get_header_date_string(self):
        """
        Returns the date in the preferred format for the HTTP date header.
        """
        date_format_utc = datetime.utcnow().strftime(
            "%a, %d %b %Y %H:%M:%S GMT")
        return date_format_utc

    def _process_response(self, response, response_type, request_path, context):
        if context is not None:
            self._update_context(response, context)
        self._throw_exception_if_necessary(response, request_path)
        return self.__marshaller.unmarshal(response.body, response_type)

    def _update_context(self, response, context):
        """
        Updates the given call context based on the contents of the given response.
        """
        idempotence_request_timestamp_value = response.get_header_value(
            "X-GCS-Idempotence-Request-Timestamp")
        if idempotence_request_timestamp_value is not None:
            idempotence_request_timestamp = int(
                idempotence_request_timestamp_value)
            context.idempotence_request_timestamp = \
                idempotence_request_timestamp
        else:
            context.idempotence_request_timestamp = None

    def _throw_exception_if_necessary(self, response, request_path):
        """
        Checks the Response for errors and throws an exception if necessary.
        """
        status_code = response.status_code
        # status codes in the 100 or 300 range are not expected
        if status_code < 200 or status_code >= 300:
            body = response.body
            if body is not None and not self.__is_json(response):
                cause = ResponseException(response)
                if status_code == 404:
                    raise NotFoundException(cause,
                        "The requested resource was not found; invalid path: "
                        + request_path)
                else:
                    raise CommunicationException(cause)
            else:
                raise ResponseException(response)

    def __is_json(self, response):
        content_type = response.get_header_value("Content-Type")
        return (content_type is None) or (
            "application/json".lower() == content_type) or (
                   content_type.lower().startswith("application/json"))

    def close_idle_connections(self, idle_time):
        """
        Utility method that delegates the call to this communicator's session's
        connection if that's an instance of PooledConnection. If not this method
        does nothing.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        connection = self.__session.connection
        if isinstance(connection, PooledConnection):
            connection.close_idle_connections(idle_time)

    def close_expired_connections(self):
        """
        Utility method that delegates the call to this communicator's session's
        connection if that's an instance of PooledConnection. If not this method
        does nothing.
        """
        connection = self.__session.connection
        if isinstance(connection, PooledConnection):
            connection.close_expired_connections()

    def enable_logging(self, communicator_logger):
        # delegate to the connection
        self.__session.connection.enable_logging(communicator_logger)

    def disable_logging(self):
        # delegate to the connection
        self.__session.connection.disable_logging()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
