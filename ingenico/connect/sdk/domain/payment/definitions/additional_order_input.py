#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.airline_data import AirlineData
from ingenico.connect.sdk.domain.payment.definitions.level3_summary_data import Level3SummaryData
from ingenico.connect.sdk.domain.payment.definitions.order_type_information import OrderTypeInformation


class AdditionalOrderInput(DataObject):
    """
    Class AdditionalOrderInput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_AdditionalOrderInput
    
    Attributes:
        airline_data:            :class:`AirlineData`
        level3_summary_data:     :class:`Level3SummaryData`
        number_of_installments:  int
        order_date:              str
        type_information:        :class:`OrderTypeInformation`
     """

    airline_data = None
    level3_summary_data = None
    number_of_installments = None
    order_date = None
    type_information = None

    def to_dictionary(self):
        dictionary = super(AdditionalOrderInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'airlineData', self.airline_data)
        self._add_to_dictionary(dictionary, 'level3SummaryData', self.level3_summary_data)
        self._add_to_dictionary(dictionary, 'numberOfInstallments', self.number_of_installments)
        self._add_to_dictionary(dictionary, 'orderDate', self.order_date)
        self._add_to_dictionary(dictionary, 'typeInformation', self.type_information)
        return dictionary

    def from_dictionary(self, dictionary):
        super(AdditionalOrderInput, self).from_dictionary(dictionary)
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        if 'level3SummaryData' in dictionary:
            if not isinstance(dictionary['level3SummaryData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['level3SummaryData']))
            value = Level3SummaryData()
            self.level3_summary_data = value.from_dictionary(dictionary['level3SummaryData'])
        if 'numberOfInstallments' in dictionary:
            self.number_of_installments = dictionary['numberOfInstallments']
        if 'orderDate' in dictionary:
            self.order_date = dictionary['orderDate']
        if 'typeInformation' in dictionary:
            if not isinstance(dictionary['typeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['typeInformation']))
            value = OrderTypeInformation()
            self.type_information = value.from_dictionary(dictionary['typeInformation'])
        return self
