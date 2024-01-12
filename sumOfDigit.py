num = int(input("Enter the number: "))
sum = 0

while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10

print(sum)

"""
num, sum = 12345, 0


def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)


print(findSum(num, sum))

"""
