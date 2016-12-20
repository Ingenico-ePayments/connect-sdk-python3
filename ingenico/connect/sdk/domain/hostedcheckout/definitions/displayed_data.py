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
    """

    __displayed_data_type = None
    __rendering_data = None
    __show_data = None

    @property
    def displayed_data_type(self):
        """
        str
        """
        return self.__displayed_data_type

    @displayed_data_type.setter
    def displayed_data_type(self, value):
        self.__displayed_data_type = value

    @property
    def rendering_data(self):
        """
        str
        """
        return self.__rendering_data

    @rendering_data.setter
    def rendering_data(self, value):
        self.__rendering_data = value

    @property
    def show_data(self):
        """
        list[:class:`KeyValuePair`]
        """
        return self.__show_data

    @show_data.setter
    def show_data(self, value):
        self.__show_data = value

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
