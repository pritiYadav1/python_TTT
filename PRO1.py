distance = int(input("Enter distance:"))
if distance>=1 and distance<=50:
    fare = distance * 8
elif distance>=51 and distance<=100:
    fare = distance * 10
elif distance>100:
    fare = distance * 12
else:
    print("Invalid fare")
print("The total fare is:",fare)
