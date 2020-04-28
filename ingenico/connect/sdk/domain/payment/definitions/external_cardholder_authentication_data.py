# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class ExternalCardholderAuthenticationData(DataObject):
    """
    | Object containing 3D secure details.
    """

    __acs_transaction_id = None
    __applied_exemption = None
    __cavv = None
    __cavv_algorithm = None
    __directory_server_transaction_id = None
    __eci = None
    __scheme_risk_score = None
    __three_d_secure_version = None
    __three_d_server_transaction_id = None
    __validation_result = None
    __xid = None

    @property
    def acs_transaction_id(self):
        """
        | Identifier of the authenticated transaction at the ACS/Issuer.
        
        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value):
        self.__acs_transaction_id = value

    @property
    def applied_exemption(self):
        """
        | Exemption code from Carte Bancaire (130) (unknown possible values so far -free format).
        
        Type: str
        """
        return self.__applied_exemption

    @applied_exemption.setter
    def applied_exemption(self, value):
        self.__applied_exemption = value

    @property
    def cavv(self):
        """
        | The CAVV (cardholder authentication verification value) or AAV (accountholder authentication value) provides an authentication validation value.
        
        Type: str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value

    @property
    def cavv_algorithm(self):
        """
        | The algorithm, from your 3D Secure provider, used to generate the authentication CAVV.
        
        Type: str
        """
        return self.__cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, value):
        self.__cavv_algorithm = value

    @property
    def directory_server_transaction_id(self):
        """
        | The 3-D Secure Directory Server transaction ID that is used for the 3D Authentication
        
        Type: str
        """
        return self.__directory_server_transaction_id

    @directory_server_transaction_id.setter
    def directory_server_transaction_id(self, value):
        self.__directory_server_transaction_id = value

    @property
    def eci(self):
        """
        | Electronic Commerce Indicator provides authentication validation results returned after AUTHENTICATIONVALIDATION
        
        * 0 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * 1 = Authentication attempted (MasterCard)
        * 2 = Successful authentication (MasterCard)
        * 5 = Successful authentication (Visa, Diners Club, Amex)
        * 6 = Authentication attempted (Visa, Diners Club, Amex)
        * 7 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * (empty) = Not checked or not enrolled
        
        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value

    @property
    def scheme_risk_score(self):
        """
        | Global score calculated by the Carte Bancaire (130) Scoring platform. Possible values from 0 to 99.
        
        Type: int
        """
        return self.__scheme_risk_score

    @scheme_risk_score.setter
    def scheme_risk_score(self, value):
        self.__scheme_risk_score = value

    @property
    def three_d_secure_version(self):
        """
        | The 3-D Secure version used for the authentication. Possible values:
        
        * v1
        * v2
        * 1.0.2
        * 2.1.0
        * 2.2.0
        
        Type: str
        """
        return self.__three_d_secure_version

    @three_d_secure_version.setter
    def three_d_secure_version(self, value):
        self.__three_d_secure_version = value

    @property
    def three_d_server_transaction_id(self):
        """
        | The 3-D Secure Server transaction ID that is used for the 3-D Secure version 2 Authentication.
        
        Type: str
        
        Deprecated; No replacement
        """
        return self.__three_d_server_transaction_id

    @three_d_server_transaction_id.setter
    def three_d_server_transaction_id(self, value):
        self.__three_d_server_transaction_id = value

    @property
    def validation_result(self):
        """
        | The 3D Secure authentication result from your 3D Secure provider.
        
        Type: str
        """
        return self.__validation_result

    @validation_result.setter
    def validation_result(self, value):
        self.__validation_result = value

    @property
    def xid(self):
        """
        | The transaction ID that is used for the 3D Authentication
        
        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value

    def to_dictionary(self):
        dictionary = super(ExternalCardholderAuthenticationData, self).to_dictionary()
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.applied_exemption is not None:
            dictionary['appliedExemption'] = self.applied_exemption
        if self.cavv is not None:
            dictionary['cavv'] = self.cavv
        if self.cavv_algorithm is not None:
            dictionary['cavvAlgorithm'] = self.cavv_algorithm
        if self.directory_server_transaction_id is not None:
            dictionary['directoryServerTransactionId'] = self.directory_server_transaction_id
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.scheme_risk_score is not None:
            dictionary['schemeRiskScore'] = self.scheme_risk_score
        if self.three_d_secure_version is not None:
            dictionary['threeDSecureVersion'] = self.three_d_secure_version
        if self.three_d_server_transaction_id is not None:
            dictionary['threeDServerTransactionId'] = self.three_d_server_transaction_id
        if self.validation_result is not None:
            dictionary['validationResult'] = self.validation_result
        if self.xid is not None:
            dictionary['xid'] = self.xid
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExternalCardholderAuthenticationData, self).from_dictionary(dictionary)
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'appliedExemption' in dictionary:
            self.applied_exemption = dictionary['appliedExemption']
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'cavvAlgorithm' in dictionary:
            self.cavv_algorithm = dictionary['cavvAlgorithm']
        if 'directoryServerTransactionId' in dictionary:
            self.directory_server_transaction_id = dictionary['directoryServerTransactionId']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'schemeRiskScore' in dictionary:
            self.scheme_risk_score = dictionary['schemeRiskScore']
        if 'threeDSecureVersion' in dictionary:
            self.three_d_secure_version = dictionary['threeDSecureVersion']
        if 'threeDServerTransactionId' in dictionary:
            self.three_d_server_transaction_id = dictionary['threeDServerTransactionId']
        if 'validationResult' in dictionary:
            self.validation_result = dictionary['validationResult']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
