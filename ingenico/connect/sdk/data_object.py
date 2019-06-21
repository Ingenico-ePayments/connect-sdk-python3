class DataObject(object):
    def to_dictionary(self):
        return {}

    def from_dictionary(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError(
                'value \'{}\' is not a dictionary'.format(dictionary))
        return self
