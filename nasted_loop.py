# for x in range(1, 11):
#     for y in range(1, 11):
#         print(f"({x}, {y})")

list = [5, 2, 5, 2, 2]
for i in list:
    output =""
    for count in range(i):
        output += "x"
    print(output)