import random

def play():
    user=input("PICK (R) FOR ROCK, (S) FOR SCISSORS AND (P)FOR PAPER:")
    computer =random.choice(["R","S","P"])

    if user == computer:
        return "it's a tie!!!"
    
    if is_win(user,computer)==True:
        return ("yayayaieee,YOW WON ")
    else:
        return (" you lost.....")
    
def is_win(player,opponent):
    if (player=="R" and opponent =="S") or (player== "P" and opponent =="R") or (player== "S" and opponent == "P"):
        return True 
    
print(play())
