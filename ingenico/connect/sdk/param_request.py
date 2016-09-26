from .request_param import RequestParam


class ParamRequest(object):
    """
    Represents a set of request parameters.
    """

    def _add_parameter(self, request_parameters, name, value):
        """
        Adds a request parameter with the given name and value to the given
        list, unless if the value is None.

        The following types are supported:
        * str
        * int
        * bool
        * list
        """
        self.__add_parameter(request_parameters, name, value, True)

    def __add_parameter(self, request_parameters, name, value,
                        allow_collection):
        if isinstance(value, str) or isinstance(
                value, int) or isinstance(value, bool):
            request_parameters.append(RequestParam(name, str(value)))
        elif allow_collection and isinstance(value, list):
            for element in value:
                self.__add_parameter(request_parameters, name, element, False)
        elif value is not None:
            raise ValueError("Unsupported request parameter type")

    def to_request_parameters(self):
        """
        :return: list[RequestParam] representing the HTTP request parameters
        """
        raise NotImplementedError
