class DataObject(object):
    def to_dictionary(self):
        return {}

    def from_dictionary(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError(
                'value \'{}\' is not a dictionary'.format(dictionary))
        return self

    def _add_to_dictionary(self, dictionary, key, value):
        if isinstance(value, DataObject):
            dictionary[key] = value.to_dictionary()
        elif isinstance(value, list):
            dictionary[key] = self.__get_list_value(value)
            pass
        elif value is not None:
            dictionary[key] = value

    def __get_list_value(self, value):
        result = []
        for element in value:
            if isinstance(element, DataObject):
                result.append(element.to_dictionary())
            else:
                result.append(element)
        return result
