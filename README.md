# Escape-From-The-Dungeon
A IDE-Based dungeon-crawler created as a Problem Set solution for Computer Science class.

          Implementation Details
          1. have Python 3.x.x installed or they can find it here
          (https://www.python.org/downloads/)

          2. After being installed the user must open Python IDLE.

          3. After that the user must go to File > Open > 
             (select Deluca_EscapeFromTheDungeon.py ) to open.

          4. Then the user must Hit f5 on their keyboard or Run > Run Module.

### - Cool Features -

- Easy-To-Read User Interface:
  Utilizes horizontal menus and whitespacing to make everything easy to read.
  
- Character Creator:
  An effective and easy-to-use character creator that can write to a file to save your character.
  Post-Creation Customizing:
      User can customize inventory items and first/last name of their created character after creation.

- Adventure Mode:
  - Utilization of RNG to create procedurally generated rooms.
  
  - Spawns chests, exits, enemies, and items in any given room.
  
  - Shopkeeper:
    Player can buy items for use in their game.
  
  - Recursion:
    ADVENTURE MODE runs solely on recursion.
  
  - Enemy Encounters:
    Player can run into enemies and is forced to fight them to the death! But, you can use weapons, items, and potions to aid in your       defense!
    
  - Cutscenes:*
    I say cutscenes, but it's really more of "dialogue-scenes"... but still!
    
  - Saveable Progress!
    Utilizes Python's built-in reading and writing capabilities to allow the player to pick up where they left off after quitting!
    The player is also able to DELETE this character from inside the program, if they wish to.
    
  - Exception Handling!
    Utilizes Python's try/except to prevent crashes.
    
  - Resources File!
    All in-game items are created from a Resources File in the .py's directory.
    
  - Object Orientated Programming!
    Characters, Enemies, and Chests are Objects.
    
  - Abilities / Increasable Stats!
    The player has ability stats, that can not only change based on Class, but also based on consumed items! These also serve a function     in-game, like allowing the user to "lockpick" a chest if a stat is high enough, etc.
  
## Known Errors --
   
   ### Adventure Mode 
   When more than one criteria is met for room generation,
   the options will not update to show everything that is possible. This is
   due to how the option-updating is set up.

   If you know the keybinds, everything still operates.

   
   If you and the AI die at the same time in an enemy
   encounter, it will allow you to go back into 'ROOM CHOOSE MODE', but once
   you make a choice, it will return you to the main menu and remove your
   character, as expected.

   
   ### Create-A-Character Mode: 
   If one of the first/last names given to a character has
   spaces, changes to the name will cause the name to get butchered.
   [ex. 'The Sock Monkey Lover' 'afs'] change last name to McGee
   == ['The' 'McGee']
