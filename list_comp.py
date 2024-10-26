squares = [x**2 for x in range(10)]
print(squares)


# List of squares of even numbers only with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


# Creating a matrix nested list
matrix = [[j for j in range(5)] for i in range(7)]
print(matrix)
