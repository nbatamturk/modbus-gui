#!/bin/bash
# PyInstaller ile Modbus GUI (pymodbus.sync destekli) tek dosya halinde derleniyor
echo ">>> PyInstaller derleme başlatılıyor..."

pyinstaller --clean --onefile --noconsole \
--hidden-import pymodbus.client.sync \
--add-data "controller.py:." \
--add-data "window.ui:." \
--add-data "__init__.py:." \
modbus-gui.py

echo ">>> Derleme tamamlandı. Çıktı: ./dist/modbus-gui"
