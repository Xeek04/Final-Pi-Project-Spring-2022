from random import randint
########################
play = input("Pick s for scissor, r for rock and p for paper: ")

if(play=="s"):
    val = 0
elif(play=="r"):
    val = 1
elif(play=="p"):
    val = 2
else:
    print("Pick either s, r or p")
    play = input("Pick s for scissor, r for rock and p for papoer: ")

def gamePlay(a, b):
    if(a==0):
        if(b==0):
            return "Tie!!"
        elif(b==1):
            return "Bot wins!!"
        else:
            return "Player wins!!"
        
    elif(a==1):
        if(b==1):
            return "Tie!!"
        elif(b==2):
            return "Bot wins!!"
        else:
            return "Player wins!!"

    elif(a==2):
        if(b==0):
            return "Bot wins!!"
        elif(b==1):
            return "Player wins!!"
        else:
            return "Tie"

bot = randint(0,3)
if(bot==0):
    b="Scissor"
elif(bot==1):
    b="Rock"
else:
    b="Paper"
print("The bot choose: {}".format(b))
print(gamePlay(val,bot))
