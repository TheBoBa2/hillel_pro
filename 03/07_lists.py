def common_elements(first_list, second_list):
    result = []
    for element in first_list:
        if element in second_list:
            result.append(element)
    return result

first_input = list(map(int, input().split()))
second_input = list(map(int, input().split()))

print("Результат: ", common_elements(first_input, second_input))
