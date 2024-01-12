a = """Strings using double quaots."""
print(a)


a = '''Strings using single quoats.'''
print(a)


#using array
a = "Hello, World!"
print(a[1])


#using Loops
for x in "Priti":
  print(x) 


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("free is in the string ")



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#string slicing

b = "Hello, World!"
print(b[2:5])


a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip())


a = "Hello"
b = "World"
c = a + " " + b
print(c)


#formaat string

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



