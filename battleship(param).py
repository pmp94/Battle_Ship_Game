'''
THINGS THAT STILL NEED TO BE DONE:

- Need to make sure that ships don't clash with one other or intersect one other when randomly placing on board


'''
import random
import turtle


# Initializing turtle screen to a 400 x 400 square
window = turtle.Screen()

# Creating our pen/turtle and hiding it
t = turtle.Turtle()
t.hideturtle()
# When we set the speed to 0, the turtle will go as fast as possible without showing animations
t.speed(0)

# Drawing each square
def draw_box(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(0, 4):
        t.forward(size)
        t.right(90)


#Draw X on Screen for Hit (H)
def draw_x(t, x, y, length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(45)
    t.forward(length/2)
    t.right(180)
    t.forward(length)
    t.right(180)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.right(180)
    t.forward(length)
    t.right(180)
    t.forward(length/2)
    t.right(45)


#Draw O on Screen for Miss (M)
def draw_o(t, x, y,radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    

# Utilizing our square function in order to create a 10x10 grid
def draw_grid():
    start_x = -200
    start_y = -200
    box_size = 40
    
    col_val = -230
    row_val = -180
    letters = "JIHGHEDCBA"

    for i in range(0, 10):
        for j in range(0, 10):

            if i == 0:
                t.penup()
                t.goto(start_x - 20,col_val)
                t.write(letters[j])
                t.goto(row_val,180)
                t.write(str(j+1))
                t.down()
                col_val += 40
                row_val += 40
                
            draw_box(t, start_x + j * box_size, start_y + i * box_size, box_size)
draw_grid()
repeat = True
while (repeat):
    #Dictionary Mappping Between Row (Letters) and Number
    mydict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}

    #Initially initalize all squares in array as empty except those that have the ships - This array keeps track of where ships are and if user correctly hit
    #or miss. We can use M for Miss and H for Hit. If all are hit then the user will win.
    rows, cols = (10, 10) 
    locationArray = [[0 for i in range(cols)] for j in range(rows)]

    #Initialize array below E = Empty Spot, B = Battleship, C = Carrier, S = Submarine, D = Destroyer, R = Cruiser
    for r in range(10):
        for c in range(10):
            locationArray[r][c] = ""
    lists =[]
    for i in range(100):
            lists.append(i)
    elements =[]
    for i in range(100):
            elements.append("e")
    while(True):   
        C = random.choice(lists)
        direct = [1, 2, 3, 4]
        arrangement = random.choice(direct)
        if arrangement == 1 and C in lists and C+10 in lists and C+20 in lists and C+30 in lists and C+40 in lists:
                elements[C] = "C"
                lists.remove(C)
                elements[C+10] = "C"
                lists.remove(C+10)
                elements[C+20] = "C"
                lists.remove(C+20)
                elements[C+30] = "C"
                lists.remove(C+30)
                elements[C+40] = "C"
                lists.remove(C+40)
                break
        elif arrangement == 2 and C in lists and C-10 in lists and C-20 in lists and C-30 in lists and C-40 in lists:
                elements[C] = "C"
                lists.remove(C)
                elements[C-10] = "C"
                lists.remove(C-10)
                elements[C-20] = "C"
                lists.remove(C-20)
                elements[C-30] = "C"
                lists.remove(C-30)
                elements[C-40] = "C"
                lists.remove(C-40)
                break
        elif arrangement == 3 and C%10 >= 4 and  C in lists and C-1 in lists and C-2 in lists and C-3 in lists and C-4 in lists:
                elements[C] = "C"
                lists.remove(C)
                elements[C-1] = "C"
                lists.remove(C-1)
                elements[C-2] = "C"
                lists.remove(C-2)
                elements[C-3] = "C"
                lists.remove(C-3)
                elements[C-4] = "C"
                lists.remove(C-4)
                break
        elif arrangement == 4 and C%10 <=5  and C in lists and C+1 in lists and C+2 in lists and C+3 in lists and C+4 in lists:
                elements[C] = "C"
                lists.remove(C)
                elements[C+1] = "C"
                lists.remove(C+1)
                elements[C+2] = "C"
                lists.remove(C+2)
                elements[C+3] = "C"
                lists.remove(C+3)
                elements[C+4] = "C"
                lists.remove(C+4)
                break
        else:
            continue

    while(True):   
        B = random.choice(lists)
        direct = [1, 2, 3, 4]
        arrangement = random.choice(direct)
        if arrangement == 1 and B in lists and B+10 in lists and    B+20 in lists and B+30 in lists:
                elements[B] = "B"
                lists.remove(B)
                elements[B+10] = "B"
                lists.remove(B+10)
                elements[B+20] = "B"
                lists.remove(B+20)
                elements[B+30] = "B"
                lists.remove(B+30)
                break
        elif arrangement == 2 and B in lists and B-10 in lists and B-20 in lists and B-30 in lists:
                elements[B] = "B"
                lists.remove(B)
                elements[B-10] = "B"
                lists.remove(B-10)
                elements[B-20] = "B"
                lists.remove(B-20)
                elements[B-30] = "B"
                lists.remove(B-30)
                break
        elif arrangement == 3 and B%10 >= 3 and  B in lists and B-1 in lists and B-2 in lists and B-3 in lists:
                elements[B] = "B"
                lists.remove(B)
                elements[B-1] = "B"
                lists.remove(B-1)
                elements[B-2] = "B"
                lists.remove(B-2)
                elements[B-3] = "B"
                lists.remove(B-3)
                break
        elif arrangement == 4 and B%10 <=6  and B in lists and B+1 in lists and B+2 in lists and B+3 in lists:
                elements[B] = "B"
                lists.remove(B)
                elements[B+1] = "B"
                lists.remove(B+1)
                elements[B+2] = "B"
                lists.remove(B+2)
                elements[B+3] = "B"
                lists.remove(B+3)
                break
        else:
            continue

    while(True):   
        R = random.choice(lists)
        direct = [1, 2, 3, 4]
        arrangement = random.choice(direct)
        if arrangement == 1 and R in lists and R+10 in lists and R+20 in lists:
                elements[R] = "R"
                lists.remove(R)
                elements[R+10] = "R"
                lists.remove(R+10)
                elements[R+20] = "R"
                lists.remove(R+20)
                break
        elif arrangement == 2 and R in lists and R-10 in lists and R-20 in lists:
                elements[R] = "R"
                lists.remove(R)
                elements[R-10] = "R"
                lists.remove(R-10)
                elements[R-20] = "R"
                lists.remove(R-20)
                break
        elif arrangement == 3 and R%10 >= 2 and  R in lists and R-1 in lists and R-2 in lists:
                elements[R] = "R"
                lists.remove(R)
                elements[R-1] = "R"
                lists.remove(R-1)
                elements[R-2] = "R"
                lists.remove(R-2)
                break
        elif arrangement == 4 and R%10 <=7  and R in lists and R+1 in lists and R+2 in lists:
                elements[R] = "R"
                lists.remove(R)
                elements[R+1] = "R"
                lists.remove(R+1)
                elements[R+2] = "R"
                lists.remove(R+2)
                break
        else:
            continue


    while(True):   
        S = random.choice(lists)
        direct = [1, 2, 3, 4]
        arrangement = random.choice(direct)
        if arrangement == 1 and S in lists and S+10 in lists and S+20 in lists:
                elements[S] = "S"
                lists.remove(S)
                elements[S+10] = "S"
                lists.remove(S+10)
                elements[S+20] = "S"
                lists.remove(S+20)
                break
        elif arrangement == 2 and S in lists and S-10 in lists and S-20 in lists:
                elements[S] = "S"
                lists.remove(S)
                elements[S-10] = "S"
                lists.remove(S-10)
                elements[S-20] = "S"
                lists.remove(S-20)
                break
        elif arrangement == 3 and S%10 >= 2 and  S in lists and S-1 in lists and S-2 in lists:
                elements[S] = "S"
                lists.remove(S)
                elements[S-1] = "S"
                lists.remove(S-1)
                elements[S-2] = "S"
                lists.remove(S-2)
                break
        elif arrangement == 4 and S%10 <=7  and S in lists and S+1 in lists and S+2 in lists:
                elements[S] = "S"
                lists.remove(S)
                elements[S+1] = "S"
                lists.remove(S+1)
                elements[S+2] = "S"
                lists.remove(S+2)
                break
        else:
            continue

    while(True):   
        D = random.choice(lists)
        direct = [1, 2, 3, 4]
        arrangement = random.choice(direct)
        if arrangement == 1 and D in lists and D+10 in lists:
                elements[D] = "D"
                lists.remove(D)
                elements[D+10] = "D"
                lists.remove(D+10)
                break
        elif arrangement == 2 and D in lists and D-10 in lists:
                elements[D] = "D"
                lists.remove(D)
                elements[D-10] = "D"
                lists.remove(D-10)
                break
        elif arrangement == 3 and D%10 >= 1 and  D in lists and D-1 in lists:
                elements[D] = "D"
                lists.remove(D)
                elements[D-1] = "D"
                lists.remove(D-1)
                break
        elif arrangement == 4 and D%10 <=8  and D in lists and D+1 in lists:
                elements[D] = "D"
                lists.remove(D)
                elements[D+1] = "D"
                lists.remove(D+1)
                break
        else:
            continue
    i = 0
    for x in range(10):
        for y in range(10):
                    locationArray[x][y] = elements[i]
                    i += 1
                    
    #Prints array for our reference
    def printArray():
        i = 0
        for x in range(10):
                for y in range(10):
                    print(locationArray[x][y],end =" ")
                    i += 1
                print("")
    printArray()
      
    Points  = 0
    BeginInput = input("Welcome to the game of Battleship! Would you like to (P)lay, Read the (I)nstructions, or (Q)uit?: ")
    quit = True
    while (quit):
            if (BeginInput == "P" or BeginInput == "Play" or BeginInput == "p" or BeginInput == "play"):
                    print("Hi lets start the game")
                    while (quit):
                        if (Points == 17):
                            print("congrats you won the game")
                            quit = False
                            break
                        else:
                            # INSERT FOLLOWING CODE OT INITIALIZING BOARD... BASICALLY THE GAME ITSELF
                            chooseRow = input("Which row do you want? or (Q)uit? ")
                            chooseRow = chooseRow.upper()
                            if (chooseRow == "Q" or chooseRow == "Quit" or chooseRow == "q" or chooseRow == "quit"):
                                quit = False
                                break
                            chooseColumn = int(input("Which column do you want? "))
                            ships = "CRBSD"
                            if chooseRow in mydict and chooseColumn < 11:
                                rowNumber = int(mydict[chooseRow])
                                chooseColumn -= 1
                                if locationArray[rowNumber][chooseColumn] in ships:
                                    print("It hit")
                                    Points +=1
                                    locationArray[rowNumber][chooseColumn] = "H"
                                    x_coord = -180+(chooseColumn*40)
                                    y_coord = 140-(rowNumber*40)
                                    t.color("green")
                                    draw_x(t,x_coord,y_coord,40)
                                    printArray()
                                elif locationArray[rowNumber][chooseColumn] == 'e':
                                    print("You missed it")
                                    locationArray[rowNumber][chooseColumn] = "M"
                                    x_coord = -180+(chooseColumn*40)
                                    y_coord = 125-(rowNumber*40)
                                    t.color("red")
                                    draw_o(t,x_coord,y_coord,16)
                                    printArray()
                                else:
                                    print("That stop is already selected")
                            else:
                                print("This is an invalid command!")
                                continue
                            print("Total points = "+str(Points))
                        #is a ship make it a H (Hit). else make it a Miss (M)
            elif (BeginInput == "I" or BeginInput == "Instructions" or BeginInput == "i" or BeginInput == "instructions"):
                print("The game of Battleship is a strategic, luck-based game! The objective is to sink all the ships of the computer which has"
                  "been randomly placed upon the board. The ships consist of: A carrier (5 spaces), a battleship (4 spaces), a cruiser (3 spaces),"
                  "a submarine (3 spaces) and a destroyer (2 spaces), which can only be placed vertically and horizontally upon the board! Occupying a"
                  "total of 17 spaces, how many shots do you think you’ll need to take?")
                BeginInput = input("Welcome to the game of Battleship! Would you like to (P)lay, Read the (I)nstructions, or (Q)uit?: ")
                continue

            elif (BeginInput == "Q" or BeginInput == "Quit" or BeginInput == "q" or BeginInput == "quit"):
                 quit = False
                 break
            else:
                print("This is an invalid command!")
                BeginInput = input("Welcome to the game of Battleship! Would you like to (P)lay, Read the (I)nstructions, or (Q)uit?: ")
                continue
    if(Points==17):
        playAgain = input("Do you want to play again?(y/n)")
        plan = True
        while (plan):
                if (playAgain == "n" or playAgain == "N"):
                    repeat = False
                    break
                elif (playAgain == "y" or playAgain == "Y"):
                    plan = False
                    continue
                else:
                    print("This is an invalid command!")

    else:
            repeat = False
            break             
