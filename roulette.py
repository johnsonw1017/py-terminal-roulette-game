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
        
        print(f"| r{row}|")

    print("    |     1-12      |     13-24     |     25-36     |")
    print(row_top3)
    print("    |  1-18 |  EVEN |  RED  | BLACK |  ODD  | 19-36 |")
    print(row_top3)

#Input handling
def get_input(prompt):
    
    user_input = input(prompt)

    # when user inputs "board", "help" or "quit"
    if user_input == "board":
        draw_board()

    if user_input == "help":
        pass

    if user_input == "quit":
        raise KeyboardInterrupt

    return user_input

##  Game play loop
def main_loop():
    # Introduction and Board
    print("Welcome to a game of Roulette! Let's start with 100 chips.")
    draw_board()
    print("Type the following at any time during the game:\nhelp - for instructions\nboard - to view board\nquit - to quit game")

    user_input = ""
    location = ""

    #Ask player the positions to place chips
    while user_input != 'done':
        user_input = get_input("Where would you like to place your chips?")
        location = user_input

    #Ask how many chips to add at that location
        user_input = get_input(f"How many chips to place at {location}?")

    #Update variable chip_placement accordingly
