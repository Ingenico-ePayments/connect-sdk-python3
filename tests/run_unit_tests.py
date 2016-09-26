#!python
import unittest
import sys
import os
# append to pythonpath to make imports work
sys.path.insert(0, os.path.abspath(".."))


def load_tests(loader, tests, pattern):
    """ Discover and load all unit tests in all files named ``test_*.py`` in ``../unit/``

    Overrides default test loading behavior to only load tests in the unit folder
    """
    unit_dir = os.path.join(os.path.dirname(__file__), "unit")
    unit_tests = loader.discover(start_dir=unit_dir, pattern="test_*.py")
    tests.addTests(unit_tests)
    return tests


if __name__ == '__main__':
    unittest.main()
