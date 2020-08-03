import dryml


def main():
    filename = "/tests/data/inputs-repository/0-in.json"

    json_result_from_file = dryml.dryml_file_to_json(filename)
    print(json_result_from_file)
    print("=========================")

    s = open(filename, "r").read()
    json_result_from_string = dryml.dryml_string_to_json(s)
    print(json_result_from_string)
    print("=========================")


if __name__ == "__main__":
    main()
