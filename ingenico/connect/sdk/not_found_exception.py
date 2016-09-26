class NotFoundException(RuntimeError):
    """
    Indicates an exception that occurs when the requested resource is not found.
    In normal usage of the SDK, this exception should not occur, however it is
    possible. For example when path parameters are set with invalid values.
    """

    def __init__(self, exception, message=None):
        super(NotFoundException, self).__init__(message, exception)
        self.cause = exception
