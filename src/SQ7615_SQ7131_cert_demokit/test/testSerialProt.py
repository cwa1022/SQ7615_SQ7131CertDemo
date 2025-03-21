import serial
import serial.tools.list_ports
import time

class SerialPortManager:

    def list_serial_ports():
        ports = serial.tools.list_ports.comports()
        for i, port in enumerate(ports):
            print(f"{i + 1}: {port.device} - {port.description}")
        return [port.device for port in ports]



    def open_serial(port_name, baudrate=115200):
        try:
            ser = serial.Serial(
                port=port_name,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            print(f"成功連接到 {port_name}")
            return ser
        except serial.SerialException as e:
            print(f"無法連接到 {port_name}：{e}")
            return None

    def main():
        ports = list_serial_ports()
        if not ports:
            print("找不到任何 Serial Port")
            return

        selected_port = ports[len(ports) - 1]
        print(f"\n嘗試連接 {selected_port}...\n")

        ser = open_serial(selected_port)
        if not ser:
            return

        try:
            test_data = "READ+CERTIFICATION=41,C8,00,00,00\r\n"
            ser.write(test_data.encode())
            print(f"已發送：{test_data.strip()}")

            buffer = ""
            start_found = False
            timeout = time.time() + 10  # 加長等 10 秒看看
            while time.time() < timeout:
                chunk = ser.read(1024).decode(errors='ignore')
                if chunk:
                    print(f"收到 chunk: {chunk}")
                    buffer += chunk
                    if not start_found and "#S#" in buffer:
                        start_found = True
                        buffer = buffer[buffer.find("#S#"):]  # 去掉前面雜訊
                    if "#E#" in buffer:
                        buffer = buffer[:buffer.find("#E#") + 3]
                        break
                else:
                    time.sleep(0.2)

            if "#S#" in buffer and "#E#" in buffer:
                print("✅ 完整接收一包資料：")
                print(buffer.strip())
            else:
                print("❌ 沒收到完整資料包")

        finally:
            ser.close()
            print("Serial Port 已關閉")

