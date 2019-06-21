# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DeviceRenderOptions(DataObject):
    """
    | Object containing rendering options of the device
    """

    __sdk_interface = None
    __sdk_ui_type = None

    @property
    def sdk_interface(self):
        """
        | Lists all of the SDK Interface types that the device supports for displaying specific challenge user interfaces within the SDK.
        
        
        
        * native = The app supports only a native user interface
        * html = The app supports only an HTML user interface
        * both = Both Native and HTML user interfaces are supported by the app
        
        Type: str
        """
        return self.__sdk_interface

    @sdk_interface.setter
    def sdk_interface(self, value):
        self.__sdk_interface = value

    @property
    def sdk_ui_type(self):
        """
        | Lists all UI types that the device supports for displaying specific challenge user interfaces within the SDK.
        
        
        
        * text = Text interface
        * single-select = Select a single option
        * multi-select = Select multiple options
        * oob = Out of ounds
        * html-other = HTML Other (only valid when cardPaymentMethodSpecificInput.threeDSecure.sdkData.deviceRenderOptions.sdkInterface is set to html)
        
        Type: str
        """
        return self.__sdk_ui_type

    @sdk_ui_type.setter
    def sdk_ui_type(self, value):
        self.__sdk_ui_type = value

    def to_dictionary(self):
        dictionary = super(DeviceRenderOptions, self).to_dictionary()
        if self.sdk_interface is not None:
            dictionary['sdkInterface'] = self.sdk_interface
        if self.sdk_ui_type is not None:
            dictionary['sdkUiType'] = self.sdk_ui_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(DeviceRenderOptions, self).from_dictionary(dictionary)
        if 'sdkInterface' in dictionary:
            self.sdk_interface = dictionary['sdkInterface']
        if 'sdkUiType' in dictionary:
            self.sdk_ui_type = dictionary['sdkUiType']
        return self
