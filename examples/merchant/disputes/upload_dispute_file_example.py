#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.uploadable_file import UploadableFile
from ingenico.connect.sdk.merchant.disputes.upload_file_request import UploadFileRequest


class UploadDisputeFileExample(object):

    def example(self):
        with self.__get_client() as client:
            body = UploadFileRequest()
            with open("file.pdf", "rb") as file_content:
                body.file = UploadableFile("file.pdf", file_content, "application/pdf")

                response = client.merchant("merchantId").disputes().upload_file("disputeId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
