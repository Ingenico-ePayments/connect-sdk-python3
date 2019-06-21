import unittest
import threading
import timeit
import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID
from ingenico.connect.sdk.merchant.services.convert_amount_params import ConvertAmountParams
from ingenico.connect.sdk.factory import Factory


class ConnectionPoolingTest(unittest.TestCase):
    """Performs multiple threaded server requests with connection pooling in order to test thread-safety and concurrency
    """

    def setUp(self):
        self.flag = threading.Event()  # flag to synchronise a start moment for the threads
        self.result_list = []          # list to collect results from the threads
        self.lock = threading.RLock()  # mutex lock for the threads to provide concurrent access to the result list

    def test_connection_pool_max_is_count(self):
        """Test with one pool per request"""
        self.run_connection_pooling_test(10, 10)

    def test_connection_pool_max_is_half(self):
        """Test with one pool per two requests"""
        self.run_connection_pooling_test(10, 5)

    def test_connection_pool_max_is_one(self):
        """Test with one pool for all 10 requests"""
        self.run_connection_pooling_test(10, 1)

    def run_connection_pooling_test(self, request_count, max_connections):
        """Sends *request_count* requests with a maximum number of connection pools equal to *max_connections*"""
        communicator_configuration = init_utils.create_communicator_configuration(max_connections=max_connections)

        with Factory.create_communicator_from_configuration(communicator_configuration) as communicator:
            # Create a number of runner threads that will execute send_request
            runner_threads = [
                threading.Thread(target=self.send_request, args=(i, communicator)) for i in range(0, request_count)
                ]
            for thread in runner_threads:
                thread.start()
            self.flag.set()

            # wait until threads are done before closing the communicator
            for i in range(0, request_count - 1):
                runner_threads[i].join()
        print("(*start time*, *end time*) for {} connection pools".format(max_connections))
        for item in self.result_list:
            if isinstance(item, Exception):
                self.fail("an exception occurred in one of the threads:/n" + str(item))
            else:
                print(repr(item))
        # check server logs for information about concurrent use of connections

    def send_request(self, i, communicator):
        """runs a (concurrent) request"""
        request = ConvertAmountParams()
        request.source = "USD"
        request.target = "EUR"
        request.amount = (100 * (i + 1))

        try:
            client = Factory.create_client_from_communicator(communicator)
            self.flag.wait()
            start_time = timeit.default_timer()
            dummy = client.merchant(MERCHANT_ID).services().convert_amount(request).converted_amount
            end_time = timeit.default_timer()
            with self.lock:
                self.result_list.append((start_time, end_time))
        except Exception as e:
            with self.lock:
                self.result_list.append(e)
        # check server logs for additional data about the requests sent


if __name__ == '__main__':
    unittest.main()
