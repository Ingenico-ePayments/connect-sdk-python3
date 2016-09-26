import io
import re
import sys
import unittest

from ingenico.connect.sdk.log.sys_out_communicator_logger import SysOutCommunicatorLogger


class SysOutCommunicatorLoggerTest(unittest.TestCase):
    """Test if the SysOutCommunicatorLogger appropriately logs messages and exceptions"""

    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = self.mock_io = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout
        self.mock_io.close()

    def test_log(self):
        """Test if the SysOutCommunicatorLogger correctly logs a message"""

        logger = SysOutCommunicatorLogger.INSTANCE()
        logger.log("test 123")

        text = self.mock_io.getvalue()
        self.assertMessage(text, "test 123")

    def test_log_exception(self):
        """Test if the SysOutCommunicatorLogger correctly logs an exception"""
        logger = SysOutCommunicatorLogger.INSTANCE()
        exception = Exception("something terrible happened /jk")
        logger.log("test 112", exception)

        text = self.mock_io.getvalue()
        self.assertMessage(text, "test 112", exception)

    def assertMessage(self, content, message, exception=None):
        """Assert that the parameter message is contained in the parameter content after the date and time"""
        message_pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} (.*)", re.DOTALL)

        expected = message + "\n"
        if exception is not None:
            expected += str(exception) + "\n"
        matcher = message_pattern.match(content)

        self.assertEqual(expected, matcher.group(1))


if __name__ == '__main__':
    unittest.main()
