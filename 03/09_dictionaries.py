def join_dictionaries(first_dict, second_dict):
    result = {**first_dict, **second_dict}
    return result

first_input = {
    "animal": "Cat",
    "name": "Zeus"
}

second_input = {
    "age": 13,
    "breed": "British"
}

print("Результат:", join_dictionaries(first_input, second_input))
