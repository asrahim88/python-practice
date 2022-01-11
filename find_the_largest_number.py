num_list = [45, 46, 21, 78, 64, 100, 89,790]

largest_num = num_list[0]
for num in num_list:
    if num > largest_num:
        largest_num = num
print(f"find out largest number: {largest_num}")

max_num = max(num_list)
print(f"find out max number: {max_num}")

