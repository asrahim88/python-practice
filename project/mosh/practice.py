# '''
# if temperature is greater than 30
#     it's a hot day 
# otherwise if it's less than 10 
#     it's a cold day 
# otherwise
#     it's neither hot nor cold.
# '''

# user_temperature = int(input("Enter temperature: "))

# def temperature_check(temp):
#     if temp > 30:
#         return "it's a hot day."
#     elif temp < 10:
#         return "it's a cold day."
#     else:
#         return "it's neither hot nor cold."
# print(temperature_check(user_temperature))
# '''
# if name is less than 3 characters long
#     name must be at least characters
# otherwise if it's more than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good!
# '''
# user_name = input("Enter your name: ")

# def proper_name(name):
#     if len(name) < 3:
#         return "name must be at least 3 characters."
#     elif len(name) > 50:
#         return "name can be a maximum of 50 characters"
#     else:
#         return "name looks good!"
# print(proper_name(user_name))

weight = int(input("Weight: "))
unit = input("(L)bs or (K): ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pound.")
 
