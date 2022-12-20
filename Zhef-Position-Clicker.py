import pyautogui as pg
import time
import keyboard
import readchar
from numpy import loadtxt
import re
import sys





def getPos(key, i):
    pos = pg.position()
    print(f"{i} position set at {pos} ( BINDED to '{key}' )")
    print(" ")
    return pos

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1




firstPos = []
secondPos = []
thirdPos = []
fourthPos = []
fifthPos = []
sixthPos = []


firstSavePos = []
secondSavePos = []
thirdSavePos = []
fourthSavePos = []
fifthSavePos = []
sixthSavePos = []
positionList = []


print("")
print("[------Welcome to Zhef's Position Clicker-----]")

print(" ")


saveOn = False

print("# Press 'y' if you want to use your SAVE FILE. If not, press any other key #")
useSave = readchar.readkey()

if(useSave == "y"):
    saveOn = True;
    fo = open("D:/Users/rules/Desktop/Pyt/Final/Zhef's Position Clicker/savefile.txt", "r")
    itemsRead = fo.read()
    itemsClean = itemsRead.replace("'","")
    items = itemsClean.split(".")
    positionList.append(items)



    


while saveOn == False:

    print("# Press y to start FIRST position capture")

    startFirstCapture = readchar.readkey()


    if (startFirstCapture == "y"):
        key = "q"
        i = "First"


        firstPos.append(getPos(key, i))
        


    print("# Press y to start SECOND position capture")
    startSecondCapture = readchar.readkey()



    if (startSecondCapture == "y"):
        key = "w"
        i = "Second"
        secondPos.append(getPos(key, i))


    ############



    print("# Press y to start THIRD position capture")
    startThirdCapture = readchar.readkey()

    if (startThirdCapture == "y"):
        key = "e"
        i = "Third"
        thirdPos.append(getPos(key, i))


    ############




    print("# Press y to start FOURTH position capture")
    startFourthCapture = readchar.readkey()

    if (startFourthCapture == "y"):
        key = "a"
        i = "Fourth"
        fourthPos.append(getPos(key, i))


    ############




    print("# Press y to start FIFTH position capture")
    startFifthCapture = readchar.readkey()

    if (startThirdCapture == "y"):
        key = "s"
        i = "Fifth"
        fifthPos.append(getPos(key, i))


    ############




    print("# Press y to start SIXTH position capture")
    startSixthCapture = readchar.readkey()

    if (startSixthCapture == "y"):
        key = "d"
        i = "Sixth"
        sixthPos.append(getPos(key, i))
        break

    if (startSixthCapture  != "y"):
        break




switch = True;
print(" ")
print("--------------------------------------------") 
print(" ")
print("Successfully collected all 6 positions :D") 
print(" ")
print("Use q, w, e, a, s, d to initiate click with their respective positions")
print(" ")
print("Listening for key presses... press  ` to end listening ")  



while saveOn == False:
    saveDecide = ''

    if (firstPos):
        if keyboard.is_pressed("q"):
            
            pg.moveTo(firstPos[0])
            pg.leftClick()

    if (secondPos):
        if keyboard.is_pressed("w"):
            pg.moveTo(secondPos[0])
            pg.leftClick()

    if (thirdPos):
        if keyboard.is_pressed("e"):
            pg.moveTo(thirdPos[0])
            pg.leftClick()

    if (fourthPos):
        if keyboard.is_pressed("a"):
            pg.moveTo(fourthPos[0])
            pg.leftClick()

    if (fifthPos):
        if keyboard.is_pressed("s"):
            pg.moveTo(fifthPos[0])
            pg.leftClick()

    if (sixthPos):
        if keyboard.is_pressed("d"):
            pg.moveTo(sixthPos[0])
            pg.leftClick()

    
    if keyboard.is_pressed("`"):
        one = [1]
        for i in one:
            print("# Save positions (PRESS Y or N ONLY)")
        
        saveDecide = readchar.readkey()
        
        if (saveDecide == "y"):
            file = open("D:/Users/rules/Desktop/Pyt/Final/Zhef's Position Clicker/savefile.txt", 'w')

            if (firstPos and secondPos and thirdPos and fourthPos and fifthPos and sixthPos):
                file.write(f"{firstPos[0]}.{secondPos[0]}.{thirdPos[0]}.{fourthPos[0]}.{fifthPos[0]}.{sixthPos[0]}")
                print("Positions saved successfully.")
                print("")
                print("Thank you for using Zhef's Position Clicker!")
                print("")
                sys.exit()
            else:
                print("Can't save. Not all positions are set. Please make sure to set all positions to continue saving next time.")
                print("Ending program...")
                countdown(5)
                sys.exit()

        if (saveDecide == "n"):
                print("")
                print("Thank you for using Zhef's Position Clicker!")
                print("")
                print("Ending program...")
                countdown(3)
                sys.exit()
              



if (saveOn == True):
    firstSavePos.append(positionList[0][0])
    secondSavePos.append(positionList[0][1])
    thirdSavePos.append(positionList[0][2])
    fourthSavePos.append(positionList[0][3])
    fifthSavePos.append(positionList[0][4])
    sixthSavePos.append(positionList[0][5])

    firstSavePosXY = re.findall(r'\d+', firstSavePos[0])
    secondSavePosXY = re.findall(r'\d+', secondSavePos[0])
    thirdSavePosXY = re.findall(r'\d+', thirdSavePos[0])
    fourthSavePosXY = re.findall(r'\d+', fourthSavePos[0])
    fifthSavePosXY = re.findall(r'\d+', fifthSavePos[0])
    sixthSavePosXY = re.findall(r'\d+', sixthSavePos[0])

while saveOn == True:
    saveDecide = ''
    
    if (firstSavePos):
        if keyboard.is_pressed("q"):
            pg.moveTo(int(firstSavePosXY[0]), int(firstSavePosXY[1]))
            pg.leftClick()

    if (secondSavePos):
        if keyboard.is_pressed("w"):
            pg.moveTo(int(secondSavePosXY[0]), int(secondSavePosXY[1]))
            pg.leftClick()

    if (thirdSavePos):
        if keyboard.is_pressed("e"):
            pg.moveTo(int(thirdSavePosXY[0]), int(thirdSavePosXY[1]))
            pg.leftClick()

    if (fourthSavePos):
        if keyboard.is_pressed("a"):
            pg.moveTo(int(fourthSavePosXY[0]), int(fourthSavePosXY[1]))
            pg.leftClick()

    if (fifthSavePos):
        if keyboard.is_pressed("s"):
            pg.moveTo(int(fifthSavePosXY[0]), int(fifthSavePosXY[1]))
            pg.leftClick()

    if (sixthSavePos):
        if keyboard.is_pressed("d"):
            pg.moveTo(int(sixthSavePosXY[0]), int(sixthSavePosXY[1]))
            pg.leftClick()

        
    if keyboard.is_pressed("`"):
        print("")
        print("Thank you for using Zhef's Position Clicker!")
        print("")
        break
        

