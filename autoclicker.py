import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
(1920, 1080)
width, height = pyautogui.size()
for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
      sleep(10.01);