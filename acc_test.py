import cwiid
import time
import pygame
import math

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
    remote = wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    nunchuk = wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_NUNCHUK

    print (remote, nunchuk)

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

def getAcc(wii):
    acc_delay = 0.2
    
    remote_angle = 0
    nunchuk_angle = 0
    
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK
    
    nunchuk_acc = wii.state['nunchuk']['acc']
    remote_acc = wii.state['acc']

    nunchuk_accList = list(nunchuk_acc)
    nunchuk_x = nunchuk_accList[0]
    nunchuk_y = nunchuk_accList[1]
    nunchuk_z = nunchuk_accList[2]

    remote_accList = list(remote_acc)
    remote_x = remote_accList[0]
    remote_y = remote_accList[1]
    remote_z = remote_accList[2]        

    #print("Remote : X = {} Y = {} Z = {}".format(remote_x,remote_y,remote_z))
    if(remote_z != 0 and remote_x !=0):
        remote_angle = math.atan(remote_x/remote_z)
    if(nunchuk_z != 0 and nunchuk_x !=0):
        nunchuk_angle = math.atan(nunchuk_x/nunchuk_z)
    
    print("Remote Angle : {}".format(remote_angle))
    print("Nunchuk Angle : {}".format(nunchuk_angle))
    
    if remote_angle != 0.0:
        soundPlay(1)
    if nunchuk_angle != 0.0:
        soundPlay(2)
    #print("Nunchuk : X = {} Y = {} Z = {}".format(nunchuk_x,nunchuk_y,nunchuk_z))    
    time.sleep(acc_delay)

def soundPlay(num):

    sound_files = ["/home/pi/Desktop/Programming/snare.wav",
                   "/home/pi/Desktop/Programming/closed_hihat.wav"]
                   
    
    if num == 1:
        print ("Snare")
        pygame.mixer.music.load(sound_files[0])
        pygame.mixer.music.play()
    elif num == 2:
        print ("HiHat")
        pygame.mixer.music.load(sound_files[1])
        pygame.mixer.music.play()
    elif num == 3:
        both = [pygame.mixer.Sound(f) for f in sound_files]
        for s in both:
            pygame.mixer.find_channel().play(s)

if __name__ == "__main__":
    wii = setup()
    pygame.init()

    while True:
        getAcc(wii)
    
        

