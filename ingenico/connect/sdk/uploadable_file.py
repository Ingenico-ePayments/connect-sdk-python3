class UploadableFile:
    """
    A file that can be uploaded.

    The allowed forms of content are defined by the Connection implementation.
    The default implementation supports strings, file descriptors and io.BytesIO objects.
    """

    def __init__(self, file_name, content, content_type, content_length=-1):
        if file_name is None or not file_name.strip():
            raise ValueError("file_name is required")
        if content is None:
            raise ValueError("content is required")
        if content_type is None or not content_type.strip():
            raise ValueError("file_name is required")

        self.__file_name = file_name
        self.__content = content
        self.__content_type = content_type
        self.__content_length = max(content_length, -1)

    @property
    def file_name(self):
        """
        :return: The name of the file.
        """
        return self.__file_name

    @property
    def content(self):
        """
        :return: The file's content.
        """
        return self.__content

    @property
    def content_type(self):
        """
        :return: The file's content type.
        """
        return self.__content_type

    @property
    def content_length(self):
        """
        :return: The file's content length, or -1 if not known.
        """
        return self.__content_length
