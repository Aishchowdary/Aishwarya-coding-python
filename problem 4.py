def count_multiples(numbers, divisors):
    result = {divisor: sum(1 for num in numbers if num % divisor == 0) for divisor in divisors}
    return result

# Example usage
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
divisors = range(1, 10)

output = count_multiples(numbers, divisors)
print("Output:", output)
