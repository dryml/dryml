import sys
from typing import List
from unittest import mock

from dryml import main


def run_dryml_cli(dryml_args: List[str]):
    with mock.patch.object(sys, "argv", ["dryml"] + dryml_args):
        return main.cli()


def ordered(obj: object) -> object:
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
