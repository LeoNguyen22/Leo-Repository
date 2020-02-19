# Simple demo of using the Adafruit TCS34725 color sensor to read values.
# Will detect the color from the sensor and print it out every second.
import time

import board
import busio

import adafruit_tcs34725


# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# Main loop reading color and printing it every second.
while True:

    #The lux is a measure of the brightness read by the color sensor.
    lux = sensor.lux

    #These lines read the color measured by the red, blue, and green channels.
    #The values range from 0 - 255.

    red_value = sensor.color_rgb_bytes[0]
    green_value = sensor.color_rgb_bytes[1]
    blue_value = sensor.color_rgb_bytes[2]

    #print('Color: ({0}, {1}, {2})'.format(red_value, green_value, blue_value))
    if(red_value > 70):
        print("RED")
    elif(green_value > 22):
        print("GREEN")
    elif(blue_value <= 11 and blue_value >= 9):
        print("CYAN")
    elif(red_value <= 40 and green_value <= 22):
        print("YELLOW")

    #print('Lux: {0}'.format(sensor.lux))

    # Delay for half a second and repeat.
    time.sleep(0.1)
