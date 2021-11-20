import time
import pyautogui 
from time import sleep

#pyautogui.position() = Farenin Konumunu Gösterir

time.sleep(5)

while True:
    #pyautogui.leftClick(x=772, y=676)
    pyautogui.write("Destek Yorumu")
    pyautogui.press("enter")
    time.sleep(1.5)