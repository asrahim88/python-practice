name_collection = ["Tamim Iqbal Khan", "Imrul Kayes", "Sakib Alhasan", "Afif Hossain Dhrubo", "Mushfiqur Rahim", "Mahmudulullah Rad", "Sheikh Mahedi", "Sayfuddin", "Taskin Ahmed", "Mustafizur Rahman", "Shariful Islam"]
print(name_collection)
print(len(name_collection))
# suing for loop
for name in name_collection:
    print(name)
#USING RANGE FOR
for name in range(len(name_collection)):
    print(name_collection[name])


number = 0
while number< len(name_collection):
    print("using while loop",name_collection[number])
    number += 1

#one line code for list using for-loop
[print("this is my one line code result. ",x) for x in name_collection]

id = [101, 102, 103, 104, 105, 106, 107, 108, 109,110, 111, 112, 113, 114, 115, 116, 117]
[print("one line code",id) for id in id]
