"""Defines functions to read contents from a file and close the file automatically,
if the relative path between this file and the resources folder is changed, this file should be updated"""
import os


def read_file(rel_path, *args, **kwargs):
    """Function to read the contents of a file located in the subfolder tests/resources into a string

    :param rel_path: the relative path to the file from tests/resources"""
    path = os.path.join(os.path.dirname(__file__), "resources", rel_path)
    with open(path, *args, **kwargs) as _file:
        return _file.read()

def write_file(rel_path, text, *args, **kwargs):
    """Function to write text to a file located in the subfolder tests/resources into a string

    :param rel_path: the relative path to the file from tests/resources
    :param text: text to write to the file
    :param args: arguments to delegate to the builtin open
    :param kwargs: arguments to delegate to the builtin open"""
    path = os.path.join(os.path.dirname(__file__), "resources", rel_path)
    with open(path, 'w+', *args, **kwargs) as _file:
        _file.write(text)
