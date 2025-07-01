from gpiozero import MCP3008, DistanceSensor
from time import sleep
from datetime import datetime

pot = MCP3008(channel=7)
ultrasonic = DistanceSensor(trigger=21,echo=20)
file = open("distance_log.txt","w")

while True:
    dist = ultrasonic.distance * 100
    span = pot.value * 100
    dist = round(dist, 3)
    span = round(span, 3)
    if dist <= span:
        print(f"scaled span : {span}, dist : {dist}")
        timestamp = datetime.now().strftime('%d/%m/%Y %HH %MM %SS')
        data = f"{timestamp} --> " \
        f"distance : {dist} , span : {span}\n"
        file.write(data)
    else:
        print(f"Dist > span!! scaled span : {span}, dist : {dist}")
    sleep(1)
file.close()