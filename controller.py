import threading

from PyQt5.QtCore import qDebug
from pymodbus.client.sync import ModbusTcpClient
import argparse
import time


class Controller:
    def __init__(self):
        self._client = ModbusTcpClient()

    def connect(self, host: str, port: int, timeout: int):
        self._client.host = host
        self._client.port = port
        self._client.timeout = timeout
        result = self._client.connect()
        alive_thread = threading.Thread(target=self.start_alive, daemon=True)
        if not alive_thread.is_alive():
            alive_thread.start()
        return result

    def disconnect(self):
        self._client.close()

    def is_connected(self):
        return self._client.is_socket_open()

    def start_alive(self):
        while self._client.is_socket_open():
            self._client.write_register(6000, 1)
            time.sleep(1)

    def read_input(self, addr, length):
        result = self._client.read_input_registers(addr, length)
        if result is None:
            print(f"[ERROR] No response from address {addr}")
            return None
        if not hasattr(result, "registers"):
            print(f"[ERROR] Result at {addr} has no 'registers'")
            return None
        return result.registers


    def write(self, addr, data):
        self._client.write_register(addr, data)

    def read_holding(self, addr, length):
        result = self._client.read_holding_registers(addr, length)
        if result is None or not hasattr(result, "registers"):
            print(f"[ERROR] Failed to read holding registers from addr {addr}")
            return []
        return result.registers

