#!/usr/bin/env python3

import RPi.GPIO as GPIO, time, random
class Lights():
    def __init__(self,pins,delay=0.1):
        self.pins = pins
        try:
            self.size = len(pins)
        except TypeError:
            self.size = 1
        self.delay = delay
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins, GPIO.OUT)
        GPIO.output(pins,0)

    def allon(self):
        GPIO.output(self.pins,1)

    def alloff(self):
        GPIO.output(self.pins,0)

    def pinon(self,pin):
        GPIO.output(pin,1)

    def pinoff(self,pin):
        GPIO.output(pin,0)
    
    def slow(self,operation,direction="RIGHT",delay=None):
        if delay == None:
            delay = self.delay
        if direction == "RIGHT":
            pins = self.pins
        else:
            pins = self.pins[::-1]

        if operation == "OFF":
            command = self.pinon
        else:
            command = self.pinoff
        for pin in pins:
            command(pin)
            time.sleep(delay)

    def onoff(self,pin,delay):
        self.pinon(pin)
        time.sleep(delay)
        self.pinoff(pin)
    def nothing(string):
        pass

    def allonoff(self,direction="RIGHT",delay=None):
        if delay == None:
            delay = self.delay
        if direction == "RIGHT":
            pins = self.pins
        else:
            pins = self.pins[::-1]

        for pin in pins:
            self.onoff(pin,delay)
    #light shows below this line#
    def slowon(self,delay=None):
        if delay == None:
            self.slow("ON")
        else:
            self.slow("ON",delay=delay)

    def slowoff(self,delay=None):
        if delay == None:
            self.slow("OFF")
        else:
            self.slow("OFF",delay=delay)

    def chase(self,times=1):
        for count in range(times):
            self.slow("ON")
            self.slow("OFF")
    def backforth(self,times=1):
        for count in range(times):
            self.slow("ON")
            self.slow("OFF",direction="LEFT")
            self.slow("ON",direction="LEFT")
            self.slow("OFF")
    def cylon(self,times=1,delay=None):
        if delay == None:
            delay = self.delay
        for count in range(times):
            self.allonoff(delay=delay)
            self.allonoff(direction="LEFT",delay=delay)
    def random(self,times=1):
        for count in range(times):
            self.onoff(random.choice(self.pins),delay=self.delay)
    def branch(self,times=1):
        if self.size % 2 == 0:
            size = int(self.size/2)
            left = self.pins[:size]
            right = self.pins[size:]
        else:
            size = int((self.size+1)/2)
            left = self.pins[:size]
            right = self.pins[size-1:]
        for count in range(times):
            for pinnum in range(size):
                self.pinon(left[::-1][pinnum])
                self.pinon(right[pinnum])
                time.sleep(self.delay)
                self.pinoff(left[pinnum])
                self.pinoff(right[::-1][pinnum])

            for pinnum in range(size):
                self.pinon(left[pinnum])
                self.pinon(right[::-1][pinnum])
                time.sleep(self.delay)
                self.pinoff(left[pinnum])
                self.pinoff(right[::-1][pinnum])
    def lightshow(self,waittime=1,descrip=True):
        if descrip:
            command = print
        else:
            command = self.nothing
        command("all on")
        self.allon()
        time.sleep(waittime)
        command("all off")
        self.alloff()
        time.sleep(waittime)
        command("slow on")
        self.slowon(delay=0.15)
        time.sleep(waittime)
        command("slow off")
        self.slowoff(delay=0.15)
        time.sleep(waittime)
        command("chase")
        self.chase()
        time.sleep(waittime)
        command("back and forth")
        self.backforth(times=3)
        time.sleep(waittime)
        command("cylon")
        self.cylon(times=2,delay=0.075)
        time.sleep(waittime)
        command("random")
        self.random(times=10)
        time.sleep(waittime)
        command("branch")
        self.branch(times=2)
