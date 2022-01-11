text1 = "I am a student. I am "
age = 34
print(text1 + format(age), "years old.")

text2 = "I am a student. I am "
age = 50
print(text2 + format(age), "years old.")
print(f"{text2} {age} years old.")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))