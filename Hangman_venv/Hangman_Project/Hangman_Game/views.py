from django.shortcuts import render
import random
            
def HangmanHome(request):
    words = ['LAPTOP','CAMERA','NOTICE','ABROAD','BORDER','COLUMN','DEVICE','ENERGY','FATHER','GARDEN',
            'FUTURE','SUCCESS','YELLOW','MEETING','ENGINE','ACCEPT','WEIRD','MISSISSIPPI','COLONY',
            'GENERATE','BALANCE','FRIEND','GENERAL','LOCATE','COUNTRY','INDIAN','AMERICA','FLEXIBLE',
            'SUPREME','KINDNESS']
    chances={6:True}
    global randomWord
    randomWord = list(random.choice(words))
    global randomWordLength
    randomWordLength = len(randomWord)
    global displayWord
    displayWord = ['_']*randomWordLength
    global remainingLives
    remainingLives = [6]
    return render(request,'Hangman_Game/Hangman.html',{'word':randomWord,'completed':'_ '*randomWordLength,'lives':6,'results':False,'chances':{6:True}})
def Hangman(request):
    if request.method == "POST":
        displayText = ''
        thisTurn = False
        gameOver = False
        finalResult = False
        chances = {0:False,1:False,2:False,3:False,4:False,5:False,6:False}
        for i in range(randomWordLength):
                displayText = displayText+(displayWord[i]+' ')
        if '_' not in displayText:
            gameOver = True
            finalResult = True          
        guessedCharacter = (request.POST['guessedCharacter']).upper()
        if guessedCharacter not in randomWord:
            remainingLives[0]-=1
            thisTurn = False
        else:
            thisTurn =True
            for i in range(randomWordLength):
                if guessedCharacter == randomWord[i]:
                    displayWord[i] = guessedCharacter
            displayText = ''        
            for i in range(randomWordLength):
                displayText = displayText+(displayWord[i]+' ')
            if '_' not in displayText:
                gameOver = True
                finalResult = True  
        if remainingLives[0] == 0 or remainingLives[0]<0:
            remainingLives[0] = 0
            gameOver = True
            finalResult = False         
        chances[remainingLives[0]] = True         
        return render(request,'Hangman_Game/Hangman.html',{'word':randomWord,'completed':displayText,'lives':remainingLives[0],'results':{'gameOver':gameOver,'finalResult':finalResult,'thisTurn':thisTurn},'chances':chances})                    