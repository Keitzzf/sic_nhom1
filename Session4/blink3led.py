from gpiozero import LED
from time import sleep

red = LED(17)
amber = LED(13)
green = LED(19)

green.on()
amber.off()
red.off()

while True:
    sleep(3)
    green.off()
    amber.on()
    sleep(3)
    amber.off()
    red.on()
    sleep(3)
    red.off()
    amber.on()
    sleep(3)