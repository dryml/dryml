from json import JSONDecodeError
from typing import Type, Union

from dryml.helpers import (
    __dryml_runner,
    __load_dryml_string,
    __load_dryml_file,
)


def dryml_to_json(dryml_s: str) -> str:
    """
    Converts a DRYML Data (provided in the String) to a JSON Document (as a String).
    Examples: https://github.com/dryml/dryml/-/tree/master/tests/data  # TODO: Validate the Path when examples are ready

    :param dryml_s: DRYML Document as a String
    :return: JSON Document as a String
    """
    # TODO: Add Implementation
    return ""


def dryml_file_to_json(path: str) -> Union[Type[JSONDecodeError], str]:
    """
    Converts a DRYML Data (provided in the DRYML File) to a JSON Document (as a String).
    Examples: https://github.com/dryml/dryml/-/tree/master/tests/data  # TODO: Validate the Path when examples are ready

    :param path: DRYML Document as a Pointer to a File
    :return: JSON Document as a String
    """

    json_data = __load_dryml_file(path)

    return __dryml_runner(json_data)


def dryml_string_to_json(s: str) -> Union[Type[JSONDecodeError], str]:
    """
    Converts a DRYML Data (provided in the DRYML String) to a JSON Document (as a String).
    Examples: https://github.com/dryml/dryml/-/tree/master/tests/data  # TODO: Validate the Path when examples are ready

    :param s: DRYML Document as a String
    :return: JSON Document as a String
    """

    json_data = __load_dryml_string(s)

    return __dryml_runner(json_data)
