from .secret_key_not_available_exception import SecretKeyNotAvailableException
from .secret_key_store import SecretKeyStore


class InMemorySecretKeyStore(SecretKeyStore):
    """
    An in-memory secret key store.
    This implementation can be used in applications where secret keys can be
    specified at application startup.
    """

    @staticmethod
    def INSTANCE():
        return _IN_MEMORY_SECRET_KEY_CACHE_INSTANCE

    __store = {}

    def get_secret_key(self, key_id):
        try:
            secret_key = self.__store[key_id]
        except KeyError:
            raise SecretKeyNotAvailableException(
                "could not find secret key for key id " + key_id, key_id)
        return secret_key

    def store_secret_key(self, key_id, secret_key):
        """
        Stores the given secret key for the given key ID.
        """
        if key_id is None or not key_id.strip():
            raise ValueError("key_id is required")
        elif secret_key is None or not secret_key.strip():
            raise ValueError("secret_key is required")
        self.__store[key_id] = secret_key

    def remove_secret_key(self, key_id):
        """
        Removes the secret key for the given key ID.
        """
        self.__store.pop(key_id)

    def clear(self):
        """
        Removes all stored secret keys.
        """
        self.__store.clear()


_IN_MEMORY_SECRET_KEY_CACHE_INSTANCE = InMemorySecretKeyStore()
