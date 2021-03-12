import RPi.GPIO as GPIO
from time import sleep
import jasperModule
class robotMove:
    def __init__(self,port1,port2,portArm,portClaw,enable):
        self.port1 = port1
        self.port2 = port2
        self.portArm = portArm
        self.enable = enable

    def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.port1,GPIO.OUT)
        GPIO.setup(self.port2,GPIO.OUT)
        pwm.start(0)

    def stop():
        pwm.ChangeDutyCycle(0)
        GPIO.output(self.port1,GPIO.LOW)
        GPIO.output(self.port2,GPIO.LOW)
        GPIO.output(self.enable,GPIO.LOW)
        
    def forward(speed):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.port1,GPIO.LOW)
        GPIO.output(self.port2,GPIO.HIGH)
        GPIO.output(self.enable,GPIO.HIGH)

    def backward(speed):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.port1,GPIO.HIGH)
        GPIO.output(self.port2,GPIO.LOW)
        GPIO.output(self.enable,GPIO.HIGH)

    def right(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.port1,GPIO.LOW)
        GPIO.output(self.port2,GPIO.LOW)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def left(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.port1,GPIO.HIGH)
        GPIO.output(self.port2,GPIO.HIGH)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def armForward(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.portArm,GPIO.HIGH)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def armBackward(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.portArm,GPIO.LOW)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def clawClose(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.portClaw,GPIO.HIGH)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def clawOpen(speed,wait):
        pwm.ChangeDutyCycle(speed)
        GPIO.output(self.portCLaw,GPIO.LOW)
        GPIO.output(self.enable,GPIO.HIGH)
        sleep(wait)
        stop()

    def end():
        GPIO.cleanup()

