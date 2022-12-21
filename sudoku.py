"""
Alfie Atkinson
Programming Fundamentals
Assessment Item 2
Task 2 - Sudoku
"""

import time, sys, random

puzzles = [
    [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ],
    [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ],
    [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ],
    [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]
]

menu = """
Welcome to Sudoku

1. Play Game
2. Computer Solve
3. Exit
"""

menu2 = """
Which board would you like to play? (1-%s)
""" % (len(puzzles))

class Grid():
    def __init__(self, grid, num):
        self.grid = grid
        self.num = num
        self.original = []
        self.display = []
        self.moves = 0

        for y in self.grid:
            row = []
            for x in y:
                row.append(x)
            self.original.append(row)

    def incMoves(self):
        self.moves += 1

    def getRow(self, y): # creates a list of the values in the same row
        return self.grid[y]

    def getCol(self, x): # creates a list of the values in the same column
        col = []

        for row in self.grid:
            col.append(row[x])
        return col

    def getSquare(self, x, y): # creates a list of the values in the same square
        square = []

        if x < 3 and y < 3:
            start_row = 0
            start_col = 0
        elif x < 6 and y < 3:
            start_row = 0
            start_col = 3
        elif x < 9 and y < 3:
            start_row = 0
            start_col = 6
        elif x < 3 and y < 6:
            start_row = 3
            start_col = 0
        elif x < 6 and y < 6:
            start_row = 3
            start_col = 3
        elif x < 9 and y < 6:
            start_row = 3
            start_col = 6
        elif x < 3 and y < 9:
            start_row = 6
            start_col = 0
        elif x < 6 and y < 9:
            start_row = 6
            start_col = 3
        elif x < 9 and y < 9:
            start_row = 6
            start_col = 6
        
        for i in range(start_row, start_row + 3):
            for n in range(start_col, start_col + 3):
                square.append(self.grid[i][n])
        return square

    def setTile(self, x, y): # checks the entered value is possible and then enters it
        print("""
What number would you like to set that tile?
To clear the tile type 'clear'
        """)
        while 1:
            entered = input("")
            try:
                num = int(entered)
                if num > 0 and num < 10:
                    break
                else:
                    print("\nPlease enter a number between 1 and 9.")
            except:
                if entered == "clear":
                    self.clearTile(x, y)
                    return
                else:
                    print("\nPlease enter a number between 1 and 9.")

        num = str(num)
        tile = self.grid[y][x]
        if tile == " ":
            self.grid[y][x] = num
            print("\nNumber entered.")
            self.incMoves()
        else:
            print("\nThat tile already has a number.")
            raise Exception

    def clearTile(self, x, y): # clears the tile chosen by the user if it was a user entered tile
        if self.original[y][x] == " ":
            self.grid[y][x] = " "
            print("\nTile Cleared.")
            self.incMoves()
        else:
            print("\nThis tile was not entered by the player.")

    def updateGrid(self): # writes the grid in a more understandable format for the player
        self.display = []
        self.display.append("    a   b   c   d   e   f   g   h   i")
        self.display.append("  +---|---|---+---|---|---+---|---|---+")

        count = 0
        for row in self.grid:
            count += 1
            line = "%s | " % (self.grid.index(row))
            for num in row:
                line = line + "%s | " % (num)
            self.display.append(line)
            if count % 3 == 0:
                self.display.append("  +---|---|---+---|---|---+---|---|---+")
            else:
                self.display.append("  |---|---|---|---|---|---|---|---|---|")

    def printGrid(self): # prints the grid to the screen
        print()
        for line in self.display:
            print(line)

    def win(self):
        self.updateGrid()
        self.printGrid()
        print("""
 -------------------
       YOU WIN
 -------------------

 Congratulations! You solved puzzle %s.
        """ % (self.num))

    def lose(self):
        print("""
 -------------------
        LOSER
 -------------------
 Oops... You failed to solve puzzle %s.
        """ % (self.num))

    def checkWin(self, x, y, num):
        num = str(num)
        row = self.getRow(y)
        col = self.getCol(x)
        square = self.getSquare(x, y)

        if row.count(num) > 1 or col.count(num) > 1 or square.count(num) > 1:
            return False
        return True

    def checkEnd(self): # checks to see if all tiles are filled in
        for y in range(0, 9):
            for x in range(0, 9):
                if self.grid[y][x] == " ":
                    return False

        for y in range(0, 9):
            for x in range(0, 9):
                if not self.checkWin(x, y, self.grid[y][x]):
                    self.lose()
                    return True
        self.win()
        return True

    def checkPossible(self, x, y, num):
        num = str(num)
        if num in self.getRow(y) or num in self.getCol(x) or num in self.getSquare(x, y):
            return False
        return True

    def computerSolve(self): # backtracking algorithm to solve the grid from it's current point
        for y in range(0, 9):
            for x in range(0, 9):
                if self.grid[y][x] == " ":
                    for n in range(1, 10):
                        if self.checkPossible(x, y, n):
                            self.grid[y][x] = str(n)
                            self.incMoves()
                            self.computerSolve()
                            self.grid[y][x] = " "
                            self.incMoves()
                    return
        self.updateGrid()
        self.printGrid()
        raise Exception

def play(game):
    playing = True
    while playing:
        game.updateGrid()
        game.printGrid()
        while 1:
            print("""
Please select a tile.
(example 'A1')
            """)
            tile = list(input(""))
            try:
                game.setTile(int(ord(tile[0].lower()) - 97), int(tile[1]))
                moves += 1
                break
            except IndexError:
                print("\nThat tile does not exist.")
            except Exception as e:
                print(e)
        
            game.updateGrid()
            game.printGrid()

        if game.checkEnd():
            playing = False

if __name__ == "__main__":
    while 1:
        print(menu)
        chosen_option = input("")
        if chosen_option == "1" or chosen_option == "2":
            while 1:
                print(menu2)
                chosen_option2 = input("")
                try:
                    game = Grid(puzzles[int(chosen_option2) - 1], int(chosen_option2))
                    if chosen_option == "1":
                        moves = 0
                        start = time.perf_counter()
                        play(game)
                        finish = time.perf_counter()
                        print("\nCompleted in {:.4f} seconds and %s moves.".format(finish - start) % (game.moves))
                    else:
                        moves = 0
                        start = time.perf_counter()
                        try:
                            game.computerSolve()
                        except:
                            pass
                        finish = time.perf_counter()
                        print("\nCompleted in {:.4f} seconds and %s moves.".format(finish - start) % (game.moves))
                    break
                except IndexError:
                    print("\n'%s' is not a valid option." % (chosen_option2))
        elif chosen_option == "3":
            quit()
        else:
            print("\n'%s' is not a valid option." % (chosen_option))
