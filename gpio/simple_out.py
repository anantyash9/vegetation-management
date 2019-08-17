import Jetson.GPIO as GPIO
import time

# Pin Definitions
enab = 19  # BOARD pin 12, BCM pin 18
int1 = 21
int2 = 23

def forward():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(enab, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(enab,GPIO.HIGH)
    GPIO.output(int1, GPIO.LOW)
    GPIO.output(int2, GPIO.HIGH)
def backward():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(enab, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(enab,GPIO.HIGH)
    GPIO.output(int1, GPIO.HIGH)
    GPIO.output(int2, GPIO.LOW)
def stop():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(enab, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(int2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(enab,GPIO.LOW)
    GPIO.output(int1, GPIO.LOW)
    GPIO.output(int2, GPIO.LOW)
