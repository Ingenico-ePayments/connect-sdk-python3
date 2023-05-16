import json
import os
import unittest
import tests.integration.init_utils as init_utils
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.multipart_form_data_object import MultipartFormDataObject
from ingenico.connect.sdk.multipart_form_data_request import MultipartFormDataRequest
from ingenico.connect.sdk.uploadable_file import UploadableFile


HTTPBIN_URL = os.getenv("httpbin.url") or 'http://httpbin.org'


class MultipartFormDataTest(unittest.TestCase):
    """Test multipart/form-data uploads"""

    def test_multipart_form_data_upload_post_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    def test_multipart_form_data_upload_post_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post('/post', None, None, MultipartFormDataObjectWrapper(multipart), HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    def test_multipart_form_data_upload_post_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post_with_binary_response('/post', None, None, multipart, None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    def test_multipart_form_data_upload_post_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post_with_binary_response('/post', None, None, MultipartFormDataObjectWrapper(multipart), None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    def test_multipart_form_data_upload_put_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put('/put', None, None, multipart, HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    def test_multipart_form_data_upload_put_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put('/put', None, None, MultipartFormDataObjectWrapper(multipart), HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    def test_multipart_form_data_upload_put_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put_with_binary_response('/put', None, None, multipart, None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    def test_multipart_form_data_upload_put_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = HTTPBIN_URL

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put_with_binary_response('/put', None, None, MultipartFormDataObjectWrapper(multipart), None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')


class HttpBinResponse(DataObject):
    form = None
    files = None

    def from_dictionary(self, dictionary):
        super(HttpBinResponse, self).from_dictionary(dictionary)
        if 'form' in dictionary:
            self.form = dictionary['form']
        if 'files' in dictionary:
            self.files = dictionary['files']
        return self


class MultipartFormDataObjectWrapper(MultipartFormDataRequest):
    __multipart = None

    def __init__(self, multipart):
        self.__multipart = multipart

    def to_multipart_form_data_object(self):
        return self.__multipart


if __name__ == '__main__':
    unittest.main()
