name_collection = ["Tamim Iqbal Khan", "Imrul Kayes", "Sakib Al hasan", "Afif Hossain Dhrubo", "Mushfiqur Rahim", "Sheikh Mahedi", "Mahmudullah Riad", "Mehedi Hasan Miraz", "Taskin Ahmed", "Mustafizur Rahma", "Shariful Islam"]
print(len(name_collection))

new_list = []
for x in name_collection:
    if "s" in x:
        new_list.append(x)
print(new_list)

new_second_list = [x for x in name_collection if "r" in x]
print("check",new_second_list)

third_new_list = [x for x in name_collection if len(x)<12]
print("recheck",type(third_new_list), third_new_list)

player_list = [player for player in name_collection if player != "Mehedi Hasan Miraz"]
print("palyer new list", player_list)

print([number for number in range(1, 101) if number % 2 != 0])
print([number for number in range(1, 101) if number % 2 == 0])

