#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.merchant_action import MerchantAction
from ingenico.connect.sdk.domain.payment.definitions.payment import Payment
from ingenico.connect.sdk.domain.payment.definitions.payment_creation_output import PaymentCreationOutput


class CreatePaymentResult(DataObject):
    """
    Class CreatePaymentResult
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_CreatePaymentResult
    """

    __creation_output = None
    __merchant_action = None
    __payment = None

    @property
    def creation_output(self):
        """
        :class:`PaymentCreationOutput`
        """
        return self.__creation_output

    @creation_output.setter
    def creation_output(self, value):
        self.__creation_output = value

    @property
    def merchant_action(self):
        """
        :class:`MerchantAction`
        """
        return self.__merchant_action

    @merchant_action.setter
    def merchant_action(self, value):
        self.__merchant_action = value

    @property
    def payment(self):
        """
        :class:`Payment`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentResult, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'creationOutput', self.creation_output)
        self._add_to_dictionary(dictionary, 'merchantAction', self.merchant_action)
        self._add_to_dictionary(dictionary, 'payment', self.payment)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentResult, self).from_dictionary(dictionary)
        if 'creationOutput' in dictionary:
            if not isinstance(dictionary['creationOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creationOutput']))
            value = PaymentCreationOutput()
            self.creation_output = value.from_dictionary(dictionary['creationOutput'])
        if 'merchantAction' in dictionary:
            if not isinstance(dictionary['merchantAction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantAction']))
            value = MerchantAction()
            self.merchant_action = value.from_dictionary(dictionary['merchantAction'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = Payment()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
