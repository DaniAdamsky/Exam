def find_median(numbers: list) -> float:
    """function gets a list of numbers and returns the median,
    if len is even, return avg of both medians"""
    numbers= sorted(numbers)
    n = len(numbers)
    if n % 2 != 0:
        median = float(numbers[n // 2])
        return median
    else:
        median1 = numbers[n // 2]
        median2 = numbers[n // 2 - 1]
        median = (median1 + median2) // 2
        return float(median)

print(find_median([7, 2, 10, 9]))