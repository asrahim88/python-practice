tuple = (1, 20, 3, 5, 8, 7, 4, 6, 2, 10, 15, 9, 14, 12, 11, 13)
convert_list = list(tuple)
# convert_list.sort()
convert_list.reverse()
print("before: ",convert_list)
convert_list.sort(reverse=True)
print("After: ",convert_list)
convert_list.remove(20)
print("after remove: ",convert_list)

del tuple
print(tuple)