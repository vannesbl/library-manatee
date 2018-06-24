Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Hacking Book Reviews

from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime


bookpic = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

sense = SenseHat()
camera = PiCamera()
buttonpic = Button(26)
buttonflip = Button(19)

r = (255, 0, 0)
w = (255, 255, 255)
b = (0, 0, 255)
g = (0, 255, 0)
bl = (0, 0, 0)
m = (255, 0, 255)

emojiHappy = [
    bl, bl, b, b, b, b, bl, bl,
    bl, b, w, w, w, w, b, bl,
    b, w, w, g, g, w, w, b,
    b, w, g, w, w, g, w, b,
    b, w, w, w, w, w, w, b,
    b, w, g, w, w, g, w, b,
    bl, b, w, w, w, w, b, bl,
    bl, bl, b, b, b, b, bl, bl,
    ]

emojiHeart = [  
    bl, bl, bl, m, m, bl, bl, bl,
    bl, bl, m, m, m, m, bl, bl,
    bl, m, m, m, m, m, m, bl,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m,
    m, m, m, m, m, m, m, m,
    bl, m, m, bl, bl, m, m, bl,
]

ThumbsUpblue = [
    bl, bl, bl, bl, bl, bl, bl, bl,
    bl, w, w, w, w, b, b, bl,
    bl, w, w, w, w, b, b, bl,
    bl, w, w, w, w, b, b, bl,
    bl, w, w, w, w, b, b, bl,
    bl, bl, bl, w, w, bl, bl, bl,
    bl, bl, bl, w, w, bl, bl, bl,
    bl, bl, bl, bl, bl, bl, bl, bl,
    ]

ThumbsUpRed = [
    w, w, w, w, w, w, w, w,
    w, r, r, r, r, bl, bl, w,
    w, r, r, r, r, bl, bl, w,
    w, r, r, r, r, bl, bl, w,
    w, r, r, r, r, bl, bl, w,
    w, w, w, r, r, w, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, w, w, w, w, w,
    ]

emojiSad = [
    bl, bl, b, b, b, b, bl, bl,
    bl, b, w, w, w, w, b, bl,
    b, w, r, w, w, r, w, b,
    b, w, w, r, r, w, w, b,
    b, w, w, w, w, w, w, b,
    b, w, r, w, w, r, w, b,
    bl, b, w, w, w, w, b, bl,
    bl, bl, b, b, b, b, bl, bl,
    ]


while True:
    if  buttonpic.wait_for_press():
        camera.start_preview(alpha=192)
        sleep(2)
        camera.capture(bookpic)
        camera.stop_preview()
    else buttonflip.wait_for_press():
         sense.set_pixels(emojiHappy)
         sleep(1)
    if buttonflip.wait_for_press():
        sense.set_pixels(emojiSad)
        sleep(1)
    if buttonflip.wait_for_press():
        sense.set_pixels(emojiHeart)
        sleep(1)
    if buttonflip.wait_for_press():
        sense.set_pixels(ThumbsUpblue)
        sleep(1)

