# DYC
Python program to play Defend Your Castle

Firstly make sure numpy, PIL, cv2, pyautogui and time modules are all installed

Run the flash game here: http://www.xgenstudios.com/game.php?keyword=castle

1. Start the flash game (click 'new game')
2. Run the python script. 
3. Make sure the browser with the game is selected and fullscreened
4. Manually move the mouse to the left of screen to start searching for enemeies (the program won't do anything before this is done).

The program will automatically go through the menu screen after each level. If you want to get upgrades, pause the program when the menu appears then repeat steps 2-4 to resume.

If you purchase the temple, the global 'temple' variable should be changed to True and the program will automatically recruit enemies.  
