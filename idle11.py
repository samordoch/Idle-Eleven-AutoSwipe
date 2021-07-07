import os
import keyboard

def swipeDefence():
    # swipe cb row
    os.system("adb shell input swipe 60 1620 958 1621 130")
    # swipe gk
    os.system("adb R58N92V6KCH shell input swipe 330 2024 770 2024 130")

def swipeSt():
    # swipe over st cf
    os.system("adb R58N92V6KCH shell input swipe 220 728 820 729 130")

def swipeMidfield():
    # swipe on cam cm
    os.system("adb R58N92V6KCH shell input swipe 100 1067 990 1067 130")
    # swipe on cdm
    os.system("adb R58N92V6KCH shell input swipe 100 1207 990 1207 130")





def swipe442D():
    while(not keyboard.is_pressed('F3')):
        swipeSt()
        swipeMidfield()
        swipeDefence()

swipe442D()