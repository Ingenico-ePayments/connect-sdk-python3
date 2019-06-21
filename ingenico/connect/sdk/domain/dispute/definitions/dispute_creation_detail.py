# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DisputeCreationDetail(DataObject):

    __dispute_creation_date = None
    __dispute_originator = None
    __user_name = None

    @property
    def dispute_creation_date(self):
        """
        | The date and time of creation of this dispute, in yyyyMMddHHmmss format.
        
        Type: str
        """
        return self.__dispute_creation_date

    @dispute_creation_date.setter
    def dispute_creation_date(self, value):
        self.__dispute_creation_date = value

    @property
    def dispute_originator(self):
        """
        | The originator of this dispute, which is either Ingenico ePayments or you as our client.
        
        Type: str
        """
        return self.__dispute_originator

    @dispute_originator.setter
    def dispute_originator(self, value):
        self.__dispute_originator = value

    @property
    def user_name(self):
        """
        | The user account name of the dispute creator.
        
        Type: str
        """
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    def to_dictionary(self):
        dictionary = super(DisputeCreationDetail, self).to_dictionary()
        if self.dispute_creation_date is not None:
            dictionary['disputeCreationDate'] = self.dispute_creation_date
        if self.dispute_originator is not None:
            dictionary['disputeOriginator'] = self.dispute_originator
        if self.user_name is not None:
            dictionary['userName'] = self.user_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(DisputeCreationDetail, self).from_dictionary(dictionary)
        if 'disputeCreationDate' in dictionary:
            self.dispute_creation_date = dictionary['disputeCreationDate']
        if 'disputeOriginator' in dictionary:
            self.dispute_originator = dictionary['disputeOriginator']
        if 'userName' in dictionary:
            self.user_name = dictionary['userName']
        return self
