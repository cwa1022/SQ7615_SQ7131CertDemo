from .SerialPort import SerialPort
import serial.tools.list_ports

class SerialPortManager:
    def __init__(self):
        self.ports = {}

    def create_port_instance(self, port):
        """Create Port instance"""
        if port not in self.ports:
            self.ports[port] = SerialPort(port)
            print(f"Create {port} Port Instance")
        else:
            print(f"{port} Port Instance already exsisted")

    def open_all_ports(self):
        """Open all Port Instance"""
        for port, serial_port in self.ports.items():
            serial_port.open()

    def close_all_ports(self):
        """Close all Port Instance"""
        for port, serial_port in self.ports.items():
            serial_port.close()

    def write_to_port(self, port, data):
        """write to particular port"""
        if port in self.ports:
            self.ports[port].write(data)
        else:
            print(f"Port {port} has not been created")

    def read_from_port(self, port, size=100):
        """read data from particular port"""
        if port in self.ports:
            return self.ports[port].read(size)
        else:
            print(f"Port {port} has not been created")
            return None

    def list_ports(self):
        """list all useable port"""
        return serial.tools.list_ports.comports()

    def create_instances_from_ports(self):
        """Create instance from all available port"""
        available_ports = self.list_ports()
        for port in available_ports:
            self.create_port_instance(port.device)
