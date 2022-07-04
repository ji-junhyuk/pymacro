import pyautogui
import time

width, height = pyautogui.size()
print('width={0}, height={1}'.format(width, height))

while (1):
    print ("current location: ", pyautogui.position())
    time.sleep(1)
