
# -----------------------------Iterative Way ---------------------------------------------

# 1st way to solve this problem. 
# user_number = int(input("enter any number: "))
# fact = 1
# for i in range(1, user_number + 1):
#     fact = fact * i
# print(fact)

# 2nd way to solve this problem  

# def get_factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact
# user_number = int(input("enter any number: "))
# print(get_factorial(user_number))

# 3rd way to solve this problem. 

# def get_fact(num):
#     i = 1
#     fact = 1
#     while i <= num:
#         fact = fact * i
#         i += 1
#     return fact
# print(get_fact(int(input("Enter any number: "))))

# 4th way to solve this problem.
# def get_fact(num):
#     fact = 1
#     while num >= 1:
#         fact = fact * num
#         num -= 1
#     return fact
# print(get_fact(int(input("enter any number: "))))

# 5th way to solve this problem.
# def get_fact_using_for_loop(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * (num+1 - i)
#     return fact
# print(get_fact_using_for_loop(int(input("any number: "))))
# 7! = (7-1)! * 7
# 7! = 7 * (7-1)!


# ---------------------------------------recursive way-----------------------------------
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)
print(recursive_factorial(int(input("any: "))))








