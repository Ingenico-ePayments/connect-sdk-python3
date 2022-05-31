from .obfuscation_rule import obfuscate_with_fixed_length


class HeaderObfuscator:
    """
    A class that can be used to obfuscate headers.
    """

    __obfuscation_rules = None

    def __init__(self, additional_rules=None):
        """
        Creates a new  header obfuscator.
        This will contain some pre-defined obfuscation rules, as well as any provided custom rules

        :param additional_rules: An optional mapping from property names to obfuscation rules,
         where an obfuscation rule is a function that obfuscates a single string,
        """
        self.__obfuscation_rules = {
            "authorization": obfuscate_with_fixed_length(8),
            "www-authenticate": obfuscate_with_fixed_length(8),
            "proxy-authenticate": obfuscate_with_fixed_length(8),
            "proxy-authorization": obfuscate_with_fixed_length(8),
            "x-gcs-authentication-token": obfuscate_with_fixed_length(8),
            "x-gcs-callerpassword": obfuscate_with_fixed_length(8),
        }
        if additional_rules:
            for name, rule in additional_rules.items():
                name = name.lower()
                self.__obfuscation_rules[name] = rule

    def obfuscate_header(self, header_name, value):
        """
        Obfuscates the value for the given header as necessary.
        """
        header_name = header_name.lower()
        obfuscation_rule = self.__obfuscation_rules.get(header_name)
        if obfuscation_rule:
            return obfuscation_rule(value)
        return value

    @staticmethod
    def default_header_obfuscator():
        return _DEFAULT_HEADER_OBFUSCATOR


_DEFAULT_HEADER_OBFUSCATOR = HeaderObfuscator()
