def generate_series(a: int):
    series = []
    for i in range(1, a + 1, 2):  # Only incrementing by 2 for odd numbers
        series.append(i)
    return series

# Example usage
a = int(input("Enter a number: "))
output = generate_series(a)

print("Output:", ', '.join(map(str, output)))
