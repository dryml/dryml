#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

"""The command line interface to dryml"""

import argparse
import sys
import textwrap

from dryml import dryml_file_to_json, dryml_string_to_json
from dryml.errors import DrymlError
from dryml.version import __version__


def print_version() -> None:
    print(__version__)


DRYML_DESCRIPTION = textwrap.dedent(
    f"""
Converts a DRYML Document to a JSON Document.
"""
)


class LineWrapRawTextHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _split_lines(self, text, width):
        text = self._whitespace_matcher.sub(" ", text).strip()
        return textwrap.wrap(text, width)


def run_dryml_command(args: argparse.Namespace):
    setup(args)

    if args.command:
        if args.path:
            target_json = dryml_file_to_json(args.dryml_input)
        else:
            target_json = dryml_string_to_json(args.dryml_input)

        print(target_json)
        return 0
    else:
        return 1


def _add_run(subparsers):
    p = subparsers.add_parser(
        "dryml-to-json",
        formatter_class=LineWrapRawTextHelpFormatter,
        help=(
            "Provide the DRYML Document String or the Path to the DRYML File you want to convert to a JSON Document."
        ),
    )
    p.add_argument(
        "dryml_input",
        metavar="dryml-input",
        help="The DRYML Document String or the Path to the DRYML File you want to convert.",
    )
    p.add_argument(
        "--path",
        "-p",
        help="Indicate that the path to the DRYML File was provided in the dryml-input parameter.",
        action="store_true",
    )
    p.set_defaults(subparser=p)


def get_command_parser():
    parser = argparse.ArgumentParser(
        prog="dryml",
        formatter_class=LineWrapRawTextHelpFormatter,
        description=DRYML_DESCRIPTION,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        description="Get help for specific command:\n> dryml dryml-to-json --help",
    )

    _add_run(subparsers)

    parser.add_argument("--version", action="store_true", help="Print version and exit")
    return parser


def setup(args):
    if "version" in args and args.version:
        print_version()
        sys.exit(0)


def cli() -> int:
    """Entry point from command line"""
    try:
        parser = get_command_parser()

        parsed_dryml_args = parser.parse_args()
        setup(parsed_dryml_args)

        if not parsed_dryml_args.command:
            parser.print_help()
            return 1
        return run_dryml_command(parsed_dryml_args)
    except DrymlError as e:
        print(str(e), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 1


if __name__ == "__main__":
    sys.exit(cli())
