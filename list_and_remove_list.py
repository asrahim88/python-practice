list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(list)
list.pop()
print(list)
list.pop(1)
print('before remove',list)
list.remove(1)
print('after',list )
list.remove(10)
print(f"10 is removed {list}")
list.remove(list[0])
print(f"3 is removed {list}")
del list[0]
print(list)
list.clear()
print(list)
del list
print(list)