from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime


led = {
   "Green" : LED(5),
   "Red"   : LED(6),
   "White" : LED(13)
   }

file = open("cpu_usage_log.txt","w")

while True:
   cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
   cpu_usage_mean = sum([i/len(cpu_usage) for i in cpu_usage])
   cpu_usage_mean = round(cpu_usage_mean,3)
   print(f"cpu usage(%) : {cpu_usage_mean}%")
   if 60 > cpu_usage_mean > 30:
      led["White"].on()
      led["Green"].off()
      led["Red"].off()
   elif cpu_usage_mean >= 60:
      led["Red"].on()
      led["Green"].off()
      led["White"].off()
   else:
      led["White"].on()
      led["Green"].off()
      led["Red"].off()
   data = f"{datetime.now().strftime('%d/%m/%Y %HH %MM %SS')} " \
   f"cpu usage(%) : {cpu_usage_mean}%\n"
   file.write(data)
   sleep(1)
file.close()