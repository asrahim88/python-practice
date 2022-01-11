list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#total len of list 
print("Total length of list: ",len(list))

#access list
print(list[0])
print(list[:15])
print(list[5:])
print(list[4:18])
print(list[-5:-1])
print(True if 50 in list else False)
print(7 if 7 in list else False)

#check item position
print(list.index(8))


#change list 
list[0] = "Abdur Rahim"
print(list)
list[3] = 400
print(list)
list[1:7] = ["Abdur ahim"]
print(list)
list[3:8] = ["Sakib Al Hasan", "Tamim Iqbal Khan", "Mushfiqur Rhaim", "Mahmudullah Riad"]
print(list)

#add list items 
list.append(800)
print(list)
list.insert(4, "Mashrafee Bin Mortaza")
print(list)
list.insert(0, 500)
print(list)
new_list = ["father", "mother", "brother", "sister"]
list.extend(new_list)
print(list)

#remove list items 
list.pop()
print(list)
list.remove(list[0])
print(list)
list.pop(0)
print(list)
del list[0]
print(list)
list.remove(8)
print(list)
list.clear()
print(list)
del list
print(list)

#create new list using range function
lit0 = []
for num in range(1, 101):
    lit0.append(num)
print("new list create by range function: ",lit0)

#sum of 1 to 100 numbers 
total = 0
for num in lit0:
    total += num
print(total)

# sum off all numbers in list 
result = sum(lit0)
print(result)

#get max number from 1 to 100 numbers 
max_number = lit0[0]
for max_num in lit0:
    if max_num > max_number:
        max_number = max_num
print(max_number)

#get max_number 1 to 100 numbers 
max = max(lit0)
print(max)

#get min_num 1 to 100 numbers
min_number = lit0[0]
for min_num in lit0:
    if min_num < min_number:
        min_number = min_num
print(min_number)

#get min_number 1 to 100 numbers.
min = min(lit0)
print(min)

#get all even number 1 to 100 numbers.
get_all_even_numbers = []
for num in lit0:
    if num % 2 == 0:
        get_all_even_numbers.append(num)
print(get_all_even_numbers)

#sum off all even numbers 1 to 100 numbers.
get_all_even_numbers = []
sum0 = 0
for num in lit0:
    if num % 2 == 0:
        get_all_even_numbers.append(num)
for even in get_all_even_numbers:
    sum0 += even
print("Total sum",sum0)

#sum of all even numbers 1 to 100 numbers
get_all_even_numbers = []
for num in lit0:
    if num % 2 == 0:
        get_all_even_numbers.append(num)
print("Total sum: ",sum(get_all_even_numbers))

#get all odd numbers 1 to 100 numbers.
get_all_odd_number = []
for num in lit0:
    if num % 2 != 0:
        get_all_odd_number.append(num)
print(get_all_odd_number)

#sum of all odd numbers 1 to 100 numbers.
get_all_odd_number = []
sum01 = 0
for num in lit0:
    if num % 2 != 0:
        get_all_odd_number.append(num)
for odd in get_all_odd_number:
    sum01 += odd
print("Sum of odd numbers: ", sum01)

#sum of all odd numbers 1 to 100 numbers.
get_all_odd_numbers = []
for num in lit0:
    if num % 2 !=0:
        get_all_odd_numbers.append(num)
print("sum of all odd numbers: ",sum(get_all_odd_numbers))

# remove duplicate item or numbers.
number_list = [54, 15, 45, 54, 78, 96, 16, 32, 45, 10, 25,]
without_duplicate = []
for num in number_list:
    if num not in without_duplicate:
        without_duplicate.append(num)
number_list.sort()
print("Duplicate: ", number_list)
without_duplicate.sort()
print("remove duplicate: ", without_duplicate)

#duplicate number count and what is it
a = ["a", "b", "a", 54, 54, 78, 15, 856]
result = dict((i, a.count(i))  for i in a)
print(result)


some_list=['a','b','c','b','d','m','n','n']

my_list=sorted(some_list)
 
duplicates=[]
for i in my_list:
    # print(i)
     if my_list.count(i)>1:
         if i not in duplicates:
             duplicates.append(i)
 
print(duplicates)

#Duplicates count number in list
list0_number_all = [1, 87, 65, 56, 1, 8, 87, 5, 6, 78,2]
duplicate = []
for i in list0_number_all:
    if list0_number_all.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print("check",duplicate)

#varaties item in list 
nums_list = [45, 12, 12, 54, 10, 5, 6, 3, 14, 70, 32, 56]
print(nums_list)
nums_list.sort()
print(nums_list)
print("Testing",sorted(nums_list))
nums_list.sort(reverse = True)
print(nums_list)
