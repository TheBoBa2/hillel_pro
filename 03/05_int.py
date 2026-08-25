def divider(a, b):
    dividing = a // b
    remaining = a % b
    return dividing, remaining

first_input = int(input())
second_input = int(input())
print("Результат: ", divider(first_input, second_input))
