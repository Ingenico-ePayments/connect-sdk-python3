class RequestHeader:
    """
    A single request header. Immutable.
    """

    def __init__(self, name, value):
        if name is None or not name.strip():
            raise ValueError("name is required")
        self.__name = name
        self.__value = value

    @property
    def name(self):
        """
        :return: The header name.
        """
        return self.__name

    @property
    def value(self):
        """
        :return: The un-encoded value.
        """
        return self.__value.decode('utf-8') if isinstance(self.__value, bytes) else self.__value

    def __str__(self):
        return self.__name + ":" + str(self.__value)
