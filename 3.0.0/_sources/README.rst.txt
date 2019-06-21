Ingenico Connect Python SDK
===========================

Introduction
------------

The Python SDK helps you to communicate with the `Ingenico
Connect <https://epayments.developer-ingenico.com/>`__ Server API. It's
primary features are:

-  convenient Python library for the API calls and responses

   -  marshalls Python request objects to HTTP requests
   -  unmarshalls HTTP responses to Python response objects or Python
      exceptions

-  handling of all the details concerning authentication
-  handling of required meta data

Its use is demonstrated by an example for each possible call. The
examples execute a call using the provided API keys.

See the `Ingenico Connect Developer
Hub <https://epayments.developer-ingenico.com/documentation/sdk/server/python/>`__
for more information on how to use the SDK.

Structure of this repository
----------------------------

This repository consists out of four main components:

#. The source code of the SDK itself: ``/ingenico/connect/sdk/``
#. The source code of the SDK unit tests: ``/tests/unit/``
#. The source code of the SDK integration tests: ``/tests/integration/``
#. Usage examples: ``/examples/``

Note that the source code of the unit tests and integration tests and
the examples can only be found on GitHub.

Requirements
------------

Python 3.3.5 or higher is required. In addition, the following packages
are required:

-  `django <https://www.djangoproject.com/>`__ 1.10 or higher
-  `requests <http://docs.python-requests.org/en/master/>`__ 2.11.0 or
   higher
-  `requests-toolbelt <https://toolbelt.readthedocs.io/>`__ 0.8.0 or
   higher

These packages will be installed automatically if the SDK is installed
manually or using pip following the below instructions.

Installation
------------

To install the SDK using pip, execute the following command:

::

    pip install connect-sdk-python3

Alternatively, you can install the SDK from a source distribution file:

#. Download the latest version of the Python SDK from GitHub. Choose the
   ``connect-sdk-python3-x.y.z.zip`` file from the
   `releases <https://github.com/Ingenico-ePayments/connect-sdk-python3/releases>`__
   page, where ``x.y.z`` is the version number.
#. Execute the following command in the folder where the SDK was
   downloaded to:

   ::

       pip install connect-sdk-python3-x.y.z.zip

Uninstalling
------------

After the Python SDK has been installed, it can be uninstalled using the
following command:

::

    pip uninstall connect-sdk-python3

The required packages can be uninstalled in the same way.

Running tests
-------------

| There are two types of tests: unit tests and integration tests. The
  unit tests will work out-of-the-box; for the integration tests some
  configuration is required.
| First, some environment variables need to be set:

-  ``connect.api.apiKeyId`` for the API key id to use. This can be
   retrieved from the Configuration Center.
-  ``connect.api.secretApiKey`` for the secret API key to use. This can
   be retrieved from the Configuration Center.
-  ``connect.api.merchantId`` for your merchant ID.

In addition, to run the proxy integration tests, the proxy URI, username
and password should be set in the
``tests/resources/configuration.proxy.ini`` file.

In order to run the unit and integration tests, the
`mock <https://pypi.python.org/pypi/mock>`__ backport and
`mockito <https://pypi.python.org/pypi/mockito>`__ are required. This
can be installed using the following command:

::

    pip install mock mockito

The following commands can now be executed from the ``tests`` directory
to execute the tests:

-  Unit tests:

   ::

       python run_unit_tests.py

-  Integration tests:

   ::

       python run_integration_tests.py

-  Both unit and integration tests:

   ::

       python run_all_tests.py
