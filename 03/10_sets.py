def join_sets(first_set, second_set):
    result = first_set | second_set
    return result


first_input = set(map(int, input().split()))
second_input = set(map(int, input().split()))

print("Об'єднання: ", join_sets(first_input, second_input))
