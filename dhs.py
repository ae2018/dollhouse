def dist():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    #print "Distance Measurement In Progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(0.5)

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

    #print "Distance:",distance,"cm"

    GPIO.cleanup()
    return distance

def servo():
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    servoPin=11
    lightpin=40
    GPIO.setup(servoPin,GPIO.OUT)
    GPIO.setup(lightpin,GPIO.OUT)
    pwm=GPIO.PWM(servoPin,50)
    pwm.start(8)
    time.sleep(1)
    GPIO.output(lightpin,True)
    time.sleep(1)

    for i in range(2,12):
    	#desiredPosition=input("Where do you want the servo? 9-180 ")
    	#DC=(desiredPosition/20.001)+3.
    	for j in range(1,11,1):
    		DC=i+(j/10.0)
    		pwm.ChangeDutyCycle(DC)
    		print DC
    		time.sleep(0.05)
    print "Done!"
    time.sleep(1)
    ####################################
    for i in range(12,1,-1):
    	#desiredPosition=input("Where do you want the servo? 9-180 ")
    	#DC=(desiredPosition/20.001)+3.
    	for j in range(11,1,-3):
    		DC=i+(j/10.0)
    		pwm.ChangeDutyCycle(DC)
    		print DC
    		time.sleep(0.05)
    print "Done!"
    ##########################################
    pwm.stop()
    GPIO.cleanup()
    return

while(True):
    d=dist()
    if d <100:
        print "Welcome home master! ",d,"cm"
        servo()
    #else:
        #print "No one home yet"
