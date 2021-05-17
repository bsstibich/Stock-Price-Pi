import RPi.GPIO as GPIO


pins = (11,12,13) # R = 11, G = 12, B = 13
 
def setup():
    global pwmR, pwmG, pwmB
    GPIO.setmode(GPIO.BOARD)
    for i in pins:  # iterate on the RGB pins, initialize each and set to HIGH to turn it off (COMMON ANODE)
        GPIO.setup(i, GPIO.OUT, initial=GPIO.HIGH)
        #GPIO.setup(i, GPIO.HIGH)
    pwmG = GPIO.PWM(pins[0], 2000)  # set each PWM pin to 2 KHz
    pwmR = GPIO.PWM(pins[1], 2000)
    pwmB = GPIO.PWM(pins[2], 2000)
    pwmR.start(0)   # initially set to 0 duty cycle
    pwmG.start(0)
    pwmB.start(0)
   
def setColor(r, g, b):  # 0 ~ 100 values since 0 ~ 100 only for duty cycle
    pwmR.ChangeDutyCycle(r)
    pwmG.ChangeDutyCycle(g)
    pwmB.ChangeDutyCycle(b)
 
def green():
     setColor(0, 100, 0)
def red():
    setColor(100, 0, 0)
def blue():
    setColor(0, 0, 100)
def maroon():
    setColor(50, 0, 0)
def destroy():
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()
    GPIO.cleanup()
 