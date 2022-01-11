list = []
for num in range(1,101):
    list.append(num)
print(list.index(5))
print(sum([x for x in list]))
print(max([x for x in list]))
print(min([x for x in list]))
print("Even Number: ",[x for x in list if x % 2 == 0])
print("Odd number: ",[x for x in list if x % 2 != 0])
print("Sum of even number: ", sum([x for x in list if x % 2 == 0]))
print("Sum of odd number: ", sum([x for x in list if x % 2 != 0]))
print("odd number from 1 to 100: ", [odd for odd in [num for num in range(1,101)] if odd % 2 != 0])
print("even number from 1 to 100: ", [even for even in [num for num in range(1,101)   ] if even % 2 == 0])
print("sum of 1 to 100 nubmers: ", sum([num for num in [x for x in range(1,101)]]))
print("sum of all odd numbers from 1 to 10: ", sum([odd for odd in [num for num in range(1, 101)] if odd % 2 != 0]))
print("sum of all even numbers from 1 to 100: ", sum([even for even in [num for num in range(1, 101)] if even % 2 == 0]))

