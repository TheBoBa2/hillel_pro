def is_subset(first_set, second_set):
    result = first_set.issubset(second_set)
    return result


first_input = set(map(int, input().split()))
second_input = set(map(int, input().split()))

print("Результат: ", is_subset(first_input, second_input))