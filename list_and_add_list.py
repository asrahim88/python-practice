list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20]
print(list)
list.append("Amar sonar Bangla ami tomay valobasi.")
print(list)
list.insert(0, 5000)
print(list)
new_list = ["Sakib", "Tamim", "mushfiq"]
list.insert(3, new_list)
print(list)
second_new_list = [100, 200, 300 ,400, 500, 600, 700, 800, 900, 1000]
list.extend(second_new_list)
print(list)
tuple = tuple(list)
print(type(tuple))
print(tuple)

