from gpiozero import MCP3008, DistanceSensor
from time import sleep
from datetime import datetime

# Khởi tạo cảm biến
pot = MCP3008(channel=7)
ultrasonic = DistanceSensor(trigger=21, echo=20)

try:
    with open("distance_log.txt", "w") as file:
        while True:
            dist = ultrasonic.distance * 100  # m -> cm
            span = pot.value * 100            # scale 0.0–1.0 to 0–100
            dist = round(dist, 3)
            span = round(span, 3)

            if dist <= span:
                print(f"scaled span : {span}, dist : {dist}")
                timestamp = datetime.now().strftime('%d/%m/%Y %Hh %Mm %Ss')
                data = f"{timestamp} --> distance : {dist} cm , span : {span}\n"
                file.write(data)
                file.flush()  # Đảm bảo ghi ngay ra file
            else:
                print(f"Dist > span!! scaled span : {span}, dist : {dist}")

            sleep(1)

except KeyboardInterrupt:
    print("\n[INFO] Program stopped by user.")
