import codecs
import re

from .obfuscation_rule import obfuscate_all, obfuscate_with_fixed_length, obfuscate_all_but_first, obfuscate_all_but_last


class BodyObfuscator:
    """
    A class that can be used to obfuscate properties in JSON bodies.
    """

    __obfuscation_rules = None
    __parameter_names = None

    def __init__(self, additional_rules=None):
        """
        Creates a new  body obfuscator.
        This will contain some pre-defined obfuscation rules, as well as any provided custom rules

        :param additional_rules: An optional mapping from property names to obfuscation rules,
         where an obfuscation rule is a function that obfuscates a single string,
        """
        self.__obfuscation_rules = {
            "cardNumber": obfuscate_all_but_last(4),
            "expiryDate": obfuscate_all_but_last(2),
            "cvv": obfuscate_all(),
            "iban": obfuscate_all_but_last(4),
            "accountNumber": obfuscate_all_but_last(4),
            "reformattedAccountNumber": obfuscate_all_but_last(4),
            "bin": obfuscate_all_but_first(6),
            "value": obfuscate_all(),
            "keyId": obfuscate_with_fixed_length(8),
            "secretKey": obfuscate_with_fixed_length(8),
            "publicKey": obfuscate_with_fixed_length(8),
            "userAuthenticationToken": obfuscate_with_fixed_length(8),
            "encryptedPayload": obfuscate_with_fixed_length(8),
            "decryptedPayload": obfuscate_with_fixed_length(8),
            "encryptedCustomerInput": obfuscate_with_fixed_length(8),
        }
        if additional_rules:
            for name, rule in additional_rules.items():
                self.__obfuscation_rules[name] = rule

        self.__parameter_names = tuple(self.__obfuscation_rules.keys())

    @staticmethod
    def __build_property_pattern(property_names):
        if not property_names:
            return re.compile("$^")
        s = "([\"'])("
        for p in property_names:
            s += '|' + re.escape(p)
        s += ")\\1\\s*:\\s*(?:([\"'])(.*?)(?<!\\\\)\\3|([^\"'\\s\\[\\{]((?!,)\\S)*))"
        return re.compile(s, re.DOTALL)

    def __obfuscate_value(self, property_name, value):
        obfuscation_rule = self.__obfuscation_rules.get(property_name)
        if obfuscation_rule:
            return obfuscation_rule(value)
        return value

    def obfuscate_body(self, body, charset=None):
        """
        Obfuscates the body from the given stream as necessary.
        :param body: The body to obfuscate, as string or bytes.
        :param charset: The charset to use to read the body bytes.
        """
        if charset:
            body = codecs.decode(body, charset)

        if body is None:
            return None
        if not body:
            return ""
        index = 0
        s_obfuscate = ""
        pattern = self.__build_property_pattern(self.__parameter_names)
        matcher = pattern.finditer(body)
        for x in matcher:
            property_name = x.group(2)
            value = x.group(4)
            value_start = x.start(4)
            value_end = x.end(4)
            if not value:
                value = x.group(5)
                value_start = x.start(5)
                value_end = x.end(5)
            obfuscated_value = self.__obfuscate_value(property_name, value)
            s_obfuscate += body[index:value_start] + obfuscated_value
            index = value_end
        return s_obfuscate + body[index:]

    @staticmethod
    def default_body_obfuscator():
        return _DEFAULT_BODY_OBFUSCATOR


_DEFAULT_BODY_OBFUSCATOR = BodyObfuscator()
