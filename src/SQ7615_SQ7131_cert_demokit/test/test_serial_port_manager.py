import time
from serialPortManagement import SerialPortManager



def test_serial_manager():
    # 創建串口管理實例
    manager = SerialPortManager()

    # 根據可用串口創建所有串口實例
    manager.create_instances_from_ports()

    # 開啟所有串口
    manager.open_all_ports()
    time.sleep(1)

    # 逐個串口發送數據
    for port in manager.ports:
        manager.write_to_port(port, f"Hello from {port}!")
        time.sleep(1)

    # 逐個串口接收數據
    for port in manager.ports:
        data = manager.read_from_port(port, 100)
        print(f"從 {port} 接收到數據: {data}")

    # 關閉所有串口
    manager.close_all_ports()





def test_serial_manager_list_port():
    manager = SerialPortManager()

    ports = manager.list_ports()

    for port in ports:
        print(f"Device: {port.device}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print(f"Manufacturer: {port.manufacturer if port.manufacturer else 'Unknown'}")
        print(f"Product: {port.product if port.product else 'Unknown'}")
        print(f"Serial Number: {port.serial_number if port.serial_number else 'Unknown'}")
        print("=" * 50)


if __name__ == "__main__":
    # test_serial_manager()
    test_serial_manager_list_port()
