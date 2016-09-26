from ingenico.connect.sdk.data_object import DataObject


class ShoppingCartExtension(DataObject):
    def __init__(self, creator, name, version):
        if not creator:
            raise ValueError("creator is required")
        if not name:
            raise ValueError("name is required")
        if not version:
            raise ValueError("version is required")
        self.__creator = creator
        self.__name = name
        self.__version = version

    def to_dictionary(self):
        dictionary = super(ShoppingCartExtension, self).to_dictionary()
        self._add_to_dictionary(dictionary, "creator", self.__creator)
        self._add_to_dictionary(dictionary, "name", self.__name)
        self._add_to_dictionary(dictionary, "version", self.__version)
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShoppingCartExtension, self).from_dictionary(dictionary)
        if 'creator' in dictionary:
            self.__creator = dictionary['creator']
        if 'name' in dictionary:
            self.__name = dictionary['name']
        if 'version' in dictionary:
            self.__version = dictionary['version']
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
        return ShoppingCartExtension(creator, name, version)

    @property
    def creator(self):
        return self.__creator

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version
