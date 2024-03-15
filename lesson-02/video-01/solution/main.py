# Single, Specific, Short, and Surround

# Python method using list to filter and return even numbers
def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


# Python method using a lambda function to filter and return even numbers
def even_numbers_lambda(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


# Python method with a for loop to filter and return even numbers
def even_numbers_for_loop(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# Python method to filter even numbers from a list, handle non-intenger values, and raise errors
def even_numbers_safe(numbers):
    even_numbers = []
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("The list contains non-integer values")
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# Assert statements
assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert even_numbers([1, 3, 5]) == []
assert even_numbers([2, 4, 6]) == [2, 4, 6]
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]
