# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.redirection_data import RedirectionData


class GPayThreeDSecure(DataObject):

    __challenge_canvas_size = None
    __challenge_indicator = None
    __exemption_request = None
    __redirection_data = None
    __skip_authentication = None

    @property
    def challenge_canvas_size(self):
        """
        | Dimensions of the challenge window that potentially will be displayed to the customer. The challenge content is formatted to appropriately render in this window to provide the best possible user experience.
        | Preconfigured sizes are width x height in pixels of the window displayed in the customer browser window. Possible values are:
        
        * 250x400 (default)
        * 390x400
        * 500x600
        * 600x400
        * full-screen
        
        | .
        
        Type: str
        """
        return self.__challenge_canvas_size

    @challenge_canvas_size.setter
    def challenge_canvas_size(self, value):
        self.__challenge_canvas_size = value

    @property
    def challenge_indicator(self):
        """
        | Allows you to indicate if you want the customer to be challenged for extra security on this transaction.Possible values:
        
        * no-preference - You have no preference whether or not to challenge the customer (default)
        * no-challenge-requested - you prefer the cardholder not to be challenged
        * challenge-requested - you prefer the customer to be challenged
        * challenge-required - you require the customer to be challenged
        
        Type: str
        """
        return self.__challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, value):
        self.__challenge_indicator = value

    @property
    def exemption_request(self):
        """
        | Type of strong customer authentication (SCA) exemption requested for this transaction. Possible values:
        
        * none - No exemption flagging is to be used of this transaction (Default).
        * automatic - Our systems will determine the best possible exemption based on the transaction parameters and the risk scores.
        * transaction-risk-analysis - You have determined that this transaction is of low risk and are willing to take the liability. Please note that your fraud rate needs to stay below thresholds to allow your use of this exemption.
        * low-value - The value of the transaction is below 30 EUR. Please note that the issuer will still require every 5th low-value transaction pithing 24 hours to be strongly authenticated. The issuer will also keep track of the cumulative amount authorized on the card. When this exceeds 100 EUR strong customer authentication is also required.
        * whitelist - You have been whitelisted by the customer at the issuer.
        
        Type: str
        """
        return self.__exemption_request

    @exemption_request.setter
    def exemption_request(self, value):
        self.__exemption_request = value

    @property
    def redirection_data(self):
        """
        | Object containing browser specific redirection related data
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.redirection_data.RedirectionData`
        """
        return self.__redirection_data

    @redirection_data.setter
    def redirection_data(self, value):
        self.__redirection_data = value

    @property
    def skip_authentication(self):
        """
        * true = 3D Secure authentication will be skipped for this transaction. This setting should be used when isRecurring is set to true and recurringPaymentSequenceIndicator is set to recurring.
        * false = 3D Secure authentication will not be skipped for this transaction.
        
        | Note: This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction.
        
        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value):
        self.__skip_authentication = value

    def to_dictionary(self):
        dictionary = super(GPayThreeDSecure, self).to_dictionary()
        if self.challenge_canvas_size is not None:
            dictionary['challengeCanvasSize'] = self.challenge_canvas_size
        if self.challenge_indicator is not None:
            dictionary['challengeIndicator'] = self.challenge_indicator
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        if self.redirection_data is not None:
            dictionary['redirectionData'] = self.redirection_data.to_dictionary()
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        return dictionary

    def from_dictionary(self, dictionary):
        super(GPayThreeDSecure, self).from_dictionary(dictionary)
        if 'challengeCanvasSize' in dictionary:
            self.challenge_canvas_size = dictionary['challengeCanvasSize']
        if 'challengeIndicator' in dictionary:
            self.challenge_indicator = dictionary['challengeIndicator']
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        if 'redirectionData' in dictionary:
            if not isinstance(dictionary['redirectionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectionData']))
            value = RedirectionData()
            self.redirection_data = value.from_dictionary(dictionary['redirectionData'])
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        return self
