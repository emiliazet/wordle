# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:24:12 2022

@author: ems
"""

#add validation for the existing word
# fix highlighting only 

import random, pygame, sys

#from pygame.locals import *

pygame.init()

white = pygame.Color("white")
yellow = pygame.Color("yellow")
grey = pygame.Color("grey")
black = pygame.Color("black")
green = pygame.Color("green")
lightGreen = pygame.Color("lightGreen")

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!",       True, lightGreen)
youLose = bigFont.render("You Lose!",     True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)

def checkGuess(turns, word, userGuess, window):
    
    #create a list with empty boxes for each letter
    wordBoxes = ["","","","",""]
    
    #define spaces between each letter
    spacing = 0
    
    #default colour for each letter box (grey)
    guessColourCode = [grey,grey,grey,grey,grey]
    
    
    # main interation: go over each letter and change colour if applicabe
    # yellow if letter in the word but wrong place
    # green if letter in the correct position
    
    
    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = yellow

        if word[x] == userGuess[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,5):
        wordBoxes[x] = font.render(userGuess[x], True, black)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(60 +spacing, 50+ (turns*80), 50, 50))
        window.blit(wordBoxes[x], (70 + spacing, 50 + (turns*80)))
        spacing+=80

    if guessColourCode == [green,green,green,green,green]:
        return True



def main():
    #open the file with the list of words and read randomly
    file = open("wordList.txt","r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    print(word)

    for x in range(0,5):
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50),2)

    pygame.display.set_caption("Wordle!")

    turns = 0
    win = False

    while True:
        
        # facilitate quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # response to other keys
            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == pygame.K_RETURN and win == True:
                    main()

                if event.key == pygame.K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    
                    # rewrite this part or enable backspace
                    guess = guess[:-1]

                if event.key == pygame.K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns+=1
                    guess = ""
                    window.fill(black,(0,500, 500, 200))

        window.fill(black,(0,500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(youWin,(90,200))
            window.blit(playAgain,(60,300))

        if turns == 6 and win != True:
            window.blit(youLose,(90,200))
            window.blit(playAgain,(60,300))
        pygame.display.update()
        clock.tick(FPS)
main()

