import uuid


class MultipartFormDataObject:
    """
    A representation of a multipart/form-data object.
    """

    def __init__(self):
        self.__boundary = str(uuid.uuid4())
        self.__content_type = "multipart/form-data; boundary=" + self.__boundary
        self.__values = {}
        self.__files = {}

    @property
    def boundary(self):
        return self.__boundary

    @property
    def content_type(self):
        return self.__content_type

    @property
    def values(self):
        return self.__values

    @property
    def files(self):
        return self.__files

    def add_value(self, parameter_name, value):
        if parameter_name is None or not parameter_name.strip():
            raise ValueError("parameter_name is required")
        if value is None:
            raise ValueError("value is required")
        if parameter_name in self.__values or parameter_name in self.__files:
            raise ValueError("duplicate parameterName: " + parameter_name)
        self.__values[parameter_name] = value

    def add_file(self, parameter_name, uploadable_file):
        if parameter_name is None or not parameter_name.strip():
            raise ValueError("parameter_name is required")
        if uploadable_file is None:
            raise ValueError("uploadable_file is required")
        if parameter_name in self.__values or parameter_name in self.__files:
            raise ValueError("duplicate parameterName: " + parameter_name)
        self.__files[parameter_name] = uploadable_file
