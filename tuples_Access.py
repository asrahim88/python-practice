
tuples = (45, 85, "Bismiallahir Rahmanir Rahim", True, False, [45, 85, 40, "Alhamdulillah", [45, 52, 87, True, 50, ["Hi", "hello", "World"]]])
# print(tuples)

#1st Way to access tuples
print(tuples[0])

#2nd way to access tuples
print(tuples[5:])

# 3rd way access to  tupels
print(tuples[:5])

# 4th way to access in tuples
print(tuples[3:5])

# 5th way to access in tuples
print("result: ",tuples[-1])
print(tuples[5][4][5][-1])

#6th way to access in tuples
if "hello" in tuples[5][4][5]:
    print("yes! This word stays in this list.")

# 7th way to access in tuples.

print(tuples[-4:-2])