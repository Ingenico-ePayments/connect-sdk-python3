#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.domain.payment.definitions.order_output import OrderOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_bank_method_specific_output import RefundBankMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_card_method_specific_output import RefundCardMethodSpecificOutput
from ingenico.connect.sdk.domain.payment.definitions.refund_e_wallet_method_specific_output import RefundEWalletMethodSpecificOutput


class RefundOutput(OrderOutput):
    """
    Class RefundOutput
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundOutput
    
    Attributes:
        amount_paid:                             int
        bank_refund_method_specific_output:      :class:`RefundBankMethodSpecificOutput`
        card_refund_method_specific_output:      :class:`RefundCardMethodSpecificOutput`
        e_wallet_refund_method_specific_output:  :class:`RefundEWalletMethodSpecificOutput`
        payment_method:                          str
     """

    amount_paid = None
    bank_refund_method_specific_output = None
    card_refund_method_specific_output = None
    e_wallet_refund_method_specific_output = None
    payment_method = None

    def to_dictionary(self):
        dictionary = super(RefundOutput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountPaid', self.amount_paid)
        self._add_to_dictionary(dictionary, 'bankRefundMethodSpecificOutput', self.bank_refund_method_specific_output)
        self._add_to_dictionary(dictionary, 'cardRefundMethodSpecificOutput', self.card_refund_method_specific_output)
        self._add_to_dictionary(dictionary, 'eWalletRefundMethodSpecificOutput', self.e_wallet_refund_method_specific_output)
        self._add_to_dictionary(dictionary, 'paymentMethod', self.payment_method)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundOutput, self).from_dictionary(dictionary)
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'bankRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['bankRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankRefundMethodSpecificOutput']))
            value = RefundBankMethodSpecificOutput()
            self.bank_refund_method_specific_output = value.from_dictionary(dictionary['bankRefundMethodSpecificOutput'])
        if 'cardRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardRefundMethodSpecificOutput']))
            value = RefundCardMethodSpecificOutput()
            self.card_refund_method_specific_output = value.from_dictionary(dictionary['cardRefundMethodSpecificOutput'])
        if 'eWalletRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['eWalletRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWalletRefundMethodSpecificOutput']))
            value = RefundEWalletMethodSpecificOutput()
            self.e_wallet_refund_method_specific_output = value.from_dictionary(dictionary['eWalletRefundMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        return self
