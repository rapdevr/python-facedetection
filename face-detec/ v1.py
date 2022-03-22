from curses import noraw
from email.errors import NoBoundaryInMultipartDefect
from enum import auto
from math import degrees
from operator import truediv
from re import T
from select import select
from statistics import mode
from time import daylight
from tkinter import X
from playsound import playsound
from pytapo import Tapo
import time

user = "rthiahulan11"
password = "br0adband@tpl11"
host = "192.168.10.236"

tapo = Tapo(host, user, password)
tapo.setDayNightMode(inf_type='auto')

def cam_motor_cal():
    tapo.calibrateMotor()
    print('calibration in progress...')
    time.sleep(26)
    tapo.moveMotor(x=0, y=45)
    print("Calibration Success! Waiting for faces...")


def motion_activ():
    print("scanning for motion...")
    while True:
        tapo.setMotionDetection(enabled=True, sensitivity='low')
        if tapo.getMotionDetection():
            tapo.setAutoTrackTarget(enabled=True)
            target = tapo.getAutoTrackTarget()

            
            
        
cam_motor_cal()
motion_activ()


