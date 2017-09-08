class ApiVersionMismatchException(RuntimeError):
    """
    Represents an error because a webhooks event has an API version that this version of the SDK does not support.
    """

    def __init__(self, event_api_version, sdk_api_version):
        super(ApiVersionMismatchException, self).__init__(
            "event API version" + event_api_version +
            " is not compatible with SDK API version" + sdk_api_version)
        self.__event_api_version = event_api_version
        self.__sdk_api_version = sdk_api_version

    @property
    def event_api_version(self):
        """
        :return: The API version from the webhooks event.
        """
        return self.__event_api_version

    @property
    def sdk_api_version(self):
        """
        :return: The API version that this version of the SDK supports.
        """
        return self.__sdk_api_version
