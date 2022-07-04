import pyautogui
import time

# issue page
pyautogui.moveTo(1139, 409)
time.sleep(1)
pyautogui.click()

pyautogui.moveTo(1017, 404)
time.sleep(1)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(981, 546)
pyautogui.click()
time.sleep(3)

for i in range(15):
    pyautogui.scroll(-10)
time.sleep(2)
pyautogui.click(1482, 826)
time.sleep(2)
pyautogui.click(1310, 474)
while (1):
    # closed click
    time.sleep(3)
    pyautogui.moveTo(1031, 469)
    pyautogui.click()

    # top issue click
    pyautogui.moveTo(972, 545)
    time.sleep(3)
    pyautogui.click()

    # delete issue click
    time.sleep(3)
    for i in range(15):
        pyautogui.scroll(-10)
    time.sleep(2)
    pyautogui.moveTo(1469, 604)
    pyautogui.click()

    # warning check
    time.sleep(2)
    pyautogui.click(1310, 474)
