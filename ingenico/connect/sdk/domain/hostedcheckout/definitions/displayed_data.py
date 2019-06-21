# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair


class DisplayedData(DataObject):

    __displayed_data_type = None
    __rendering_data = None
    __show_data = None

    @property
    def displayed_data_type(self):
        """
        | Action merchants needs to take in the online payment process. Possible values are:
        
        * SHOW_INSTRUCTIONS - The customer needs to be shown payment instruction using the details found in showData. Alternatively the instructions can be rendered by us using the renderingData
        * SHOW_TRANSACTION_RESULTS - The customer needs to be shown the transaction results using the details found in showData. Alternatively the instructions can be rendered by us using the renderingData
        
        Type: str
        """
        return self.__displayed_data_type

    @displayed_data_type.setter
    def displayed_data_type(self, value):
        self.__displayed_data_type = value

    @property
    def rendering_data(self):
        """
        | This property contains the blob with data for the instructions rendering service.
        
        | This service will be available at the following endpoint:http(s)://{{merchant specific subdomain}}.{{base MyCheckout hosted payment pages domain}}/instructions/{{merchantId}}/{{clientSessionId}}
        
        | This instructions page rendering service accepts the following parameters:
        
        * renderingData (required, the content of this property)
        * locale (optional, if present overrides default locale, e.g. "en_GB")
        * variant (optional, code of a variant, if present overrides default variant, e.g. "100")
        
        | You can offer a link to a customer to see an instructions page for a payment done earlier. Because of the size of the renderingData this will need to be set in a web form as a value of a hidden field. Before presenting the link you need to obtain a clientSessionId by creating a session using the S2S API. You will need to use the MyCheckout hosted payment pages domain hosted in the same region as the API domain used for the createClientSession call.
        
        | The renderingData is a String blob that is presented to you via the Server API as part of the merchantAction (if available, and non-redirect) in the JSON return values for the createPayment call or the getHostedCheckoutStatus call (merchantAction inside createdPaymentOutput when available).You are responsible to store the renderingData blob in order to be able to present the instructions page at a later time, when this information might no longer be available through Server API calls.
        
        Type: str
        """
        return self.__rendering_data

    @rendering_data.setter
    def rendering_data(self, value):
        self.__rendering_data = value

    @property
    def show_data(self):
        """
        | Array of key value pairs of data that needs to be shown to the customer. This is returned for both the SHOW_INSTRUCTION as well as the SHOW_TRANSACTION_RESULTS actionType.
        | Note: The returned value for the key BARCODE is a base64 encoded gif image. By prepending 'data:image/gif;base64,' this value can be used as the source of an HTML inline image.
        
        Type: list[:class:`ingenico.connect.sdk.domain.definitions.key_value_pair.KeyValuePair`]
        """
        return self.__show_data

    @show_data.setter
    def show_data(self, value):
        self.__show_data = value

    def to_dictionary(self):
        dictionary = super(DisplayedData, self).to_dictionary()
        if self.displayed_data_type is not None:
            dictionary['displayedDataType'] = self.displayed_data_type
        if self.rendering_data is not None:
            dictionary['renderingData'] = self.rendering_data
        if self.show_data is not None:
            dictionary['showData'] = []
            for element in self.show_data:
                if element is not None:
                    dictionary['showData'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary):
        super(DisplayedData, self).from_dictionary(dictionary)
        if 'displayedDataType' in dictionary:
            self.displayed_data_type = dictionary['displayedDataType']
        if 'renderingData' in dictionary:
            self.rendering_data = dictionary['renderingData']
        if 'showData' in dictionary:
            if not isinstance(dictionary['showData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['showData']))
            self.show_data = []
            for element in dictionary['showData']:
                value = KeyValuePair()
                self.show_data.append(value.from_dictionary(element))
        return self
