import unittest

from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.token.definitions.customer_token import CustomerToken
from ingenico.connect.sdk.domain.token.definitions.token_card import TokenCard
from ingenico.connect.sdk.domain.token.definitions.token_card_data import TokenCardData
from ingenico.connect.sdk.domain.token.token_response import TokenResponse
from ingenico.connect.sdk.defaultimpl.default_marshaller import DefaultMarshaller


class DefaultMarshallerTest(unittest.TestCase):
    """Tests that the default marshaller is able to marshal an object
    and unmarshal that same object to a more generic version
    """

    def test_unmarshal_with_extra_fields(self):
        """Tests if the marshaller is able to marshal an object and unmarshal it as an instance of a parent class"""
        dummy_object = JsonDummyExtended()
        mini_dummy = JsonMiniDummy()
        mini_mini_dummy = JsonMiniMiniDummy()
        mini_mini_dummy.foo = "hiddenfoo"
        mini_dummy.foo = mini_mini_dummy
        dummy_object.foo = mini_dummy
        dummy_object.bar = True
        dummy_object.boo = 0o1
        dummy_object.far = "close"
        dummy_object.extra_field = "something else"
        marshaller = DefaultMarshaller.INSTANCE()

        json = marshaller.marshal(dummy_object)
        unmarshalled = marshaller.unmarshal(json, JsonDummy)

        self.assertEqual(True, unmarshalled.bar)
        self.assertEqual(0o1, unmarshalled.boo)
        self.assertEqual("close", unmarshalled.far)
        self.assertEqual("hiddenfoo", unmarshalled.foo.foo.foo)

    def test_unmarshal_extended_token_response(self):
        """Tests if the marshaller is able to marshal an object that inherits from token_response
        in such a way that it can be interpreted as a token_response
        """
        token_response = TokenResponseWithExtraField()
        billing_address = Address()
        billing_address.country_code = "NL"
        customer = CustomerToken()
        customer.billing_address = billing_address
        card = TokenCard()
        card_data = TokenCardData()
        card.customer = customer
        card.data = card_data
        token_response.card = card
        token_response.extraField = "a random string"
        marshaller = DefaultMarshaller.INSTANCE()
        # Marshal the extended token response and unmarshal as a regular token response
        json = marshaller.marshal(token_response)
        unmarshalled = marshaller.unmarshal(json, TokenResponse)

        self.assertIsNotNone(unmarshalled.card)
        self.assertIsNotNone(unmarshalled.card.customer)
        self.assertIsNotNone(unmarshalled.card.customer.billing_address)
        self.assertEqual("NL", unmarshalled.card.customer.billing_address.country_code)
        self.assertIsNotNone(unmarshalled.card.data)


# --------------- A number of dummy objects for testing -------------

class TokenResponseWithExtraField(TokenResponse):

    def __init__(self, extra_field=None):
        TokenResponse.__init__(self)
        self.extra_field = extra_field


class JsonMiniMiniDummy(DataObject):
    foo = "standardfoo"

    def to_dictionary(self, dictionary=None):
        dictionary = super(JsonMiniMiniDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo

        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonMiniMiniDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            self.foo = dictionary['foo']
        return self


class JsonMiniDummy(DataObject):
    foo = JsonMiniMiniDummy()

    def to_dictionary(self, dictionary=None):
        # type: () -> object
        dictionary = super(JsonMiniDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonMiniDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            if not isinstance(dictionary['foo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['foo']))
            value = JsonMiniMiniDummy()
            self.foo = value.from_dictionary(dictionary['foo'])
        return self


class JsonDummy(DataObject):
    foo = JsonMiniDummy()
    bar = False
    boo = 00
    far = "far"

    def to_dictionary(self):
        dictionary = super(JsonDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo
        if self.bar is not None:
            dictionary['bar'] = self.bar
        if self.boo is not None:
            dictionary['boo'] = self.boo
        if self.far is not None:
            dictionary['far'] = self.far

        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            if not isinstance(dictionary['foo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['foo']))
            value = JsonMiniDummy()
            self.foo = value.from_dictionary(dictionary['foo'])
        if 'bar' in dictionary:
            self.bar = dictionary['bar']
        if 'boo' in dictionary:
            self.boo = dictionary['boo']
        if 'far' in dictionary:
            self.far = dictionary['far']

        return self


class JsonDummyExtended(JsonDummy):
    extra_field = "something something"

    def to_dictionary(self):
        dictionary = super(JsonDummyExtended, self).to_dictionary()
        if self.extra_field is not None:
            dictionary['extraField'] = self.extra_field
        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonDummyExtended, self).from_dictionary(dictionary)
        if 'extraField' in dictionary:
            self.far = dictionary['extraField']
        return self


if __name__ == '__main__':
    unittest.main()
