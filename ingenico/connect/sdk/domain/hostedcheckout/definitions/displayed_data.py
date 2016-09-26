#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class DisplayedData(DataObject):
    """
    Class DisplayedData
    See also https://developer.globalcollect.com/documentation/api/server/#schema_DisplayedData
    
    Attributes:
        displayed_data_type:  str
        rendering_data:       str
        show_data:            list[:class:`KeyValuePair`]
     """

    displayed_data_type = None
    rendering_data = None
    show_data = None

    def to_dictionary(self):
        dictionary = super(DisplayedData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'displayedDataType', self.displayed_data_type)
        self._add_to_dictionary(dictionary, 'renderingData', self.rendering_data)
        self._add_to_dictionary(dictionary, 'showData', self.show_data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(DisplayedData, self).from_dictionary(dictionary)
        if 'displayedDataType' in dictionary:
            self.displayed_data_type = dictionary['displayedDataType']
        if 'renderingData' in dictionary:
            self.rendering_data = dictionary['renderingData']
        if 'showData' in dictionary:
            if not isinstance(dictionary['showData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['showData']))
            self.show_data = []
            for showData_element in dictionary['showData']:
                showData_value = KeyValuePair()
                self.show_data.append(showData_value.from_dictionary(showData_element))
        return self
