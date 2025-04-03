import random
import os
raw = []
mat = []
display = []
def placemine():
    ra = []
    ra.append(random.randint(0,len(raw)-1))
    ra.append(random.randint(0,len(raw)-1))
    if not raw[ra[0]][ra[1]]:
        raw[ra[0]][ra[1]] = True
    else:
        placemine()
def generate(size, mines):
    for i in range(0,size):
        raw.append([])
    for i in range(0,size):
        for j in range(0, size):
            raw[i].append(False)
    for i in range(0, mines):
        placemine()
def checktile(x,y):
    ret = 0
    if raw[x][y]:
        return "X"
    else:
        if x>0 and y>0 and raw[x-1][y-1]:
            ret+=1
        if x>0 and raw[x-1][y]:
            ret+=1
        if x>0 and y < len(raw)-1 and raw[x-1][y+1]:
            ret+=1
        if y>0 and raw[x][y-1]:
            ret+=1
        if y < len(raw)-1 and raw[x][y+1]:
            ret+=1
        if y>0 and x < len(raw)-1 and raw[x+1][y-1]:
            ret+=1
        if x < len(raw)-1 and raw[x+1][y]:
            ret+=1
        if x < len(raw)-1 and y < len(raw)-1 and raw[x+1][y+1]:
            ret+=1
        return str(ret)
def generatemat():
    global mat
    global display
    for i in range(0,len(raw)):
        mat.append([])
        display.append([])
        for j in range(0,len(raw)):
            mat[i].append(checktile(i,j))
            display[i].append("?")
        
def revealtiles(x,y):
    global display
    global mat
    if display[x][y] == "?":
        display[x][y] = mat[x][y]
        if mat[x][y] == "0":
            if x-1 >= 0 and y-1 >= 0:
                revealtiles(x-1,y-1)
            if x-1 >= 0:
                revealtiles(x-1,y)
            if x-1 >= 0 and y+1 < len(raw):
                revealtiles(x-1,y+1)
            if y-1 >= 0:
                revealtiles(x,y-1)
            if y+1 < len(raw):
                revealtiles(x,y+1)
            if x+1 < len(raw) and y-1 >= 0:
                revealtiles(x+1,y-1)
            if x+1 < len(raw):
                revealtiles(x+1,y)
            if x+1 < len(raw) and y+1 < len(raw):
                revealtiles(x+1,y+1)
        if raw[x][y]:
            display = mat
            lose()
        for x in range(0,len(raw)):
            for y in range(0,len(raw)):
                if x>0 and y>0 and display[x-1][y-1] == "0":
                    display[x][y]=mat[x][y]
                if x>0 and display[x-1][y] == "0":
                    display[x][y]=mat[x][y]
                if x>0 and y < len(raw)-1 and display[x-1][y+1] == "0":
                    display[x][y]=mat[x][y]
                if y > 0 and display[x][y-1] == "0":
                    display[x][y]=mat[x][y]
                if y < len(raw)-1 and display[x][y+1] == "0":
                    display[x][y]=mat[x][y]
                if x < len(raw)-1 and y > 0 and display[x+1][y-1] == "0":
                    display[x][y]=mat[x][y]
                if x < len(raw)-1 and display[x+1][y] == "0":
                    display[x][y]=mat[x][y]
                if y < len(raw)-1 and x < len(raw)-1 and display[x+1][y+1] == "0":
                    display[x][y]=mat[x][y]
            
def lose():
    printdisplay()
    print("You lose! Boohoo")
    exit(0)
def printdisplay():
    os.system("clear")
    print("Size: " + str(len(raw)) + "x" + str(len(raw)))
    print("Bombs: " + str(len(raw)))
    print("1 2 3 4 5 6 7 8 9 10")
    print("---------------------")
    for i in range(0,len(display)):
        for j in display[i]:
            if j == "?":
                print("⬛", end='')
            elif j == "X":
                print("💣", end='')
            else:
                e = 0
                if j == "0":
                    e = "0️⃣"
                if j == "1":
                    e = "1️⃣"
                if j == "2":
                    e = "2️⃣"
                if j == "3":
                    e = "3️⃣"
                if j == "4":
                    e = "4️⃣"
                if j == "5":
                    e = "5️⃣"
                if j == "6":
                    e = "6️⃣"
                if j == "7":
                    e = "7️⃣"
                if j == "8":
                    e = "8️⃣"
                print(e, end=" ")
        print(" | ",i+1)
def checkwin():
    for x in range(0,len(raw)):
        for y in range(0,len(raw)):
            if not raw[x][y]:
               if display[x][y] == "?":
                   return False
    return True
def maingame():
    printdisplay()
    x = int(input("X: "))-1
    y = int(input("Y: "))-1
    revealtiles(y,x)
    if checkwin():
        display = mat
        printdisplay()
        print("You win!")
        exit(0)
    maingame()
generate(int(input("Size: ")),int(input("Bombs: ")))
generatemat()
maingame()
