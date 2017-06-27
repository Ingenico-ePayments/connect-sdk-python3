# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.capture.definitions.capture import Capture


class CaptureResponse(Capture):

    def to_dictionary(self):
        dictionary = super(CaptureResponse, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CaptureResponse, self).from_dictionary(dictionary)
        return self
