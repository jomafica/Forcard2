
import pyautogui
from time import sleep

screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position()
def sleep_time(times: int) -> sleep: return int(times)
seconds = sleep_time(int(input('Time to sleep(s): ')))
print('To break loop press CTRL + C')
try:
    while True:
        pyautogui.click()
        print(f'Just clicked! Now i will sleep {seconds} seconds')
        sleep(seconds) 
except KeyboardInterrupt:
    pass