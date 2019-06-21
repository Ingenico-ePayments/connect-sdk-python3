# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProduct863ThirdPartyData(DataObject):

    __app_id = None
    __nonce_str = None
    __package_sign = None
    __pay_sign = None
    __prepay_id = None
    __sign_type = None
    __time_stamp = None

    @property
    def app_id(self):
        """
        | The appId to use in third party calls to WeChat.
        
        Type: str
        """
        return self.__app_id

    @app_id.setter
    def app_id(self, value):
        self.__app_id = value

    @property
    def nonce_str(self):
        """
        | The nonceStr to use in third party calls to WeChat
        
        Type: str
        """
        return self.__nonce_str

    @nonce_str.setter
    def nonce_str(self, value):
        self.__nonce_str = value

    @property
    def package_sign(self):
        """
        | The packageSign to use in third party calls to WeChat
        
        Type: str
        """
        return self.__package_sign

    @package_sign.setter
    def package_sign(self, value):
        self.__package_sign = value

    @property
    def pay_sign(self):
        """
        | The paySign to use in third party calls to WeChat
        
        Type: str
        """
        return self.__pay_sign

    @pay_sign.setter
    def pay_sign(self, value):
        self.__pay_sign = value

    @property
    def prepay_id(self):
        """
        | The prepayId to use in third party calls to WeChat.
        
        Type: str
        """
        return self.__prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self.__prepay_id = value

    @property
    def sign_type(self):
        """
        | The signType to use in third party calls to WeChat
        
        Type: str
        """
        return self.__sign_type

    @sign_type.setter
    def sign_type(self, value):
        self.__sign_type = value

    @property
    def time_stamp(self):
        """
        | The timeStamp to use in third party calls to WeChat
        
        Type: str
        """
        return self.__time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self.__time_stamp = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct863ThirdPartyData, self).to_dictionary()
        if self.app_id is not None:
            dictionary['appId'] = self.app_id
        if self.nonce_str is not None:
            dictionary['nonceStr'] = self.nonce_str
        if self.package_sign is not None:
            dictionary['packageSign'] = self.package_sign
        if self.pay_sign is not None:
            dictionary['paySign'] = self.pay_sign
        if self.prepay_id is not None:
            dictionary['prepayId'] = self.prepay_id
        if self.sign_type is not None:
            dictionary['signType'] = self.sign_type
        if self.time_stamp is not None:
            dictionary['timeStamp'] = self.time_stamp
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct863ThirdPartyData, self).from_dictionary(dictionary)
        if 'appId' in dictionary:
            self.app_id = dictionary['appId']
        if 'nonceStr' in dictionary:
            self.nonce_str = dictionary['nonceStr']
        if 'packageSign' in dictionary:
            self.package_sign = dictionary['packageSign']
        if 'paySign' in dictionary:
            self.pay_sign = dictionary['paySign']
        if 'prepayId' in dictionary:
            self.prepay_id = dictionary['prepayId']
        if 'signType' in dictionary:
            self.sign_type = dictionary['signType']
        if 'timeStamp' in dictionary:
            self.time_stamp = dictionary['timeStamp']
        return self
