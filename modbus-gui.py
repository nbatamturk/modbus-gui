#!/usr/bin/env python3
import sys
import threading
import time
from abc import ABC
from enum import Enum

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, qDebug

from controller import Controller


class DataType(Enum):
    UINT16 = "uint16"
    UINT32 = "uint32"
    STRING = "string"


class RegisterType(Enum):
    INPUT = "R"
    HOLDING = "R/W"


class Register(ABC):
    def __init__(self):
        self.addr = 0
        self.nb = 0
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class SerialNumberRegister(Register):
    def __init__(self):
        self.addr = 100
        self.nb = 25
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class ChargepointIDRegister(Register):
    def __init__(self):
        self.addr = 130
        self.nb = 50
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class BrandRegister(Register):
    def __init__(self):
        self.addr = 190
        self.nb = 10
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class ModelRegister(Register):
    def __init__(self):
        self.addr = 210
        self.nb = 5
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class FirmwareVersionRegister(Register):
    def __init__(self):
        self.addr = 230
        self.nb = 50
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.STRING


class DateRegister(Register):
    def __init__(self):
        self.addr = 290
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class TimeRegister(Register):
    def __init__(self):
        self.addr = 294
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class ChargepointPowerRegister(Register):
    def __init__(self):
        self.addr = 400
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class NumberOfPhasesRegister(Register):
    def __init__(self):
        self.addr = 404
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class ChargepointStateRegister(Register):
    def __init__(self):
        self.addr = 1000
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class ChargingStateRegister(Register):
    def __init__(self):
        self.addr = 1001
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class EquipmentStateRegister(Register):
    def __init__(self):
        self.addr = 1002
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class CableStateRegister(Register):
    def __init__(self):
        self.addr = 1004
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class EvseFaultCodeRegister(Register):
    def __init__(self):
        self.addr = 1006
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class CurrentL1Register(Register):
    def __init__(self):
        self.addr = 1008
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class CurrentL2Register(Register):
    def __init__(self):
        self.addr = 1010
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class CurrentL3Register(Register):
    def __init__(self):
        self.addr = 1012
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class VoltageL1Register(Register):
    def __init__(self):
        self.addr = 1014
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class VoltageL2Register(Register):
    def __init__(self):
        self.addr = 1016
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class VoltageL3Register(Register):
    def __init__(self):
        self.addr = 1018
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class ActivePowerTotalRegister(Register):
    def __init__(self):
        self.addr = 1020
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class ActivePowerL1Register(Register):
    def __init__(self):
        self.addr = 1024
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class ActivePowerL2Register(Register):
    def __init__(self):
        self.addr = 1028
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class ActivePowerL3Register(Register):
    def __init__(self):
        self.addr = 1032
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class MeterReadingRegister(Register):
    def __init__(self):
        self.addr = 1036
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class SessionMaxCurrentRegister(Register):
    def __init__(self):
        self.addr = 1100
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class EvseMinCurrentRegister(Register):
    def __init__(self):
        self.addr = 1102
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class EvseMaxCurrentRegister(Register):
    def __init__(self):
        self.addr = 1104
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class CableMaxCurrentRegister(Register):
    def __init__(self):
        self.addr = 1106
        self.nb = 1
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT16


class SessionEnergyRegister(Register):
    def __init__(self):
        self.addr = 1502
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class SessionStartTimeRegister(Register):
    def __init__(self):
        self.addr = 1504
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class SessionDurationRegister(Register):
    def __init__(self):
        self.addr = 1508
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class SessionEndTimeRegister(Register):
    def __init__(self):
        self.addr = 1512
        self.nb = 2
        self.reg_type = RegisterType.INPUT
        self.data_type = DataType.UINT32


class FailsafeCurrentRegister(Register):
    def __init__(self):
        self.addr = 2000
        self.nb = 1
        self.reg_type = RegisterType.HOLDING
        self.data_type = DataType.UINT16


class FailsafeTimeoutRegister(Register):
    def __init__(self):
        self.addr = 2002
        self.nb = 1
        self.reg_type = RegisterType.HOLDING
        self.data_type = DataType.UINT16


class ChargingCurrentRegister(Register):
    def __init__(self):
        self.addr = 5004
        self.nb = 1
        self.reg_type = RegisterType.HOLDING
        self.data_type = DataType.UINT16


class AliveRegister(Register):
    def __init__(self):
        self.addr = 6000
        self.nb = 1
        self.reg_type = RegisterType.HOLDING
        self.data_type = DataType.UINT16


registers = {
    "Serial Number": SerialNumberRegister,
    "Chargepoint ID": ChargepointIDRegister,
    "Brand": BrandRegister,
    "Model": ModelRegister,
    "Firmware Version": FirmwareVersionRegister,
    "Date": DateRegister,
    "Time": TimeRegister,
    "Chargepoint Power": ChargepointPowerRegister,
    "Number of Phases": NumberOfPhasesRegister,
    "Chargepoint State": ChargepointStateRegister,
    "Charging State": ChargingStateRegister,
    "Equipment State": EquipmentStateRegister,
    "Cable State": CableStateRegister,
    "EVSE Fault Code": EvseFaultCodeRegister,
    "Current L1": CurrentL1Register,
    "Current L2": CurrentL2Register,
    "Current L3": CurrentL3Register,
    "Voltage L1": VoltageL1Register,
    "Voltage L2": VoltageL2Register,
    "Voltage L3": VoltageL3Register,
    "Active Power Total": ActivePowerTotalRegister,
    "Active Power L1": ActivePowerL1Register,
    "Active Power L2": ActivePowerL2Register,
    "Active Power L3": ActivePowerL3Register,
    "Meter Reading": MeterReadingRegister,
    "Session Max Current": SessionMaxCurrentRegister,
    "EVSE Min Current": EvseMinCurrentRegister,
    "EVSE Max Current": EvseMaxCurrentRegister,
    "Cable Max Current": CableMaxCurrentRegister,
    "Session Energy": SessionEnergyRegister,
    "Session Start Time": SessionStartTimeRegister,
    "Session End Time": SessionEndTimeRegister,
    "Failsafe Current": FailsafeCurrentRegister,
    "Failsafe Timeout": FailsafeTimeoutRegister,
    "Charging Current": ChargingCurrentRegister,
    "Alive Register": AliveRegister
}


def convert_to(data_type, read_data):
    if data_type == DataType.UINT16:
        text = " ".join(str(x) for x in read_data)
    elif data_type == DataType.UINT32:
        result = 0
        multiplier = 0
        read_data.reverse()
        for chunk in read_data:
            result += int(chunk) * (2 ** multiplier)
            multiplier += 16
        text = str(result)
    elif data_type == DataType.STRING:
        text = "".join(chr(x) for x in read_data)
    return text


class Ui_MainWindow(QObject):
    def __init__(self):
        super().__init__()
        self.c = Controller()
        self.is_reading = False

    def setupUi(self, MainWindow):
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 255)

        # Tab Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")

        #  Connect Tab
        self.tab_connect = QtWidgets.QWidget()
        self.tab_connect.setObjectName("tab_connect")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_connect)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_connect)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.host_edit = QtWidgets.QLineEdit(self.widget_2)
        self.host_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.host_edit.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.host_edit, 0, 4, 1, 1)
        self.port_edit = QtWidgets.QLineEdit(self.widget_2)
        self.port_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.port_edit.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.port_edit, 1, 4, 1, 1)
        self.timeout_edit = QtWidgets.QLineEdit(self.widget_2)
        self.timeout_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeout_edit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.timeout_edit, 3, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.tab_connect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: green")
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.clicked.connect(self.connect_clicked)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.tab_connect, "")

        # Read Tab
        self.tab_read = QtWidgets.QWidget()
        self.tab_read.setEnabled(False)
        self.tab_read.setObjectName("tab_read")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_read)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_read)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.widget_6 = QtWidgets.QWidget(self.tab_read)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_5.addWidget(self.lineEdit_19)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_read)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.read_clicked)
        self.pushButton_6.setStyleSheet("background-color: green")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tab_read, "")

        # Write Tab
        self.tab_write = QtWidgets.QWidget()
        self.tab_write.setEnabled(False)
        self.tab_write.setObjectName("tab_write")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_write)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_write)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_3)
        self.widget_9 = QtWidgets.QWidget(self.tab_write)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_7.addWidget(self.lineEdit_21)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_write)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.write_clicked)
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.tabWidget.addTab(self.tab_write, "")


        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setFixedSize(MainWindow.size())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVC04 ModbusTCP GUI"))

        # Connect Tab
        self.label_4.setText(_translate("MainWindow", "Timeout"))
        self.label.setText(_translate("MainWindow", "Host Address"))
        self.label_2.setText(_translate("MainWindow", "Port Number"))
        self.host_edit.setText(_translate("MainWindow", "127.0.0.1"))
        self.port_edit.setText(_translate("MainWindow", "502"))
        self.timeout_edit.setText(_translate("MainWindow", "10"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_connect), _translate("MainWindow", "Connect"))

        # Read Tab
        self.comboBox.setItemText(0, _translate("MainWindow", "Serial Number"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Chargepoint ID"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Brand"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Model"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Firmware Version"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Date"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Time"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Chargepoint Power"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Number of Phases"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Chargepoint State"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Charging State"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Equipment State"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Cable State"))
        self.comboBox.setItemText(13, _translate("MainWindow", "EVSE Fault Code"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Current L1"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Current L2"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Current L3"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Voltage L1"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Voltage L2"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Voltage L3"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Active Power Total"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Active Power L1"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Active Power L2"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Active Power L3"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Meter Reading"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Session Max Current"))
        self.comboBox.setItemText(26, _translate("MainWindow", "EVSE Min Current"))
        self.comboBox.setItemText(27, _translate("MainWindow", "EVSE Max Current"))
        self.comboBox.setItemText(28, _translate("MainWindow", "Cable Max Current"))
        self.comboBox.setItemText(29, _translate("MainWindow", "Session Energy"))
        self.comboBox.setItemText(30, _translate("MainWindow", "Session Start Time"))
        self.comboBox.setItemText(31, _translate("MainWindow", "Session End Time"))
        self.comboBox.setItemText(32, _translate("MainWindow", "Failsafe Current"))
        self.comboBox.setItemText(33, _translate("MainWindow", "Failsafe Timeout"))
        self.comboBox.setItemText(34, _translate("MainWindow", "Charging Current"))
        self.comboBox.setItemText(35, _translate("MainWindow", "Alive Register"))
        self.lineEdit_19.setPlaceholderText(_translate("MainWindow", "Data"))
        self.pushButton_6.setText(_translate("MainWindow", "Start"))
        self.pushButton_6.setShortcut(_translate("MainWindow", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_read), _translate("MainWindow", "Read"))

        # Write Tab
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Failsafe Current"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Failsafe Timeout"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Charging Current"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Alive Register"))
        self.lineEdit_21.setPlaceholderText(_translate("MainWindow", "Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Write"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_write), _translate("MainWindow", "Write"))

    def get_register(self, text):
        return registers.get(text)()

    def connect_clicked(self):
        if self.c.is_connected():
            self.c.disconnect()
            self.pushButton_2.setText("Connect")
            self.pushButton_2.setStyleSheet("background-color: green")
            self.host_edit.setEnabled(True)
            self.port_edit.setEnabled(True)
            self.timeout_edit.setEnabled(True)
            self.tab_read.setEnabled(False)
            self.tab_write.setEnabled(False)
            self.lineEdit_19.clear()
            self.is_reading = False
            self.pushButton_6.setText("Start")
            self.pushButton_6.setStyleSheet("background-color: green")
        else:
            if self.c.connect(self.host_edit.text(), int(self.port_edit.text()), int(self.timeout_edit.text())):
                self.pushButton_2.setText("Disconnect")
                self.pushButton_2.setStyleSheet("background-color: red")
                self.host_edit.setEnabled(False)
                self.port_edit.setEnabled(False)
                self.timeout_edit.setEnabled(False)
                self.tab_read.setEnabled(True)
                self.tab_write.setEnabled(True)

    def read_clicked(self):
        if self.is_reading:
            self.is_reading = False
            self.pushButton_6.setText("Start")
            self.pushButton_6.setStyleSheet("background-color: green")
        else:
            self.is_reading = True
            self.pushButton_6.setText("Stop")
            self.pushButton_6.setStyleSheet("background-color: red")
            read_thread = threading.Thread(target=self.read_func, daemon=True)
            read_thread.start()

    def write_clicked(self):
        if self.c.is_connected():
            self.write_register(self.get_register(self.comboBox_3.currentText()), int(self.lineEdit_21.text()))

    def read_func(self):
        try:
            while self.is_reading and self.c.is_connected():
                reg = self.get_register(self.comboBox.currentText())
                text = self.read_register(reg)
                self.lineEdit_19.setText(text)
                time.sleep(0.25)
        except Exception as e:
            qDebug(str(e))

    def read_register(self, reg: Register):
        text = ""
        if reg.reg_type == RegisterType.INPUT:
            read_data = self.c.read_input(reg.addr, reg.nb)
        else:
            read_data = self.c.read_holding(reg.addr, reg.nb)
        if read_data:
            text = convert_to(reg.data_type, read_data)
        return text

    def write_register(self, reg: Register, data):
        if reg.data_type == DataType.UINT16:
            self.c.write(reg.addr, data)
        else:
            #TODO
            pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
