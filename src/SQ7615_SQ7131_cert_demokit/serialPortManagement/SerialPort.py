import serial

class SerialPort:
    def __init__(self, port, baudrate=9600, timeout=1, bytesize=8, parity='N', stopbits=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.ser = None

    def open(self):
        """開啟串口"""
        if self.ser is None:
            try:
                self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout,
                                         bytesize=self.bytesize, parity=self.parity, stopbits=self.stopbits)
                if self.ser.is_open:
                    print(f"串口 {self.port} 開啟成功")
            except serial.SerialException as e:
                print(f"開啟串口 {self.port} 失敗: {e}")

    def close(self):
        """關閉串口"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.port} 已關閉")
        else:
            print(f"串口 {self.port} 未開啟")

    def write(self, data):
        """發送數據"""
        if self.ser and self.ser.is_open:
            if isinstance(data, str):
                data = data.encode()  # 如果是字符串，轉換為 bytes
            self.ser.write(data)
        else:
            print(f"串口 {self.port} 未開啟，無法發送數據")

    def read(self, size=100):
        """接收數據"""
        if self.ser and self.ser.is_open:
            data = self.ser.read(size)
            return data
        else:
            print(f"串口 {self.port} 未開啟，無法接收數據")
            return None

    def readline(self):
        """接收一行數據"""
        if self.ser and self.ser.is_open:
            return self.ser.readline()
        else:
            print(f"串口 {self.port} 未開啟，無法接收數據")
            return None
