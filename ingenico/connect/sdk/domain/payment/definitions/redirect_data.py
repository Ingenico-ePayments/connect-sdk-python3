#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class RedirectData(DataObject):
    """
    Class RedirectData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RedirectData
    """

    __returnmac = None
    __redirect_url = None

    @property
    def returnmac(self):
        """
        str
        """
        return self.__returnmac

    @returnmac.setter
    def returnmac(self, value):
        self.__returnmac = value

    @property
    def redirect_url(self):
        """
        str
        """
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self.__redirect_url = value

    def to_dictionary(self):
        dictionary = super(RedirectData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'RETURNMAC', self.returnmac)
        self._add_to_dictionary(dictionary, 'redirectURL', self.redirect_url)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectData, self).from_dictionary(dictionary)
        if 'RETURNMAC' in dictionary:
            self.returnmac = dictionary['RETURNMAC']
        if 'redirectURL' in dictionary:
            self.redirect_url = dictionary['redirectURL']
        return self
