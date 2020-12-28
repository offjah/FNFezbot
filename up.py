from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import time
Keyboard = Controller()

uniy1=148
uniy2=150
presstime=.06

def countdown(sec):
    
    while sec > 0:
        print(sec)
        time.sleep(1)
        sec-=1

def grabdat():
    countdown(3)


    #leftA = ImageGrab.grab(bbox=(1090,uniy1,1092,uniy2))
    #downA = ImageGrab.grab(bbox=(1280,uniy1,1282,uniy2))
    upA = ImageGrab.grab(bbox=(1455,uniy1,1457,uniy2))
    #rightA = ImageGrab.grab(bbox=(1640,uniy1,1642,uniy2))
    return upA

grab = True

if grab:
    RefU= grabdat()




countdown(1)



   
while True:
    #leftA = ImageGrab.grab(bbox=(1090,uniy1,1092,uniy2))
    #downA = ImageGrab.grab(bbox=(1280,uniy1,1282,uniy2))
    upA = ImageGrab.grab(bbox=(1455,uniy1,1457,uniy2))
    #rightA = ImageGrab.grab(bbox=(1640,uniy1,1642,uniy2))


    if not(upA==RefU):
        print("up")
        Keyboard.press(Key.up)
        time.sleep(presstime)
        Keyboard.release(Key.up)

'''    
while True:
    time.sleep(.01)
    leftA = ImageGrab.grab(bbox=(1090,uniy1,1100,uniy2))
    downA = ImageGrab.grab(bbox=(1280,uniy1,1290,uniy2))
    upA = ImageGrab.grab(bbox=(1455,uniy1,1465,uniy2))
    rightA = ImageGrab.grab(bbox=(1640,uniy1,1650,uniy2))

    leftA.save("leftA.jpg")
    rightA.save("rightA.jpg")
    upA.save("upA.jpg")
    downA.save("downA.jpg")

    if not(filecmp.cmp("leftA.jpg",".Refleft.jpg")):
        #print("left")
        Keyboard.press(Key.left)
        time.sleep(presstime)
        Keyboard.release(Key.left)
    if not(filecmp.cmp("rightA.jpg",".Refright.jpg")):
        #print("right")
        Keyboard.press(Key.right)
        time.sleep(presstime)
        Keyboard.release(Key.right)
    if not(filecmp.cmp("upA.jpg",".Refup.jpg")):
        #print("up")
        Keyboard.press(Key.up)
        time.sleep(presstime)
        Keyboard.release(Key.up)
    if not(filecmp.cmp("downA.jpg",".Refdown.jpg")):
        #print("down")
        Keyboard.press(Key.down)
        time.sleep(presstime)
        Keyboard.release(Key.down)
    
'''
