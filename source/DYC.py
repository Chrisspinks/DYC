import numpy as np
import PIL
import cv2
import pyautogui
import time

coords = [608, 633, 985, 786]   # Coordinates of game on screen (top left corner (X,Y) and bottom right corner (X,Y))
menu = False
temple = False      # Must manually set to true if you purchase temple
recruiting = False
t = 1


def kill_ppl():
    global coords, menu, temple, recruiting, t
    while True:
        time.sleep(0.001)
        enemy_found = 0
        screen = np.array(PIL.ImageGrab.grab(bbox=None))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        # check menu pixel
        if screen[814][613] < 10:   # Check if it has gone into menu
            menu = True
            break

        if screen[496][1090] == 79 or screen[495][1090] == 79:  # 79/90 when castle upgraded
            if time.time() - t > 1:
                recruiting = False

        # loop through image of screen, searching for enemies
        for x in range(coords[0], coords[2]):
            for y in range(coords[1], coords[3]):
                if x > 910 and screen[y][x] < 10:
                    pyautogui.moveTo(x, y)
                    pyautogui.drag(1240 - x, 340 - y, 0.001, button='left')
                    enemy_found = 1
                elif x <= 910 and screen[y][x] > 200:
                    pyautogui.moveTo(x + 20, y)
                    # If temple has been bought and no one is being recruited, recruit next enemy
                    if not recruiting and temple:
                        pyautogui.drag(930 - x, 580 - y, 0.75, button='left')
                        recruiting = True
                        t = time.time()
                    else:
                        pyautogui.drag(1240 - x, 340 - y, 0.001, button='left')
                    enemy_found = 1
                if enemy_found == 1:
                    break
            if enemy_found == 1:
                break

        enemy_found = 0
        screen = np.array(PIL.ImageGrab.grab(bbox=None))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        # check menu pixel
        if screen[814][613] < 10:
            menu = True
            break

        # loop through image of screen
        for x in range(coords[2], coords[0], -1):
            for y in range(coords[3], coords[1], -1):
                if x > 910 and screen[y][x] < 10:
                    pyautogui.moveTo(x, y)
                    pyautogui.drag(1240 - x, 340 - y, 0.001, button='left')
                    enemy_found = 1
                elif x <= 910 and screen[y][x] > 200:
                    pyautogui.moveTo(x + 20, y)
                    pyautogui.drag(1240 - x, 340 - y, 0.001, button='left')
                    enemy_found = 1
                if enemy_found == 1:
                    break
            if enemy_found == 1:
                break


def menu_screen():
    global menu
    time.sleep(4)
    screen = np.array(PIL.ImageGrab.grab(bbox=None))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    if screen[814][613] < 10:
        pyautogui.moveTo(1059, 769)     # Move mouse to ok button
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1240, 790)     # Move mouse to ok button
        time.sleep(1)
        pyautogui.click()
        time.sleep(4)
        menu = False
    else:
        menu = False


# Move mouse to left of screen to start program
while True:
    time.sleep(0.01)
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX < 10:
        break

# Main Loop
while True:
    if not menu:
        kill_ppl()
    elif menu:
        menu_screen()

