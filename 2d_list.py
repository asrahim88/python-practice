'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
access_list = matrix[0][0]
print(access_list)
'''
matrix = [
    ["Abdur Rahim", "Abdul Kayum", "Abdur Rouf", "Abdul High"],
    [45, 65, 43, 87],
    [78, 97, 23, 450]
]
print(f"abdur Rouf = {matrix[0][2]}")
print(f"450 = {matrix[2][3]}")

for row in matrix:
    for item in row:
        print(f"{item}")