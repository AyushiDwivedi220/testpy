import random
def Guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess= int(input("Guess a number between 1 and {x}:"))
        if guess< random_number:
            print("TOO LOW,GUESS A LARGER NUMBER AGAIN!")
        elif guess> random_number:
            print("TOO HIGH< GUESS A SMALLER NUMBER")
    
    print("YAYIEEE YOU GUESSED THE NUMBER!!!!!!")
    print("THE NUMBER IS:",random_number)



Guess(10)

  


