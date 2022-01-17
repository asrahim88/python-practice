all_num = [45, 20, 98,100005, 65, 45, 35, 100, 1001]

def largest_number(n):
    largest = n[0]
    for i in n:
        if i >= largest:
            largest = i
    return largest
print(largest_number(all_num))
print(max(all_num))