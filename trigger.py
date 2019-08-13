import RPi.GPIO as gpio
import sys

channel = 4
gpio.setmode(gpio.BCM)
args = sys.argv
ctl = args[1]

if (int(ctl) == 1):
    gpio.setup(channel, gpio.OUT)
    gpio.output(channel, gpio.HIGH)

if (int(ctl) == 0):
    gpio.setup(channel, gpio.OUT)
    gpio.output(channel, gpio.LOW)

gpio.cleanup()
