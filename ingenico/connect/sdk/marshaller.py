class Marshaller(object):
    """
    Used to marshal and unmarshal Ingenico ePayments platform request and response
    objects to and from JSON.
    """

    def marshal(self, request_object):
        """
        Marshal a request object to a JSON string.

        :param request_object: the object to marshal into a serialized JSON string
        :return: the serialized JSON string of the request_object
        """
        raise NotImplementedError

    def unmarshal(self, response_json, type_class):
        """
        Unmarshal a JSON string to a response object.

        :param response_json: the json body that should be unmarshalled
        :param type_class: The class to which the response_json should be unmarshalled
        :raise: MarshallerSyntaxException if the JSON is not a valid
         representation for an object of the given type
        """
        raise NotImplementedError
