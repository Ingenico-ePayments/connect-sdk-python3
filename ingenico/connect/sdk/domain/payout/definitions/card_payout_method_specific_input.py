# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payout.definitions.abstract_payout_method_specific_input import AbstractPayoutMethodSpecificInput
from ingenico.connect.sdk.domain.payout.definitions.payout_recipient import PayoutRecipient


class CardPayoutMethodSpecificInput(AbstractPayoutMethodSpecificInput):

    __card = None
    __payment_product_id = None
    __recipient = None
    __token = None

    @property
    def card(self):
        """
        | Object containing the card details.
        
        Type: :class:`ingenico.connect.sdk.domain.definitions.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier
        | Please see payment products <https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/paymentproducts.html> for a full overview of possible values.
        
        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    @property
    def recipient(self):
        """
        | Object containing the details of the recipient of the payout
        
        Type: :class:`ingenico.connect.sdk.domain.payout.definitions.payout_recipient.PayoutRecipient`
        """
        return self.__recipient

    @recipient.setter
    def recipient(self, value):
        self.__recipient = value

    @property
    def token(self):
        """
        | ID of the token that holds previously stored card data. Note that this is only supported for transactions on the Ogone payment engine.
        
        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(CardPayoutMethodSpecificInput, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.recipient is not None:
            dictionary['recipient'] = self.recipient.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPayoutMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'recipient' in dictionary:
            if not isinstance(dictionary['recipient'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recipient']))
            value = PayoutRecipient()
            self.recipient = value.from_dictionary(dictionary['recipient'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
