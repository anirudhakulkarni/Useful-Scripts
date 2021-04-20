import pyautogui
import time
import os
os.system("openvpn-gui --connect client")
time.sleep(5)
pyautogui.press('enter')
# time.sleep(2)
#to capture locations
# t=0
# while(t==0):
# 	x,y = pyautogui.position()
# 	print(x,y)
# found 80,840 for start vpn icon
# 106,593 for connect icon
# 1248,333 for minimiize
# pyautogui.press('win')
# time.sleep(0.6)
# pyautogui.write("openvpn gui")
# time.sleep(0.6)
# pyautogui.press('enter')
# time.sleep(0.6)
# pyautogui.rightClick(80,840)
# #time.sleep(0.1)
# pyautogui.click(106,593)
# time.sleep(1)
# pyautogui.press('enter')
time.sleep(2)

pyautogui.click(1248,333)
