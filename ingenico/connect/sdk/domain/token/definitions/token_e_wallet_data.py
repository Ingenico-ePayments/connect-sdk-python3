#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class TokenEWalletData(DataObject):
    """
    Class TokenEWalletData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_TokenEWalletData
    """

    __billing_agreement_id = None

    @property
    def billing_agreement_id(self):
        """
        str
        """
        return self.__billing_agreement_id

    @billing_agreement_id.setter
    def billing_agreement_id(self, value):
        self.__billing_agreement_id = value

    def to_dictionary(self):
        dictionary = super(TokenEWalletData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'billingAgreementId', self.billing_agreement_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenEWalletData, self).from_dictionary(dictionary)
        if 'billingAgreementId' in dictionary:
            self.billing_agreement_id = dictionary['billingAgreementId']
        return self
