'''
------------------------------1st problem-------------------------------------------------
Convert input
User input to Number

Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.

Hints
Use input. By default, input gives you a string. Then use int and float to convert the input to a number. And then multiply them. That’s it.

'''
#1st way
# first_number = int(input("Enter first number as an integer: "))
# second_number = float(input("Enter second number as an float: "))
# multiply_result = first_number * second_number
# print(f"{first_number} X {second_number} = {multiply_result}")

# second way
# print("Result",int(input("integer number: ")) * float (input("float number: ")))


'''
------------------------------2nd problem--------------------------------------------------
Math power
Take two numbers from the users. Calculate the result of second number power of the first number.
Hints
To power, you will need to use two asterisks symbols (two multiplication symbols). For example 4 to the power 3 will be

'''
#1st way to calculate
# fNumber = int(input("Enter base number"))
# sNumber = int(input("Enter power number: "))
# result = fNumber ** sNumber
# print(f"{fNumber} power {sNumber} = {result}")

#2nd way to calculate
# print(int(input("Enter base number: ")) ** int(input("Enter power number: ")))
#3rd way to calculate power number
# print("Result:",pow(int(input("enter base number: ")), int(input("enter power number: "))))

'''
-------------------------------------3rd problem-------------------------------------------
Random Number
Create a random number between 0 to 10

Hints
To create a random number, you have to import a built-in library named random. And then you can call the randint method on it

'''
# 1st way to create a random number
# import random
# result = random.randint(0, 10)
# print(result)

#2nd way to create a random
# import random
# print(random.randint(0, 10))


'''
----------------------------------4th problem----------------------------------------------
Floor Division
Floor division means the integer part of a division operation. For example, if you divide 17/5 the quotient will be 3.4.

Hints
Floor division means the integer part of a division operation. For example, if you divide 17/5 the quotient will be 3.4.
'''
#1st way to solve this problem
# divisible = int(input("enter divisible number: "))
# divisor = int(input("enter divisor number: "))
# result = divisible // divisor
# print(result)

#2nd way to solve this problem
# print(int(input("enter divisible number: ")) // int(input("enter divisor number: ")))


'''
---------------------------------5th problem-----------------------------------------------
 Temporary variable
Swap two variables.To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.
Hints
To swap two variables, you can use a temp variable.
'''


#  1st way to solution this problem.
# a = 5
# b = 10
# print("Before swap: ",a, b)
# temp = a
# a = b
# b = temp
# print("after swap: ", a, b)


#2nd way to solution this problem.
# a = 5
# b = 10
# print("before swap: ",a, b)
# c = a
# a = b
# b = c
# print("after swap: ", a, b)

#3rd way to solution this problem.
# a = 5
# b = 10
# print("before swap: ",a, b)
# a, b = b, a
# print("after swap:", a, b)

'''
-----------------------------------------6th problem---------------------------------------
Divisible by 3 and 5
For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.
Hints
So, you have to check two conditions: make sure the number is divisible by 3, and also by 5. Hence, you will need to use two conditions.
'''

# 1st way to solve this problem
# user_number = int(input("enter any number: "))
# i = 1
# disabled_list = []
# while i <= user_number:
#     if i % 3 == 0 and i % 5 == 0:
#         disabled_list.append(i)
#     i += 1
# print(disabled_list)

#2nd way to solve this problem.

# user_number = int(input("Please enter any number: "))
# disbled_list = []
# for x in range(1,user_number + 1):
#     if x % 3 == 0 and x % 5 == 0:
#         disbled_list.append(x)
# print(disbled_list)

#3rd way to solve this problem.

# def disable_by_3_and_5(num):
#     disable_List = []
#     for i in range(1, num + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             disable_List.append(i)
#     return disable_List
# print(disable_by_3_and_5(int(input("enter any number: "))))


# 4th way to solve this problem
# print([x for x in range(1, int(input("enter any number:"))) if x % 3 == 0 and x % 5 == 0])

'''
-------------------------------------7th problem-------------------------------------------
Find the max number of two numbers.
Hints
Ask the user to enter two numbers.
Then, you can run a comparison to compare which one is larger.
Think about it and try yourself first.
'''

# 1st wat to solve this problem
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))

# def larger_number(num1, num2):
#     larger_number = 0
#     if num1 > num2:
#         larger_number = num1
#     else:
#         larger_number = num2
#     return larger_number
# print("larger_number is ",larger_number(num1, num2))

# 2nd way to solve this problem. 
# print("large number is ",(lambda a , b: a if a > b else b) (int(input("1st number: ")), int(input("2nd number: "))))

#3rd way to solve this problem
# print("large number is ",max(int(input("1st number: ")), int(input("2nd number: "))))

'''
-----------------------------------------8th problem---------------------------------------
Max of three. Find the largest of the three numbers.
Hints 
Ask the user to enter three numbers.
Then, you can run multiple comparisons to compare which one is the largest.
At first, you can consider that the first number is the largest.
Then compare the second number with the first number and the third number. If the second number is greater or equal to the first number and the second number is greater or equal to the third number, then the second number is the largest.
Similarly, compare the third number with the first or second number.
Otherwise, the first number will be the largest.Think about it. And try yourself first.

'''

#1st wat to solve this problem.
# num1 = int(input("enter 1st number: "))
# num2 = int(input("enter 2nd number: "))
# num3 = int(input("enter 3rd number: "))

# def get_largest_number_of_3(num1, num2, num3):
#     largest_number = 0
#     if num1 > num2 and num1 > num3:
#         largest_number = num1
#     elif num2 >= num1 and num2 >= num3:
#         largest_number = num2
#     elif num3 >= num1 and num3 >= num2:
#         largest_number = num3
#     else:
#         largest_number = num1
#     return largest_number
# print("largest number is: ",get_largest_number_of_3(num1, num2, num3))

#2nd way to solve this problem.
# def largest_number(num1, num2, num3):
#     largest_number = num1
#     if (num2 > num1) and (num2 > num3):
#         largest_number = num2
#     elif (num3 > num1) and (num3 > num2):
#         largest_number = num3
#     else:
#         largest_number = num1
#     return largest_number
# print(largest_number(int(input("enter 1st number: ")), int(input("enter 2nd number: ")), int(input("enter 3rd number: "))))
# 3rd way to solve this problem
# print('Max number: ',max(int(input("enter first number: ")), int(input("enter second number: ")), int(input("enter 3rd number: "))))

'''
----------------------------------9th problem----------------------------------------------
n
Average of numbers
The problem
Take numbers from a user and show the average of the numbers the user entered.

Hints
To solve this problem.
First, ask the user - How many numbers you want to enter?
Then, run a for-loop. Each time, take input from the user and put it in a list.
Once you get all the numbers, you can send the list to the sum function. The sum function will add all the numbers and give you the total.
Finally, divide the total by the number of elements the user entered.
That’s it, you will get the answer.
Want to try it yourself first? Go to the code editor and try it.

'''
# 1st wah to solve this problem
user_number = int(input("total quantity of list elements: "))
def get_average(num):
    total_item = []
    for i in range(num):
        list_item = int(input("Enter any number: "))
        total_item.append(list_item)
    total_sum = sum(total_item)
    average = total_sum / len(total_item)
    return average
print(get_average(user_number))



