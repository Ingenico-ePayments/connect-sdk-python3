#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.hostedcheckout.definitions.created_payment_output import CreatedPaymentOutput


class GetHostedCheckoutResponse(DataObject):
    """
    Class GetHostedCheckoutResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_GetHostedCheckoutResponse
    """

    __created_payment_output = None
    __status = None

    @property
    def created_payment_output(self):
        """
        :class:`CreatedPaymentOutput`
        """
        return self.__created_payment_output

    @created_payment_output.setter
    def created_payment_output(self, value):
        self.__created_payment_output = value

    @property
    def status(self):
        """
        str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(GetHostedCheckoutResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'createdPaymentOutput', self.created_payment_output)
        self._add_to_dictionary(dictionary, 'status', self.status)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetHostedCheckoutResponse, self).from_dictionary(dictionary)
        if 'createdPaymentOutput' in dictionary:
            if not isinstance(dictionary['createdPaymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['createdPaymentOutput']))
            value = CreatedPaymentOutput()
            self.created_payment_output = value.from_dictionary(dictionary['createdPaymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self
