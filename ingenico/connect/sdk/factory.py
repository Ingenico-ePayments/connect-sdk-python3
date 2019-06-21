from configparser import ConfigParser

from .communicator import Communicator
from .communicator_configuration import CommunicatorConfiguration
from .client import Client
from ingenico.connect.sdk.defaultimpl.default_authenticator import \
    DefaultAuthenticator
from ingenico.connect.sdk.defaultimpl.default_connection import \
    DefaultConnection
from ingenico.connect.sdk.defaultimpl.default_marshaller import \
    DefaultMarshaller
from .meta_data_provider import MetaDataProvider
from .session import Session


class Factory:
    """
    Ingenico ePayments platform factory for several SDK components.
    """

    def __init__(self):
        pass

    @staticmethod
    def create_configuration(configuration_file_name, api_key_id,
                             secret_api_key):
        """
        Creates a CommunicatorConfiguration based on the configuration
        values in configuration_file_name, api_key_id and secret_api_key.
        """
        try:
            parser = ConfigParser()
            parser.read(configuration_file_name)
            with open(configuration_file_name) as f:
                parser.read_file(f)
            return CommunicatorConfiguration(properties=parser,
                                             api_key_id=api_key_id,
                                             secret_api_key=secret_api_key)
        except IOError as e:
            raise RuntimeError("Unable to read configuration located at {}".format(e.filename), e)

    @staticmethod
    def create_session_from_configuration(communicator_configuration,
                                          meta_data_provider=None,
                                          connection=None, authenticator=None):
        """
        Creates a Session based on the configuration stored in the
        CommunicatorConfiguration argument
        """
        # If an authenticator is not given,  api_key_id and secret_api_key are
        # used to create a DefaultAuthenticator used to create the session.
        if meta_data_provider is None:
            meta_data_provider = MetaDataProvider(
                integrator=communicator_configuration.integrator,
                shopping_cart_extension=
                communicator_configuration.shopping_cart_extension)
        if connection is None:
            connection = DefaultConnection(
                communicator_configuration.connect_timeout,
                communicator_configuration.socket_timeout,
                communicator_configuration.max_connections,
                communicator_configuration.proxy_configuration)
        if authenticator is None:
            authenticator = DefaultAuthenticator(
                communicator_configuration.authorization_type,
                communicator_configuration.api_key_id,
                communicator_configuration.secret_api_key)
        return Session(api_endpoint=communicator_configuration.api_endpoint,
                       meta_data_provider=meta_data_provider,
                       connection=connection, authenticator=authenticator)

    @staticmethod
    def create_session_from_file(configuration_file_name, api_key_id,
                                 secret_api_key,
                                 meta_data_provider=None,
                                 connection=None, authenticator=None):
        """
        Creates a Session based on the configuration values in
        configuration_file_name, api_id_key and secret_api_key.
        """
        configuration = Factory.create_configuration(configuration_file_name,
                                                     api_key_id,
                                                     secret_api_key)
        return Factory.create_session_from_configuration(
            configuration,
            meta_data_provider=meta_data_provider,
            connection=connection,
            authenticator=authenticator)

    @staticmethod
    def create_communicator_from_session(session):
        """
        Create a Communicator based on the settings stored in the Session
        argument
        """
        return Communicator(session, DefaultMarshaller.INSTANCE())

    @staticmethod
    def create_communicator_from_configuration(communicator_configuration):
        """
        Create a Communicator based on the configuration stored in the
        CommunicatorConfiguration argument
        """
        session = Factory.create_session_from_configuration(
            communicator_configuration)
        return Communicator(session, DefaultMarshaller.INSTANCE())

    @staticmethod
    def create_communicator_from_file(configuration_file_name, api_key_id,
                                      secret_api_key):
        """
        Creates a Communicator based on the configuration values in
        configuration_file_name, api_key_id and secret_api_key.
        """
        configuration = Factory.create_configuration(configuration_file_name,
                                                     api_key_id, secret_api_key)
        session = Factory.create_session_from_configuration(configuration)
        return Communicator(session, DefaultMarshaller.INSTANCE())

    @staticmethod
    def create_client_from_configuration(communicator_configuration):
        """
        Create a Client based on the configuration stored in the
        CommunicatorConfiguration argument
        """
        communicator = Factory.create_communicator_from_configuration(
            communicator_configuration)
        return Client(communicator)

    @staticmethod
    def create_client_from_communicator(communicator):
        """
        Create a Client based on the settings stored in the Communicator
        argument
        """
        return Client(communicator)

    @staticmethod
    def create_client_from_session(session):
        """
        Create a Client based on the settings stored in the Session argument
        """
        communicator = Factory.create_communicator_from_session(session)
        return Client(communicator)

    @staticmethod
    def create_client_from_file(configuration_file_name, api_key_id,
                                secret_api_key):
        """
        Creates a Client based on the configuration values in
        configuration_file_name, api_key_id and secret_api_key.
        """
        communicator = Factory.create_communicator_from_file(
            configuration_file_name, api_key_id, secret_api_key)
        return Client(communicator)
