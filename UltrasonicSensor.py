#This is for the ultrasonic sensor to read to the LCD

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

# Import necessary libraries for communication and display use
import lcddriver

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

display.lcd_display_string("Distance in cm", 1) # Write line of text to first line of display
print "Starting Measurement..."

try:
    while True:
        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)
        while GPIO.input(ECHO) == 0:
                    pass
                    start = time.time()
        while GPIO.input(ECHO) == 1:
                    pass
                    stop = time.time()
                    
        distance = (stop - start)*17000

        display.lcd_display_string(str(distance), 2)

        time.sleep(0.2)
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()

GPIO.cleanup()
