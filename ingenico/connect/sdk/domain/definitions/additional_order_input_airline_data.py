#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.airline_data import AirlineData


class AdditionalOrderInputAirlineData(DataObject):
    """
    Class AdditionalOrderInputAirlineData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AdditionalOrderInputAirlineData
    """

    __airline_data = None

    @property
    def airline_data(self):
        """
        :class:`AirlineData`
        """
        return self.__airline_data

    @airline_data.setter
    def airline_data(self, value):
        self.__airline_data = value

    def to_dictionary(self):
        dictionary = super(AdditionalOrderInputAirlineData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'airlineData', self.airline_data)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AdditionalOrderInputAirlineData, self).from_dictionary(dictionary)
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        return self
