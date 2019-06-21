from ingenico.connect.sdk.data_object import DataObject


class ShoppingCartExtension(DataObject):
    def __init__(self, creator, name, version, extension_id=None):
        if not creator:
            raise ValueError("creator is required")
        if not name:
            raise ValueError("name is required")
        if not version:
            raise ValueError("version is required")
        self.__creator = creator
        self.__name = name
        self.__version = version
        self.__extension_id = extension_id

    def to_dictionary(self):
        dictionary = super(ShoppingCartExtension, self).to_dictionary()
        if self.__creator is not None:
            dictionary['creator'] = self.__creator
        if self.__name is not None:
            dictionary['name'] = self.__name
        if self.__version is not None:
            dictionary['version'] = self.__version
        if self.__extension_id is not None:
            dictionary['extensionId'] = self.__extension_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShoppingCartExtension, self).from_dictionary(dictionary)
        if 'creator' in dictionary:
            self.__creator = dictionary['creator']
        if 'name' in dictionary:
            self.__name = dictionary['name']
        if 'version' in dictionary:
            self.__version = dictionary['version']
        if 'extensionId' in dictionary:
            self.__extension_id = dictionary['extensionId']
        return self

    @staticmethod
    def create_from_dictionary(dictionary):
        if 'creator' in dictionary:
            creator = dictionary['creator']
        else:
            raise ValueError("creator is required")
        if 'name' in dictionary:
            name = dictionary['name']
        else:
            raise ValueError("name is required")
        if 'version' in dictionary:
            version = dictionary['version']
        else:
            raise ValueError("version is required")
        if 'extensionId' in dictionary:
            extension_id = dictionary['extensionId']
        else:
            extension_id = None
        return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def creator(self):
        return self.__creator

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    @property
    def extension_id(self):
        return self.__extension_id
