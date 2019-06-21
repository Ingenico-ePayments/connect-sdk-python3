import codecs
import re


class LoggingUtil:
    """
    A utility class to support logging.
    """

    def __init__(self):
        pass

    class Obfuscator(object):

        __obfuscators = None
        __obfuscator_keys = None

        def __init__(self, obfuscators, case_insensitive, fixed_length=None,
                     keep_start_count=None, keep_end_count=None, full=None):
            self.case_insensitive = case_insensitive
            if fixed_length:
                for name, count in list(fixed_length.items()):
                    obfuscators[name] = self.ValueObfuscator(count, 0, 0)
            if keep_start_count:
                for name, count in list(keep_start_count.items()):
                    obfuscators[name] = self.ValueObfuscator(0, count, 0)
            if keep_end_count:
                for name, count in list(keep_end_count.items()):
                    obfuscators[name] = self.ValueObfuscator(0, 0, count)
            if full:
                for name in full:
                    obfuscators[name] = self.ValueObfuscator(0, 0, 0)
            self.__obfuscators = tuple(obfuscators.items())
            self.__obfuscator_keys = tuple(obfuscators)

        def obfuscate_value(self, key, value):
            obfuscator = self.find_obfuscator(key)
            if obfuscator is not None:
                return obfuscator.obfuscate_value(value)
            return value

        def find_obfuscator(self, key):
            for item in self.__obfuscators:
                x, y = item
                if self.case_insensitive:
                    if x.lower() == key.lower():
                        return y
                else:
                    if x == key:
                        return y
            return None

        class ValueObfuscator:
            __mask_character = None
            __fixed_length = None
            __keep_start_count = None
            __keep_end_count = None

            def __init__(self, fixed_length, keep_start_count, keep_end_count):
                self.__mask_character = '*'
                self.__fixed_length = fixed_length
                self.__keep_start_count = keep_start_count
                self.__keep_end_count = keep_end_count

            def obfuscate_value(self, value):
                if not value:
                    return value
                if self.__fixed_length > 0:
                    return self.__mask_character * self.__fixed_length
                if self.__keep_start_count == 0 and self.__keep_end_count == 0:
                    return self.__mask_character * len(value)
                if len(value) < self.__keep_start_count + self.__keep_end_count:
                    return value
                start = self.__keep_start_count
                end = len(value) - self.__keep_end_count
                value_between = self.__mask_character * (end - start)
                return value[:start] + value_between + value[end:]

        def build_property_pattern(self, property_names):
            if not property_names:
                return re.compile("$^")
            s = "([\"'])("
            for p in property_names:
                s += '|' + re.escape(p)
            s += ")\\1\\s*:\\s*(?:([\"'])(.*?)(?<!\\\\)\\3|([^\"'\\s]\\S*))"
            return re.compile(s, re.DOTALL)

        def obfuscate(self, body):
            if body is None:
                return None
            if not body:
                return ""
            index = 0
            s_obfuscate = ""
            pattern = self.build_property_pattern(self.__obfuscator_keys)
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
                obfuscated_value = self.obfuscate_value(property_name, value)
                s_obfuscate += body[index:value_start] + obfuscated_value
                index = value_end
            return s_obfuscate + body[index:]

    __fixed = dict([("keyId", 8), ("secretKey", 8), ("publicKey", 8),
                    ("userAuthenticationToken", 8), ("encryptedPayload", 8),
                    ("decryptedPayload", 8), ("encryptedCustomerInput", 8)])
    __start = dict([("bin", 6)])
    __end = dict([("cardNumber", 4), ("expiryDate", 2), ("iban", 4),
                  ("accountNumber", 4), ("reformattedAccountNumber", 4)])
    __all = ["value", "cvv"]
    __property_obfuscator = Obfuscator({}, False, __fixed, __start, __end, __all)

    __fixed_length = dict([("Authorization", 8), ("WWW-Authenticate", 8),
                           ("Proxy-Authenticate", 8), ("Proxy-Authorization", 8),
                           ("X-GCS-Authentication-Token", 8),
                           ("X-GCS-CallerPassword", 8)])
    __header_obfuscator = Obfuscator({}, True, __fixed_length)

    @staticmethod
    def obfuscate_body(arg, charset=None):
        """
        Obfuscates the body from the given stream as necessary.
        :param charset: The charset to use to read the body input stream.
        """
        if charset is None:
            return LoggingUtil.__property_obfuscator.obfuscate(arg)
        else:  # possible dead code
            return LoggingUtil.obfuscate_body(codecs.decode(arg, charset))

    @staticmethod
    def obfuscate_header(name, value):
        """
        Obfuscates the value for the given header as necessary.
        """
        return LoggingUtil.__header_obfuscator.obfuscate_value(name, value)
