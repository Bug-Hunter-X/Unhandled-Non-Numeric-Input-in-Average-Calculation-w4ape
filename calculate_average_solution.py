def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric values
    return sum(numeric_numbers) / len(numeric_numbers) 
    #or use statistics.mean(numeric_numbers)