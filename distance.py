import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
RED = 17
GREEN = 27
BLUE = 22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

def setLedState(distance):
    roundedDistnce = int(round(distance))
    red = range(1, 10)
    green = range(12,200)
    blue = range(10, 12)

    if roundedDistnce in red:
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)
        GPIO.output(BLUE, False)
    elif roundedDistnce in green:
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
        GPIO.output(BLUE, False)
    elif roundedDistnce in blue:
        GPIO.output(RED, False)
        GPIO.output(GREEN, False)
        GPIO.output(BLUE, True)
    else:
        print "no range"
        GPIO.output(RED, False)
        GPIO.output(GREEN, False)
        GPIO.output(BLUE, False)

print "Distance measurement began"

while True:

  GPIO.output(TRIG, False)
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150
  distance = round(distance, 2)

  if distance > 1 and distance < 400:
    setLedState(distance)
    print "Distance:",distance - 0.5,"cm"
  else:
    print "Out Of Range"

try:
    while True:
        print " "
except KeyboardInterrupt:
    GPIO.cleanup()
