from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from lib.sniffing import getInterfaces
from workers.sniffing_worker import SniffingWorker

itemBuffer = []
maxItemsBeforeFlush = 20


class SniffingTab(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup
        self.setObjectName("SniffingTab")
        self.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(1000, 800))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 931, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_info = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.horizontalLayout.addWidget(self.label_info)
        self.comboBox_Interfaces = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_Interfaces.setObjectName("comboBox_Interfaces")
        self.horizontalLayout.addWidget(self.comboBox_Interfaces)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 740, 931, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_StartSniffing = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_StartSniffing.setObjectName("pushButton_StartSniffing")
        self.horizontalLayout_2.addWidget(self.pushButton_StartSniffing)
        self.pushButton_StopSniffing = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_StopSniffing.setObjectName("pushButton_StopSniffing")
        self.horizontalLayout_2.addWidget(self.pushButton_StopSniffing)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 90, 931, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_protocols = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_protocols.sizePolicy().hasHeightForWidth())
        self.label_protocols.setSizePolicy(sizePolicy)
        self.label_protocols.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_protocols.setFont(font)
        self.label_protocols.setObjectName("label_protocols")
        self.horizontalLayout_3.addWidget(self.label_protocols)
        self.radioButton_TCP = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_TCP.sizePolicy().hasHeightForWidth())
        self.radioButton_TCP.setSizePolicy(sizePolicy)
        self.radioButton_TCP.setCheckable(True)
        self.radioButton_TCP.setObjectName("radioButton_TCP")
        self.horizontalLayout_3.addWidget(self.radioButton_TCP)
        self.radioButton_UDP = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_UDP.sizePolicy().hasHeightForWidth())
        self.radioButton_UDP.setSizePolicy(sizePolicy)
        self.radioButton_UDP.setObjectName("radioButton_UDP")
        self.horizontalLayout_3.addWidget(self.radioButton_UDP)
        self.radioButton_Both = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_Both.setChecked(True)
        self.radioButton_Both.setObjectName("radioButton_Both")
        self.horizontalLayout_3.addWidget(self.radioButton_Both)

        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 931, 591))
        self.listWidget.setObjectName("listWidget")

        # Retranslate
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SniffingTab", "Form"))
        self.label_info.setText(_translate("SniffingTab", "Choose interface"))
        self.pushButton_StartSniffing.setText(_translate("SniffingTab", "Start sniffing"))
        self.pushButton_StopSniffing.setText(_translate("SniffingTab", "Stop Sniffing"))
        self.label_protocols.setText(_translate("SniffingTab", "Protocol settings"))
        self.radioButton_TCP.setText(_translate("SniffingTab", "TCP"))
        self.radioButton_UDP.setText(_translate("SniffingTab", "UDP"))
        self.radioButton_Both.setText(_translate("SniffingTab", "Both"))

        # Post initialization
        self.Label = QLabel("Scanning")
        self.Layout = QGridLayout()
        self.setLayout(self.Layout)

        self.fillInterfaces(getInterfaces())
        self.startSniffingAllPackets()

    # Vullen van interfaces in de GUI
    def fillInterfaces(self, interfaces):
        self.comboBox_Interfaces.clear()
        self.comboBox_Interfaces.addItems(interfaces)

    def handle_scan_start(self):
        worker = SniffingWorker(self.comboBox_Interfaces.currentText())
        worker.signals.result.connect(self.handlePacket)
        QThreadPool.globalInstance().start(worker)

    def handlePacket(self, packet):
        # Creating item chunks before adding item to widget
        if len(itemBuffer) < maxItemsBeforeFlush:
            itemBuffer.append(packet)
        else:
            # If buffer is full:
            self.listWidget.addItems(itemBuffer)
            self.listWidget.scrollToBottom()
            itemBuffer.clear()

    # Button on click event
    # Triggers wrapper function above
    def startSniffingAllPackets(self):
        self.pushButton_StartSniffing.clicked.connect(self.handle_scan_start)

    def stopSniffingAllPackets(self):
        self.pushButton_StopSniffing.clicked.connect()
