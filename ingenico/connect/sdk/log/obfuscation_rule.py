def obfuscate_all():
    """
    Returns an obfuscation rule (function) that will replace all characters with *
    """
    return lambda value: '*' * len(value) if value else value


def obfuscate_with_fixed_length(fixed_length):
    """
    Returns an obfuscation rule (function) that will replace values with a fixed length string containing only *
    """
    return lambda value: '*' * fixed_length


def obfuscate_all_but_first(count):
    """
    Returns an obfuscation rule (function) that will keep a fixed number of characters at the start,
    then replaces all other characters with *
    """
    def obfuscate_value(value):
        if not value:
            return value
        length = len(value)
        if length < count:
            return value
        end = '*' * (length - count)
        return value[:count] + end
    return obfuscate_value


def obfuscate_all_but_last(count):
    """
    Returns an obfuscation rule that will keep a fixed number of characters at the end,
    then replaces all other characters with *
    """
    def obfuscate_value(value):
        if not value:
            return value
        length = len(value)
        if length < count:
            return value
        start = '*' * (length - count)
        return start + value[-count:]
    return obfuscate_value
