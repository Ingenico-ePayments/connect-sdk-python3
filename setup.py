import os
import unittest

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def test_collector():
    """Function to collect tests cases to run for the 'pip connect-sdk-python3 tests' command"""
    from tests import run_unit_tests
    loader = unittest.TestLoader()
    return loader.discover(start_dir=run_unit_tests.__file__)


setup(
    name="connect-sdk-python3",
    version="3.1.0",
    author="Ingenico ePayments",
    author_email="github@epay.ingenico.com",
    description="SDK to communicate with the Ingenico ePayments platform using the Ingenico Connect Server API",
    license="MIT",
    platforms="python 3.5",
    keywords="Ingenico ePayments Connect SDK",
    url="https://github.com/Ingenico-ePayments/connect-sdk-python3",
    packages=find_packages(
        exclude=["*.examples", "*.examples.*", "examples.*", "examples",  # exclude examples
                 "*.tests", "*.tests.*", "tests.*", "tests"],             # and tests
        include="ingenico.*"),  # finds all source packages, recursively
    # list non-code files used by the SDK
    package_data={".": ["MANIFEST.in", "README.md", "setup.py"]},
    # data_files=[(".", ["LICENSE.txt"])],
    # installs all files listed in the MANIFEST.in into the installation (currently does not seem to happen either way)
    include_package_data=True,
    # data_files=[("index.rst", "README.md", "setup.py, MANIFEST.in")],  # list miscellaneous files to include
    # The pypi homepage is based on the long description, standard interpretation is reStructuredText
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License"
    ],
    scripts=[],  # executable python scripts, none since this is a library
    install_requires=[
        "requests >= 2.11.0",
        "django >= 1.10"
    ],
    # test_suite="tests/run_unit_tests"   # enables command 'pip connect-sdk-python3 test', which runs unit tests)

    # setup_requires=[               # setuptools_scm automatically reads the version from version control
    #     'setuptools_scm'
    # ],
    # use_scm_version=True           # turns setuptools_scm on
)
