#!/usr/bin/python

from Tkinter import *

from Adafruit_PWM_Servo_Driver import PWM
import time


# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)  # Set frequency to 60 Hz

root = Tk()

root.title("Dispense Battery")
root.geometry("800x480")

app = Frame(root)
app.grid()



button1 = Button(app, text="Borrow 1", command=dispense1, height=4, width=20)
button1.grid(row=0, column=0)

button2 = Button(app, text="Borrow 2", command=dispense2, height=4, width=20)
button2.grid(row=0, column=1)

button3 = Button(app, text = "Borrow 3",command= dispense3, height = 4, width = 20)
button3.grid(row=0, column=2)

button4 = Button(app, text = "Borrow 4",command= dispense4, height = 4, width = 20)
button4.grid(row=1, column=0)

button5 = Button(app, text = "Borrow 5",command= dispense5, height = 4, width = 20)
button5.grid(row=1, column=1)

button6 = Button(app, text = "Borrow 6",command= dispense6, height = 4, width = 20)
button6.grid(row=1, column=2)

button7 = Button(app, text = "Borrow 7",command= dispense7, height = 4, width = 20)
button7.grid(row=2, column=0)

button8 = Button(app, text = "Borrow 8",command= dispense8, height = 4, width = 20)
button8.grid(row=2, column=1)

button9 = Button(app, text = "Borrow 9",command= dispense9, height = 4, width = 20)
button9.grid(row=2, column=2)

button10 = Button(app, text = "Borrow 10",command= dispense10, height = 4, width = 20)
button10.grid(row=3, column=0)

button11 = Button(app, text = "Borrow 11",command= dispense11, height = 4, width = 20)
button11.grid(row=3, column=1)

button12 = Button(app, text = "Borrow 12",command= dispense12, height = 4, width = 20)
button12.grid(row=3, column=2)

button13 = Button(app, text = "Borrow 13",command= dispense13, height = 4, width = 20)
button13.grid(row=4, column=0)

button14 = Button(app, text = "Borrow 14",command= dispense14, height = 4, width = 20)
button14.grid(row=4, column=1)

button15 = Button(app, text = "Borrow 15",command= dispense15, height = 4, width = 20)
button15.grid(row=4, column=2)


def dispense1():
    pwm.setPWM(0, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMin)


def dispense2():
    pwm.setPWM(1, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(1, 0, servoMin)


def dispense3():
    pwm.setPWM(2, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(2, 0, servoMin)


def dispense4():
    pwm.setPWM(3, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(3, 0, servoMin)


def dispense5():
    pwm.setPWM(4, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(4, 0, servoMin)


def dispense6():
    pwm.setPWM(5, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(5, 0, servoMin)


def dispense7():
    pwm.setPWM(6, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(6, 0, servoMin)


def dispense8():
    pwm.setPWM(7, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(7, 0, servoMin)


def dispense9():
    pwm.setPWM(8, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(8, 0, servoMin)


def dispense10():
    pwm.setPWM(9, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(9, 0, servoMin)


def dispense11():
    pwm.setPWM(10, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(10, 0, servoMin)


def dispense12():
    pwm.setPWM(11, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(11, 0, servoMin)


def dispense13():
    pwm.setPWM(12, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(12, 0, servoMin)


def dispense14():
    pwm.setPWM(13, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(13, 0, servoMin)


def dispense15():
    pwm.setPWM(14, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(14, 0, servoMin)


root.mainloop()



