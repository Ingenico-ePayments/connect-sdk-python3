import logging
import unittest

from ingenico.connect.sdk.log.python_communicator_logger import PythonCommunicatorLogger


class SDKCommunicatorLoggerTest(unittest.TestCase):
    """Contains tests to test log normal messages and exceptions using the CommunicatorLogger"""

    def test_log(self):
        """Tests that the Python communicator logger appropriately logs messages"""
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)
        handler = TestHandler()
        logger.addHandler(handler)

        communicator_logger = PythonCommunicatorLogger(logger, logging.INFO, logging.WARNING)
        communicator_logger.log("test 123")

        self.assertEqual(1, len(handler.records),
                         "The communication logger should have logged one message, it logged "
                         + str(len(handler.records)))
        record = handler.records[0]
        self.assertEqual("test 123", record.msg)
        self.assertEqual('INFO', record.levelname)
        self.assertEqual(self.__class__.__name__, record.name)
        # self.assertEqual(JdkCommunicatorLogger.__module__, record.module)
        self.assertEqual("log", record.funcName)
        self.assertIsNone(record.exc_info)

    def test_log_exception(self):
        """Tests that the Python communicator logger appropriately logs exceptions"""
        logger = logging.Logger(self.__class__.__name__)
        handler = TestHandler()
        logger.addHandler(handler)

        communicator_logger = PythonCommunicatorLogger(logger, logging.INFO, logging.WARNING)
        exception = Exception("foo")
        communicator_logger.log("test 112", exception)

        self.assertEqual(1, len(handler.records))
        record = handler.records[0]
        self.assertEqual("test 112", record.msg)
        self.assertEqual('WARNING', record.levelname)
        self.assertEqual(self.__class__.__name__, record.name)
        # self.assertEqual(JdkCommunicatorLogger.__module__, record.module)
        self.assertEqual("log", record.funcName)
        self.assertIs(exception, record.args[0], "Exception sbould be recorded in record.args[0]")


class TestHandler(logging.NullHandler):
    """Test handler that records any logs in a list for testing"""

    def __init__(self):
        super(TestHandler, self).__init__()
        self.records = []

    def handle(self, record):
        self.records.append(record)


if __name__ == '__main__':
    unittest.main()
