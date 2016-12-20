class MarshallerSyntaxException(RuntimeError):
    """
    Thrown when a JSON string cannot be converted to a response object.
    """

    def __init__(self, cause=False):
        if cause:
            super(MarshallerSyntaxException, self).__init__(cause)
        else:
            super(MarshallerSyntaxException, self).__init__()
