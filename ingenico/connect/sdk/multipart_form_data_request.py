class MultipartFormDataRequest:
    """
    A representation of a multipart/form-data request.
    """

    def to_multipart_form_data_object(self):
        """
        :return: :class:`ingenico.connect.sdk.MultipartFormDataObject`
        """
        raise NotImplementedError
