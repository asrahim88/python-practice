weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ").lower()
if (unit == "k" or unit == "l"):
        if unit == "k":
            convert = weight * 0.45
            print(f"you are {convert} pounds.")
        else:
            convert = weight / 0.45
            print(f"you are {convert} kilos.")
else:
    print("Please enter the proper unit as 'K' or 'L'")
