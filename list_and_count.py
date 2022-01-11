numbers = [1,2,3,4,5,6,7,8,9,5,5,5,5,5,10,11,12,13,14,15,16,17,18,11,12,11,12,11,12,19,20,21,22,23,24,25,]
numbers.sort()
remove_duplicate = []
max_number = numbers[0]
minimum_number = numbers[0]
total_sum = 0
odd_number_list = []
even_number_list = []
for i in numbers:
    total_sum += i
    if i not in remove_duplicate:
        remove_duplicate.append(i)
    if i > max_number:
        max_number = i
    print(numbers.count(i), i)
    if i < minimum_number:
        minimum_number = i
    if i % 2 != 0:
        odd_number_list.append(i)
    if i % 2 == 0:
        even_number_list.append(i)
print("without duplicate",remove_duplicate)
print("Max_number from list: ",max_number)
print("Minimum_number: ", minimum_number)
print("Total sum of list: ", total_sum)
print("total sum: ", sum(numbers))
print("Odd number list and count of odd numbers:  ",len(odd_number_list), odd_number_list)
print("Even number list and count of even numbers: ",len(even_number_list), even_number_list)



