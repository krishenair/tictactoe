#tiktactoe by Krish Nair
# made on march 6, 2023

#just play tic-tac toe - its a simple program that took an hour(ish) to code
import time

gameboard = ['   ', '   ', '   ',
            '   ', '   ', '   ',
            '   ', '   ', '   '] # a 3 x 3 gameboard

def printboard():
    global gameboard
    print ("Printing gameboard...")
    print("-------------\n" + "|" + gameboard[0] + "|" + gameboard[1] + "|" + gameboard[2] + "|\n" 
    + "-------------\n" + "|" + gameboard[3] + "|" + gameboard[4] + "|" + gameboard[5] + "|\n" +
    "-------------\n" + "|" + gameboard[6] + "|" + gameboard[7] + "|" + gameboard[8] + "|\n" +
    "-------------")

def checkwin(var):
    global gameboard
    if (gameboard[0]== var and gameboard[1] == var and gameboard[2] == var) or (gameboard[3]== var and gameboard[4] == var and gameboard[5] == var) or (gameboard[6]== var and gameboard[7] == var and gameboard[8] == var) or (gameboard [0] == var and gameboard[3] == var and gameboard[6] == var) or (gameboard [1] == var and gameboard[4] == var and gameboard[7] == var) or (gameboard [2] == var and gameboard[5] == var and gameboard[8] == var) or (gameboard [0] == var and gameboard[4] == var and gameboard[8] == var) or (gameboard [6] == var and gameboard[4] == var and gameboard[2] == var):
        return True
    else:
        return False


def countx():
    xcount = 0
    for i in range(len(gameboard)):
        if gameboard[i] == " X ":
            xcount+=1
    return xcount

def counto():
    ocount = 0
    for i in range(len(gameboard)):
        if gameboard[i] == " O ":
            ocount+=1
    return ocount

def xoro():
    if countx() > counto():
        return "o"
    elif countx() == counto():
        return "x"
    else:
        print ("there was an error, restarting...")
        main()
        
        

def main():
    global gameboard
    while checkwin(" X ") == False and checkwin(" O ") == False:
        if xoro() == "x":
            printboard()
            x_input = int(input("X, your turn (pick a number from 1 thru 9):\n"))
            if gameboard[x_input -1] == "   ":
                gameboard[x_input - 1] = " X "
                if checkwin(" X ") == True:
                    printboard()
                    print ("X wins")
                    break
                if checkwin(" O ") == True:
                    printboard()
                    print ("O wins")
                    break
                else:
                    continue
            else:
                print("oops! that's taken! Try again!\n")
                continue
        if xoro() == "o":
            printboard()
            o_input = int(input("O, your turn (pick a number from 1 thru 9):\n"))
            if gameboard[o_input -1] == "   ":
                gameboard[o_input - 1] = " O "
                if checkwin(" X ") == True:
                    printboard()
                    print ("X wins")
                    break
                if checkwin(" O ") == True:
                    printboard()
                    print ("O wins")
                    break
                else:
                    continue
            else:
                print("oops! that's taken! Try again!\n")
                continue



print("tic tac toe! iykyk- if udk then just google it idk what to tell you...")
time.sleep(3)
print("here is a sample board labeled with all the spots, one through nine. When making a selection, make sure to use the number on the corresponding spot!")
time.sleep(3)
print("-------------\n" + "|" + " 1 " + "|" + " 2 " + "|" + " 3 " + "|\n" 
    + "-------------\n" + "|" + " 4 " + "|" + " 5 " + "|" + " 6 " + "|\n" +
    "-------------\n" + "|" + " 7 " + "|" + " 8 " + "|" + " 9 " + "|\n" +
    "-------------")
time.sleep(3)
main()