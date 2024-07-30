import random

def Guesscomputer(x):
    low =1
    high=x
    feedback=" "
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f"if {guess} is too high(h),too low(l) or correct(c) enter the required letter: ")
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess +1
    print(f"yayayiee,The number was {guess}")

Guesscomputer(10)