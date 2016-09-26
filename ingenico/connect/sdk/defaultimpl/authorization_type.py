class AuthorizationType:
    def __init__(self):
        pass

    V1HMAC = "v1HMAC"
    AUTHORIZATION_TYPES = [V1HMAC]

    @staticmethod
    def get_authorization(name):
        if name in AuthorizationType.AUTHORIZATION_TYPES:
            return name
        else:
            raise RuntimeError("Authorization '{}' not found".format(name))
