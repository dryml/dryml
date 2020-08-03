#!/usr/bin/env python3
import json
import sys
from unittest import mock

import pytest

from tests.helpers_tests import run_dryml_cli

TEST_CASES_DATA_FILE = "./test-cases/test-cases-data.json"

with open(TEST_CASES_DATA_FILE) as cli_test_cases_data_json_file:
    f = json.load(cli_test_cases_data_json_file)

dryml_test_cases_data = []
dryml_test_cases_data.extend(
    [(i["input_dryml_file"], i["output_json_file"]) for i in f]
)
dryml_test_cases_data.extend(
    [(i["input_dryml_file"], i["output_json_file"]) for i in f]
)


# dryml dryml-to-json "./data/inputs-repository/0-in.json" --path
@pytest.mark.parametrize(
    "input_dryml_file,output_json_file", dryml_test_cases_data
)
def test_dryml_file_to_json(
        capsys, input_dryml_file, output_json_file
):
    # Given
    with open(output_json_file) as output_json:
        expected_output_test_data_json = json.load(output_json)
    print(json.dumps(expected_output_test_data_json, indent=2))
    out, err = capsys.readouterr()
    # When
    run_dryml_cli(["dryml-to-json", input_dryml_file, "--path"])
    # Then
    captured = capsys.readouterr()
    assert captured.out == out


# dryml dryml-to-json "{...}"
@pytest.mark.parametrize("input_dryml_file,output_json_file", dryml_test_cases_data)
def test_dryml_string_to_json(capsys, input_dryml_file, output_json_file):
    # Given
    with open(input_dryml_file, "r") as input_json:
        given_input_test_data_s = input_json.read()
    with open(output_json_file) as output_json:
        expected_output_test_data_json = json.load(output_json)
    print(json.dumps(expected_output_test_data_json, indent=2))
    out, err = capsys.readouterr()
    # When
    run_dryml_cli(["dryml-to-json", given_input_test_data_s])
    # Then
    captured = capsys.readouterr()
    assert captured.out == out


# dryml --help
def test_help_text(monkeypatch, capsys):
    # When
    mock_exit = mock.Mock(side_effect=ValueError("raised in test to exit early"))
    with mock.patch.object(sys, "exit", mock_exit), pytest.raises(
            ValueError, match="raised in test to exit early"
    ):
        run_dryml_cli(["--help"])
    # Then
    captured = capsys.readouterr()
    assert "Provide the DRYML Document String or the Path" in captured.out


# dryml dryml-to-json -h
# TODO: Works when run from the CLI, but not here... FixIt
@pytest.mark.skip(reason="Works when run from the CLI, but not here. ")
def test_simple_run(monkeypatch, capsys):
    # When
    run_dryml_cli(["dryml-to-json", "-h"])
    # Then
    captured = capsys.readouterr()
    assert "Provide the DRYML Document String or the Path" not in captured.out
