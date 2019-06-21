# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address


class Seller(DataObject):

    __address = None
    __channel_code = None
    __description = None
    __geocode = None
    __id = None
    __invoice_number = None
    __mcc = None
    __name = None
    __type = None

    @property
    def address(self):
        """
        | Object containing the seller address details
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.address.Address`
        """
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def channel_code(self):
        """
        | This property is specific to Visa Argentina. Channelcode according to Prisma. Please contact the acquirer to get the full list you need to use.
        
        Type: str
        """
        return self.__channel_code

    @channel_code.setter
    def channel_code(self, value):
        self.__channel_code = value

    @property
    def description(self):
        """
        | Description of the seller
        
        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def geocode(self):
        """
        | The sellers geocode
        
        Type: str
        """
        return self.__geocode

    @geocode.setter
    def geocode(self, value):
        self.__geocode = value

    @property
    def id(self):
        """
        | The sellers identifier
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def invoice_number(self):
        """
        | Invoice number of the payment
        
        Type: str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value

    @property
    def mcc(self):
        """
        | Merchant category code
        
        Type: str
        """
        return self.__mcc

    @mcc.setter
    def mcc(self, value):
        self.__mcc = value

    @property
    def name(self):
        """
        | Name of the seller
        
        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        """
        | Seller type. Possible values:
        
        * passport
        * dni
        * arg-identity-card
        * civic-notebook
        * enrollment-book
        * cuil
        * cuit
        * general-register
        * election-title
        * cpf
        * cnpj
        * ssn
        * citizen-ship
        * col-identity-card
        * alien-registration
        
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(Seller, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.channel_code is not None:
            dictionary['channelCode'] = self.channel_code
        if self.description is not None:
            dictionary['description'] = self.description
        if self.geocode is not None:
            dictionary['geocode'] = self.geocode
        if self.id is not None:
            dictionary['id'] = self.id
        if self.invoice_number is not None:
            dictionary['invoiceNumber'] = self.invoice_number
        if self.mcc is not None:
            dictionary['mcc'] = self.mcc
        if self.name is not None:
            dictionary['name'] = self.name
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary):
        super(Seller, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = Address()
            self.address = value.from_dictionary(dictionary['address'])
        if 'channelCode' in dictionary:
            self.channel_code = dictionary['channelCode']
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'geocode' in dictionary:
            self.geocode = dictionary['geocode']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'mcc' in dictionary:
            self.mcc = dictionary['mcc']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self
