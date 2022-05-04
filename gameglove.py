from random import randint

botwin = 0
playerwin = 0

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

while(botwin < 3 and playerwin < 3):
    
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


    bot = randint(0,3)
    if(bot==0):
        b="Scissor"
    elif(bot==1):
        b="Rock"
    else:
        b="Paper"
    
    # keeping track of the players and bots wins
    if(gamePlay(val,bot)=="Bot wins!!"):
        botwin += 1
    if(gamePlay(val,bot)=="Player wins!!"):
        playerwin += 1

    print("The bot choose: {}".format(b))
    print(gamePlay(val,bot))
    print("Player's wins: {}".format(playerwin))
    print("Bot's wins: {}".format(botwin))

print(10*"===")
if(botwin==3):
    print("The bot wins {} to {}".format(botwin, playerwin))
else:
    print("The player wins {} to {}".format(playerwin, botwin))
print(10*"===")
