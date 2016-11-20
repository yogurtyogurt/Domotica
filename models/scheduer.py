# -*- coding: utf-8 -*-
from gluon.scheduler import Scheduler
'''
MANSARDA_UP=4
MANSARDA_DW=24
PIANO_UP=17
PIANO_DW=18
TERRA_UP=22
TERRA_DW=23

'''


def task_stop_current(all_pins):
    pins=[4,24,17,18,22,23]
    #pins=all_pins
    if not GPIO.getmode():
        GPIO.setmode(GPIO.BCM)        
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


scheduler = Scheduler(db,tasks=dict(stop_current=task_stop_current))
