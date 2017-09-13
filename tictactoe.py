def printBoard(theBoard):
    """ Function for printing the board """
    print(theBoard['topleft'] + '  |  ' + theBoard['topmiddle'] + '  |  ' + theBoard['topright'])
    print('--------------')
    print(theBoard['middleleft'] + '  |  ' + theBoard['middlemiddle'] + '  |  ' + theBoard['middleright'])
    print('--------------')
    print(theBoard['bottomleft'] + '  |  ' + theBoard['bottommiddle'] + '  |  ' + theBoard['bottomright'])

'''
 #commented because one function will be enough to do the trick
def winnerX(theBoard):
    """ Function for checking if the X user or computer wins """
    return ((theBoard['topleft'] == 'x' and theBoard['topmiddle'] == 'x' and theBoard['topright'] == 'x') or
        (theBoard['topleft'] == 'x' and theBoard['middleleft'] == 'x' and theBoard['bottomleft'] == 'x') or
        (theBoard['topleft'] == 'x' and theBoard['middlemiddle'] == 'x' and theBoard['bottomright'] == 'x') or
        (theBoard['topright'] == 'x' and theBoard['middleright'] == 'x' and theBoard['bottomright'] == 'x') or
        (theBoard['topright'] == 'x' and theBoard['middlemiddle'] == 'x' and theBoard['bottomleft'] == 'x') or
        (theBoard['topmiddle'] == 'x' and theBoard['middlemiddle'] == 'x' and theBoard['bottommiddle'] == 'x') or
        (theBoard['middleleft'] == 'x' and theBoard['middlemiddle'] == 'x' and theBoard['middleright'] == 'x') or
        (theBoard['bottomleft'] == 'x' and theBoard['bottommiddle'] == 'x' and theBoard['bottomright'] == 'x'))
'''
def winner(theBoard, sign):
    """ Function for checking if the X user or computer wins """
    return ((theBoard['topleft'] == sign and theBoard['topmiddle'] == sign and theBoard['topright'] == sign) or
        (theBoard['topleft'] == sign and theBoard['middleleft'] == sign and theBoard['bottomleft'] == sign) or
        (theBoard['topleft'] == sign and theBoard['middlemiddle'] == sign and theBoard['bottomright'] == sign) or
        (theBoard['topright'] == sign and theBoard['middleright'] == sign and theBoard['bottomright'] == sign) or
        (theBoard['topright'] == sign and theBoard['middlemiddle'] == sign and theBoard['bottomleft'] == sign) or
        (theBoard['topmiddle'] == sign and theBoard['middlemiddle'] == sign and theBoard['bottommiddle'] == sign) or
        (theBoard['middleleft'] == sign and theBoard['middlemiddle'] == sign and theBoard['middleright'] == sign) or
        (theBoard['bottomleft'] == sign and theBoard['bottommiddle'] == sign and theBoard['bottomright'] == sign))
'''
 #commented because one function will be enough to do the trick
def WinnerO(theBoard):
    """ Function for checking if the O user of User wins """
    return ((theBoard['topleft'] == 'o' and theBoard['topmiddle'] == 'o' and theBoard['topright'] == 'o') or
        (theBoard['topleft'] == 'o' and theBoard['middleleft'] == 'o' and theBoard['bottomleft'] == 'o') or
        (theBoard['topleft'] == 'o' and theBoard['middlemiddle'] == 'o' and theBoard['bottomright'] == 'o') or
        (theBoard['topright'] == 'o' and theBoard['middleright'] == 'o' and theBoard['bottomright'] == 'o') or
        (theBoard['topright'] == 'o' and theBoard['middlemiddle'] == 'o' and theBoard['bottomleft'] == 'o') or
        (theBoard['topmiddle'] == 'o' and theBoard['middlemiddle'] == 'o' and theBoard['bottommiddle'] == 'o') or
        (theBoard['middleleft'] == 'o' and theBoard['middlemiddle'] == 'o' and theBoard['middleright'] == 'o') or
        (theBoard['bottomleft'] == 'o' and theBoard['bottommiddle'] == 'o' and theBoard['bottomright'] == 'o'))
'''
def computerMove(theBoard):
    """ Function for making a random move by computer """
    import random
    choices = ['topleft','topmiddle','topright','middleleft','middlemiddle','middleright','bottomleft','bottommiddle','bottomright']
    pcchoice = random.choice(choices)
    while theBoard[pcchoice] != ' ':
        pcchoice = random.choice(choices)
    theBoard[pcchoice] = 'x'
        
if __name__ == '__main__':

    gameBoard = {
    'topleft': ' ',
    'topmiddle': ' ',
    'topright': ' ',
    'middleleft': ' ',
    'middlemiddle': ' ',
    'middleright': ' ',
    'bottomleft': ' ',
    'bottommiddle': ' ',
    'bottomright': ' ',
    }

    count = 0
    while True:
        
        if count >= 9:
            print("Please try again.")

        printBoard(gameBoard)
        print("Select a choice from the board.")
        print("""
            topleft      middleleft     bottomleft
            topmiddle    middlemiddle   bottommiddle
            topright     middleright    bottomright
         """)


        val = input("Your Choice: ")
        val = val.lower()
        gameBoard[val] = 'o'
        # result = (gameBoard)
        
        if winner(gameBoard,'o'):
            printBoard(gameBoard)
            print("Human Player Wins The Game.")
            break

        '''
         #commented because one function will be enough to do the trick
        if WinnerO(gameBoard):
            printBoard(gameBoard)
            print("Human Player Wins The Game.")
            break
        '''

        computerMove(gameBoard)
        if winner(gameBoard,'x'):
            printBoard(gameBoard)
            print("Computer Player Wins The Game")
            break

        '''
        #commented because one function will be enough to do the trick
        if winnerX(gameBoard):
            printBoard(gameBoard)
            print("Computer Player Wins The Game")
            break
        '''
        count += 2
