#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentProductFieldTooltip(DataObject):
    """
    Class PaymentProductFieldTooltip
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFieldTooltip
    """

    __image = None
    __label = None

    @property
    def image(self):
        """
        str
        """
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def label(self):
        """
        str
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldTooltip, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'image', self.image)
        self._add_to_dictionary(dictionary, 'label', self.label)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldTooltip, self).from_dictionary(dictionary)
        if 'image' in dictionary:
            self.image = dictionary['image']
        if 'label' in dictionary:
            self.label = dictionary['label']
        return self
