#!/usr/bin/env python

import pigpio
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="Send a message in morse blinking a led.")
parser.add_argument("message", nargs="?", default="Hello world in morse", help="The message to send in morse")
parser.add_argument("-p", "--pin", type=int, default=4, help="The GPIO pin for controlling the led.")
parser.add_argument("-b", "--baseTime", type=float, default=0.2, help="The base time for dots.")
args = parser.parse_args()

message = args.message
ledPin = args.pin
baseTime = args.baseTime
dotQuantum = 1
dashQuantum = 3
partSeparatorQuantum = 1
letterSeparatorQuantum = 3
wordSeparatorQuantum = 5

morseCode = {
'a':'.-'   , 'b':'-...' , 'c':'-.-.' , 'd':'-..'  , 'e':'.'    ,
'f':'..-.' , 'g':'--.'  , 'h':'....' , 'i':'..'   , 'j':'.---' ,
'k':'-.-'  , 'l':'.-..' , 'm':'--'   , 'n':'-.'   , 'o':'---'  ,
'p':'.--.' , 'q':'--.-' , 'r':'.-.'  , 's':'...'  , 't':'-'    ,
'u':'..-'  , 'v':'...-' , 'w':'.--'  , 'x':'-..-' , 'y':'-.--' ,
'z':'--..' , '1':'.----', '2':'..---', '3':'...--', '4':'....-',
'5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----'}

def send_single_code(code):
    c = code.lower()
    if c in morseCode:
        v = morseCode[c]
        for s in v:
            if s == '.':
                pi.write(ledPin, 0)
                time.sleep(dotQuantum * baseTime)
            else:
                pi.write(ledPin, 0)
                time.sleep(dashQuantum * baseTime)
            pi.write(ledPin, 1)
            time.sleep(partSeparatorQuantum * baseTime)
        time.sleep((letterSeparatorQuantum - partSeparatorQuantum) * baseTime)
    elif c == ' ':
        time.sleep((wordSeparatorQuantum-letterSeparatorQuantum) * baseTime)

pi = pigpio.pi()
pi.set_mode(ledPin, pigpio.OUTPUT)

for l in message:
    sys.stdout.write(l)
    sys.stdout.flush()
    send_single_code(l)
print('')
pi.stop()
