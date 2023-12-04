import mouse
import time
import win32api
import keyboard
from PIL import ImageGrab
from pyautogui import sleep
import tkinter as tk
import threading

screenW = win32api.GetSystemMetrics(0)
screenH = win32api.GetSystemMetrics(1)
centerX = screenW / 2
centerY = screenH / 2

aimbot = False
is_aimbot_visible = False

def aim():
    posX = 0
    posY = 0
    lightestRed = 0
    
    if aimbot:
        print("players searching")
        for i in range(0, 100, 1):
            for j in range(0, 100, 1):
                if tempIm[i, j][0] > lightestRed and tempIm[i, j][1] == 0 and tempIm[i, j][2] == 0:
                    lightestRed = tempIm[i, j][0]
                    posX = i
                    posY = j
        if posX != 0 or posY != 0:
            print("aiming user")
            (mouseX, mouseY) = mouse.get_position()
            mouse.move(mouseX + posX - 50, mouseY + posY - 50)

def toggle_aimbot():
    global aimbot, is_aimbot_visible
    aimbot = not aimbot
    is_aimbot_visible = not is_aimbot_visible
    print("aimbot" + str(aimbot))
    update_gui()

def update_gui():
    if is_aimbot_visible:
        aimbot_text.pack(side="top", padx=10, pady=10, anchor="w")
    else:
        aimbot_text.pack_forget()


def on_p_press(event):
    toggle_aimbot()
    sleep(0.1)


pencere = tk.Tk()
pencere.overrideredirect(True)
pencere.attributes("-transparentcolor", "gray")
pencere.attributes("-topmost", True)
pencere.geometry("+0+50")

frame = tk.Frame(pencere, bg="gray")
frame.pack()

etiket = tk.Label(frame, text="BQuer Aimbot", font=("Terminal", 34), fg="white", bg="gray")
etiket.pack(side="top")

aimbot_text = tk.Label(frame, text="AimBot", font=("Terminal", 18), fg="white", bg="gray", anchor="w")
keyboard.on_press_key('p', on_p_press)

def aim_loop():
    while True:
        myImage = ImageGrab.grab(bbox=(centerX - 50, centerY - 50, centerX + 50, centerY + 50))
        global tempIm
        tempIm = myImage.load()
        aim()

aim_thread = threading.Thread(target=aim_loop)
aim_thread.start()

pencere.mainloop()
