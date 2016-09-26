#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class FraudFields(DataObject):
    """
    Class FraudFields
    See also https://developer.globalcollect.com/documentation/api/server/#schema_FraudFields
    
    Attributes:
        customer_ip_address:       str
        default_form_fill:         str
        gift_card_type:            str
        gift_message:              str
        has_forgotten_pwd:         bool
        has_password:              bool
        is_previous_customer:      bool
        order_timezone:            str
        ship_comments:             str
        shipment_tracking_number:  str
        user_data:                 list[str]
        website:                   str
     """

    customer_ip_address = None
    default_form_fill = None
    gift_card_type = None
    gift_message = None
    has_forgotten_pwd = None
    has_password = None
    is_previous_customer = None
    order_timezone = None
    ship_comments = None
    shipment_tracking_number = None
    user_data = None
    website = None

    def to_dictionary(self):
        dictionary = super(FraudFields, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'customerIpAddress', self.customer_ip_address)
        self._add_to_dictionary(dictionary, 'defaultFormFill', self.default_form_fill)
        self._add_to_dictionary(dictionary, 'giftCardType', self.gift_card_type)
        self._add_to_dictionary(dictionary, 'giftMessage', self.gift_message)
        self._add_to_dictionary(dictionary, 'hasForgottenPwd', self.has_forgotten_pwd)
        self._add_to_dictionary(dictionary, 'hasPassword', self.has_password)
        self._add_to_dictionary(dictionary, 'isPreviousCustomer', self.is_previous_customer)
        self._add_to_dictionary(dictionary, 'orderTimezone', self.order_timezone)
        self._add_to_dictionary(dictionary, 'shipComments', self.ship_comments)
        self._add_to_dictionary(dictionary, 'shipmentTrackingNumber', self.shipment_tracking_number)
        self._add_to_dictionary(dictionary, 'userData', self.user_data)
        self._add_to_dictionary(dictionary, 'website', self.website)
        return dictionary

    def from_dictionary(self, dictionary):
        super(FraudFields, self).from_dictionary(dictionary)
        if 'customerIpAddress' in dictionary:
            self.customer_ip_address = dictionary['customerIpAddress']
        if 'defaultFormFill' in dictionary:
            self.default_form_fill = dictionary['defaultFormFill']
        if 'giftCardType' in dictionary:
            self.gift_card_type = dictionary['giftCardType']
        if 'giftMessage' in dictionary:
            self.gift_message = dictionary['giftMessage']
        if 'hasForgottenPwd' in dictionary:
            self.has_forgotten_pwd = dictionary['hasForgottenPwd']
        if 'hasPassword' in dictionary:
            self.has_password = dictionary['hasPassword']
        if 'isPreviousCustomer' in dictionary:
            self.is_previous_customer = dictionary['isPreviousCustomer']
        if 'orderTimezone' in dictionary:
            self.order_timezone = dictionary['orderTimezone']
        if 'shipComments' in dictionary:
            self.ship_comments = dictionary['shipComments']
        if 'shipmentTrackingNumber' in dictionary:
            self.shipment_tracking_number = dictionary['shipmentTrackingNumber']
        if 'userData' in dictionary:
            if not isinstance(dictionary['userData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['userData']))
            self.user_data = []
            for userData_element in dictionary['userData']:
                self.user_data.append(userData_element)
        if 'website' in dictionary:
            self.website = dictionary['website']
        return self
