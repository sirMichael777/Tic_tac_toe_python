
# Program for Tic-Tac-Toe game
# Michael Maseko
# 24-11-2022
import random

positions_list = []
positions_rows = {"A": 1, "B": 3, "C": 5}
positions_column = {"1": 1, "2": 3, "3": 5}
testers = []


def createGrid():
    matrix = []
    for count in range(7):
        matrix.append(['   '] * 7)
        for row2n in range(0, 7, 2):
            matrix[count][row2n] = "   "
    for row2n in range(0, 7, 2):
        for column2n in range(1, 6, 2):
            matrix[row2n][column2n] = '---'
            matrix[column2n][row2n] = ' | '

    return matrix


def drawGrid(matrix):
    print("     1     2     3 ")
    for row in range(7):
        if row == 1:
            print('A', end='')
        elif row == 3:
            print("B", end='')
        elif row == 5:
            print('C', end='')
        else:
            print(' ', end='')
        for column in range(7):
            print(matrix[row][column], end='')
        print("\n", end='')


def insert(matrix, position, variable):
    row = position[0].upper()
    column = position[1]
    if matrix[positions_rows[row]][positions_column[column]] != ' X ' and \
            matrix[positions_rows[row]][positions_column[column]] != ' O ':
        matrix[positions_rows[row]][positions_column[column]] = variable
    else:
        position = input("Occupied!! enter another position:\n")
        position = check_Validity(position, variable)
        insert(matrix, position, variable)


def check_Validity(position, variable):
    positions_list.append(position)
    if len(positions_list[-1]) != 2:
        print("Your response should be just 2 characters, the Letter for the row followed by the number for column"
              ", no space or anything else eg.'B2'.\nEnter the position where you want to place", variable + ':')
        position = input()
        positions_list.append(position)
        return check_Validity(position, variable)

    else:
        row = position[0]
        column = position[1]
        if row.upper() not in "ABC" or column not in "123":
            print("The row can only be A,B, or C and column can each ony be 1,2 or 3.\nEnter the position where you "
                  "want to place", variable + ':')
            position = input()
            positions_list.append(position)
            return check_Validity(position, variable)
    return positions_list[-1]


def check_left_right(matrix, row=1):
    if row <= 5:
        if matrix[row][1] == " X " == matrix[row][3] == matrix[row][5]:
            return "X"
        elif matrix[row][1] == " O " == matrix[row][3] == matrix[row][5]:
            return "O"
        else:
            return check_left_right(matrix, row + 2)


def check_up_down(matrix, column=1):
    if column <= 5:
        if matrix[1][column] == " X " == matrix[3][column] == matrix[5][column]:
            return "X"
        elif matrix[1][column] == " O " == matrix[3][column] == matrix[5][column]:
            return "O"
        else:
            return check_up_down(matrix, column + 2)


def check_diagonals(matrix):
    if matrix[1][1] == " X " == matrix[3][3] == matrix[5][5]:
        return "X"
    elif matrix[1][1] == " O " == matrix[3][3] == matrix[5][5]:
        return "O"
    elif matrix[5][1] == " X " == matrix[3][3] == matrix[1][5]:
        return "X"
    elif matrix[5][1] == " O " == matrix[3][3] == matrix[1][5]:
        return "O"


def check_Winner(matrix):
    if check_left_right(matrix) is not None:
        return check_left_right(matrix)
    elif check_up_down(matrix) is not None:
        return check_up_down(matrix)
    elif check_diagonals(matrix) is not None:
        return check_diagonals(matrix)


def Stay_Leave(decision):
    if decision == '1':
        mode = input("Would you like to play vs Computer (1) or Multiplayer (2)\nSelect 1 or 2:\n")
        matrix = createGrid()
        while mode not in "12" or len(mode) == 0:
            mode = input("Invalid input. Would you like to play vs Computer (1) or Multiplayer (2)\nSelect 1 or 2:\n")
        else:
            if mode == "1":
                Computer_main(matrix)
            else:
                Multiplayer_main(matrix)
        if check_Winner(matrix) is None:
            print("Game over, It's a draw!! Thanks for playing!, see you again.")
        else:
            print("Game over!! The winner is", check_Winner(matrix) + ", Thanks for playing!, see you again.")
        decision = input("Select 1 to play again or any other key to exit:\n")
        Stay_Leave(decision)
    else:
        print("We're sad to see you leave, hoping to see you soon again.")
        exit(0)


def play_random(matrix):
    variable = " O "
    choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    if choice == 1 and matrix[1][1].isspace():
        matrix[1][1] = variable
        print("Played A1")
    elif choice == 2 and matrix[1][3].isspace():
        matrix[1][3] = variable
        print("Played A2")
    elif choice == 3 and matrix[1][5].isspace():
        matrix[1][5] = variable
        print("Played A3")
    elif choice == 4 and matrix[3][1].isspace():
        matrix[3][1] = variable
        print("Played B1")
    elif choice == 5 and matrix[3][5].isspace():
        matrix[3][5] = variable
        print("Played B3")
    elif choice == 6 and matrix[5][1].isspace():
        matrix[5][1] = variable
        print("Played C1")
    elif choice == 7 and matrix[5][3].isspace():
        matrix[5][3] = variable
        print("Played C2")
    elif choice == 8 and matrix[5][5].isspace():
        matrix[5][5] = variable
        print("Played C3")
    else:
        play_random(matrix)


def Check_play(matrix, tester, count, edges):
    variable = " O "
    testers.append(tester)
    if count == 1:
        if matrix[3][3].isspace():
            matrix[3][3] = variable
            print("Played B2")
        else:
            play_random(matrix)
    elif matrix[1][1] == matrix[1][3] == tester and matrix[1][5].isspace():
        matrix[1][5] = variable
        edges.remove(3)
        print("Played A3")
    elif matrix[3][1] == matrix[3][3] == tester and matrix[3][5].isspace():
        matrix[3][5] = variable
        edges.remove(5)
        print("Played B3")
    elif matrix[5][1] == matrix[5][3] == tester and matrix[5][5].isspace():
        matrix[5][5] = variable
        edges.remove(8)
        print("Played C3")
    elif matrix[1][3] == matrix[1][5] == tester and matrix[1][1].isspace():
        matrix[1][1] = variable
        edges.remove(1)
        print("Played A1")
    elif matrix[3][3] == matrix[3][5] == tester and matrix[3][1].isspace():
        matrix[3][1] = variable
        edges.remove(4)
        print("Played B1")
    elif matrix[5][3] == matrix[5][5] == tester and matrix[5][1].isspace():
        matrix[5][1] = variable
        edges.remove(6)
        print("Played C1")
    elif matrix[1][1] == matrix[3][1] == tester and matrix[5][1].isspace():
        matrix[5][1] = variable
        edges.remove(6)
        print("Played C1")
    elif matrix[1][3] == matrix[3][3] == tester and matrix[5][3].isspace():
        matrix[5][3] = variable
        edges.remove(7)
        print("Played C2")
    elif matrix[1][5] == matrix[3][5] == tester and matrix[5][5].isspace():
        matrix[5][5] = variable
        edges.remove(8)
        print("Played C3")
    elif matrix[3][1] == matrix[5][1] == tester and matrix[1][1].isspace():
        matrix[1][1] = variable
        edges.remove(1)
        print("Played A1")
    elif matrix[3][3] == matrix[5][3] == tester and matrix[1][3].isspace():
        matrix[1][3] = variable
        edges.remove(2)
        print("Played A2")
    elif matrix[3][5] == matrix[5][5] == tester and matrix[1][5].isspace():
        matrix[1][5] = variable
        edges.remove(3)
        print("Played A3")
    elif matrix[1][1] == matrix[1][5] == tester and matrix[1][3].isspace():
        matrix[1][3] = variable
        edges.remove(2)
        print("Played A2")
    elif matrix[5][1] == matrix[5][5] == tester and matrix[5][3].isspace():
        matrix[5][3] = variable
        edges.remove(7)
        print("Played C2")
    elif matrix[1][1] == matrix[5][1] == tester and matrix[3][1].isspace():
        matrix[3][1] = variable
        edges.remove(4)
        print("Played B1")
    elif matrix[1][5] == matrix[5][5] == tester and matrix[3][5].isspace():
        matrix[3][5] = variable
        edges.remove(5)
        print("Played B3")
    elif matrix[3][3] == matrix[1][1] == tester and matrix[5][5].isspace():
        matrix[5][5] = variable
        edges.remove(8)
        print("Played C3")
    elif matrix[3][3] == matrix[5][5] == tester and matrix[1][1].isspace():
        matrix[1][1] = variable
        edges.remove(1)
        print("Played A1")
    elif matrix[3][3] == matrix[1][5] == tester and matrix[5][1].isspace():
        matrix[5][1] = variable
        edges.remove(6)
        print("Played C1")
    elif matrix[3][3] == matrix[5][1] == tester and matrix[1][5].isspace():
        matrix[1][5] = variable
        edges.remove(3)
        print("Played A3")
    elif testers[-1] == " O ":
        Check_play(matrix, " X ", count, edges)
    else:
        play_random(matrix)


def Computer_main(matrix):
    testers.clear()
    edges = [1, 2, 3, 4, 5, 6, 7, 8]
    for count in range(9):
        if count > 4 and check_Winner(matrix) is not None:
            drawGrid(matrix)
            print("Game over!!The winner is", check_Winner(matrix) + ", Thanks for playing!, see you again.")
            decision = input("Select 1 to play again or 0 to exit:\n")
            if decision == "1":
                print("We're happy to see you back")
            Stay_Leave("1")
            break
        if count % 2 == 0:
            drawGrid(matrix)
            variable = ' X '
            print("Enter the position where you want to place", variable + ":")
            position = check_Validity(input(), variable)
            insert(matrix, position, variable)
        else:
            print("Computer thinking...")
            Check_play(matrix, " O ", count, edges)
    drawGrid(matrix)


def Multiplayer_main(matrix):
    positions_list.clear()
    for count in range(9):
        drawGrid(matrix)
        if count > 4 and check_Winner(matrix) is not None:
            print("Game over!!The winner is", check_Winner(matrix) + ", Thanks for playing!, see you again.")
            decision = input("Select 1 to play again or 0 to exit:\n")
            if decision == "1":
                print("We're happy to see you back")
            Stay_Leave("1")
        if count % 2 == 0:
            variable = ' X '
        else:
            variable = ' O '
        print("Enter the position where you want to place", variable + ":")
        position = check_Validity(input(), variable)
        insert(matrix, position, variable)
    drawGrid(matrix)


def main():
    print("Welcome to Sir Michael's Tic-Tac-Toe Game!\nThe instructions are:\nEnter the row's Alphabet followed by "
          "the column number of the position where you want to enter 'X' or 'O' for example 'B1'  will result in the "
          "following:")
    matrix = createGrid()
    insert(matrix, "B1", " X ")
    drawGrid(matrix)
    Stay_Leave("1")
    if check_Winner(matrix) is None:
        print("Game over, It's a draw!! Thanks for playing!, see you again.")
    else:
        print("Game over!! The winner is", check_Winner(matrix) + ", Thanks for playing!, see you again.")
    decision = input("Select 1 to play again or any other key to exit:\n")
    if decision == "1":
        print("We're happy to see you back")
    Stay_Leave("1")


if __name__ == '__main__':
    main()
