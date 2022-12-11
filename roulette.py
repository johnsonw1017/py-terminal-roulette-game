#Global variables/parameters
valid_locations = ["R1", "R2", "R3", "1-12", "13-24", "25-36", "1-18", "19-36", "EVEN", "ODD", "RED", "BLACK"]
location_syntax = ["u", "l", "d", "r", "c"]

# Create string for the roulette game board
def draw_board():
    row_top1 = "+---" * 14 + "+"
    row_top2 = "+   " + "+---" * 13 + "+"
    row_top3 = "    " + "+---" * 12 + "+"

    for row in range(3, -1, -1):

        if row in [1, 2]:
            print(row_top2)
        else:
            print(row_top1)
            if row == 0:
                break
        
        if row == 2:
            print("| 0", end=" ")
        else:
            print("|  ", end=" ")

        for col in range(1, 13):
            boardnum = row + 3 * (col - 1)

            if boardnum / 10 < 1:
                print(f"| {boardnum}", end=" ")
            else:
                print(f"| {boardnum}", end="")
        
        print(f"| R{row}|")

    print("    |     1-12      |     13-24     |     25-36     |")
    print(row_top3)
    print("    |  1-18 |  EVEN |  RED  | BLACK |  ODD  | 19-36 |")
    print(row_top3)

#Player instructions
def print_instructions():
    print("    u\n  +---+ \nl | 1 | r\n  +---+ \n    d")
    print("Use the above diagram to add chips to edges of a number (except 0). For example u1 to add chips on top edge of number 1.")
    print("To place chip at the corner between 3-4 numbers, use cN, where N is the largest of the numbers.")
    print("For the remainder, add chips as appeared on the board.")

#Input handling
def get_input(prompt):
    
    user_input = input(prompt)

    # when user inputs "board", "help" or "quit"
    if user_input == "board":
        draw_board()

    elif user_input == "help":
        print_instructions()

    elif user_input == "quit":
        raise KeyboardInterrupt

    return user_input

#Check if user input for chip placement is valid
def is_location(user_input):
    location_number = 0

    if user_input in valid_locations:
        return True
    
    # For user input beginning with u, d, l, r, c
    elif user_input[0] in location_syntax:
        try:
            location_number = int(user_input[1:])
        except ValueError:
            return False

        #syntax r is only valid for numbers between 1 and 33
        if user_input[0] == "r" and location_number in range(1, 34):
            return True
        #syntax c is only valid for R2 and R3 numbers
        elif user_input[0] == "c" and location_number in range(1, 37) and location_number % 3 != 1:
            return True
        #syntax u, d, l is valid as long as number is between 1 and 36
        elif user_input[0] in location_syntax[:2] and location_number in range(1, 37):
            return True
        else:
            return False

    # For numerical user input
    elif len(user_input) <= 2:
        try:
            location_number = int(user_input)
        except ValueError:
            return False
        
        if location_number in range(0, 37):
            return True
        else:
            return False

    else:
        return False

##  Game play loop
def main_loop():
    # Introduction and Board
    print("Welcome to a game of Roulette! Let's start with 100 chips.")
    draw_board()
    print("Type the following at any time during the game:\nhelp - for instructions\nboard - to view board\nquit - to quit game")

    chip_amount = 100
    user_input = ""
    location = ""

    try:
        #Ask player the positions to place chips
        while user_input != 'done':
            while True:
                user_input = get_input("Where would you like to place your chips?")
                location = user_input
                if is_location(location):
                    break
                else:
                    print("Error: Please enter a valid location on the board")
                    continue

        #Ask how many chips to add at that location
            user_input = get_input(f"How many chips to place at {location}?")
    except KeyboardInterrupt:
        print(f"Thanks for playing! You finished with {chip_amount} chips in your stack.")
    

    #Update variable chip_placement accordingly

main_loop()