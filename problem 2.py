def generate_series(a: int):
    series = [i for i in range(1, 2*a, 2)]
    return series

# Example usage
a = int(input("Enter a number: "))
output = generate_series(a)

print("Output:", ', '.join(map(str, output)))
