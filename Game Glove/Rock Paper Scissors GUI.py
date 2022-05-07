from msilib import text
from tkinter import *
# import RPi.GPIO as GPIO
from time import sleep
from random import randint
from serial import Serial

ser=Serial('COM5',9600,timeout=None)
ser.flush()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

botwin = 0
playerwin = 0
red = 17
green = 16
blue = 13
yellow = 12

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

GPIO.output(red, 0)
GPIO.output(green, 0)
GPIO.output(yellow, 0)
GPIO.output(blue, 1)

class CPU:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.outs = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def outs(self):
        return self._outs

    @outs.setter
    def outs(self, value):
        self._outs = value

    def addOuts(self, out, room):
        self._outs[out] = room

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createOutputs(self):
        r = CPU("Rock", "rock.gif")
        p = CPU("Paper", "paper.gif")
        s = CPU("Scissors", "scissors.gif")
        n = CPU("Blank", "start.gif")

        n.addOuts("r", r)
        n.addOuts("p", p)
        n.addOuts("s", s)

        r.addOuts("r", r)
        r.addOuts("p", p)
        r.addOuts("s", s)

        s.addOuts("r", r)
        s.addOuts("p", p)
        s.addOuts("s", s)

        p.addOuts("r", r)
        p.addOuts("p", p)
        p.addOuts("s", s)

        Game.currentOutput = n

    def setupGUI(self):
        self.pack(fill = BOTH, expand = 1)

        # shows the player input
        Game.player_input = Entry(self, bg = "white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side = BOTTOM, fill = X)
        Game.player_input.focus()

        #image on left of GUI
        img = None
        Game.image = Label(self, width = WIDTH // 2, image = img)
        Game.image.image = img
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False)

        #text on right of GUI
        text_frame = Frame(self, width = WIDTH // 2)
        Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
        Game.text.pack(fill = Y, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)

    def setCPUImage(self):
        Game.img = PhotoImage(file = Game.currentOutput.image)
        Game.image.config(image = Game.img)
        Game.image.image = Game.img

    def mainText(self, status):
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)
        Game.text.insert(END, "Welcome to the Game Glove!\n")
        global botwin
        global playerwin
        global blue
        GPIO.output(blue, 1)
        if playerwin >= 3:
            GPIO.output(blue, 0)
            GPIO.output(green, 1)
            message = ("The player wins {} to {}".format(playerwin, botwin))
            Game.text.insert(END, "Man, you are pretty good at this.")
            GPIO.output(green, 0)
            Game.text.insert(END, message)
            
        elif botwin >= 3:
            GPIO.output(blue, 0)
            GPIO.output(red, 1)
            message = ("The bot wins {} to {}".format(botwin, playerwin))
            Game.text.insert(END, "Hh ha, you just lost to the computer!")
            GPIO.output(red, 0)
            Game.text.insert(END, message)
            
        else:
            Game.text.insert(END, "Player's wins: {} \n".format(playerwin))
            Game.text.insert(END, "Bot's wins: {} \n".format(botwin))
            Game.text.insert(END, "Pick rock, paper, or scissors and press enter.")    
        Game.text.config(state = DISABLED)

    def play(self):
        # add the CPU outputs to the game
        self.createOutputs()
        # configure the GUI
        self.setupGUI()
        # set the current CPU output
        self.setCPUImage()
        # set the current status
        self.mainText("")
   
    def process(self, event):
        global playerwin
        global botwin
        global red
        global green
        global blue
        global yellow
        val=1

        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(yellow, 0)
        GPIO.output(blue, 1)
        
        if(ser.in_waiting>0):
            play=ser.readline().decode('utf-8').rstrip()
        try:
            GPIO.output(blue, 0)
            def gamePlay(a, b):
                if(a == 0):
                    if(b == 0):
                        return 2
                    elif(b == 1):
                        return 0
                    else:
                        return 1
                    
                elif(a == 1):
                    if(b == 1):
                        return 2
                    elif(b == 2):
                        return 0
                    else:
                        return 1

                elif(a == 2):
                    if(b == 0):
                        return 0
                    elif(b == 1):
                        return 1
                    else:
                        return 2

            bot = randint(0,3)
            if(bot == 0):
                x = "s"
                b = "scissors"
            elif(bot == 1):
                x = "r"
                b = "rock"
            else:
                x = "p"
                b = "paper"
            print(play)
            if(play == "1101"):
                val = 0
            elif(play == "0001"):
                val = 1
            elif(play == "1111"):
                val = 2
                    
            if(gamePlay(val,bot) == 0):
                botwin += 1
                GPIO.output(red, 1)
            elif(gamePlay(val,bot) == 1):
                playerwin += 1
                GPIO.output(green, 1)
            else:
                GPIO.output(yellow, 1)
                pass

        except KeyboardInterrupt:
            GPIO.cleanup()
            print("EXITED")

        Game.currentOutput = Game.currentOutput.outs[x]
        self.mainText(gamePlay(val, bot))
        self.setCPUImage()
        ser.reset_input_buffer()
        Game.player_input.delete(0, END)
    
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Game Glove")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()



