def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


numbers = list(map(int, input().split()))
print("Результат: ", even_numbers(numbers))
