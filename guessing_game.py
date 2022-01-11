import random
random_number = random.randint(0, 10)
limit_Count = 0
while limit_Count < 3:
    guess = int(input("guess any number 1 to 10: "))
    if guess == random_number:
        print("Congratulations! You won the game!")
        break
    limit_Count += 1
else:
    print("Sorry! you failed!")
