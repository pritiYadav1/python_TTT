a = input("Enter first number")
b = input("Enter second number")

# addition
print ('Sum: ', int(a) + int(b))  

# subtraction
print ('Subtraction: ', int(a) - int(b))   

# multiplication
print ('Multiplication: ', int(a) * int(b))  

# division
print ('Division: ', int(a) / int(b)) 

# floor division
print ('Floor Division: ', int(a) // int(b))

# modulo
print ('Modulo: ', int(a) % int(b))  

# a to the power b
print ('Power: ', int(a) ** int(b)) 

x = 5

x **= 3

print(x)



a = 10
b = 5 


a += b      
print(a)
a -=b
print(a)
a *=b
print(a)
a /=b
print(a)
a %=b
print(a)






x = 5
y = 3

print(x == y)

print(x != y)

print(x > y)

print(x < y)

print(x >= y)

print(x <= y)






x = 5




print(x > 3 and x < 10)


print(x > 3 or x < 4)

print(not(x > 3 and x < 10))




#identity

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


num1=6
num2=3
print(num1 & num2)

print(num1 | num2)

print(num1 ^ num2)

print(~(num1 & num2))

print((num1 & num2)<<3)

print((num1 & num2)>>3)










