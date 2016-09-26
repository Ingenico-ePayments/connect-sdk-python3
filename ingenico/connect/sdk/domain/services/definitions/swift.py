#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Swift(DataObject):
    """
    Class Swift
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Swift
    
    Attributes:
        bic:              str
        category:         str
        chips_uid:        str
        extra_info:       str
        po_box_country:   str
        po_box_location:  str
        po_box_number:    str
        po_box_zip:       str
        routing_bic:      str
        services:         str
     """

    bic = None
    category = None
    chips_uid = None
    extra_info = None
    po_box_country = None
    po_box_location = None
    po_box_number = None
    po_box_zip = None
    routing_bic = None
    services = None

    def to_dictionary(self):
        dictionary = super(Swift, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'bic', self.bic)
        self._add_to_dictionary(dictionary, 'category', self.category)
        self._add_to_dictionary(dictionary, 'chipsUID', self.chips_uid)
        self._add_to_dictionary(dictionary, 'extraInfo', self.extra_info)
        self._add_to_dictionary(dictionary, 'poBoxCountry', self.po_box_country)
        self._add_to_dictionary(dictionary, 'poBoxLocation', self.po_box_location)
        self._add_to_dictionary(dictionary, 'poBoxNumber', self.po_box_number)
        self._add_to_dictionary(dictionary, 'poBoxZip', self.po_box_zip)
        self._add_to_dictionary(dictionary, 'routingBic', self.routing_bic)
        self._add_to_dictionary(dictionary, 'services', self.services)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Swift, self).from_dictionary(dictionary)
        if 'bic' in dictionary:
            self.bic = dictionary['bic']
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'chipsUID' in dictionary:
            self.chips_uid = dictionary['chipsUID']
        if 'extraInfo' in dictionary:
            self.extra_info = dictionary['extraInfo']
        if 'poBoxCountry' in dictionary:
            self.po_box_country = dictionary['poBoxCountry']
        if 'poBoxLocation' in dictionary:
            self.po_box_location = dictionary['poBoxLocation']
        if 'poBoxNumber' in dictionary:
            self.po_box_number = dictionary['poBoxNumber']
        if 'poBoxZip' in dictionary:
            self.po_box_zip = dictionary['poBoxZip']
        if 'routingBic' in dictionary:
            self.routing_bic = dictionary['routingBic']
        if 'services' in dictionary:
            self.services = dictionary['services']
        return self
