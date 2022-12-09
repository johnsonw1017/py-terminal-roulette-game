# Create string for the roulette game board

def drawBoard():
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

drawBoard()

