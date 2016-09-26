#!python
import unittest
import sys
import os
# append to pythonpath to make imports work
sys.path.insert(0, os.path.abspath(".."))


def load_tests(loader, tests, pattern):
    """ Discover and load all integration tests in all files named ``test_*.py`` in ``../integration/``

    Overrides default test loading behavior to load only the tests in the integration subfolder
    """
    integration_dir = os.path.join(os.path.dirname(__file__), "integration")
    integration_tests = loader.discover(start_dir=integration_dir, pattern="test_*.py")
    tests.addTests(integration_tests)
    return tests


if __name__ == '__main__':
    unittest.main()
