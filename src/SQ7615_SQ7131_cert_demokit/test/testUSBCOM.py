import serial
import sys

if sys.platform == "win32":
    port = "COM3"  
elif sys.platform == "linux":
    port = "/dev/ttyUSB0"  
else:
    raise Exception("Unsupported OS")


ser = serial.Serial(port, 115200, timeout=1)

ser.write(b'Hello MCU!\n')

response = ser.readline().decode('utf-8').strip()
print(f'MCU Response: {response}')

ser.close()
