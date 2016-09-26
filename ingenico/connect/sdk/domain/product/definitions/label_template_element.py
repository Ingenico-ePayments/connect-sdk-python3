#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LabelTemplateElement(DataObject):
    """
    Class LabelTemplateElement
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LabelTemplateElement
    
    Attributes:
        attribute_key:  str
        mask:           str
     """

    attribute_key = None
    mask = None

    def to_dictionary(self):
        dictionary = super(LabelTemplateElement, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'attributeKey', self.attribute_key)
        self._add_to_dictionary(dictionary, 'mask', self.mask)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LabelTemplateElement, self).from_dictionary(dictionary)
        if 'attributeKey' in dictionary:
            self.attribute_key = dictionary['attributeKey']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        return self
