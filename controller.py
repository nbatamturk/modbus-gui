import threading

from PyQt5.QtCore import qDebug
from pyModbusTCP.client import ModbusClient
import argparse
import time


class Controller:
    def __init__(self):
        self._client = ModbusClient()

    def connect(self, host, port, unit_id, timeout):
        self._client.host(host)
        self._client.port(port)
        self._client.unit_id(unit_id)
        self._client.timeout(timeout)
        result = self._client.open()
        alive_thread = threading.Thread(target=self.start_alive, daemon=True)
        if not alive_thread.isAlive():
            alive_thread.start()
        return result

    def disconnect(self):
        return self._client.close()

    def is_connected(self):
        return self._client.is_open()

    def start_alive(self):
        while self._client.is_open():
            a = self._client.write_single_register(6000, 1)
            time.sleep(1)

    def read_input(self, addr, length):
        return self._client.read_input_registers(addr, length)

    def read_holding(self, addr, length):
        return self._client.read_holding_registers(addr, length)
