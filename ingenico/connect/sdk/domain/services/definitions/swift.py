#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class Swift(DataObject):
    """
    Class Swift
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Swift
    """

    __bic = None
    __category = None
    __chips_uid = None
    __extra_info = None
    __po_box_country = None
    __po_box_location = None
    __po_box_number = None
    __po_box_zip = None
    __routing_bic = None
    __services = None

    @property
    def bic(self):
        """
        str
        """
        return self.__bic

    @bic.setter
    def bic(self, value):
        self.__bic = value

    @property
    def category(self):
        """
        str
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def chips_uid(self):
        """
        str
        """
        return self.__chips_uid

    @chips_uid.setter
    def chips_uid(self, value):
        self.__chips_uid = value

    @property
    def extra_info(self):
        """
        str
        """
        return self.__extra_info

    @extra_info.setter
    def extra_info(self, value):
        self.__extra_info = value

    @property
    def po_box_country(self):
        """
        str
        """
        return self.__po_box_country

    @po_box_country.setter
    def po_box_country(self, value):
        self.__po_box_country = value

    @property
    def po_box_location(self):
        """
        str
        """
        return self.__po_box_location

    @po_box_location.setter
    def po_box_location(self, value):
        self.__po_box_location = value

    @property
    def po_box_number(self):
        """
        str
        """
        return self.__po_box_number

    @po_box_number.setter
    def po_box_number(self, value):
        self.__po_box_number = value

    @property
    def po_box_zip(self):
        """
        str
        """
        return self.__po_box_zip

    @po_box_zip.setter
    def po_box_zip(self, value):
        self.__po_box_zip = value

    @property
    def routing_bic(self):
        """
        str
        """
        return self.__routing_bic

    @routing_bic.setter
    def routing_bic(self, value):
        self.__routing_bic = value

    @property
    def services(self):
        """
        str
        """
        return self.__services

    @services.setter
    def services(self, value):
        self.__services = value

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
