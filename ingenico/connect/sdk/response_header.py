import re


def get_header_value(headers, header_name):
    """
    :return: The value of the header with the given name, or None if there
     was no such header.
    """
    if headers is None:
        return None
    for name, value in headers.items():
        if name.lower() == header_name.lower():
            return value
    return None


def get_header(headers, header_name):
    """
    :return: The header with the given name as a tuple with the name and
     value, or None if there was no such header.
    """
    if headers is None:
        return None
    for name, value in headers.items():
        if name.lower() == header_name.lower():
            return name, value
    return None


def get_disposition_filename(headers):
    """
    :return: The value of the filename parameter of the Content-Disposition
     header, or None if there was no such header or parameter.
    """
    header_value = get_header_value(headers, "Content-Disposition")
    if header_value is None:
        return None
    pattern = re.compile(
        "(?:^|;)\\s*filename\\s*=\\s*(.*?)\\s*(?:;|$)", re.IGNORECASE)
    match = pattern.search(header_value)
    if match is not None:
        filename = match.group(1)
        return __trim_quotes(filename)
    return None


def __trim_quotes(filename):
    if len(filename) < 2:
        return filename
    if (filename.startswith("\"") and filename.endswith("\"")) or \
       (filename.startswith("'") and filename.endswith("'")):
        return filename[1:-1]
    return filename
