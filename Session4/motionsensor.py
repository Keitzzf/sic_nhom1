from gpiozero import MotionSensor
import time

pir = MotionSensor(17)
print("Waiting for PIR to settle")
pir.wait_for_inactive()
while True:
    print("Ready")
    pir.wait_for_active()
    print("Motion detected!")
    time.sleep(1)