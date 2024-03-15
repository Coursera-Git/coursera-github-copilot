# Single, Specific, Short, and Surround

# Python method using list to filter and return even numbers.
# Zero-shot learning: no examples of expected output are provided. 
def filter_even_numbers_list(numbers):
    return [number for number in numbers if number % 2 == 0]

# Python method using a lambda function to extract even numbers from a list.
# One-shot learning: one example of expected output is provided.
def filter_even_numbers_lambda(numbers):
    """example of expected output: filter_even_numbers_lambda([1, 2, 3, 4, 5, 6]) == [2, 4, 6]"""
    return list(filter(lambda number: number % 2 == 0, numbers))

# Python method filter even numbers. 
# Few-shot learning: a few examples of expected output are provided.
def filter_even_numbers(numbers):
    """examples of expected output:
    filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    filter_even_numbers([1, 2, 3, 4, 5, 6, 'a']) == ValueError
    filter_even_numbers([1, 2, 3, 4, 5, 6, 7.0]) == ValueError
    """
    even_numbers = []
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError(f'Invalid input: {number} is not an integer.')
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
