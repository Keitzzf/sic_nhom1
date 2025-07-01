import sys
import time
import board
import adafruit_dht
import pymysql

# C?m bi?n DHT11 k?t n?i GPIO2
sensor = adafruit_dht.DHT11(board.D18)

# K?t n?i co s? d? li?u
db, cur = None, None
try:
    db = pymysql.connect(
        host='192.168.1.10',
        user='root',
        password='1234',
        db='mysql',
        charset='utf8'
    )
    cur = db.cursor()

    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            data = (temperature, humidity)

            if humidity is not None and temperature is not None:
                sql = "INSERT INTO temperature(temp, humid) VALUES (%s, %s)"
                print(sql % data)
                cur.execute(sql, data)
                db.commit()
            else:
                print("Failed to get reading. Try again!")

            time.sleep(5)

        except RuntimeError as e:
            print("L?i c?m bi?n:", e)

except KeyboardInterrupt:
    print("D?ng chuong tr�nh.")

finally:
    if db:
        db.close()
