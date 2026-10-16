from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import socket


host = socket.gethostname()
PC_IP = socket.gethostbyname(host)

        
class CameraViewer(QMainWindow):
    def __init__(self, cam1, cam2, parent=None):
        super(CameraViewer, self).__init__(parent, QtCore.Qt.Window)
        self.cam1 = cam1
        self.cam2 = cam2
        self.rtsp_url = ["rtsp://10.42.0.1:8554/cam", 
                        "rtsp://10.42.0.1:8554/cam2", 
                        "rtsp://10.42.0.1:8554/cam3", 
                        "rtsp://10.42.0.1:8554/cam4"]
        self.resize(800, 600)
        self.setup()
        
        
    def setup(self):
        # For one camera
        if self.cam2 == None:
            self.media_player = QMediaPlayer(self)
            self.video_widget = QVideoWidget()

            central_widget = QWidget()
            central_layout = QVBoxLayout(central_widget)
            central_layout.addWidget(self.video_widget)

            self.setCentralWidget(central_widget)
            self.media_player.setVideoOutput(self.video_widget)
            
            cam_string = [str(self.cam1-1), ''][self.cam1<2]
            
            self.media_player.setMedia(QMediaContent(QUrl('rtsp://192.168.2.100:8554/cam' + cam_string)))
            
            self.setWindowTitle("RTSP Camera Viewer, Cam Stream:" + str(self.cam1))

            self.media_player.play()
            
            print(str(self.cam1) + ' is running')

            def closeEvent(self, event):
                self.media_player.stop()
                event.accept()
                print('stopped')
        #Two cameras. Feel like the above function may not work properly
        else:
        
            self.media_players = []
            self.video_widgets = []

            # Creates 2 media player windows 
            self.media_players.append(QMediaPlayer(self))
            self.video_widgets.append(QVideoWidget())
            self.media_players.append(QMediaPlayer(self))
            self.video_widgets.append(QVideoWidget())

            central_widget = QWidget()
            central_layout = QVBoxLayout(central_widget)

            for video_widget in self.video_widgets:
                central_layout.addWidget(video_widget)
                

            self.setCentralWidget(central_widget)

            for i, media_player in enumerate(self.media_players):
                video_widget = self.video_widgets[i]
                media_player.setVideoOutput(video_widget)
                
            
            # Don't know if this would work properly. May have to put it into the above loop    
            media_player.setMedia(QMediaContent(QUrl(self.rtsp_url[self.cam1-1])))
            media_player.setMedia(QMediaContent(QUrl(self.rtsp_url[self.cam2-1])))
            
            self.setWindowTitle("RTSP Camera Viewer, Cam Streams:" + str(self.cam1)+ ' ' + str(self.cam2))
            
            media_player.play()

            def closeEvent(self, event):
                for media_player in self.media_players:
                    media_player.stop()
                event.accept()


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        
        self.setObjectName("MainWindow")
        self.resize(448, 620)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")       
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.setStyleSheet("background-color: pink;")
        
        #Camera
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.Cam1 = QtWidgets.QPushButton(self.groupBox_4)
        self.Cam1.setObjectName("Cam1")
        self.gridLayout.addWidget(self.Cam1, 0, 0, 1, 1)
        self.Cam4 = QtWidgets.QPushButton(self.groupBox_4)
        self.Cam4.setObjectName("Cam4")
        self.gridLayout.addWidget(self.Cam4, 1, 1, 1, 1)
        self.Cam3 = QtWidgets.QPushButton(self.groupBox_4)
        self.Cam3.setObjectName("Cam3")
        self.gridLayout.addWidget(self.Cam3, 1, 0, 1, 1)
        self.Cam2 = QtWidgets.QPushButton(self.groupBox_4)
        self.Cam2.setObjectName("Cam2")
        self.gridLayout.addWidget(self.Cam2, 0, 1, 1, 1)
        
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)

        
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Cam1_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam1_3.setObjectName("Cam1_3")
        self.gridLayout_3.addWidget(self.Cam1_3, 0, 1, 1, 1)
        self.Cam1_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam1_4.setObjectName("Cam1_4")
        self.gridLayout_3.addWidget(self.Cam1_4, 0, 2, 1, 1)
        self.Cam2_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam2_4.setObjectName("Cam2_4")
        self.gridLayout_3.addWidget(self.Cam2_4, 1, 1, 1, 1)
        self.Cam2_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam2_3.setObjectName("Cam2_3")
        self.gridLayout_3.addWidget(self.Cam2_3, 1, 0, 1, 1)
        self.Cam3_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam3_4.setObjectName("Cam3_4")
        self.gridLayout_3.addWidget(self.Cam3_4, 1, 2, 1, 1)
        self.Cam1_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.Cam1_2.setObjectName("Cam1_2")
        self.gridLayout_3.addWidget(self.Cam1_2, 0, 0, 1, 1)
        
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 1, 1, 1)

        
        #Functions box
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.func_4 = QtWidgets.QPushButton(self.groupBox)
        self.func_4.setObjectName("func_4")
        self.gridLayout_5.addWidget(self.func_4, 2, 1, 1, 1)
        self.func_2 = QtWidgets.QPushButton(self.groupBox)
        self.func_2.setObjectName("func_2")
        self.gridLayout_5.addWidget(self.func_2, 0, 1, 1, 1)
        self.func_1 = QtWidgets.QPushButton(self.groupBox)
        self.func_1.setObjectName("func_1")
        self.gridLayout_5.addWidget(self.func_1, 1, 1, 1, 1)
        self.func_3 = QtWidgets.QPushButton(self.groupBox)
        self.func_3.setObjectName("func_3")
        self.gridLayout_5.addWidget(self.func_3, 1, 2, 1, 1)
        self.func_5 = QtWidgets.QPushButton(self.groupBox)
        self.func_5.setObjectName("func_5")
        self.gridLayout_5.addWidget(self.func_5, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 2)
        
        #Pi Stuff
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QtCore.QRect(40, 260, 800, 500))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comp_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.comp_ip.setEnabled(False)
        self.comp_ip.setText(PC_IP)
        self.comp_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_ip.setObjectName("comp_ip")
        self.gridLayout_2.addWidget(self.comp_ip, 9, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 4)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.internal_temp_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.internal_temp_2.setEnabled(False)
        self.internal_temp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.internal_temp_2.setObjectName("internal_temp_2")
        self.gridLayout_2.addWidget(self.internal_temp_2, 3, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 4)
        self.pi_temp = QtWidgets.QLineEdit(self.groupBox_2)
        self.pi_temp.setEnabled(False)
        self.pi_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.pi_temp.setObjectName("pi_temp")
        self.gridLayout_2.addWidget(self.pi_temp, 5, 0, 1, 4)
        self.rpi_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.rpi_ip.setEnabled(False)
        self.rpi_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.rpi_ip.setObjectName("rpi_ip")
        self.gridLayout_2.addWidget(self.rpi_ip, 7, 0, 1, 4)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 2)
        self.internal_temp = QtWidgets.QLineEdit(self.groupBox_2)
        self.internal_temp.setEnabled(False)
        self.internal_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.internal_temp.setObjectName("internal_temp")
        self.gridLayout_2.addWidget(self.internal_temp, 3, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 2)
        
        
        self.setCentralWidget(self.centralwidget)
        
        # Naming the things

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "RoboticsGUI"))
        self.setStatusTip(_translate("MainWindow", "Running"))
        self.Cam1.setText(_translate("MainWindow", "Cam1"))
        self.Cam4.setText(_translate("MainWindow", "Cam4"))
        self.Cam3.setText(_translate("MainWindow", "Cam3"))
        self.Cam2.setText(_translate("MainWindow", "Cam2"))
        self.Cam1_3.setText(_translate("MainWindow", "Cam 1+3"))
        self.Cam1_4.setText(_translate("MainWindow", "Cam 1+4"))
        self.Cam2_4.setText(_translate("MainWindow", "Cam 2+4"))
        self.Cam2_3.setText(_translate("MainWindow", "Cam 2+3"))
        self.Cam3_4.setText(_translate("MainWindow", "Cam 3+4"))
        self.Cam1_2.setText(_translate("MainWindow", "Cam 1+2"))
        self.groupBox.setTitle(_translate("MainWindow", "Buttons"))
        self.func_4.setText(_translate("MainWindow", "func_4"))
        self.func_2.setText(_translate("MainWindow", "func_2"))
        self.func_1.setText(_translate("MainWindow", "func_1"))
        self.func_3.setText(_translate("MainWindow", "func_3"))
        self.func_5.setText(_translate("MainWindow", "func_5"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Pi Stuff"))
        self.label_6.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Internal Temp (C)"))
        self.lineEdit_3.setText(_translate("MainWindow", "0.0"))
        self.label_5.setText(_translate("MainWindow", "Computer IP Address"))
        self.label_3.setText(_translate("MainWindow", "PI CPU Temp (C)"))
        self.lineEdit.setText(_translate("MainWindow", "0.0"))
        self.lineEdit_2.setText(_translate("MainWindow", "0.0"))
        self.internal_temp_2.setText(_translate("MainWindow", "0.0"))
        self.label_4.setText(_translate("MainWindow", "RPI IP Address"))
        self.pi_temp.setText(_translate("MainWindow", "0.0"))
        self.rpi_ip.setText(_translate("MainWindow", "x.x.x.x"))
        self.label_8.setText(_translate("MainWindow", "Y"))
        self.label_9.setText(_translate("MainWindow", "Humidity"))
        self.internal_temp.setText(_translate("MainWindow", "0.0"))
        self.label_7.setText(_translate("MainWindow", "Z"))
        
        #Pop-up Window
        self.Cam1.clicked.connect(self.camera)
        self.Cam2.clicked.connect(self.camera)
        self.Cam3.clicked.connect(self.camera)
        self.Cam4.clicked.connect(self.camera)
        self.Cam1_2.clicked.connect(self.camera)
        self.Cam2_3.clicked.connect(self.camera)
        self.Cam1_3.clicked.connect(self.camera)
        self.Cam1_4.clicked.connect(self.camera)
        self.Cam3_4.clicked.connect(self.camera)
        self.Cam2_4.clicked.connect(self.camera)    
        
        # Makes everything work. DO NOT REMOVE!!
        self.show()
        
        
    def correct_cam(self, signal):
        self.cameras = {'Cam1': [1, None],
                        'Cam2': [2, None],
                        'Cam3': [3, None],
                        'Cam4': [4, None],
                        'Cam 1+2': [1, 2],
                        'Cam 1+3': [1, 3],
                        'Cam 1+4': [1, 4],
                        'Cam 2+3': [2, 3],
                        'Cam 2+4': [2, 4],
                        'Cam 3+4': [3, 4]}
        return self.cameras[str(signal)]
    
    def camera(self):
        signal = self.sender()
        self.correct = self.correct_cam(signal.text())
        print(self.correct)
        
        self.newindow = CameraViewer(self.correct[0], self.correct[1])
        self.newindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())       
