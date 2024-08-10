print("WELCOME TO MY COMPUTER QUIZ")
play=input("Do you wanna play my quiz?....type (Y) for yes and (N) for no ")
if play != "y":
    print("Hawwwww.... you loose!")
    quit()

else:
    total_score=0
    a=input("What is the capital of India? ")
    if a.lower=="delhi":
        print("correct!!")
        total_score+=1
    else:
       print( "aww...incorrect")

    b=input("what is the rpeceding number of 1? ")
    if b=="0":
        print("correct!!")
        total_score+=1
    else:
        print("aww...incorrect")


    c=input("2+2= _ ?")
    if c.lower=="4":
        total_score += 1
        print("correct..your score rn is: ",total_score)
       
    else:
        print("Incorrectttt")

    d=input("what was the first capital of India?")
    if d.lower=="kolkata":
        total_score += 1
        print("correct")
    else:
        print("incorrect")

    print(total_score, "is your total scorrreeee")

    