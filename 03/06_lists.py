def average(numbers):
    result = sum(numbers) / len(numbers)
    return result

numbers = list(map(int, input().split()))
print("Результат: ", average(numbers))
