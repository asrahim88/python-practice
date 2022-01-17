num_list = [45, 54, 45, 12, 85, 75, 48, 75]

def remove_duplicate(n):
    without_duplicate = []
    for i in n:
        if i not in without_duplicate:
            without_duplicate.append(i)
    return without_duplicate
print(remove_duplicate(num_list))
