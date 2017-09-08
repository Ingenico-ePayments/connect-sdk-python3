class SecretKeyStore(object):
    """
    A store of secret keys. Implementations could store secret keys in a database, on disk, etc.
    """

    def get_secret_key(self, key_id):
        """
        :return: The secret key for the given key ID. Never None.
        :raises SecretKeyNotAvailableException: If the secret key for the given
        key ID is not available.
        """
        raise NotImplementedError
