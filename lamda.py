# print((lambda a : a * a * a)(3))

# Mathmetical Operations 

f_num = int(input("Enter first number: "))
s_num = int(input("Enter second number: "))


print("Addition Result: ",(lambda fNum, sNum : fNum + sNum) (f_num, s_num))
print("Substraction Result: ", (lambda fNum, sNum : fNum - sNum) (f_num, s_num))
print("Multiplication Result: ", (lambda fNum, sNum : fNum * sNum) (f_num, s_num))
print("Division Result: ", (lambda fNum, sNum : fNum / sNum) (f_num, s_num))
print("Remainder Result: ", (lambda fNum, sNum : fNum % sNum) (f_num, s_num))
print("Exponentiation Result:", (lambda fNum, sNum : fNum // sNum) (f_num, s_num))
print("Power Result: ", (lambda fNum, sNum : fNum ** sNum) (f_num, s_num))
