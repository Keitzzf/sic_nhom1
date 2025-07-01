from gpiozero import LED
from time import sleep

led = {
    "Green" : LED(5),
    "Red"   : LED(6),
    "White" : LED(13)
}

# while True:
#     for i in led:
#         print(i)
#         led[i].on()
#         sleep(1)
#         led[i].off()
#         sleep(1)
while True:
    led["Green"].on()
    led["Red"].on()
    led["White"].on()

