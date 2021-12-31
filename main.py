# Console Prompt colors
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Print winning message and keep stats
def messageWon(player):
    global gameScore
    global gameOver
    printBoard()
    if player == 0:
        print(f'X has three in a row')
        gameScore[0] += 1
        gameOver = True
    else:
        print(f'O has three in a row')
        gameScore[1] += 1

# Check if player has three in a row right, down or diagonals
def checkWin():
    # Check Right
    for i in range(0, 9, 3):
        if ((boardNumbers[0 + i] == 'X') and (boardNumbers[1 + i] == 'X') and (boardNumbers[2 + i] == 'X')):
            messageWon(0)
        elif ((boardNumbers[0 + i] == 'O') and (boardNumbers[1 + i] == 'O') and (boardNumbers[2 + i] == 'O')):
            messageWon(1)
    # Check Down
    for i in range(0, 3):
        if ((boardNumbers[0 + i] == 'X') and (boardNumbers[3 + i] == 'X') and (boardNumbers[6 + i] == 'X')):
            messageWon(0)
        elif ((boardNumbers[0 + i] == 'O') and (boardNumbers[3 + i] == 'O') and (boardNumbers[6 + i] == 'O')):
            messageWon(1)
    # Check Diagonals
    if ((boardNumbers[0] == 'X') and (boardNumbers[4] == 'X') and (boardNumbers[8] == 'X')):
        messageWon(0)
    elif ((boardNumbers[0] == 'O') and (boardNumbers[4] == 'O') and (boardNumbers[8] == 'O')):
        messageWon(1)
    elif ((boardNumbers[6] == 'X') and (boardNumbers[4] == 'X') and (boardNumbers[2] == 'X')):
        messageWon(0)
    elif ((boardNumbers[6] == 'O') and (boardNumbers[4] == 'O') and (boardNumbers[2] == 'O')):
        messageWon(1)

# Printing the current gameboard
def printBoard():

    board = f"{Color.UNDERLINE}" \
            f" {boardNumbers[0]} | {boardNumbers[1]} | {boardNumbers[2]} \n" \
            f" {boardNumbers[3]} | {boardNumbers[4]} | {boardNumbers[5]} {Color.END}\n" \
            f" {boardNumbers[6]} | {boardNumbers[7]} | {boardNumbers[8]} \n"
    print(board)

# Create the GameBoard Array
boardNumbers = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ',
]
# Players Game Score
gameScore = [0, 0]
# Keeping track if the game is over or not
gameOver = False
# Always starts with X as player start
playerTurn = "X"
divider = '#################################################'

# Game Loop
howManyRounds = int(input('How many rounds to win?\n'))
for gameRound in range(0, howManyRounds):

    # Max tries are 9, if the board is full and no one won it is a draw.
    for rounds in range(0, 9):
        # If someone won, break the loop
        if gameOver is True:
            break

        # Show current board status
        printBoard()

        # Cheater check, keep looping input until player picks legal move
        turnLoop = False
        while turnLoop is False:
            print(f"It's player {playerTurn} turn")
            turn = int(input('Choose a cell number 1-9\n')) - 1

            # Check that user enters an actual cell
            if (turn < 10 and turn > -1):
                # Check that the cell is empty
                if boardNumbers[turn] == " ":
                    # Use odds and even to determine player turn
                    if (rounds % 2) == 0:
                        boardNumbers[turn] = "X"
                        playerTurn = "O"
                    else:
                        boardNumbers[turn] = "O"
                        playerTurn = "X"

                    # The turn is over, continue
                    turnLoop = True
                else:
                    print("It's already taken, try again")
            else:
                print("Cell number out of bounds, try again")

        # Check if its a win
        checkWin()

    if gameOver == False:
        print("It's a draw!")

    gameOver = False
    boardNumbers = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ',
    ]
    print(divider)
    input(f'Press enter to continue\n')
    print(divider)

print(divider)
print(f'X: {gameScore[0]} \nO: {gameScore[1]}')
print(divider)