# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal


class ShippingRiskAssessment(DataObject):
    """
    | Object containing information regarding shipping / delivery
    """

    __address = None
    __comments = None
    __tracking_number = None

    @property
    def address(self):
        """
        | Object containing address information
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.address_personal.AddressPersonal`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def comments(self):
        """
        | Comments included during shipping
        
        Type: str
        """
        return self.__comments

    @comments.setter
    def comments(self, value):
        self.__comments = value

    @property
    def tracking_number(self):
        """
        | Shipment tracking number
        
        Type: str
        """
        return self.__tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self.__tracking_number = value

    def to_dictionary(self):
        dictionary = super(ShippingRiskAssessment, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.comments is not None:
            dictionary['comments'] = self.comments
        if self.tracking_number is not None:
            dictionary['trackingNumber'] = self.tracking_number
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShippingRiskAssessment, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = AddressPersonal()
            self.address = value.from_dictionary(dictionary['address'])
        if 'comments' in dictionary:
            self.comments = dictionary['comments']
        if 'trackingNumber' in dictionary:
            self.tracking_number = dictionary['trackingNumber']
        return self
