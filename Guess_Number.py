import random
print("Welcome to the computer guess game🔢🫵")
while True:
    customer = int(input("Guess the number from (1,10)  : "))

    random_num = random.randint(1,11)

    if customer == random_num:
        print("You guessed correctly 👏")
    else:
        print("You lost the game 🤦‍♂️")

    again = input("Do you want to play again (yes/no) : ").lower()
    if again !="yes":
        break

