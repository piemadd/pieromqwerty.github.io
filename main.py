import random, string, os, time
from pyautogui import hotkey

x = 0
while True:
    os.system("start chrome :https://www.bing.com/search?q=" + ''.join(random.choice(string.ascii_lowercase) for i in range(32)))
    time.sleep(1)
    hotkey('ctrl', 'w')
    time.sleep(3)
    hotkey('ctrl', 'w')
    time.sleep(3)
    hotkey('ctrl', 'w')
    time.sleep(3)
    os.system("taskkill /im chrome.exe /f")
    print("Searches: " + str(x))
    x = x + 1
    time.sleep(0.45)
