from ingenico.connect.sdk.defaultimpl.default_marshaller import \
    DefaultMarshaller
from .web_hooks_helper_builder import WebhooksHelperBuilder


class Webhooks:
    """
    Ingenico ePayments platform factory for several webhooks components.
    """

    @staticmethod
    def create_helper_builder(secret_key_store):
        """
        Creates a WebhooksHelperBuilder that will use the given SecretKeyStore.
        """
        return WebhooksHelperBuilder().with_marshaller(
            DefaultMarshaller.INSTANCE()).with_secret_key_store(
                secret_key_store)

    @staticmethod
    def create_helper(secret_key_store):
        web_hooks_helper_builder = Webhooks.create_helper_builder(secret_key_store)
        return web_hooks_helper_builder.build()
