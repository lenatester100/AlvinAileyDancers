import random
number = random.randint(1,10)

def randomnumber():
    attempt = 0
    print("  ")
    while attempt != 3:
        attempt = attempt + 1
        number = input("Would you please be so kind and guess a number from 1 to 10. You have three attempts.   ")
        if number >= number:
            print("That number is too high. Try again please.")
        else:
            print ("That number is to low. Try again please.")
if number == number:
        print ("thats the right number")

randomnumber()




