# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.label_template_element import LabelTemplateElement


class AccountOnFileDisplayHints(DataObject):

    __label_template = None
    __logo = None

    @property
    def label_template(self):
        """
        | Array of attribute keys and their mask
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.label_template_element.LabelTemplateElement`]
        """
        return self.__label_template

    @label_template.setter
    def label_template(self, value):
        self.__label_template = value

    @property
    def logo(self):
        """
        | Partial URL that you can reference for the image of this payment product. You can use our server-side resize functionality by appending '?size={{width}}x{{height}}' to the full URL, where width and height are specified in pixels. The resized image will always keep its correct aspect ratio.
        
        Type: str
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    def to_dictionary(self):
        dictionary = super(AccountOnFileDisplayHints, self).to_dictionary()
        if self.label_template is not None:
            dictionary['labelTemplate'] = []
            for element in self.label_template:
                if element is not None:
                    dictionary['labelTemplate'].append(element.to_dictionary())
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileDisplayHints, self).from_dictionary(dictionary)
        if 'labelTemplate' in dictionary:
            if not isinstance(dictionary['labelTemplate'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['labelTemplate']))
            self.label_template = []
            for element in dictionary['labelTemplate']:
                value = LabelTemplateElement()
                self.label_template.append(value.from_dictionary(element))
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
