# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.fraud_results import FraudResults
from ingenico.connect.sdk.domain.definitions.fraud_results_retail_decisions import FraudResultsRetailDecisions
from ingenico.connect.sdk.domain.definitions.fraugster_results import FraugsterResults


class CardFraudResults(FraudResults):
    """
    | Details of the card payment fraud checks that were performed
    """

    __avs_result = None
    __cvv_result = None
    __fraugster = None
    __retail_decisions = None

    @property
    def avs_result(self):
        """
        | Result of the Address Verification Service checks. Possible values are:
        
        * A - Address (Street) matches, Zip does not
        * B - Street address match for international transactions—Postal code not verified due to incompatible formats
        * C - Street address and postal code not verified for international transaction due to incompatible formats
        * D - Street address and postal code match for international transaction, cardholder name is incorrect
        * E - AVS error
        * F - Address does match and five digit ZIP code does match (UK only)
        * G - Address information is unavailable; international transaction; non-AVS participant
        * H - Billing address and postal code match, cardholder name is incorrect (Amex)
        * I - Address information not verified for international transaction
        * K - Cardholder name matches (Amex)
        * L - Cardholder name and postal code match (Amex)
        * M - Cardholder name, street address, and postal code match for international transaction
        * N - No Match on Address (Street) or Zip
        * O - Cardholder name and address match (Amex)
        * P - Postal codes match for international transaction—Street address not verified due to incompatible formats
        * Q - Billing address matches, cardholder is incorrect (Amex)
        * R - Retry, System unavailable or Timed out
        * S - Service not supported by issuer
        * U - Address information is unavailable
        * W - 9 digit Zip matches, Address (Street) does not
        * X - Exact AVS Match
        * Y - Address (Street) and 5 digit Zip match
        * Z - 5 digit Zip matches, Address (Street) does not
        * 0 - No service available
        
        Type: str
        """
        return self.__avs_result

    @avs_result.setter
    def avs_result(self, value):
        self.__avs_result = value

    @property
    def cvv_result(self):
        """
        | Result of the Card Verification Value checks. Possible values are:
        
        * M - CVV check performed and valid value
        * N - CVV checked and no match
        * P - CVV check not performed, not requested
        * S - Cardholder claims no CVV code on card, issuer states CVV-code should be on card
        * U - Issuer not certified for CVV2
        * Y - Server provider did not respond
        * 0 - No service available
        
        Type: str
        """
        return self.__cvv_result

    @cvv_result.setter
    def cvv_result(self, value):
        self.__cvv_result = value

    @property
    def fraugster(self):
        """
        | Results of Fraugster fraud prevention check. Fraugster collects transaction data points such as name, email address, billing, etc. to analyze whether or not the transaction is fraudulent.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraugster_results.FraugsterResults`
        """
        return self.__fraugster

    @fraugster.setter
    def fraugster(self, value):
        self.__fraugster = value

    @property
    def retail_decisions(self):
        """
        | Additional response data returned by RetailDecisions
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.fraud_results_retail_decisions.FraudResultsRetailDecisions`
        """
        return self.__retail_decisions

    @retail_decisions.setter
    def retail_decisions(self, value):
        self.__retail_decisions = value

    def to_dictionary(self):
        dictionary = super(CardFraudResults, self).to_dictionary()
        if self.avs_result is not None:
            dictionary['avsResult'] = self.avs_result
        if self.cvv_result is not None:
            dictionary['cvvResult'] = self.cvv_result
        if self.fraugster is not None:
            dictionary['fraugster'] = self.fraugster.to_dictionary()
        if self.retail_decisions is not None:
            dictionary['retailDecisions'] = self.retail_decisions.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardFraudResults, self).from_dictionary(dictionary)
        if 'avsResult' in dictionary:
            self.avs_result = dictionary['avsResult']
        if 'cvvResult' in dictionary:
            self.cvv_result = dictionary['cvvResult']
        if 'fraugster' in dictionary:
            if not isinstance(dictionary['fraugster'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraugster']))
            value = FraugsterResults()
            self.fraugster = value.from_dictionary(dictionary['fraugster'])
        if 'retailDecisions' in dictionary:
            if not isinstance(dictionary['retailDecisions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['retailDecisions']))
            value = FraudResultsRetailDecisions()
            self.retail_decisions = value.from_dictionary(dictionary['retailDecisions'])
        return self
