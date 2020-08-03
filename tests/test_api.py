import json

import pytest

import dryml

TEST_CASES_DATA_FILE = "./test-cases/test-cases-data.json"

with open(TEST_CASES_DATA_FILE) as api_test_cases_data_json_file:
    f = json.load(api_test_cases_data_json_file)

dryml_test_cases_data = []
dryml_test_cases_data.extend(
    [(i["input_dryml_file"], i["output_json_file"]) for i in f]
)


@pytest.mark.parametrize("input_dryml_file,output_json_file", dryml_test_cases_data)
def test_dryml_file_to_json(input_dryml_file, output_json_file):
    # Given
    with open(output_json_file) as output_json:
        expected_output_test_data_json = json.load(output_json)
    # When
    actual_output_test_data_s = dryml.dryml_file_to_json(input_dryml_file)
    actual_output_test_data_json = json.loads(actual_output_test_data_s)
    # Then
    assert actual_output_test_data_json == expected_output_test_data_json


@pytest.mark.parametrize("input_dryml_file,output_json_file", dryml_test_cases_data)
def test_dryml_string_to_json(input_dryml_file, output_json_file):
    # Given
    with open(input_dryml_file, "r") as input_json:
        given_input_test_data_s = input_json.read()
    with open(output_json_file) as output_json:
        expected_output_test_data_json = json.load(output_json)
    # When
    actual_output_test_data_s = dryml.dryml_string_to_json(given_input_test_data_s)
    actual_output_test_data_json = json.loads(actual_output_test_data_s)
    # Then
    assert actual_output_test_data_json == expected_output_test_data_json
