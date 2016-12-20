#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair
from ingenico.connect.sdk.domain.payment.definitions.redirect_data import RedirectData


class MerchantAction(DataObject):
    """
    Class MerchantAction
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_MerchantAction
    """

    __action_type = None
    __redirect_data = None
    __rendering_data = None
    __show_data = None

    @property
    def action_type(self):
        """
        str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value):
        self.__action_type = value

    @property
    def redirect_data(self):
        """
        :class:`RedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value):
        self.__redirect_data = value

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
        dictionary = super(MerchantAction, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'actionType', self.action_type)
        self._add_to_dictionary(dictionary, 'redirectData', self.redirect_data)
        self._add_to_dictionary(dictionary, 'renderingData', self.rendering_data)
        self._add_to_dictionary(dictionary, 'showData', self.show_data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(MerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = RedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
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
