import RPi.GPIO as io
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER_1 = 17
GPIO_ECHO_1 = 18
GPIO_TRIGGER_2 = 22
GPIO_ECHO_2 = 23
GPIO_TRIGGER_3 = 9
GPIO_ECHO_3 = 25
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
def distance_Left():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance_Left = (TimeElapsed * 34300) / 2
 
    return distance_Left

def distance_Right():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_3, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_3, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_3) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_3) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance_Right = (TimeElapsed * 34300) / 2
 
    return distance_Right

io.setwarnings(False)
io.setmode(io.BCM)
#Ideally, let's try and smooth the transitions between as right now it's a jarring jolt with the motors. [
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    
motor1 = 13
motor2 = 12
motor1F = 16
motor2F = 20
motor1R = 6
motor2R = 5
trigger = 26
echo = 19
frequency = 100

io.setup(motor1, io.OUT)
io.setup(motor2, io.OUT)
io.setup(motor1F, io.OUT)
io.setup(motor2F, io.OUT)
io.setup(motor1R, io.OUT)
io.setup(motor2R, io.OUT)
io.setup(trigger, io.OUT)
io.setup(echo, io.IN)

motor1 = io.PWM(motor1,frequency)
motor2 = io.PWM(motor2,frequency)


motor1.start(0)
motor2.start(0)

duty = 100
def distance():
    # set Trigger to HIGH
    io.output(trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    io.output(trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while io.input(echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while io.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def forward():
    io.output(motor1F, True)
    io.output(motor2F,True)
    io.output(motor1R, False)
    io.output(motor2R, False)
    motor1.ChangeDutyCycle(duty)
    motor2.ChangeDutyCycle(duty)
        
def left():
    io.output(motor1F, False)
    io.output(motor2F, True)
    io.output(motor1R, True)
    io.output(motor2R, False)
        
def right():
    io.output(motor1F, True)
    io.output(motor2F, False)
    io.output(motor1R,False)
    io.output(motor2R,True)
        
def back():
    io.output(motor1F, False)
    io.output(motor2F, False)
    io.output(motor1R, True)
    io.output(motor2R, True)


def stop():
    io.output(motor1F, False)
    io.output(motor2F, False)
    io.output(motor1R, False)
    io.output(motor2R, False)
    motor1.ChangeDutyCycle(0)
    motor2.ChangeDutyCycle(0)

def Exit():
    print("Program Ended")
    stop()
    io.cleanup
    motor1.stop()
    motor2.stop()
    print("It is now safe to close the program")
        
        
def GUIControls():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    root.title("GUI Controls")
    
    LeftButton = Button(frame, text='Left', command=left)
    RightButton = Button(frame, text='Right', command=right)
    ForwardButton = Button(frame, text='Forward', command=forward)
    BackwardButton = Button(frame, text='Reverse', command=back)
    StopButton = Button(frame, text='Stop', command=stop)
    
    ExitProgram = Button(frame, text='Exit Program', command=Exit)
    
    LeftButton.config(width=25, height=3)
    RightButton.config(width=25, height=3)
    ForwardButton.config(width=25, height=3)
    BackwardButton.config(width=25, height=3)
    StopButton.config(width=25, height=3)
    ExitProgram.config(width=25, height=1)
    
    LeftButton.grid(row=1, column=0, columnspan=3)
    RightButton.grid(row=1, column=30, columnspan=3)
    ForwardButton.grid(row=0, column=15, columnspan=3)
    BackwardButton.grid(row=2, column=15, columnspan=3)
    StopButton.grid(row=1, column=15, columnspan=3)

    ExitProgram.grid(row=6, column=15, columnspan=3)
    
   # root.mainloop()

if __name__ == '__main__':
    forward()
    try:
        while True:
            dist = distance()
            #print ("Measured Distance = %.1f cm" % dist)
            if(dist <= 10.0):
                #print("Stop")
                stop()
            else:
                forward()
                
            time.sleep(0.05)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
