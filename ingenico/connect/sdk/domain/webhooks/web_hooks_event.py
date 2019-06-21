from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.payment_response import PaymentResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse
from ingenico.connect.sdk.domain.payout.payout_response import PayoutResponse
from ingenico.connect.sdk.domain.token.token_response import TokenResponse


class WebhooksEvent(DataObject):
    __api_version = None
    __id = None
    __created = None
    __merchant_id = None
    __type = None
    __payment = None
    __refund = None
    __payout = None
    __token = None

    @property
    def api_version(self):
        return self.__api_version

    @api_version.setter
    def api_version(self, api_version):
        self.__api_version = api_version

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, created):
        self.__created = created

    @property
    def merchant_id(self):
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, mercahant_id):
        self.__merchant_id = mercahant_id

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, payment):
        self.__payment = payment

    @property
    def refund(self):
        return self.__refund

    @refund.setter
    def refund(self, refund):
        self.__refund = refund

    @property
    def payout(self):
        return self.__payout

    @payout.setter
    def payout(self, payout):
        self.__payout = payout

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    def to_dictionary(self):
        dictionary = super(WebhooksEvent, self).to_dictionary()
        if self.__api_version is not None:
            dictionary['apiVersion'] = self.__api_version
        if self.__id is not None:
            dictionary['id'] = self.__id
        if self.__created is not None:
            dictionary['created'] = self.__created
        if self.__merchant_id is not None:
            dictionary['merchantId'] = self.__merchant_id
        if self.__type is not None:
            dictionary['type'] = self.__type
        if self.__payment is not None:
            dictionary['payment'] = self.__payment
        if self.__refund is not None:
            dictionary['refund'] = self.__refund
        if self.__payout is not None:
            dictionary['payout'] = self.__payout
        if self.__token is not None:
            dictionary['token'] = self.__token
        return dictionary

    def from_dictionary(self, dictionary):
        super(WebhooksEvent, self).from_dictionary(dictionary)
        if 'apiVersion' in dictionary:
            self.__api_version = dictionary['apiVersion']
        if 'id' in dictionary:
            self.__id = dictionary['id']
        if 'created' in dictionary:
            self.__created = dictionary['created']
        if 'merchantId' in dictionary:
            self.__merchant_id = dictionary['merchantId']
        if 'type' in dictionary:
            self.__type = dictionary['type']
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.__payment = value.from_dictionary(dictionary['payment'])
        if 'payout' in dictionary:
            if not isinstance(dictionary['payout'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payout']))
            value = PayoutResponse()
            self.__payout = value.from_dictionary(dictionary['payout'])
        if 'refund' in dictionary:
            if not isinstance(dictionary['refund'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refund']))
            value = RefundResponse()
            self.__refund = value.from_dictionary(dictionary['refund'])
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenResponse()
            self.__token = value.from_dictionary(dictionary['token'])
        return self
