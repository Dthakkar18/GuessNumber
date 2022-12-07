
import random

print("\nI am going to pick a number...")
low = int(input("What is the lower bound: "))
high = int(input("What is the upper bound: "))

computer_choice = random.randint(low,high)
print("\nI am thinking of a number " + str(low) + " and " + str(high))
print("Take a guess\n")

tries = 1
while True:
    try:  
        my_choice = int(input('num: '))
        if my_choice < computer_choice:
            print("too small\n")
            tries += 1
        elif my_choice > computer_choice:
            print("too big\n")
            tries += 1
        else:
            print('\nYou got it!')
            print("It took you " + str(tries) + ' tries!')
            break

    except Exception:
        print("\nMake sure you type a number\n")


