# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# N: Sebastian Deluca
# D: April 18th, 2020
# FN: Deluca_EscapeFromTheDungeon.py
# D: The purpose of this program is to create a dungeon-crawling experience for the user
#   utilizing the power of file-reading. The user will enter procedurally generated rooms
#   that will have a unique experience in them whilst trying to find the escape.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
What To Do:



'''

import random
import time
savefile = 'Deluca_EscapeFromTheDungeon_SavedCharacter.txt'
resourcesfile = 'Deluca_EscapeFromTheDungeon_Resources.txt'
roomCount = 0 # Set constant for room count
shopGoodbye = ['I\'ll see you \'round... I\'m packin\' up outta here right now.', 'Thank you for yer business fella. Catch you later.', 'Bye now.']

class Character():  # A class for the playerCharacter
    def __init__(self, information, inventory): # Construct the Player based on the information given by CharCreator()
        self.name = information[0]
        self.race = information[1]
        self.className = information[2]
        self.powerPerc = float(information[3])
        self.speedPerc = float(information[4])
        self.intellectPerc = float(information[5])
        self.lockPick = float(information[6])
        self.inv = inventory
        self.weapon = Weapon(inventory[0])
        try: # Exception Handling for when the character is made in Create-A-Character Mode. Health & Balance are not assigned in this case.
            self.health = float(information[7])
            self.balance = float(information[8])
        except IndexError:
            self.health = 20
            self.balance = 0
        self.armor = []
        self.statistics = [self.name,self.race,self.className,self.powerPerc,self.speedPerc,self.intellectPerc,self.lockPick] # Encompass all in a list for viewStats()

    def viewStats(self): # Show the player their stats
        print('----PLAYER STATS----'.center(100,' '))
        print(('Name: ' + self.name).center(100,' '))
        print(('Race: ' + self.race).center(100,' '))
        print(('Class: ' + self.className).center(100,' '))
        print('--Power Levels---'.center(100,' '))
        print(('Extra Damage: ' + str(self.powerPerc /20) + '%').center(100,' '))
        print(('Dodge Chance: ' + str(self.speedPerc) + '%').center(100,' '))
        print(('Barter Chance: ' + str(self.intellectPerc) + '%').center(100,' '))
        print(('Unlockable Chest Chance: ' + str(self.lockPick) + '%').center(100,' '))
        wS(1)
        print(('Your current weapon, ' + str(self.weapon.name) + ', does ' + str(self.weapon.damage) + ' damage.').center(100,' '))
        wS(1)
        input('ME: Okay. [Press Enter to Continue]'.center(100,' ')) # ALLOW USER TO CONTINUE

    def showInv(self): # Show the player their inventory
        print('---YOUR ITEMS----'.center(100,' '))
        count = 0
        for i in self.inv: # Display the user their items in a list
            count +=1
            if count == 1:
                print('EQUIPPED: '+ str(count) + ': ' + i + ' | ', end='')
            else:
                print(str(count) + ': ' +i + ' | ', end ='')
        wS(1)
        print(('COINS: ' + str(self.balance)).center(100,' ')) # Display coins to the user
        print('Health: ' + str(self.health), '| Power: ' +str(self.powerPerc), '| Speed: ' +str(self.speedPerc), '| Intellect: ' +str(self.intellectPerc), '| Lockpick: ' +str(self.lockPick)) # Show the user their stats
    def eatFood(self,food): # Add health to the player when they eat food
        if food == 'Bread':
            self.health += 2
        elif food == 'Steak':
            self.health += 5
        index = self.inv.index(food)
        del(self.inv[index])

    def drinkPotion(self, potion): # Add to user stats with potion
        self.speedPerc = int(self.speedPerc)
        self.intellectPerc = int(self.intellectPerc)
        self.lockPick = int(self.lockPick)
        if potion == 'Red Potion' or potion == 'Ring of Healing':
            self.health += 10 # Add Health to Player
            wS(1)
            print('Health Increased by 10')
        elif potion == 'Blue Potion':
            self.speedPerc += 2 # Add Speed to Player
            wS(1)
            print('Speed Increased by 2')
        elif potion == 'Green Potion':
            self.intellectPerc += 2 # Add Intellect to Player
            wS(1)
            print('Intellect Increased by 2')
        elif potion == 'Purple Potion':
            self.lockPick += 2 # Add Unlockable Chest Chance
            wS(1)
            print('Lockpicking Increased by 2')
        elif potion == 'Ring of Damage':
            self.powerPerc += 4
            wS(1)
            print('Power Increased by 4')
        elif potion == 'Ring of Resistance': # OP Ring!!!!
            self.powerPerc += 1
            self.speedPerc +=1
            self.health += 1
            self.intellectPerc +=1
            self.lockPick +=1
            wS(1)
            print('All Stats Increased!')
        index = self.inv.index(potion)
        del(self.inv[index])

    def equipArmor(self,armor): # Allow user to equip armor

        #Leather Armor
        if armor == 'Leather Boots' and 'Leather Boots' not in self.armor: # All lines check if the user already has the armor equipped to prevent duplication.
            self.health += 2
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Leather Leggings'and 'Leather Leggings' not in self.armor:
            self.health += 3
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Leather Chestplate'and 'Leather Chestplate' not in self.armor:
            self.health +=3
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Leather Helmet'and 'Leather Helmet' not in self.armor:
            self.health += 2
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        #Steel Armor
        elif armor == 'Steel Boots' and 'Steel Boots' not in self.armor:
            self.health += 5
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Steel Leggings' and 'Steel Leggings' not in self.armor:
            self.health += 6
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])

        elif armor == 'Steel Chestplate' and 'Steel Chestplate' not in self.armor:
            self.health +=6
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])

        elif armor == 'Steel Helmet' and 'Steel Helmet' not in self.armor:
            self.health += 5
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])

        #Impen. Armor
        elif armor == 'Impenetrable Boots' and 'Impenetrable Boots' not in self.armor:
            self.health += 10
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Impenetrable Leggings' and 'Impenetrable Leggings' not in self.armor:
            self.health += 10
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])

        elif armor == 'Impenetrable Chestplate' and 'Impenetrable Chestplate' not in self.armor:
            self.health +=10
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        elif armor == 'Impenetrable Helmet' and 'Impenetrable Helmet' not in self.armor:
            self.health += 10
            self.armor.append(armor)
            index = self.inv.index(armor)
            del(self.inv[index])
            
        else: # Tell user they cant equip
            wS(1)
            print(('ME: Huh... I can\'t put this armor on. I\'m gonna drop it.').center(100, ' '))
            index = self.inv.index(armor)
            del (self.inv[index])
        
    def equipUnequip(self,wep): # Equip and Unequip Weapons
        replaceNum = self.inv.index(wep)
        del(self.inv[replaceNum]) # Delete the duplicate weapon
        self.weapon = Weapon(wep)
        self.inv.insert(0,wep)   # Make the weapon selected the 'EQUIPPED' weapon
    
    def useInventory(self): # Allow the user to use whatever is in their inventory
        wS(1)
        try:
            choice = input(('ME: I gotta pick something... #').center(100,' '))
            if int(choice)-1 == 0: #User selects equipped weapon
                wS(1)
                print(('ME: ...I already have that equipped.').center(100, ' '))
                wS(1)
                print(('Press Enter.').center(100, ' '))
            elif choice == '': # User just presses enter
                pass
            elif self.inv[int(choice) - 1] in food: # If the selected item is a fooditem
                self.eatFood(self.inv[int(choice) - 1])
            elif self.inv[int(choice) - 1] == 'Red Potion' or self.inv[int(choice) - 1] == 'Blue Potion' or self.inv[int(choice) - 1] == 'Green Potion' or self.inv[int(choice) - 1] == 'Purple Potion' or self.inv[int(choice) - 1] == 'Ring of Healing' or self.inv[int(choice) - 1] == 'Ring of Damage' or self.inv[int(choice) - 1] == 'Ring of Resistance' : #The user selects a potion

                self.drinkPotion(self.inv[int(choice) - 1])
            elif self.inv[int(choice) - 1] in armor: # If user wants to equip armor
                self.equipArmor(self.inv[int(choice) - 1])
            elif self.inv[int(choice) - 1] in weapons or self.inv[int(choice) - 1] in magicItems and (self.inv[int(choice) - 1] != 'Ring of Damage' and self.inv[int(choice) - 1] != 'Ring of Healing' and self.inv[int(choice) - 1] != 'Ring of Resistance'): # User wants to switch weapons
                self.equipUnequip(self.inv[int(choice) - 1])
            else: # User Doesnt Pick SOMETHING
                pass
        except IndexError: # User selects a non-existent space
            print(('I don\'t have that space in my pack.'))
        except ValueError:  # User doesn't enter a number
            pass
        wS(1)
        print('ME: I\'m gonna close up my backpack now.')
        input('Press any key to Continue')
        wS(100)

class Weapon(): # A class for weapons
    def __init__(self, wepName):  # Determine weapon damage dependant on weapon name
        self.name = wepName
        if wepName == 'Small Sword':
            self.damage = 1
        elif wepName == 'Medium Sword':
            self.damage = 1.25
        elif wepName == 'Large Sword':
            self.damage = 1.85
        elif wepName == 'Small Axe':
            self.damage = 1.60
        elif wepName == 'Medium Axe':
            self.damage = 1.90
        elif wepName == 'Large Axe':
            self.damage = 2.10
        elif wepName == 'Crossbow':
            self.damage = 2.0
        elif wepName == 'Short Bow':
            self.damage = 1.85
        elif wepName == 'Long Bow':
            self.damage = 1.90
        elif wepName == 'Weak Wand':
            self.damage = 1
        elif wepName == 'Wand':
            self.damage = 1.5
        elif wepName == 'Strong Wand':
            self.damage = 2.0
        elif wepName == 'Master Wand': # STRONGEST WEAPON IN THE GAME
            self.damage = 3.0
        else:
            self.damage = 0

class Enemy():
    def __init__(self,name,dmg,able,hlth): # Construct the enemy with the values given outside the program
        self.name = name
        self.damage = dmg
        self.ability = able
        self.health = hlth

    def useAbility(self,player): # Use a special ability that increases damage on the player
        player.health -=self.damage *3

    def attack(self,player): # Damage the player
        player.health -= self.damage

class Chest(): # Chest class for when a chest is in a room
    def __init__(self,type): # Construct the chest with a random item and gold amount
        number = random.randint(1,44)
        self.type = type
        self.item = detItem(number)
        self.gold = random.randint(10,50)

    def getOpened(self,player): # Open the chest [Player]
        if self.type == 'Normal':
            if 'Chest Key' in player.inv:
                player.balance += self.gold # Add the gold from the chest to the player's coins
                print(('You found ' + str(self.gold) + ' Coins in the Chest!').center(100, ' '))
                wS(1)
                self.gold = 0 # Set to 0
                player.inv.append(self.item) # Append the item in the chest to the player's inventory
                print(('You found a ' + str(self.item) + ' in the Chest!').center(100, ' '))
                wS(1)
                key = player.inv.index('Chest Key')
                del (player.inv[key])
            else:
                wS(1)
                print(('ME: Shoot, I don\'t have a Chest Key.').center(100, ' ')) # Tell user they don't have a chest key
        elif self.type == 'Master':
            num = random.randint(25,37)
            self.item = detItem(num)
            if 'Master Chest Key' in player.inv:
                player.balance += self.gold * 2 # Add the gold from the chest to the player's coins
                print(('You found ' + str(self.gold *2) + ' Coins in the Chest!').center(100,' '))
                wS(1)
                self.gold = 0 # Set to 0
                player.inv.append(self.item) # Append the item in the chest to the player's inventory
                print(('You found a ' + str(self.item) + ' in the Chest!').center(100, ' '))
                wS(1)
                key = player.inv.index('Master Chest Key')
                del(player.inv[key])
            else:
                wS(1)
                print(('ME: Shoot, I don\'t have a Master Chest Key.').center(100, ' ')) # Tell user they don't have a chest key

def charCreator(): # Function that creates the Character for the Player
    wS(1)
    print(('You can\'t seem to remember who you are... why don\'t you give yourself a name?').center(100, ' '))
    wS(1)
    firstName = input('ME: My first name is ') # Get user first name
    lastName = input('ME: ...and my last name is ') # Get user last name
    userName = firstName + ' ' + lastName # Concatenate both names to create Char name
    wS(1)
    raceLoop = True # Begin a loop to prevent not picking a race
    while raceLoop:
        print(('You look down at your hands... what Race are you?').center(100, ' '))
        counter = 0
        for i in races: # Show user all of the races
            counter += 1
            print('| ' + str(counter) + ': ' + i)
        print('| 5: Random')
        wS(1)
        race = input('I am a ')
        if race == '1' or race == 'Nord' or race == 'nord': # User chose Nord
            raceChc = 'Nord'
            raceLoop = False
        elif race == '2' or race == 'Khajit' or race == 'khajit': # User picks Khajit race
            raceChc = 'Khajit'
            raceLoop = False
        elif race == '3' or race == 'Dwarf' or race == 'dwarf': # User picks Dwarf race
            raceChc = 'Dwarf'
            raceLoop = False
        elif race == '4' or race == 'Celestial' or race =='celestial': # User picks Celestial race
            raceChc ='Celestial'
            raceLoop = False
        elif race == '5' or race == 'random' or race == 'Random': # User picks random
            raceNum = random.randint(0,3) #Randomize a number between the amount of races available, and pick one from the list
            raceChc = races[raceNum]
            raceLoop = False
        else: # User picks something that is not available
            print(('That Race does not exist.').center(100, ' '))
            wS(1)
            print(('ME: Let me try that again. [Press Enter to Continue]'))

    wS(1)
    print(('Well ' + userName + ', you are remembering some abilities you\'ve learned in your life... somehow. ').center(100, ' '))
    wS(1)
    print('Generating abilities, Please Wait...')

    #RANDOMLY GENERATE THE ABILITIES - Its only between 1 and 5 because making the value too high will make the dungeon crawling mode too easy and they use the same function
    power = random.randint(1,5)
    speed = random.randint(1, 5)
    intel = random.randint(1, 5)
    lock = random.randint(1, 5)
    time.sleep(1)
    classLoop = True # Begin a loop to prevent not picking a class
    while classLoop:
        print(('You feel power in your veins.. what Class are you?').center(100, ' '))
        counter = 0
        for i in classes:  # Show user all of the races
            counter += 1
            print('| ' + str(counter) + ': ' + i)
        print('| 5: Random')
        wS(1)
        classNm = input('I am a ')

        if classNm == '5' or classNm == 'random' or classNm == 'Random': # User picks a random class
            classVal = random.randint(0,3)
            classNm = classes[classVal]
            classLoop = False

        elif classNm == '1' or classNm == 'Thief' or classNm == 'thief':  # User chooses thief
            classNm= 'Thief'
            lock += 2
            wS(1)
            print(('Your Lockpicking stat has been upgraded.').center(100, ' '))
            classLoop = False
        elif classNm == '2' or classNm == 'warrior' or classNm == 'Warrior': # User chooses warrior
            classNm = 'Warrior'
            power += 2
            wS(1)
            print(('Your Power stat has been upgraded.').center(100, ' '))
            classLoop = False
        elif classNm == '3' or classNm == 'elder wizard' or classNm == 'Elder wizard' or classNm == 'elder Wizard' or classNm == 'Elder Wizard': # User chose elder wizard
            classNm = 'Elder Wizard'
            intel += 2
            wS(1)
            print(('Your Intellect stat has been upgraded.').center(100, ' '))
            classLoop = False
        elif classNm == '4' or classNm == 'mystic' or classNm == 'Mystic': # User chose mystic
            classNm == 'Mystic'
            speed += 2
            wS(1)
            print(('Your Speed stat has been upgraded.').center(100, ' '))
            classLoop = False
        else: # User did not pick an appropriate class
            print(('That Class does not exist.').center(100, ' '))
            wS(1)
            print(('ME: Let me try that again. [Press Enter to Continue]'))

    wS(1)
    print('Character Created.') # Tell user that the character has been made
    playerInformation = [userName,raceChc,classNm,power,speed,intel,lock] #Encompass all data into a list to return
    return playerInformation # Return the list

def writeToFile(player): # For writing to the 'Create-A-Character' save file [This is a different function because the Dungeon-Crawler one operates differently]
    wS(1)
    print(('What would you like to name the Character File?').center(100, ' '))
    fileName = input('I\'d like to call it: ')
    with open(fileName+'.txt', 'w') as charInfo: # Create a new file with the name the user entered, and write all character data to that file.
        charInfo.write('N:' + player.name + '\n')
        charInfo.write('R:' + player.race + '\n')
        charInfo.write('C:' + player.className + '\n')
        charInfo.write('P:' + str(player.powerPerc) + '\n')
        charInfo.write('S:' + str(player.speedPerc) + '\n')
        charInfo.write('I:' + str(player.intellectPerc) + '\n')
        charInfo.write('L:' + str(player.lockPick) + '\n')
        charInfo.write('~:' + player.inv[0] + '\n')
        count = 0
        charInfo.write('*:')
        for i in range(len(player.inv)): # Append the player's inventory to the file
            count += 1
            try:
                if player.inv[count] is player.inv[-1]:
                    charInfo.write(player.inv[count])
                else:
                    charInfo.write(player.inv[count] + ',')
            except IndexError:

                charInfo.write('\n')
                break
    # APPEND ALL INFORMATION TO FILE
    charInfo.close() # Close the file
    wS(1)
    print(('Character Information Saved.')) # Tell the user their info saved
    input()
    return fileName # Return the filename

def endGame(player): # Ending cutscene for the game

    ###This is to simulate a conversation between the Player and the Narrator
    wS(50)
    print(('Wait...').center(100, ' '))
    time.sleep(1)
    wS(50)
    print(('No way...').center(100, ' '))
    time.sleep(1)
    wS(50)
    print(('Y-you actually escaped?').center(100, ' '))
    time.sleep(2)
    print(('This has never happened befo- I should probably just keep narrating, right?').center(100, ' '))
    time.sleep(3)
    wS(1)
    input(('ME: Yes, please.  [Press Enter]').center(100, ' '))
    time.sleep(1)
    wS(1)
    print(('The mysterious door flies open-- you finally see the light. Without hesitation, you rush out the do-').center(100, ' '))
    time.sleep(2)
    wS(1)
    print(('Hold on, hold on. Let me just say... this is the first time this has happened. You\'re like, a legend ' + player.name + '!').center(100, ' '))
    time.sleep(3)
    print(('Like, I thought that place was endl-').center(100, ' '))
    time.sleep(2)
    wS(1)
    print(('ME:Yo, seriously. I\'m trying to run to freedom here. Let\'s get it over with.').center(100, ' '))
    wS(1)
    time.sleep(2)
    print(('DID YOU JUST SPEAK TO ME?!? THE ONE, THE ONLY ' + (player.name).upper() + ' JUST SP-').center(100, ' '))
    wS(1)
    time.sleep(2)
    print(('ME:This can\'t be happening right now.').center(100, ' '))
    time.sleep(2)
    wS(1)
    print(('I CAN\'T BELIEVE THAT JUST HAPPENED... WOW!!!! *phew* Okay... okay...').center(100,' '))
    time.sleep(2)
    print(('Deep breaths... deeeeep--').center(100, ' '))
    time.sleep(1)
    wS(1)
    print(('ME: COME ON!').center(100, ' '))
    time.sleep(1)
    print(('AH! Okay, fine.').center(100, ' '))
    time.sleep(3)
    print(('Without hesitation, you rush out the door into freedom! The door slams behind you-- you are finally free.').center(100,' '))
    time.sleep(3)
    wS(2)
    print(('You have Escaped From the Dungeon.').center(100, ' '))
    time.sleep(5)
    wS(200)

def roomMaker(player,gameLoop): # Create rooms for player to explore
    global roomCount # Use the global roomCount value
    chest = False # Set whether a chest is in the room to false
    masterChest = False # Set whether a master chest is in the room to false
    door = False # Set whether a door is in the room to false
    spawnItem = False # Set whether a spawned item is in the room to false
    pickUp = 0 # Set base to be updated when playing picks up a spawned item
    enemy = False # Set whether an enemy is in the room to false
    roomCount +=1 # Increase roomCount
    try: # Exception handling to prevent crashes
        if player.health <= 0: # If the player died in gameplay
            selectLoop = False # Stop the game
            gameLoop = False # Stop the game
        else: # Continue the game-- player is still alive.
            pass
    except AttributeError: # If there is no Player set up yet
        pass
    if gameLoop == False: # If the game has been ended
        pass
    else: # The game has not been ended
        if roomCount == 1: # Intro cutscene for Adventure Mode.
            #SIMULATES NARRATION
            wS(1)
            print(('You awaken in a dark room. You have no idea how you got here.').center(100, ' '))
            time.sleep(2)
            wS(1)
            print(('ME: This looks... like a Dungeon?').center(100, ' '))
            time.sleep(1)
            wS(1)
            print(('ME:W-what is going on here?').center(100, ' '))
            wS(1)
            time.sleep(2)
            print(('There is only one thing you know for certain--.').center(100, ' '))
            wS(1)
            time.sleep(1)
            print(('You must Escape From the Dungeon.').center(100, ' '))
            wS(1)
            time.sleep(3)
            wS(1)
            print('Checking for saved Characters...')
            time.sleep(2)
            #Check directory for saved Character for Adventure Mode
            playerInfo, playerInv = checkforSave(True, '')  # Check for save-games
            if playerInfo == []: # If there is no Character, create the character
                playerInfo = charCreator() # CREATE THE CHARACTERS
            if playerInv == []: # If the player's inventory is empty, add a Small Sword to it.
                wS(1)
                print(('The Gods of Fate have smiled upon you today, as you have found a Small Sword!').center(100, ' '))
                playerInv.append('Small Sword')
                player = Character(playerInfo, playerInv) # Create the instance of the Character class with the new data
            else: #If a Character does exist
                wS(1)
                print(('Welcome back to The Dungeon, ' + player.name).center(100, ' ')) # Welcome player back to the dungeon

        else: # The user is not in their first room
            room = random.randint(1,20) # Generate a random number for whether the Room is a shop or not.
            if room == 20: # If the player enters a shop
                playerGold = shop(player)
            else:# Generate whether an enemy, chest or door is in the room
                itemChance = random.randint(1,5)
                enemyChance = random.randint(1,5)
                chestChance = random.randint(1,50)
                doorChance = random.randint(1,50)

                if chestChance == 20:
                    chest = True # Spawn a chest in the room

                elif chestChance == 50:
                    masterChest = True #Spawn a master chest

                if doorChance == 50:
                    door = True # Spawn a door in the room

                if enemyChance == 5:
                    enemy = True # Spawn an enemy in the Room

                if itemChance ==5: #If an item is meant to be spawned, spawn it.
                    num = random.randint(1,37)
                    item =detItem(num)
                    spawnItem = True

                #Create the Room
                if enemy == True:
                    #Generate Random stuff for the Enemy Generation
                    name = random.sample(['Crede the Orc', 'Lei the Dragon', 'Prele the Dwarf', 'Mascete the Hunter','The Spider Queen', 'Valire the Fang-Toothed', 'Plaet the Werewolf'], 1) # Pick a random item from the list of enemies.
                    if player.powerPerc <= 10:  # To balance the game, if the player strength is a certain level, the enemy damage will be less or more.
                        damage = random.randint(1,5)
                    else:
                        damage = random.randint(10,13)
                    ability = random.sample(['Smashdown', 'Cringe', 'Toosie Slice', 'Star-Destroying Punch','Switch-Up'], 1)
                    if player.powerPerc <= 10: # To balance the game, if the player strength is a certain level, the enemy health will be less or more.
                        health = random.randint(5,30)
                    else:
                        health = random.randint(25,70)
                    enemy = Enemy(name,damage,ability,health) # Create the Enemy instance with this data
                    gameLoop = encounterEnemy(enemy,player) # Get whether the player has died or not.
                    if gameLoop == False:
                        removeSaveFile() # Delete the saved character

                    else:
                        pass # Dont delete
                if gameLoop == True: # Player is alive
                    wS(1)
                    print(('You enter a new room.').center(100, ' '))
                    wS(1)
                    if chest == True: # If a chest has spawned, tell the user
                        print(('There is a Chest.').center(100, ' '))
                        chestInRoom = Chest('Normal')
                        wS(1)
                    elif masterChest == True: # If a chest has spawned, tell the user
                        print(('There is a Master Chest.').center(100, ' '))
                        chestInRoom = Chest('Master')
                        wS(1)

                    if door == True: # If a door has spawned, tell the user.
                        chest = False
                        masterChest = False
                        if 'Exit Key' in player.inv: # If the user has a key, tell them they can leave.
                            print(('There is an exit.').center(100, ' '))
                            wS(1)
                        else: # if the user doesn't have a key, tell them they can't leave
                            print(('There is an exit, but you have no key.').center(100, ' '))
                            wS(1)
                    if spawnItem == True: # If an item has spawned, tell the user.
                        print(('There is a ' + item + ' on the floor.').center(100, ' '))
                        wS(1)

                    elif chest == False and masterChest == False and door == False and spawnItem == False: # If nothing has spawned, tell the user.
                        print(('...There\'s nothing in it.').center(100, ' '))
                        wS(1)
        if gameLoop == True: # If the user didn't die, allow the select loop
            selectLoop = True
        else: # If the user has died, dont allow the select llop
            selectLoop = False
        while selectLoop: # While user is selecting options
            print(('What would you like to do?').center(100, ' ')) # Prompt for user input
            wS(1)

            #Determine available options determined by what is in the room
            if chest == True:
                print(('F/1: Go Forward | B/2: Go Backward | L/3: Go Left | R/4: Go Right | C/5: Go to Chest| Q: Quit | H: Help | I: View Inventory').center(100, ' '))

            elif masterChest == True:
                print(('F/1: Go Forward | B/2: Go Backward | L/3: Go Left | R/4: Go Right | C/5: Go to Chest| Q: Quit | H: Help | I: View Inventory').center(100, ' '))

            elif door == True:
                print(('F/1: Go Forward | B/2: Go Backward | L/3: Go Left | R/4: Go Right | D/6: Go to Door| Q: Quit | H: Help | I: View Inventory').center(100, ' '))

            elif spawnItem == True:
                print(('F/1: Go Forward | B/2: Go Backward | L/3: Go Left | R/4: Go Right | P/7: Pickup Item| Q: Quit | H: Help | I: View Inventory').center(100, ' '))

            else: # TESTING
                print(('F/1: Go Forward | B/2: Go Backward | L/3: Go Left | R/4: Go Right | Q: Quit | H: Help | I: View Inventory').center(100, ' '))
            getChoice = input(('ME: I guess I\'ll ').center(100,' ')) # Get the user input

            #Run specific code dependant on User Input
            lockPickChance = random.randint(0, 100) # Generate the chance whether the user will pick the chest lock or not
            if getChoice == 'Q' or getChoice == 'q': # User wants to quit
                choiceLoop = True  # Activate loop for choice
                while choiceLoop:
                    wS(1)
                    print('Would you like to save your Character Information?') # Get user input for if they want to save
                    save = input('Y/N: ')

                    if save == 'Y' or save =='y': # user does want to save their character
                        createSaveFile(player) # Save the character
                        choiceLoop = False # Stop the game
                    elif save == 'N' or save == 'n': # User does not want to save information
                        wS(1)
                        print(('See you next time!').center(100,' '))
                        choiceLoop = False # Stop the game
                    else: # User has invalid input.
                        wS(1)
                        print(('Please Enter either Y or N.').center(100, ' '))
                    roomCount = 0

                wS(1)
                selectLoop = False # Stop the game
                gameLoop = False
                break # Break the loop
            elif getChoice == 'H' or getChoice == 'h': # user wants help
                helpMenu() # Open the help menu
            elif getChoice == 'I' or getChoice == 'i': # user wants to see inventory
                player.showInv()
                player.useInventory()
            elif (getChoice == 'c' or getChoice == 'C' or getChoice == '5') and (chest == True or masterChest == True): # user finds a chest
                if 0<= lockPickChance <= player.lockPick: # Player chance for lockpicking the chest.
                    if chestInRoom.type == 'Normal': # If the chest type is normal, add a key to the players inventory to simulate Lockpicking
                        player.inv.append('Chest Key')
                        wS(1)
                        print(('You picked the chest\'s lock.').center(100, ' '))
                    elif chestInRoom.type == 'Master':# If the chest type is Master, add a key to the players inventory to simulate Lockpicking
                        player.inv.append('Master Chest Key')
                        print(('You picked the Master Chest\'s lock.').center(100, ' '))
                chestInRoom.getOpened(player) # Allow player to open the chest.

            elif (getChoice == 'd' or getChoice == 'D' or getChoice == '6') and (door == True): # User finds a door and escapes the dungeon
                if 'Exit Key' in player.inv: # Check if the player has the exit key
                    gameLoop = False
                    roomCount = 0 # Reset roomcount
                    endGame(player) # Show end cutscene
                    removeSaveFile() # Delete the player character
                    break
                else: # User does not have a key, they can't escape yet.
                    wS(1)
                    print(('Just out of reach of redemption... you don\'t have an Exit Key. Press Enter.').center(100,' '))
                    input() # Tell the user they still need a key.

            elif (getChoice == 'p' or getChoice == 'P' or getChoice == '7') and (spawnItem == True) and pickUp == 0: # User wants to pick up the item
                spawnItem = False # Despawn the item for the next instance of recursion
                if item in weapons or item in magicItems and (item != 'Ring of Damage' and item != 'Ring of Healing' and item != 'Ring of Resistance'): # If the item is an equippable one, delete the previously equipped weapon.
                    del(player.inv[0])
                    player.inv.insert(0,item)
                    print(('You picked up the ' + item + ', but you dropped your old weapon.').center(100, ' ')) # Tell the user that they dropped their old weapon
                #ELIF USER INV IS FULL
                else:
                    pickUp = 1
                    player.inv.append(item)
                    print(('You picked up the ' + item + '.').center(100, ' '))
                    if item in armor and item not in player.inv:
                        player.equipArmor(item)

            #USER PICKS A DIRECTION
            elif (getChoice == '1' or getChoice == 'F' or getChoice == 'f') or (getChoice == '2' or getChoice == 'B' or getChoice == 'b') or (getChoice == '3' or getChoice == 'L' or getChoice == 'l') or (getChoice == '4' or getChoice == 'r' or getChoice == 'R'):
                selectLoop = False # Stop the selection loop
                gameLoop = roomMaker(player,gameLoop) # Use recursion to create the next room

            else: # User has an invalid input
                wS(1)
                print(('ME: I gotta do something, and quickly.').center(100, ' '))  # Tell the user their input is invalid


    return gameLoop # Return whether the game should run or not

def loseScreen(): # A screen for when the player loses

    #SIMULATE NARRATION
    wS(50)
    print(('You lost. Another warrior has been lost to the Dungeon.').center(100, ' '))
    wS(1)
    print(('But... there is a silver lining...').center(100, ' '))
    wS(1)
    input(('ME: ...and what is that?').center(100, ' '))
    wS(1)
    print(('Just as one warrior\'s journey ends,').center(100,' '))
    wS(1)
    print(('Another\'s begins.').center(100,' '))
    wS(1)
    print(('Please Wait...').center(100, ' '))
    time.sleep(5)
    wS(5)
    game = False
    return game # Return that the user has died.

def encounterEnemy(enemy,player): # Generate the enemy encounter for the player
    wS(1)
    print(('Oh no! You\'ve encountered ' + enemy.name[0] + '! It\'s too late to escape!').center(100, ' ')) # Tell the user they've encountered an enemy
    wS(1)
    input(('ME: *under my breath* Oh boy. [Press Enter to Continue]').center(100,' ')) # Allow user to continue at own pace
    wS(1)
    gameLoop = True # The game is still running
    fightLoop = True # Activate fight loop
    while fightLoop: # While the fight is still going
        if player.health <=0: # Check if player has died-- if they have, stop the fight.
            wS(1)
            print(('You have 0 health remaining.').center(100, ' '))
            fightLoop = False
            gameLoop = False
            break # Break the loop
        else: # User is still alive
            pass
        print(('ME: I\'ve got two options...').center(100 , ' ')) # Tell user they have options
        wS(1)
        print(('1: Access Inventory  |  2: Attack  | 3: Help').center(100 , ' ')) # Show user the options available
        wS(1)
        choice = input('ME: I need to #') # Get user input
        if choice == '1': # Player accesses inventory
            player.showInv()
            player.useInventory()

        elif choice == '2': # Player attacks
            wS(1) ### Damage the enemy and
            enemy.health -= (player.weapon.damage + (int(player.powerPerc)))
            print(('Whoa! You dealt ' + str(player.weapon.damage + int(player.powerPerc)) + ' damage!').center(100, ' '))
            wS(1)
            (input('Okay. [Press Enter to Continue]').center(100, ' ')) # Allow user to continue at own pace
            wS(1)
            if enemy.health >= 0: # Check if user hasnt defeated the enemy.
                print((enemy.name[0] + ' has ' + str(enemy.health)+ ' health remaining!').center(100, ' '))
                ####ENEMY ATTACKS BACK
                abilityChance = random.randint(1,10) # Generate whether the enemy will use their ability
                dodge = random.randint(1,100) # Generate whether the user will dodge
                if 0 <= dodge <= player.speedPerc: # Player dodge chance
                    dodge = True
                    wS(1)
                    print(('You dodged the attack!').center(100, ' ')) # Tell user they dodged the attack
                else: # User did not dodge the attack
                    dodge = False
                if dodge == False: # If the user did not dodge
                    if abilityChance == 100: # If the enemy can use their ability
                        enemy.useAbility(player) # Use the ability
                        wS(1)
                        print((enemy.name[0] + ' used their Special Ability, '+ str(enemy.ability) + '!').center(100, ' ')) # Tell the user the enemy used their special ability
                    else: # If the enemy did not use their ability
                        enemy.attack(player)
                        print((enemy.name[0] + ' dealt ' + str(enemy.damage)+' damage!').center(100, ' ')) # Tell the user that the enemy attacked them
                    wS(1)
                    print(('You have ' + str(player.health) + ' health remaining!').center(100, ' ')) # Tell the user how much of their health remains
            else: # The user has defeated the enemy
                print((enemy.name[0] + ' has 0 health remaining!').center(100, ' ')) # Tell the user they defeated the enemy
        elif choice == '3': # User wants to see the help menu

            #EXPLAIN ENCOUNTER MODE TO USER
            wS(1)
            print(('=-=-=-=-=-=-=-= HELP MENU =-=-=-=-=-=-=-=').center(100,' '))
            wS(1)
            print(('Pressing 1 will allow you to access your inventory. You can \n consume items and potions.').center(100, ' '))
            wS(1)
            print(('Pressing 2 will attack the mob you\'re in battle with. This \n will deal whatever damage your weapon can \n plus your power percentage.').center(100, ' '))
            wS(1)
            input(('ME: *in my head* Yeah, that makes sense.').center(100, ' '))

        else: #User does not make a choice
            wS(1)
            print(('You didn\'t do anything! ' + enemy.name[0] + ' is attacking!').center(100, ' '))
            wS(1)
            abilityChance = random.randint(1, 100)  # Generate ability chance
            if abilityChance == 100: # If the enemy can use their ability
                enemy.useAbility(player) # Enemy uses their ability on the player
                wS(1)
                print((enemy.name[0] + ' used their Special Ability, '+ str(enemy.ability) + '!').center(100, ' ')) # Tell the user the enemy used their special ability
            else: # Enemy did not use special ability
                enemy.attack(player) # Attack the player
                print((enemy.name[0] + ' dealt ' + str(enemy.damage) + ' damage!').center(100, ' '))
        if enemy.health <= 0: # If the enemy has died
            wS(1)
            print(('Whoa! You defeated ' + enemy.name[0] + '!').center(100, ' ')) # Tell the user they defeated the enemy
            wS(1)
            print(('You looted 15 Coins from their body. Please Wait.').center(100, ' ')) # Tell the user they got 15 more coins
            fightLoop = False # STOP THE ENEMY ENCOUNTER
            gameLoop = True
            player.balance += 15 # ADD 15 COINS TO USER BALANCE
            time.sleep(3)
        elif player.health <= 0: # If the user dies
            wS(1)
            print(('Oh, no. Another brave hero lost to ' + enemy.name[0] + '...')) # Tell the user theyve died
            time.sleep(1)
            gameLoop = loseScreen()
            fightLoop = False # STOP THE ENEMY ENCOUNTER
            break # break the loop
        else: # Nobody has died yet
            wS(1)
            print(('Looks like it\'s not over yet.').center(100 , ' ')) # Tell user fight is still going.
            wS(1)
            input('ME: Okay. [Press Enter to Continue]')
            wS(1)

    return gameLoop # Return whether the game should be running or not

def wS(times): # Print whitespace
    for i in range(times):
        print('')

def detItem(num): # Generate random item for the shops
    global weapons, items, food, magicItems, armor,misc
    #Gen Potions
    if num == 1:
        item = items[0]
    elif num ==2:
        item = items[1]
    elif num ==3:
        item = items[2]
    elif num ==4:
        item = items[3]

    #Gen Swords
    elif num ==5:
        item = weapons[0] # Give small sword
    elif num == 6:
        item = weapons[1] # Medium Sword
    elif num == 7:
        item = weapons[2] # Large Sword

    #Gen Axe
    elif num == 8:
        item = weapons[3]
    elif num == 9:
        item = weapons[4]
    elif num == 10:
        item = weapons[5]

    #Gen Bows
    elif num == 11:
        item = weapons[6]
    elif num == 12:
        item = weapons[7]
    elif num == 13:
        item = weapons[8]

    #Magic Items
        #wands
    elif num == 14:
        item = magicItems[0]
    elif num == 15:
        item = magicItems[1]
    elif num == 16:
        item = magicItems[2]
    elif num == 17:
        item = magicItems[3]

        #rings
    elif num == 18:
        item = magicItems[4]
    elif num ==19:
        item = magicItems[5]
    elif num == 20:
        item = magicItems[6]

    #Armor
        #Leather
    elif num == 21:
        item = armor[0]
    elif num == 22:
        item = armor[1]
    elif num == 23:
        item = armor[2]
    elif num == 24:
        item = armor[3]
        
        #Steel
    elif num == 25:
        item = armor[4]
    elif num == 26:
        item = armor[5]
    elif num == 27:
        item = armor[6]
    elif num == 28:
        item = armor[7]

        #Impenetrable Armor
    elif num == 29:
        item = armor[8]
    elif num == 30:
        item = armor[9]
    elif num == 31:
        item = armor[10]
    elif num == 32:
        item = armor[11]

    #KEYS
    elif num == 33:
        item = items[4]
    elif num == 34:
        item = items[5]
    elif num == 35:
        item = items[6]

    #FOOD
    elif num == 36:
        item = food[0]
    elif num == 37:
        item = food[1]


    #MISC STUFF
    elif num == 38:
        item = misc[0]
    elif num == 39:
        item = misc[1]
    elif num == 40:
        item = misc[2]
    elif num == 41:
        item = misc[3]
    elif num == 42:
        item = misc[4]
    elif num == 43:
        item = misc[5]
    elif num == 44:
        item = misc[6]

    #EMPTY / NONE
    elif num == 45:
        item = 'Nothing'

    return item
        
def shop(player): # Create a shop
    global shopGoodbye
    priceLower = (int(player.intellectPerc)) // 10
    item1 = detItem(random.randint(1,37)) # generate an item
    item2 = detItem(random.randint(1,37)) # generate an item

    if item2 == item1:
        item2 = detItem(random.randint(1,37)) # Re-generate item

    item3 = detItem(random.randint(1,37)) # generate an item

    if item3 == item2 or item3 == item1:
        item3 = detItem(random.randint(1,37)) # Re-generate item

    shopkeepItem = [item1,item2,item3] # Set the items the seller is selling

    loop = True # Activate dialogue loop
    print(('SHOPKEEPER: Hiya there. I\'m the SHOPKEEPER. Wanna see what I\'ve got \'ere for ya?').center(100,' '))
    while loop: 
        val = random.randint(0,2) # A random number
        wS(1)
        yesNo = input(('ME (Y/N): ').center(100,' ')) # Get the user input
        wS(1)
        
        if yesNo == 'Y' or yesNo == 'y': # User wants to shop
            shopping = True
            loop = False
        elif yesNo == 'N' or yesNo == 'n': # User doesnt want to shop
            shopping = False
            bought = False
            loop = False
        else: # Tell user their input was incorrect
            val = random.randint(0,2) # Generate a random number

            #Random voice lines
            if val == 0:
                print(('SHOPKEEPER: ...Uh, that don\'t seem like an answer buddy. Wanna try \'gain?') .center(100,' '))
            elif val == 1:
                print(('SHOPKEEPER: I\'mma need you to try \'gain bud.').center(100,' '))
            elif val == 2:
                print(('SHOPKEEPER: You gone crazy \'r sum\'n? That don\'t answer my questi\'n.').center(100,' '))
                
    while shopping: # Shopping loop
        wS(1)
        print(('SHOPKEEPER: This \'ere\'s what I got fer sale. Check \'em out.').center(100,' ')) # Prompt User
        count = 0
        wS(1)
        for i in shopkeepItem: # Show the items to the user
            count += 1
            print((str(count) +': ' + i).center(100,' ')) 
        wS(1)
        print(('SHOPKEEPER: If you\'re unsure how to use the shop, type in Q.').center(100,' ')) # Tell user how to use shop
        wS(1)
        player.showInv() # Show the player their items
        wS(1)
        choice = input(('ME: Hm... I\'d like... #').center(100,' ')) # Get user input
        wS(1)
        if choice == 'Q' or choice == 'q': # Explain the shop to the user
            print(('SHOPKEEPER: To use the shop, jus\' enter the number of the item. Every item costs \'bout ' + str(10 - priceLower) + ' coins.').center(100,' '))
            print(('SHOPKEEPER: But \'member, I gots a 1 Item per cust\'mer policy.').center(100,' ')) # Tell user they can only buy 1 item
            input(('ME: Okay. [Press Enter to Continue]').center(100,' ')) # Allow user to play at own pace
        elif choice == '1' and player.balance >= (10 - priceLower): # If the user buys item 1
            print(('SHOPKEEPER: Ah, so you\'d like the ' + item1 + '? Sure thing bud.').center(100,' ')) #Tell the user they bought item 1
            player.balance -= 10 - priceLower
            player.inv.append(item1)
            bought = True  # The user has bought something
            shopping = False  # End shopping loop
        elif choice == '2' and player.balance >= (10 - priceLower): # If the user buys item 2
            print(('SHOPKEEPER: Ah, so you\'d like the ' + item2 + '? Sure thing bud.').center(100,' ')) #Tell the user they bought item 2
            player.balance -= 10 * priceLower
            player.inv.append(item2)
            bought = True  # The user has bought something
            shopping = False  # End shopping loop
        elif choice == '3' and player.balance >= (10 - priceLower): # If the user buys item 3
            print(('SHOPKEEPER: Ah, so you\'d like the ' + item3 + '? Sure thing bud.').center(100,' ')) #Tell the user they bought item 3
            player.balance -= 10 - priceLower
            player.inv.append(item3)
            bought = True # The user has bought something
            shopping = False # End shopping loop
            
        
        elif player.balance <(10 * priceLower): # User doesnt have enough money
            print(('SHOPKEEPER: Aw, shucks. Seems you\'ve fallen down on some \'dem hard times. You\'ve don\'t got th\' funds for any of my items. I\'mma have to show you th\' door feller.').center(100,' '))
            input('ME: Okay.')
            bought = False # User did not buy something
            shopping = False # End shopping loop
        else: # User enters something incorrect
            print(('SHOPKEEPER: You\'re messin\' with me. I\'mma have to ask you to leave.').center(100, ' '))
            bought = False  # User did not buy something
            shopping = False  # End shopping loop
        
        wS(1)
    print(('SHOPKEEPER: ' + shopGoodbye[val]).center(100,' ')) # Say goodbye to user
    input(('ME: See ya. [Press Enter to Continue]').center(100,' ')) # Allow user to continue
    wS(1)
    if bought == True: # If the user has bought something, tell them their inventory has been updated.
        print(('Your Inventory has been updated!').center(100,' '))
        player.showInv()
    else: # If user did not buy something, dont say anything
        pass
        
        
    return player.inv, player.balance # Return updated inventory and balance

def checkforSave(bool,file):  # This function will read the saved character from when the last instance of the program ended-- allowing for saved characters.
    global savefile
    if bool == True: # Adventure Mode file
        charInfo = open(savefile, 'r')  # Open the savefile for reading
    else: # If it is a create-a-character file
        charInfo = open(file + '.txt','r') # Open create-a-char file for reading
    character = []
    charInv = []
    count = 0
    for line in charInfo:  # Read the lines and append information to appropriate lists
        count += 1
        if count <= 11:
            if line[0:2] == 'N:':  # If file read is reading name
                if line[2:].strip('\n') == 'NOCHAR' or line[2:].strip('\n') == '' :
                    break
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'R:':  # If file read is reading race
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'C:':  # If file read is reading class
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'P:':  # If file read is reading power val
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'S:':  # If file read is reading speed val
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'I:':  # If file read is reading Intellect val
                character.append(line[2:].strip('\n'))
            elif line[0:2] == 'L:':  # If file read is reading lockpick chance
                character.append(line[2:].strip('\n'))
            elif line[0:2] == '*:':  # If file read is reading inventory
                if line[2:] == None:
                    pass
                else:
                    charItems = (line[2:].strip('\n')).split(',')
                    for i in charItems:
                        charInv.append(i)
            elif line[0:2] == '~:':  # If file read is reading equipped items
                charInv.insert(0, (line[2:].strip('\n')))
            elif line[0:2] == 'H:': # Reading Health
                character.append(line[2:].strip('\n'))
            elif line[0:2] == '$:': # Reading Coins
                character.append(line[2:].strip('\n'))
        else:
            break
    charInfo.close()  # Close the file to save resources
    return character, charInv # Return data

def readResources(): # This function reads the Resources.txt file to retrieve assets for the game
    global resourcesfile
    weapons, items, food, magicItems, armor, classes, races, enemyTypes,misc = [],[],[],[],[],[],[],[],[]
    gameInfo = open(resourcesfile, 'r')  # Open the resources file to read
    count = 0
    for line in gameInfo:
        count += 1
        if count <= 10:
            if line[0:2] == 'W:':  # If it is reading weapons

                weapons = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'I:':  # If reading items
                items = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'F:':  # If reading food
                food = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'M:':  # If reading magic items
                magicItems = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'A:':  # If reading armor
                armor = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'C:':  # If reading classes
                classes = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'R:':  # If reading races
                races = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'E:':  # If reading enemy types
                enemyTypes = ((line[2:].strip('\n')).split(','))
            elif line[0:2] == 'S:':  # If reading misc
                misc = ((line[2:].strip('\n')).split(','))
        else:
            break
    gameInfo.close() # Close file
    return weapons, items, food, magicItems, armor, classes, races, enemyTypes,misc # Return everything

def createSaveFile(player):
    with open('Deluca_EscapeFromTheDungeon_SavedCharacter.txt', 'r+') as charInfo: # Open the resources file to read
        charInfo.write('N:' + player.name + '\n')
        charInfo.write('R:' + player.race + '\n')
        charInfo.write('C:' + player.className + '\n')
        charInfo.write('P:' + str(player.powerPerc) + '\n')
        charInfo.write('S:' + str(player.speedPerc) + '\n')
        charInfo.write('I:' + str(player.intellectPerc) + '\n')
        charInfo.write('L:' + str(player.lockPick) + '\n')
        charInfo.write('~:' + player.inv[0] + '\n')
        count = 0
        charInfo.write('*:')
        for i in range(len(player.inv)):
            count += 1
            try:
                if player.inv[count] == player.inv[-1]:
                    charInfo.write(player.inv[count])
                else:
                    charInfo.write(player.inv[count] + ',')
            except IndexError:
                charInfo.write('\n')
                break
        charInfo.write('H:' + str(player.health) + '\n')
        charInfo.write('$:' + str(player.balance) + '\n')
        #APPEND ALL INFORMATION TO FILE
        charInfo.close()
        wS(1)
        print('Character Information Saved. Press Enter.')# Tell user their data has been saved
        input()

def removeSaveFile(): # Opposite of Create File
    with open('Deluca_EscapeFromTheDungeon_SavedCharacter.txt', 'r+') as charInfo: # Open the resources file to read
        charInfo.truncate(0) # Clear the file
        charInfo.close() # Close the file
        wS(1)
        print('Character Information Removed. Press Enter.') # Tell user their information was removed.
        input()

def mainMenu(): # Show user main menu, explain game, and get choice
    global player,gameLoop,roomCount # Get global variables
    wS(1)
    print(('Welcome to Escape From the Dungeon.').center(100, ' '))
    wS(1)
    print(('Coded by Sebastian Deluca').center(100, ' '))
    time.sleep(1)
    print(('Please Wait...').center(100, ' '))
    time.sleep(3)
    menu = True # Activate menu and game booleans to run menu
    game = True
    while menu: ##Show the user the menu
        wS(25)
        print(('| ~ | ~ | ~ | ~ | ESCAPE FROM THE DUNGEON | ~ | ~ | ~ | ~ |').center(100, ' ')) # Title header
        wS(1)
        print(('|  1/C: Character Creation Mode  |  2/A: Adventure Mode  |  H: Help  |  Q: Quit  |').center(100, ' ')) # Show user their options
        choice = input('#: ') # Get user input
        if choice == '1' or choice == 'c' or choice == 'C': # User wants Character Creation Mode
            playerInf = charCreator() # Create a base character
            ##RANDOMLY GENERATE 10 INVENTORY ITEMS
            playerInven = [detItem(random.randint(5,17)),detItem(random.randint(1,37)),detItem(random.randint(1,37)),detItem(random.randint(38,44)),detItem(random.randint(38,44)),detItem(random.randint(1,37)),detItem(random.randint(38,44)),detItem(random.randint(1,37)),detItem(random.randint(38,44)),detItem(random.randint(1,37)),]
            for i in playerInven: #  The player has an empty slot, rearrange the inventory so Nothing is at the end
                if i == 'Nothing':
                    itemLoc = playerInven.index(i)
                    del(playerInven[itemLoc])
                    playerInven.append('Nothing')
                else:
                    pass
            newPlayer = Character(playerInf, playerInven) # GENERATE A BASE CHAR FOR SAVING TO FILE
            fileName = writeToFile(newPlayer) # Save info to custom file
            newInfo,newStats = checkforSave(False,fileName) # Read off of the new file
            examplePlayer = Character(newInfo,newStats) # GENERATE A NEW CHARACTER FROM THE WRITTEN FILE

            #SHOW PLAYER STATS AND INVENTORY
            examplePlayer.viewStats()
            wS(1)
            examplePlayer.showInv()
            wS(1)

            #Loop to prevent incorrect inputs
            editLoop = True
            while editLoop:
                print(('Would you like to Edit the Inventory, or your Character?').center(100,' ')) # Get user input for if they want to edit
                edit = input('Y/N: ')

                if edit == 'Y' or edit == 'y': # User wants to edit

                    edit2Loop =True
                    while edit2Loop: # Loop to prevent incorrect inputs
                        wS(1)
                        print(('1: Inventory  |  2: Character').center(100,' '))  # Get user input for if they want to edit
                        choice2 = input('1/2: ')
                        if choice2 == '1': # Edit inventory
                            invLoop = True
                            while invLoop:
                                wS(1)
                                print(('Which slot would you like to edit? (1-10)').center(100, ' ')) # Edit inventory slot
                                try:
                                    val = int(input('#: ')) # Get val
                                    if 1<= val <= 10:
                                        invLoop = False
                                    else:
                                        wS(1)
                                        print('Invalid Number. Try Again. [Press Enter]')
                                        input()
                                except: #User input is invalid
                                    wS(1)
                                    print(('Invalid Input.').center(100,  ' '))

                            wS(1)
                            print(('Enter the Name of the Item (This can be Custom Items as Well)').center(100, ' ')) # Prompt for input
                            name = input('|~|: ') # Get name of item
                            del(examplePlayer.inv[val-1]) # Delete the previous item
                            examplePlayer.inv.insert(val-1,name) # Insert the new item into the old spt
                            wS(1)
                            print('Please Wait...')
                            time.sleep(2)
                            print('Inventory Updated!') # Tell the user they've updated their inventory
                            wS(1)
                            examplePlayer.showInv() # Show the user their new inventory
                            edit2Loop = False # Stop the loop
                        elif choice2 == '2': # Edit name
                            wS(1)
                            nameLoop = True # Activate loop to prevent invalid inputs
                            while nameLoop:
                                print(('Want to change your First or Last Name? (1/2)').center(100, ' '))
                                try:
                                    nameChange = int(input('1/2: ')) # Check if int works so name can be changed
                                    if 1<= nameChange <= 2:
                                        nameLoop = False
                                    else:
                                        pass
                                except: # User input is invalid
                                    wS(1)
                                    print(('Invalid Input.').center(100,  ' '))

                            if nameChange == 1: # Want to Change first name
                                wS(1)
                                new = input('My new first name is: ') # Get new name
                                nameList = examplePlayer.name.split() # Split previous name by spaces
                                examplePlayer.name = new + ' ' + nameList[-1]
                                wS(1)
                                print(('Your name has been updated!').center(100, ' ')) # Tell the user their name has been updated
                                wS(1)
                                examplePlayer.viewStats() # Show the player their new stats
                                edit2Loop = False # Stop the loop
                            elif nameChange == 2: # Want to change Last Name
                                wS(1)
                                new = input('My new last name is: ')  # Get new name
                                nameList = examplePlayer.name.split() # Split old name by spaces
                                examplePlayer.name = nameList[0] + ' ' + new # Create new name
                                wS(1)
                                print(('Your name has been updated!').center(100, ' ')) # Tell the user their name has been ipdated
                                wS(1)
                                examplePlayer.viewStats()
                                edit2Loop = False # stop the loop

                elif edit == 'N' or edit == 'n': # User does not want to edit
                    editLoop = False # Stop the loop
                    wS(1)
            saveAgainLoop = True
            while saveAgainLoop:
                print(('Would you like to save this new Character to a File as well? (Y/N)').center(100, ' '))

                saveOrNot = input('Y/N: ') # Get user input for saving again
                print(saveOrNot)
                if saveOrNot == 'Y' or saveOrNot == 'y' or saveOrNot == 'n' or saveOrNot == 'N':
                    saveAgainLoop = False
                elif (saveOrNot != 'Y' or saveOrNot != 'y') or (saveOrNot != 'N' or saveOrNot != 'n'): # User has incorrect input
                    wS(1)
                    print('Incorrect Input. Try Again.')
            if saveOrNot == 'Y' or saveOrNot == 'y': # User wants to save again
                newFile = writeToFile(examplePlayer)
                wS(1)
            else: # user does not want to save
                wS(1)


            input(('To Return to the Main Menu, Press Enter.').center(100, ' ')) # Allow user to continue at own pace
            print('Please Wait...')
            time.sleep(1)
        elif choice == '2' or choice == 'a' or choice == 'A': # User wants adventure mode
            keepRunning = True # Bool to keep RoomMaker running
            try:
                if resetStats == True: # Reset the global roomcount
                    roomCount = 0
            except: # Prevent crashes for if resetStats doesnt exist
                pass
            while keepRunning: # While the loop is running
                keepRunning = roomMaker(player,True) # Run adventure mode
                resetStats = True # Reset the stats when it ends
        elif choice == 'h' or choice == 'H': # Help Menu
            helpMenu()
        elif choice == 'Q' or choice == 'q': # User wants to quit
            menu = False # Stop the menu
            game = False # Stop the game
    return game # Return the game bool

def helpMenu(): # Help Menu to explain the game
    wS(1)
    print(('Escape From the Dungeon -- By Sebastian Deluca').center(100, ' ')) # Header
    wS(2)
    print(('CREATE - A - CHARACTER MODE:').center(100, ' ')) # Header
    wS(1)
    print(('In this mode, you create a random character, and can save the character to a text file in the directory.'))  # Explain Option 1 to User
    input('Okay. [Press Enter to Continue]') # Allow user to continue at own pace
    wS(2)
    print(('ADVENTURE MODE: ').center(100, ' ')) # Header
    wS(1)
    print(('Randomly generating rooms, recursion, boss fights, shops, and more! A dungeon-crawling lovers\'s dream.').center(100, ' ')) # Explain option 2 to user
    input('Okay. [Press Enter for ADVENTURE MODE Help]') # Allow user to continue at own pace
    wS(2)
    print(('INVENTORY: ').center(100, ' ')) # Header
    wS(1)
    print(('To access the inventory, Press I. Selecting an item in your inventory will equip it, normally boosting your stats or replenishing health.').center(100, ' ')) # Explain Inventory
    input('Okay. [Press Enter to Explain Skills]') # Allow user to continue at own pace
    wS(2)
    print(('ABILITIES: ').center(100,' ')) # Header
    wS(1)
    print('POWER: Increases attack damage \n| SPEED: Increases dodge chance \n| INTELLECT: Increases price reductions in shops \n| LOCKPICKING: Increases chance to not need a key to unlock a Chest') # Explain abilities
    input('Okay. [Press Enter to Explain Weapons]') #Allow user to continue at own pace
    wS(2)
    print(('WEAPONS HIERARCHY: ').center(100, ' ')) # Header
    wS(1)
    print(('Every weapon has a specific Damage value-- increased by your POWER skill. Magic Weapons are typically the strongest.').center(100, ' ')) # Explain weapons
    input('Show me the Hierarchy! [Press Enter to Continue]') # Allow to continue at own pace
    wS(2)
    print(('WEAPON STATS:').center(100, ' ')) # Header
    wS(1)
    print('| SWORDS |\nSmall Sword: 1 Damage, Medium Sword: 1.25 Damage, Large Sword: 1.85 Damage \n| AXES |\nSmall Axe: 1.60 Damage, Medium Axe: 1.90 Damage, Large Axe: 2.10 Damage\n| BOWS |\nShort Bow: 1.85 Damage, Long Bow: 1.90 Damage, Crossbow: 2.0 Damage\n| WANDS |\nWeak Wand: 1 Damage, Wand: 1.50 Damage, Strong Wand: 2.0 Damage, Master Wand: 3.0 Damage') # DAMAGE RANGES
    input('Okay. [Press Enter to Go to Options]')
    wS(1)
    print(('Would you like to remove a Saved Character? (Y/N)').center(100, ' ')) # Give user the option to remove character save
    print(('(If you have no Character Saved, this does not matter.)').center(100, ' '))
    delete = input('Y/N: ') # Get user input
    if delete == 'Y' or delete == 'y': # User wants to delete saved character
        removeSaveFile()
    else:
        wS(1)
        print(('Understood. Please Wait.').center(100, ' '))
        time.sleep(1)

    input('Okay. [Press Enter to Return to the Main Menu]') # Allow user to return
    wS(25)
#Read the Resources
weapons, items, food, magicItems, armor, classes, races, enemyTypes,misc = readResources() # Get all resources for global use

try: # Check for save games
    playerInfo, playerInv = checkforSave(True, '') # Check for save-games
    player = Character(playerInfo, playerInv)
except IndexError: # No save game
    player = 0
gameLoop = True # Run the game
while gameLoop: # While game is running
    gameLoop = mainMenu()

