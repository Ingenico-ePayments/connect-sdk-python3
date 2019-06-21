class ParamRequest(object):
    """
    Represents a set of request parameters.
    """

    def to_request_parameters(self):
        """
        :return: list[:class:`ingenico.connect.sdk.RequestParam`] representing the HTTP request parameters
        """
        raise NotImplementedError
