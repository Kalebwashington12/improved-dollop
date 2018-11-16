from turtle import *
from random import randint
import time

wordList = [ 'dangerous', 'awesome', 'wisdom', 'intelligence', 'father', 'the office', 'Hello', 'Why', 'Mother', 'Fortune', 'Wealth', 'Ketchup']

#print(len(wordList))

sw = 600
sh = 800
s=getscreen()
s.setup(600, 800)
s.bgcolor('#011d49')
t=getturtle()
t.color('#fffbe8')
t.width(8)
t.speed(0)


#We need to make 2 turtles
tWriter = Turtle()
tWriter.hideturtle()
tWriter.speed(0)
tWriter.color('#ffffff')

tBadLetters = Turtle()
tBadLetters.hideturtle()

#things we need to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord= ""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 6
fontS= int(sh*0.05)
gameDone = False

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto( -int(sw*0.4), -int(sh*0.375) )
    tWriter.write( newText, font=('Arial', fontS, 'bold') )

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.color("White")
    tBadLetters.penup()
    tBadLetters.goto( -int(sw*0.4), int(sh*0.375) )
    tBadLetters.write( newText, font=('Arial', fontS, 'bold') )

def chooseWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, seceretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter in lettersCorrect:
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used:" + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to gues the word")
    #guess = input(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawBody()
    if fails == 3:
        drawRLeg()
    if fails == 2:
        drawLLeg()
    if fails == 0:
        drawRArm()
    if fails == 0:
       drawLArm()
        
    

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the Word!!!"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess.lower() == secretWord.lower():
        displayText("YES!!! " + secretWord + " is the word!!!")
        gameDone = True
    else:
        displayText("Ha!!! " + theGuess + " YOU WRONG!!!")
        time.sleep(1)
        displayText(displayWord)
        fails -=1
        updateHangmanPerson()
 

#This def will hold the main runnin loop for the game
def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        if theGuess == "$$":
            checkWordGuess()
        # more to come here...
        elif len(theGuess) > 1 or theGuess == "":
                 displayText("Ha!!! " + theGuess + " only one letter, please!")
                 time.sleep(1)
                 displayText(displayWord)
        elif theGuess not in alpha:
             displayText("Ha!!! " + theGuess + " not a letter.")
             time.sleep(1)
             displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            #letter is correct
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess.lower() not in lettersWrong:
            #letter is wrong
            displayText("Ha!!! " + theGuess + " is not in word!!!")
            time.sleep(1)
            displayBadLetters("Not in word: {" + lettersWrong +"} ") 
            lettersWrong += theGuess.lower()
            displayText(displayWord)
            fails -=1
            updateHangmanPerson()
        else:
            # new will give error
            displayText("Ha!!! " + theGuess + " is already guessed you bum!!!")
            time.sleep(1)
            displayText(displayWord)
        #final conditions to endGame
        if fails <= 0: # if you run out of guesses
            displayBadLetters("Ha you ran out of guesses you bum")
            displayText("You trash. Wor is : " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("you got it")
            gameDone = True
        
            
            
        



def drawGallows():
    t.penup()
    t.goto(-int(sw*0.25), -int(sh*0.25) )
    t.pendown()
    t.forward(int(sw*0.5) )
    #pole
    t.backward(int(sw*0.1))
    t.left(90)
    t.forward(int(sh*0.5))
    #top
    t.left(90)
    t.forward(int(sw*0.3))
    #noose
    t.left(90)
    t.forward(int(sh*0.1))

def drawHead():
    hr = int(sw*0.07)
    t.penup()
    t.goto(t.xcor() - hr, t.ycor()-hr)
    t.pendown()
    t.circle(hr)
    #setup for body
    t.penup()
    t.goto(t.xcor() + hr, t.ycor()-hr)

def drawBody():
    hr= int(sw*0.09)
    t.penup()
    #t.goto(t.xcor()-hr, t.ycor()-hr)
    t.pendown()
    t.forward(150)

def drawRLeg():
    hr= int(sw*0.07)
    t.penup
    #t.goto(t.xcor()-hr, t.ycor()-hr)
    t.pendown
    t.right(45)
    t.forward(45)
    t.penup()
    t.left(180)
    t.forward(45)
    t.right(90)

def drawLLeg():
    t.pendown()
    t.forward(45)
    t.penup()
    t.left(180)
    t.forward(45)
    t.left(45)

def drawRArm():
    t.penup()
    t.pendown()
    t.right(90)
    t.forward(60)
    t.left(40)
    t.forward(60)
    t.backward(60)
    t.right(80)
    t.forward(60)
    

    #hr= int(sw*0.07)
    #t.penup
    #t.goto(t.xcor()-hr, t.ycor()-hr)
   # t.pendown
   # t.left(45)
   # t.forward(45)

   



             







    


#program starts here..
drawGallows()
drawHead()
drawBody()
drawRLeg()
drawLLeg()
drawRArm()

#start playing game
time.sleep(1)
t.clear()
t.penup()
t.goto(-int(sw*0.25), -int(sh*0.25) )
t.right(50)
t.pendown()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word:{" + lettersWrong +"}")
playGame()


