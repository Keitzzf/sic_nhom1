import time
import board
import adafruit_dht
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Cảm biến DHT11 nối vào GPIO18
dhtDevice = adafruit_dht.DHT11(board.D18)

# Cấu hình đồ thị
fig, ax = plt.subplots()
ax.set_xlim(0, 30)
ax.set_ylim(0, 100)
ax.set_title("Biểu đồ nhiệt độ và độ ẩm từ DHT11")
ax.set_xlabel("Lần đo")
ax.set_ylabel("Giá trị")
ax.grid(True)

# Dữ liệu ban đầu
max_points = 30
x_data = np.arange(max_points)
temp_data = np.ones(max_points) * np.nan
humi_data = np.ones(max_points) * np.nan

# Hai đường biểu diễn: nhiệt độ và độ ẩm
temp_line, = ax.plot(x_data, temp_data, lw=2, c='blue', marker='o', label='Nhiệt độ (°C)')
humi_line, = ax.plot(x_data, humi_data, lw=2, c='orange', marker='s', label='Độ ẩm (%)')

# Hiển thị chú thích
ax.legend(loc='upper right')

def init():
    return temp_line, humi_line

def animate(i):
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if temperature is not None and humidity is not None:
            # Cập nhật dữ liệu nhiệt độ
            old_temp = temp_line.get_ydata()
            new_temp = np.r_[old_temp[1:], temperature]
            temp_line.set_ydata(new_temp)

            # Cập nhật dữ liệu độ ẩm
            old_humi = humi_line.get_ydata()
            new_humi = np.r_[old_humi[1:], humidity]
            humi_line.set_ydata(new_humi)

            print(f"Nhiệt độ: {temperature}°C - Độ ẩm: {humidity}%")

    except RuntimeError as error:
        print(f"Lỗi đọc cảm biến: {error}")
    return temp_line, humi_line

# Khởi tạo animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=200, interval=2000, blit=False
)

plt.tight_layout()
plt.show()
