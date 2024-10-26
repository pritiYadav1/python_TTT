# Flattening a list of lists
list_of_lists = [[1, 2, 3], [4, 5], [6]]
flattened = [num for sublist in list_of_lists for num in sublist]
print(flattened)

# Generating a Fibonacci Sequence
# Function to generate Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
    return fib[:n]

# Generate the first 10 Fibonacci numbers
fib_sequence = fibonacci(10)
print(fib_sequence)

