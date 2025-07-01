from gpiozero import LED,DistanceSensor
import time

sensor = DistanceSensor(echo = 13, trigger = 19)
led = LED(17)

while True:
    distance = sensor.distance*100 # don vi la met, *100 de doi sang cm
    print("distance: ",distance)
    if distance<10:
        led.on()
    else:
        led.off()
    time.sleep(0.5)