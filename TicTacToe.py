def wins(canvas,sym1):
    sym = chr(91) + sym1 + chr(93)
    for i in range(3):
        if canvas[i][0] == canvas[i][1] == canvas[i][2] == sym:
            return True

    for i in range(3):
        if canvas[0][i] == canvas[1][i] == canvas[2][i] == sym:
            return True

    if canvas[0][0] == canvas[1][1] == canvas[2][2] == sym:
        return True

    if canvas[0][2] == canvas[1][1] == canvas[2][0] == sym:
        return True
    return False

def isokay(r,c):
    if r < 0 or r >= 3:
        return False
    if c < 0 or c>=3:
        return False
    return True

def isempty(canvas, r, c,element):
    if canvas[r][c] == element:
        return True
    else:
        return False

def updatecanvas(canvas,r,c,add):
    canvas[r][c] = chr(91) + add + chr(93)


def showcanvas(canvas):
    for i in range(3):
        for j in range(3):
            print(canvas[i][j], end=" ")
        print()

def showdetails(canvas,players,symbol):
    players[0] = input("Enter Name of first player: ")
    players[1] = input("Enter Name of first player: ")

    print("Player1: ",players[0]," Symbol: ",symbol[0])
    print("Player1: ", players[1], " Symbol: ", symbol[1])
    print("Let's begins the Game....")

def isdraw(canvas, element):
    for i in range(3):
        for j in range(3):
            if canvas[i][j] ==  element:
                return False
    return True
def doempty(canvas,element):
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            canvas[i][j] = element
def main():
    current = 0
    element = chr(91) + " " + chr(93)
    players = ['Player1', 'Player2']
    canvas = [ [element]*3, [element]*3, [element]*3]
    symbol = ['O', 'X']
    ch = 'y'
    c = 'y'
    showdetails(canvas, players, symbol)
    showcanvas(canvas)
    while c == 'y':
        while ch == 'y':
            r = int(input("Enter Row Number: "))
            c = int(input("Enter column Number: "))
            if isokay(r,c):
                if isempty(canvas, r, c,element):
                    updatecanvas(canvas,r,c,symbol[current])
                    showcanvas(canvas)
                    if wins(canvas,symbol[current]):
                        print(players[current],"Wins!!!")
                        break
                    else:
                        current = (current + 1) % 2

                    if isdraw(canvas, element):
                        print("Match Draw { task fail successfully 😂😂 }")
                        break
        c = input("Wanna Play again? (y/n)")
        doempty(canvas,element)

main()