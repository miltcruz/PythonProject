def clean_text(text: str) -> str:
    """
    Clean the input text by removing extra whitespace and converting to lowercase.
    
    Parameters:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    return text.strip().lower()


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def average(numbers: list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def is_in_range(value: int, min_value: int, max_value: int) -> bool:
    """
    Check if a value is within a specified range (inclusive).

    Parameters:
        value (int): The value to check.
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        bool: True if the value is within the range, False otherwise.
    """
    return min_value <= value <= max_value