#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.services.definitions.bank_details import BankDetails


class BankDetailsRequest(BankDetails):
    """
    Class BankDetailsRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_BankDetailsRequest
    """

    def to_dictionary(self):
        dictionary = super(BankDetailsRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankDetailsRequest, self).from_dictionary(dictionary)
        return self
