# Write your code here :-)
# Starter code for figuring out what color the sensor is seeing from the color wheel.
# The readColor function doesn't work yet. That's your job.

#sorry for the delay Leo - let's see if we can put this into the Java project today

import time
import board
import busio
import adafruit_tcs34725

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

def readColor(colorValues):

    red_value = colorValues[0]
    green_value = colorValues[1]
    blue_value = colorValues[2]

    returnValue = "UNKNOWN"

    if(red_value > 70):
        returnValue = "RED"
    elif(green_value > 22):
        returnValue = "GREEN"
    elif(blue_value <= 11 and blue_value >= 9):
        returnValue = "CYAN"
    elif(red_value <= 40 and green_value <= 22):
        returnValue ="YELLOW"

    return returnValue


def readColorSensor():
    #These lines read the color measured by the red, blue, and green channels.
    #The values range from 0 - 255.

    red_value = sensor.color_rgb_bytes[0]
    green_value = sensor.color_rgb_bytes[1]
    blue_value = sensor.color_rgb_bytes[2]

    sumValues = red_value+green_value+blue_value * 1.0

    #Let's now try to normalize the values as a percentage that uses the three color values together to measure brightness.
    red_value_scaled = red_value/sumValues
    green_value_scaled = green_value/sumValues
    blue_value_scaled = blue_value/sumValues

    return [red_value, green_value, blue_value]


changeCount = 0
oldColor = readColor(readColorSensor())

displayDelay = 10
displayCount = 0
while True:

    #print('Color: ({0}, {1}, {2})'.format(red_value_scaled, green_value_scaled, blue_value_scaled))

    currentColor = readColor(readColorSensor())

    if(currentColor != oldColor and currentColor != "UNKNOWN"):
        changeCount +=1

    #print('Lux: {0}'.format(sensor.lux))
    if(displayCount > displayDelay):
        print("{0}, {1}".format(changeCount, currentColor))
        displayCount = 0
    else:
        displayCount += 1
    #Delay for half a second and repeat.
    oldColor = currentColor
    time.sleep(0.001)
