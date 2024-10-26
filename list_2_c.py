#List Comprehension with Functions

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0

temperatures_f = [32, 68, 100, 212]
temperatures_c = [fahrenheit_to_celsius(f) for f in temperatures_f]
print(temperatures_c)
