import os


def file_name_conversion(file_path: str, extension_to_remove=None) -> str:
    """Convert a file.py to it's usable string name such as `file`.

    :param file_path: the absolute path of a file preferable the __file__ constant.
    :param extension_to_remove: the string that you find irrelevant and needs to be removed
    :return: str
    """

    name, extension = os.path.splitext(os.path.basename(file_path))

    return str.lower(str(name.split(extension_to_remove)[0]))
