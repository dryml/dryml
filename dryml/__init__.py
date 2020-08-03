"""Converts DRYML File to the JSON File,
in conformance with the Standardised Process Definition JSON Schema
(https://gitlab.com/aiforse/aiforse-framework/-/blob/master/Integration%20Framework%20(AIFORSE_intgF)/Schemas/aiforse-integration-framework---process-json-schema.json)

https://github.com/dryml/dryml
https://pypi.python.org/pypi/dryml  # TODO: Publish DRYML Package to the PyPI
"""

from dryml.apis import (
    dryml_file_to_json,
    dryml_string_to_json
)
from dryml.version import __version__

__author__ = "Valentin Grigoryevskiy"
__license__ = "MIT"
__version__ = __version__
