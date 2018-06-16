import RPi.GPIO as GPIO
import time
import uinput
from evdev import UInput, ecodes as e

btnLeft = 12
btnUp = 7
btnRight = 8
btnDown = 15
btnLeftJump = 5
btnRightJump = 29
btnGreen = 38
btnPurple = 40
btnYellow = 37
btnRed = 32
btnSelect = 31
btnStart = 33
btn2nd = 35

GPIO.setmode(GPIO.BOARD)

""" Enable Sound """
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)

""" Buttons """	
GPIO.setup(btnLeft, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnUp, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnRight, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnDown, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnLeftJump, GPIO.IN)
GPIO.setup(btnRightJump, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnGreen, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnPurple, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnYellow, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnRed, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnSelect, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btnStart, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn2nd, GPIO.IN, pull_up_down = GPIO.PUD_UP)

""" Devices for keystrokes """
device = uinput.Device([uinput.KEY_E])
ui = UInput()

def hold(key):
	ui.write(e.EV_KEY, key, 1)
	ui.syn()
	return 0

def release(key):
	ui.write(e.EV_KEY, key, 0)
	ui.syn()
	return 0

bA = False
bB = False
bC = False
bD = False
bE = False
bF = False
bG = False
bH = False
bI = False
bLeft = False
bRight = False
bUp = False
bDown = False

""" Polling """
while True:
	time.sleep(0.02)
	if (not bLeft) and (not GPIO.input(btnLeft)):
                bLeft = True
		hold(e.KEY_LEFT)
	if bLeft and GPIO.input(btnLeft):
                release(e.KEY_LEFT)
		bLeft = False
	if (not bRight) and (not GPIO.input(btnRight)):
                bRight = True
		hold(e.KEY_RIGHT)
	if bRight and GPIO.input(btnRight):
                release(e.KEY_RIGHT)
		bRight = False
	if (not bUp) and (not GPIO.input(btnUp)):
                bUp = True
		hold(e.KEY_UP)
	if bUp and GPIO.input(btnUp):
                release(e.KEY_UP)
		bUp = False
	if (not bDown) and (not GPIO.input(btnDown)):
                bDown = True
		hold(e.KEY_DOWN)
        if bDown and GPIO.input(btnDown):
                release(e.KEY_DOWN)
		bDown = False
	if (not bA) and (not GPIO.input(btnLeftJump)):
                if not bI:
                        hold(e.KEY_A)
                else:
                        hold(e.KEY_KPMINUS)
		bA = True
	if bA and GPIO.input(btnLeftJump):
                if not bI:
                        release(e.KEY_A)
                else:
                        release(e.KEY_KPMINUS)
		bA = False
	if (not bB) and (not GPIO.input(btnRightJump)):
                if not bI:
                        hold(e.KEY_B)
                else:
                        hold(e.KEY_KPPLUS)
		bB = True
	if bB and GPIO.input(btnRightJump):
                if not bI:
                        release(e.KEY_B)
                else:
                        release(e.KEY_KPPLUS)
		bB = False
	if (not bC) and (not GPIO.input(btnGreen)):
                if not bI:
                        hold(e.KEY_C)
                else:
                        GPIO.output(16, GPIO.HIGH)
		bC = True
	if bC and GPIO.input(btnGreen):
                release(e.KEY_C)
		bC = False
	if (not bD) and (not GPIO.input(btnRed)):
                if not bI:
                        hold(e.KEY_D)
                else:
                        hold(e.KEY_ENTER)
		bD = True
	if bD and GPIO.input(btnRed):
                if not bI:
                        release(e.KEY_D)
                else:
                        release(e.KEY_ENTER)
		bD = False
	if (not bE) and (not GPIO.input(btnPurple)):
                if not bI:
                        hold(e.KEY_E)
                else:
                        GPIO.output(16, GPIO.LOW)
		bE = True
	if bE and GPIO.input(btnPurple):
                release(e.KEY_E)
		bE = False
	if (not bF) and (not GPIO.input(btnYellow)):
                if not bI:
                        hold(e.KEY_F)
                else:
                        hold(e.KEY_BACKSPACE)
		bF = True
	if bF and GPIO.input(btnYellow):
                if not bI:
                        release(e.KEY_F)
                else:
                        release(e.KEY_BACKSPACE)
		bF = False
	if (not bG) and (not GPIO.input(btnSelect)):
		hold(e.KEY_G)
		bG = True
	if bG and GPIO.input(btnSelect):
                release(e.KEY_G)
		bG = False
	if (not bH) and (not GPIO.input(btnStart)):
		hold(e.KEY_H)
		bH = True
	if bH and GPIO.input(btnStart):
                release(e.KEY_H)
		bH = False
	if (not bI) and (not GPIO.input(btn2nd)):
		bI = True
	if bI and GPIO.input(btn2nd):
		bI = False


GPIO.cleanup()
