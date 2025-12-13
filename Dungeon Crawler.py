# helpers.py

# Dependencies:
#   - Colorama

# Operating System Dependencies:
#   - sys 
#   - time 
#   - os 
#   - platform 
#   - ctypes 

from colorama import Fore, Style, Back, init
import platform
import ctypes
import sys
import time
import os

# Color Print Function
# Description:
# - Allows printing with the ability to customize the back color and the text color.

def cPrint(string, textColor, backColor='black'):
    colorText = getattr(Fore, textColor.upper())
    backText = getattr(Back, backColor.upper())
    print(colorText + backText + string + Style.RESET_ALL)

# Print Spacer + Partial Color Print
# Description:
# - Prints a spacer above the message being printed, allows the user to overide the color as well.

def printSpacer(string, textColor='white'):
    colorText = getattr(Fore, textColor.upper())
    print('')
    print(colorText + string + Style.RESET_ALL)
    
# Slow Print
# Description:
# - Prints text slowly at a set delay

def slowPrint(text, delay):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush() # Forces the output to be written immediately
        time.sleep(delay) # Adjust the delay here

# Clear Terminal
# Description:
# - Clears the terminal based on the operating system type

def clearTerm():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Full Screen Terminal
# Descrption:
# - Fullscreen's the terminal being used
# WARNING:
# - This script talks to the Windows kernel! There may be instability running this script

def fullscreenTerm():
    if platform.system() == 'Windows':
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_MAXIMIZE = 3
        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
    else:
        print('Automatic Fullscreen is not supported on this system!')
        print('It is recommended to fullscreen the window yourself')
        time.sleep(5)

# dungeonCrawler.py

from colorama import Fore, Style, Back, init
# from helpers import * - HELPERS IS ABOVE THIS
import platform
import os

clearTerm()
fullscreenTerm()

responseTempBeginingAscii = input('Do you want to enable Ascii art? (yes / no):  ')
if responseTempBeginingAscii.lower() == 'yes':
    asciiArtEnabled = True
elif responseTempBeginingAscii.lower() == 'no':
    asciiArtEnabled = False
else:
    print('Please type a valid answer!')
    quit()

osType = platform.system()

def printMap(arr):
    for row in arr:
        print(row)

def grabTxt():
    print('Use "grab" to pick it up!')

DEBUG = False

map = [
    ['_____', '_____', '_____', '_____', '_____'],
    ['_____', '_____', '_____', '_____', '_____'],
    ['_____', '_____', '_____', '_____', '_____'],
    ['_____', '_____', '_____', '_____', '_____']
]

roomInventories = [ 
    ['', '', '', 'swordGreat', ''],
    ['', '', 'waterBucket', 'sword', '', ''],
    ['', 'sword', '', '', ''],
    ['', '', '', '', ''],
]

roomDangers = [    
    ['', '', '', 'fire', 'boss1'],
    ['', 'monster', '', '', ''],
    ['', '', '', 'monster', ''],
    ['', '', '', '', '']]

roomStaircases = [
    ['stairsTop', '', '', '', ''],
    ['', 'stairs', '', 'stairs', ''],
    ['stairs', '', '', 'stairs', ''],
    ['stairsBottom', '', '', 'stairsBottom', '']
]

# ASCII ART

asciiCastle = '''                                                  !_
                                                  |*~=-.,
                                                  |_,-'`
                                                  |
                                                  |
                                                 /^\\
                   !_                           /   \\
                   |*`~-.,                     /,    \\
                   |.-~^`                     /#"     \\
                   |                        _/##_   _  \\_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\\  |=_= -        |   |_,-~`  /^\\ |_ - =[]  |
      _  /   \\_|_=- _   _   _|  _|  _   /   \\|=_-      |
     [ ]/,    \\[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \\[ ]=-    |
      |/#"     \\_=-___=__=__- =-_ -=_ /#"     \\| _ []  |
     _/##_   _  \\_-_ =  _____       _/##_   _  \\_ -    |\\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \\
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
     | _- =-     |-_   | ((* |      |= _=       | -    |___\\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\\    | -=               |_=- /+\\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \\     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
'''

asciiBossType1 = '''
                 /\\
                 ||
   ____ (((+))) _||_
  /.--.\  .-.  /.||.\\
 /.,   \\\\(0.0)// || \\\\
/;`";/\ \\\\|m|//  ||  ;\\
|:   \ \__`:`____||__:|
|:    \__ \T/ (@~)(~@)|
|:    _/|     |\_\/  :|
|:   /  |     |  \   :|
|'  /   |     |   \  '|
 \_/    |     |    \_/
        |     |
        |_____|
    jgs |_____|'''

asciiUp = '''
       ##   
      ####  
     ###### 
       ##   
       ##   
       ##   
       ##   
'''
asciiSword= '''
       /\\   
       ||   
       ||   
      /||\\  
     |||||| 
       ||   
       ||   
       ||   
'''

asciiBucket = '''
       ##   
      #  #  
     #~~~~# 
     #~~~~# 
     #~~~~# 
     #~~~~# 
     #____# 
       ##   
'''

asciiMonster = '''
       /^^\\   
      /><  \\  
     (  OO  ) 
     (  ><  ) 
      \\ -- /  
      / /\\ \\  
     /_/  \\_\\ 
      ||  ||  
'''

asciiDown = '''
       ##   
       ##   
       ##   
       ##   
     ###### 
      ####  
       ##   
'''

asciiDownUp = '''
       ##          ##
       ##         #### 
       ##        ###### 
       ##          ## 
     ######        ## 
      ####         ##  
       ##          ##   
'''

asciiTorch = '''
       /\\   
      /^^\\  
      \\^^/  
       ||   
       ||   
       ||   
       ||   
       ||   
'''

def asciiPrint(asciiArt):
    for line in asciiArt:
        print(line)

currentInventory = []

monster = ''

firstRun = True

directionsAllowed = 'None'

playerY = 3
playerX = 0

map[playerY][playerX] = '__X__'

def lengthCheck():
    mapY = len(map)
    mapX = len(map[0])
    return mapY, mapX

mapY, mapX = lengthCheck()

def itemRoomCheck(roomInventories, playerX, playerY):
    if DEBUG == True:
        cPrint('INVENTORY CHECK = PANIC CODE: LAST PLAYER Y VALUE CHECKED WAS: ' + str(playerX), 'red')
    if roomInventories[playerY][playerX] != '':
        if 'sword' in roomInventories[playerY][playerX]:
            itemType = 'sword'
        if 'swordGreat' in roomInventories[playerY][playerX]:
            itemType = 'swordGreat'
        if 'waterBucket' in roomInventories[playerY][playerX]:
            itemType = 'waterBucket'
    else:
        itemType = 'noItems'
    return itemType

def stairsRoomCheck(directionsAllowed, playerY, playerX):
    if roomStaircases[playerY][playerX] != '':
        if 'stairsBottom' in roomStaircases[playerY][playerX]:
            directionsAllowed = 'up'
        elif 'stairsTop' in roomStaircases[playerY][playerX]:
            directionsAllowed = 'down'
        elif 'stairs' in roomStaircases[playerY][playerX]:
            directionsAllowed = 'all'
    else:
        directionsAllowed = 'noStairs'

    return directionsAllowed

def dangerRoomCheck():
    if roomDangers[playerY][playerX] != '':
        if 'monster' in roomDangers[playerY][playerX]:
            dangerType = 'monster'
        if 'fire' in roomDangers[playerY][playerX]:
            dangerType = 'fire'
        if 'boss1' in roomDangers[playerY][playerX]:
            dangerType = 'boss1'
    else:
        dangerType = 'noDangers'
        if DEBUG == True:
            printSpacer('PANIC CODE: NO DANGERTYPES DECTECTED - 2', 'red')
    return dangerType

def printInv(inv):
    print()
    print('Inventory: ' + str(inv))

def actionsHelpPrompt():
    print()
    print('h: shows this menu')
    print('up: goes to an upper room (if applicable)')
    print('down: goes to an lower room (if applicable)')
    print('left: goes to the left room (if applicable)')
    print('right: goes to the right room (if applicable)')
    print('grab: picks up an item (if there is an item in the room)')
    print('attack: attacks a monster (if there is an monster in the room)')
    print('use: uses an item (if you can use an item in this room)')
    print()
    
def actionTrigger(playerY, playerX, map, roomInventories, roomDangers, currentInventory):

# Mr. Fowler, if your wondering why I individulaly added isValidChoice = True to everything instead of the very end, it is so it does not interfere with
# the actionsHelpPrompt() script.

    isValidChoice = False

    # Checking for a valid prompt

    while not isValidChoice:
        print('')
        bob = input('What would you like to do?: ')
        #print(bob)
        if (bob != 'h') and (bob != 'up') and (bob != 'down') and (bob != 'left') and (bob != 'right') and (bob != 'grab') and (bob != 'attack') and (bob != 'use') and (bob != 'flee'):
            isValidChoice = False
            printSpacer('Please try again, that is not a valid prompt')
            input('Press Enter to continue...')
        else:
            if bob == 'h':
                actionsHelpPrompt()
                isValidChoice = False
            elif bob == 'up':
                if "monster" in roomDangers[playerY][playerX] or "boss1" in roomDangers[playerY][playerX]:
                    printSpacer('You try to pass the enemy. The enemy prevents you from passing!', 'cyan')
                    input('Press Enter to continue...')
                elif "fire" in roomDangers[playerY][playerX]:
                    printSpacer('You try to pass the fire, but the fire is too hot for you to pass', 'cyan')
                    input('Press Enter to continue...')
                else:
                    if roomStaircases[playerY][playerX] == 'stairsBottom' or roomStaircases[playerY][playerX] == 'stairs':
                        map[playerY][playerX] = '_____'
                        playerY -= 1
                        map[playerY][playerX] = '__X__'
                        print(playerY)
                    elif roomStaircases[playerY][playerX] == 'stairsTop':
                        printSpacer('You cant go up any further.', 'red')
                        input('Press Enter to continue...')
                    else:
                        printSpacer('There are no stairs in this room', 'red')
                        input('Press Enter to continue...')
                isValidChoice = True
            elif bob == 'down':
                if roomStaircases[playerY][playerX] == 'stairsTop' or roomStaircases[playerY][playerX] == 'stairs':
                    map[playerY][playerX] = '_____'
                    playerY += 1
                    map[playerY][playerX] = '__X__'
                elif roomStaircases[playerY][playerX] == 'stairsBottom':
                    printSpacer('You cant go down any further.', 'red')
                    input('Press Enter to continue...')
                else:
                    printSpacer('There are no stairs that lead you in that direction in this room', 'red')
                    input('Press Enter to continue...')
                isValidChoice = True
            elif bob == 'left':
                if playerX != 0:
                    map[playerY][playerX] = '_____'
                    playerX -= 1
                    map[playerY][playerX] = '__X__'
                    isValidChoice = True
                else:
                    printSpacer('You can not go left any further')
                    input('Please press enter to continue...')
            elif bob == 'right':
                if "monster" in roomDangers[playerY][playerX] or "boss1" in roomDangers[playerY][playerX]:
                    printSpacer('You try to pass the enemy. The enemy prevents you from passing!', 'cyan')
                    input('Press Enter to continue...')
                elif "fire" in roomDangers[playerY][playerX]:
                    printSpacer('You try to pass the fire, but the fire is too hot for you to pass', 'cyan')
                    input('Press Enter to continue...')
                else:
                    if playerX != len(map[playerY]) -1: 
                        map[playerY][playerX] = '_____'
                        playerX += 1
                        map[playerY][playerX] = '__X__'
                        isValidChoice = True
                    else:
                        printSpacer('You can not go right any further')
                        input('Please press enter to continue...')
            elif bob == 'grab':
                if roomInventories[playerY][playerX] == 'swordGreat' or roomInventories[playerY][playerX] == 'waterBucket' or roomInventories[playerY][playerX] == 'sword':
                    if "monster" in roomDangers or "boss1" in roomDangers:
                        printSpacer('You try to grab the item. The enemy prevents you from grabing the item!', 'cyan')
                    elif "fire" in roomDangers[playerY][playerX]:
                        printSpacer('You try to reach over the fire, but the fire is too hot for you to grab the item!', 'cyan')
                    else:
                        if roomInventories[playerY][playerX] == 'swordGreat':
                            print()
                            cPrint('You grabbed the Great Sword off the ground, gaining a sudden surge of power', 'yellow')
                            currentInventory.append('Great Sword')
                            roomInventories[playerY][playerX] = ''
                        elif roomInventories[playerY][playerX] == 'waterBucket':
                            currentInventory.append('Water Bucket')
                            roomInventories[playerY][playerX] = ''
                            print()
                            cPrint('You Grabbed the water bucket off the ground, splashing some water on yourself in the process', 'yellow')
                        elif roomInventories[playerY][playerX] == 'sword':
                            currentInventory.append('Sword')
                            roomInventories[playerY][playerX] = ''
                            print()
                            cPrint('You grabbed the sword off the ground', 'yellow')
                        else:
                            print('There is nothing in this room.', 'red')
                    input('Press Enter to continue...')
                isValidChoice = True
            elif bob == 'flee':
                # Second Easter Egg
                print('')
                cPrint('You flee the house, being a little coward and baby in the process. However, on your way out, you ran into a street full of commerical trucks! ', 'magenta')
                cPrint('You can guess on what your stupidity caused ', 'magenta')
                quit()
            elif bob == 'attack':
                if roomDangers[playerY][playerX] == 'monster' or roomDangers[playerY][playerX] == 'boss1':
                    if roomDangers[playerY][playerX] == 'monster':
                        if 'Sword' in currentInventory or 'Great Sword' in currentInventory:
                            if 'Great Sword' in currentInventory:
                                if DEBUG == True:
                                    cPrint('DEBUG: Attacked Using Great Sword - LINE 233 - SCENARIO 3', 'red')
                                    print()
                                # Easter Egg :)
                                userTryingToUseGreatSwordOnNormalMonster = input('\033[35mAre you really sure you want to do this? (yes / no): \033[0m')
                                if userTryingToUseGreatSwordOnNormalMonster == 'yes':
                                    print()
                                    cPrint('So two things: One, you softlocked yourself. Two, please get your head checked', 'magenta')
                                    cPrint('So Im just going to end the program here, saves us both time', 'magenta')
                                    quit()
                            elif 'Great Sword' in currentInventory and 'Sword':
                                if DEBUG == True:
                                    cPrint('DEBUG: Attacked Using Sword - LINE 225 - SCENARIO 1', 'red')
                                roomDangers[playerY][playerX] = ''
                                currentInventory.remove('Sword')
                                print()
                                cPrint('You attack the monster and it faded away to the underground!', 'cyan')
                                input('Press Enter to continue...')
                            elif 'Sword' in currentInventory:
                                if DEBUG == True:
                                    cPrint('DEBUG: Attacked Using Sword - LINE 243 - SCENARIO 2', 'red')
                                roomDangers[playerY][playerX] = ''
                                currentInventory.remove('Sword') 
                                print()
                                cPrint('You attack the monster and it faded away to the underground!', 'cyan')
                                input('Press Enter to continue...')
                        else:
                            print('')
                            cPrint('You need a weapon to attack the monster...', 'cyan')
                            input('Press Enter to continue...')
                    elif roomDangers[playerY][playerX] == 'boss1':
                        if 'Great Sword' in currentInventory:
                            printSpacer('Congrats! You killed the boss. For your hard work, we will delete this save :)', 'magenta')
                            quit()
                        else:
                            printSpacer('You need a Great Sword to fight this boss!', 'blue')
                            input('Press Enter to continue...')
                else:
                    cPrint('You need an enemy to attack ಠ_ಠ', 'cyan')
                    input('Press Enter to continue...')
                isValidChoice = True
            elif bob == 'use':
                if 'fire' in roomDangers[playerY][playerX]:
                    print()
                    cPrint('You try to extinguish the fire', 'cyan')
                    if 'Water Bucket' in currentInventory:
                        cPrint('You Sucessfully Extinguish the fire', 'cyan')
                        roomDangers[playerY][playerX] = ''
                        currentInventory.remove('Water Bucket')
                    else:
                        cPrint('You realize you need a water bucket to extinguish the fire', 'cyan')
                else:
                    print()
                    print('You cant use any items in this room')
                input('Press Enter to continue...')
                isValidChoice = True
    return playerY, playerX, map, roomInventories, roomDangers, currentInventory

while True:
    clearTerm()

    if asciiArtEnabled == True:
        print(asciiCastle)

    if firstRun == True:
        firstRun = False
        slowPrint('Deep in the Abyssal Crypt, Kael faces the awakening Void Reaper—a deadly force threatening to consume the world. With no one else left, he must fight or be swallowed by darkness.', 0.01)
        print()
        slowPrint('\033[31mAt any time, you can use "h" as an action to see a menu that shows the options you have.\033[0m', 0.05)
        print()
        firstRunAnswerToQuestion = input('\033[35mReady? (yes / no): \033[0m ')
        clearTerm()
        if asciiArtEnabled == True:
            print(asciiCastle)
        if firstRunAnswerToQuestion.lower() == 'yes' or firstRunAnswerToQuestion.lower() == 'no':
            if firstRunAnswerToQuestion.lower() == 'no':
                print('Re run the program to continue!')
                quit()   
        else:
            print('Re run the program to continue! Please specify a correct answer next time')
            quit()          

    if DEBUG == True:
        cPrint('##################', 'red')
        cPrint('DEBUG MODE ACTIVE', 'red')
        cPrint('##################', 'red')

    if DEBUG == True:
        cPrint('Y:' + str(playerY) + ' X:' +  str(playerX), 'red')

    printMap(map)
    printInv(currentInventory)

    # Checking room Dangers

    dangerType = dangerRoomCheck()
    if dangerType == 'monster':
        printSpacer('You enter the next room to be ambushed by a monster!', 'cyan')
        if asciiArtEnabled == True:
            print(asciiMonster)
    elif dangerType == 'boss1':
        printSpacer('You enter the room to see a dangerous enemy who needs to be stopped!', 'cyan')
        if asciiArtEnabled == True: 
            print(asciiBossType1)
    elif dangerType == 'fire':
        printSpacer('You enter the room to see a raging fire', 'cyan')
        if asciiArtEnabled == True:
            print(asciiTorch)
    else:
        if DEBUG == True:
            cPrint('PANIC CODE: NO DANGERTYPES DECTECTED - 1', 'red')
    
    # Checking Items

    itemType= itemRoomCheck(roomInventories, playerX, playerY)
    if itemType == 'sword':
        print()
        cPrint('You enter the room to see a sword on the ground!', 'yellow')
        grabTxt()
        if asciiArtEnabled == True:
            print(asciiSword)
    elif itemType == 'swordGreat':
        print()
        cPrint('You enter the room to see a large sword!', 'yellow')
        if asciiArtEnabled == True:
            print(asciiSword)
        grabTxt()
    elif itemType == 'waterBucket':
        print()
        cPrint('You enter the room to see a rusty water bucket!', 'yellow')
        if asciiArtEnabled == True:
            print(asciiBucket)
        grabTxt()
    
    # Checking Stairs

    directionsAllowed = stairsRoomCheck(directionsAllowed, playerY, playerX)
    if directionsAllowed == 'up' or directionsAllowed == 'down' or directionsAllowed == 'all':
        if directionsAllowed == 'up':
            print()
            cPrint('You see some stairs that can take you to the next floor', 'green')
            if asciiArtEnabled == True: 
                print(asciiUp)
        elif directionsAllowed == 'down':
            print()
            cPrint('You enter the room, you can still go down a floor.', 'green')
            if asciiArtEnabled == True: 
                print(asciiDownUp)
        elif directionsAllowed == 'all':
            print()
            cPrint('You see some stairs that allows you to go up and down floors!', 'green')
            if asciiArtEnabled == True: 
                print(asciiDownUp)

    if DEBUG == True:
        print('')
        cPrint('DEBUG: ', 'red')
        cPrint('directionsAllowed: ' + directionsAllowed, 'red')
        cPrint('roomInventories: ' + roomInventories[playerY][playerX], 'red')
        cPrint('roomDangers: ' + roomDangers[playerY][playerX], 'red')
        cPrint('dangerType: ' + dangerType, 'red')

    playerY, playerX, map, roomInventories, roomDangers, currentInventory  = actionTrigger(playerY, playerX, map, roomInventories, roomDangers, currentInventory)