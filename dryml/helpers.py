from typing import Union, Type

from dryml.errors import DrymlDecodeError


# TODO: Unit Tests
def __dryml_runner(dryml_data):
    # TODO: Add Implementation below - get use of /dryml/drymlparser
    return "{}"


# TODO: Unit Tests
def __load_dryml_string(s: str) -> Union[Type[DrymlDecodeError], str]:
    try:
        # TODO: Add Implementation below
        dryml_data = ""
    except DrymlDecodeError:
        return DrymlDecodeError
    return dryml_data


# TODO: Unit Tests
def __load_dryml_file(path: str) -> Union[Type[DrymlDecodeError], str]:
    try:
        # TODO: Add Implementation below
        with open(path, "r") as dryml_file:
            dryml_data = ""
    except DrymlDecodeError:
        return DrymlDecodeError
    return dryml_data
