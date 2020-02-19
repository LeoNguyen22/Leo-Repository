# Starter code for figuring out what color the sensor is seeing from the color wheel.
# The readColor function doesn't work yet. That's your job.

import time
import board
import busio
import adafruit_tcs34725

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

def readColor(red, green, blue):

    returnValue = "UNKNOWN"

    if(red_value > 70):
        returnValue = "RED"
    elif(green_value > 22):
        returnValue = "GREEN"
    elif(blue_value <= 11 and blue_value >= 9):
        returnValue = "CYAN"
    elif(red_value <= 40 and green_value <= 22):
        returnValue = "YELLOW"

    return returnValue

while True:

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

    print('Color: ({0}, {1}, {2})'.format(red_value_scaled, green_value_scaled, blue_value_scaled))
    print(readColor(red_value_scaled, green_value_scaled, blue_value_scaled))
    #print('Lux: {0}'.format(sensor.lux))

    #Delay for half a second and repeat.
    time.sleep(0.5)
