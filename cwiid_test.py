# -*- coding: utf-8 -*-
 
# based on Raspberry Pi Spi source
# http://www.raspberrypi-spy.co.uk/?p=1101

import cwiid
import time

def setup():

    # Try to connect Wii Mote
    print ("Press 1 + 2 button on Wii Remote")
    time.sleep(1)

    try:
        wii = cwiid.Wiimote()
    except RuntimeError:
        print ("Failed to connect Wii Remote")
        quit()

    print ("Success to connect Wii Remote")
    print ("Press PLUS + MINUS to terminate")

    # Set areas for Wii Mote to process
    wii.rpt_mode = cwiid.RPT_BTN

    wii.led = setLedNum()
    wii.rumble = True
    time.sleep(0.1)
    wii.rumble = False

    stateDict = wii.state
    stateList = list(stateDict)

    return wii

def setLedNum(led = None, bin = None):
    ledDict = {1: 1, 2: 2, 3: 4, 4: 8}
    ledList = [1, 2, 3, 4]

    if led == None:
        import random
        led = random.randrange(4)
        led = ledList[led]
    else:
        led = ledDict[led]
    if bin != None:
        led = bin
    return led

 
def getButtons(wii):
    button_delay = 0.1
    buttons = wii.state['buttons']
 
    # Press Plus and Minus
    # Terminate after rumble
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print ('\nStop connecting...')
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)
 
    # Check button pressed
    # wii.state['buttons']and button number(constants)
    # Processing by bitwise AND 
    if (buttons & cwiid.BTN_LEFT):
        print ('Left button pressed')
        time.sleep(button_delay)
 
    if(buttons & cwiid.BTN_RIGHT):
        print ('Right button pressed')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_UP):
        print ('Up button pressed')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_DOWN):
        print ('Down button pressed')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_1):
        print ('Button 1')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_2):
        print ('Button 2')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_A):
        print ('Button A')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_B):
        print ('Button B')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_HOME):
        print ('Home button')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_MINUS):
        print ('Minus button')
        time.sleep(button_delay)
 
    if (buttons & cwiid.BTN_PLUS):
        print ('Plus button')
        time.sleep(button_delay)    
 
def getAcc(wii):
    acc_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    acc = wii.state['acc']
    print ("acc=",acc)
    time.sleep(acc_delay) 
 
def getIR(wii):
    ir_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_IR
    ir = wii.state['ir_src']
    print ("ir=",ir)
    time.sleep(ir_delay)   
 
def getNunchuk(wii):
    nunchuk_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK
    nunchuk = wii.state['nunchuk']
    print ("Nunchuk =",nunchuk)
    time.sleep(nunchuk_delay)     
 
def getNunchukAcc(wii):
    nunchuk_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK
    nunchuk = wii.state['nunchuk']['acc']
    print ("Nunchuk Acc =",nunchuk)
    time.sleep(nunchuk_delay)
 
def getNunchukButtons(wii):
    nunchuk_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK
    nunchuk = wii.state['nunchuk']['buttons']
    if (nunchuk & cwiid.NUNCHUK_BTN_C):
        print ('Nunchuk button C')
        time.sleep(nunchuk_delay)
    if (nunchuk & cwiid.NUNCHUK_BTN_Z):
        print ('Nunchuk button Z')
        time.sleep(nunchuk_delay)   
 
def getNunchukStick(wii):
    nunchuk_delay = 0.1
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK
    nunchuk = wii.state['nunchuk']['stick']
    print ('Nunchuk Stick =', nunchuk)
    time.sleep(nunchuk_delay) 
 
if __name__ == "__main__":
    wii = setup()
    while True:
        getNunchuk(wii)
        getAcc(wii)
