#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductNetworksResponse(DataObject):
    """
    Class PaymentProductNetworksResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductNetworksResponse
    """

    __networks = None

    @property
    def networks(self):
        """
        list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value):
        self.__networks = value

    def to_dictionary(self):
        dictionary = super(PaymentProductNetworksResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'networks', self.networks)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductNetworksResponse, self).from_dictionary(dictionary)
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for networks_element in dictionary['networks']:
                self.networks.append(networks_element)
        return self
