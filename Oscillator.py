from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
import images_rc
import sys
import pyaudio
from utils import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 610)
        MainWindow.setMaximumSize(QtCore.QSize(486, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.parametersFrame = QtWidgets.QFrame(self.centralwidget)
        self.parametersFrame.setGeometry(QtCore.QRect(20, 20, 451, 221))
        self.parametersFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.parametersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parametersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parametersFrame.setObjectName("parametersFrame")


        self.comboBoxFunction = QtWidgets.QComboBox(self.parametersFrame)
        self.comboBoxFunction.setGeometry(QtCore.QRect(120, 10, 69, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBoxFunction.setFont(font)
        self.comboBoxFunction.setObjectName("comboBoxFunction")
        self.comboBoxFunction.addItem("")
        self.comboBoxFunction.addItem("")
        self.comboBoxFunction.addItem("")      
        self.comboBoxFunction.view().pressed.connect(self.updateGraph)


        self.functionLabel = QtWidgets.QLabel(self.parametersFrame)
        self.functionLabel.setGeometry(QtCore.QRect(10, 15, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.functionLabel.setFont(font)
        self.functionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.functionLabel.setObjectName("functionLabel")

        self.sampleRateLabel = QtWidgets.QLabel(self.parametersFrame)
        self.sampleRateLabel.setGeometry(QtCore.QRect(10, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sampleRateLabel.setFont(font)
        self.sampleRateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sampleRateLabel.setObjectName("sampleRateLabel")

        self.sampleRate = QtWidgets.QLineEdit(self.parametersFrame)
        self.sampleRate.setGeometry(QtCore.QRect(130, 60, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sampleRate.setFont(font)
        self.sampleRate.setObjectName("sampleRate")            
        

        self.frequencyLabel = QtWidgets.QLabel(self.parametersFrame)
        self.frequencyLabel.setGeometry(QtCore.QRect(0, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frequencyLabel.setFont(font)
        self.frequencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencyLabel.setObjectName("frequencyLabel")

        self.frequencySlider = QtWidgets.QSlider(self.parametersFrame)
        self.frequencySlider.setGeometry(QtCore.QRect(100, 140, 251, 21))
        self.frequencySlider.setMinimum(20)
        self.frequencySlider.setMaximum(20000)
        self.frequencySlider.setSliderPosition(440)
        self.frequencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.frequencySlider.setObjectName("frequencySlider")
        self.frequencySlider.valueChanged.connect(self.updateGraph)

        self.currentFrequencyLabel = QtWidgets.QLabel(self.parametersFrame)
        self.currentFrequencyLabel.setGeometry(QtCore.QRect(370, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.currentFrequencyLabel.setFont(font)
        self.currentFrequencyLabel.setObjectName("currentFrequencyLabel")

        self.volumeLabel = QtWidgets.QLabel(self.parametersFrame)
        self.volumeLabel.setGeometry(QtCore.QRect(30, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeLabel.setObjectName("volumeLabel")

        self.volumeSlider = QtWidgets.QSlider(self.parametersFrame)
        self.volumeSlider.setGeometry(QtCore.QRect(100, 180, 251, 21))
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSliderPosition(50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")     
        self.volumeSlider.valueChanged.connect(self.updateGraph)   

        self.currentVolume = QtWidgets.QLabel(self.parametersFrame)
        self.currentVolume.setGeometry(QtCore.QRect(370, 180, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.currentVolume.setFont(font)
        self.currentVolume.setObjectName("currentVolume")
        

        self.durationLabel = QtWidgets.QLabel(self.parametersFrame)
        self.durationLabel.setGeometry(QtCore.QRect(10, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.durationLabel.setFont(font)
        self.durationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.durationLabel.setObjectName("durationLabel")

        self.duration = QtWidgets.QLineEdit(self.parametersFrame)
        self.duration.setGeometry(QtCore.QRect(130, 100, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.duration.setFont(font)
        self.duration.setObjectName("duration")        

        self.buttonFrame = QtWidgets.QFrame(self.centralwidget)
        self.buttonFrame.setGeometry(QtCore.QRect(20, 250, 451, 61))
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")


        self.playBtn = QtWidgets.QPushButton(self.buttonFrame)
        self.playBtn.setGeometry(QtCore.QRect(150, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.playBtn.setFont(font)
        self.playBtn.setObjectName("playBtn")
        self.playBtn.clicked.connect(self.play)

        self.graphFrame = QtWidgets.QFrame(self.centralwidget)
        self.graphFrame.setGeometry(QtCore.QRect(20, 320, 451, 281))
        self.graphFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphFrame.setObjectName("graphFrame")

        self.mplWidget = MplWidget(self.graphFrame)
        self.mplWidget.setGeometry(QtCore.QRect(10, 10, 431, 301))
        self.mplWidget.setObjectName("mplWidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oscillator"))
        self.comboBoxFunction.setItemText(0, _translate("MainWindow", "sin"))
        self.comboBoxFunction.setItemText(1, _translate("MainWindow", "square"))
        self.comboBoxFunction.setItemText(2, _translate("MainWindow", "saw-tooth"))        
        self.functionLabel.setText(_translate("MainWindow", "Wave Function:"))
        self.sampleRateLabel.setText(_translate("MainWindow", "Sample Rate(Hz):"))
        self.sampleRate.setText(_translate("MainWindow", "44100"))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency:"))
        self.currentFrequencyLabel.setText(_translate("MainWindow", "440Hz"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume:"))
        self.currentVolume.setText(_translate("MainWindow", "50%"))
        self.durationLabel.setText(_translate("MainWindow", "Duration(seconds):"))
        self.duration.setText(_translate("MainWindow", "5"))
        self.playBtn.setText(_translate("MainWindow", "Play"))        
        self.updateGraph()
        
    
    def play(self):
        #getting the parameters
        try:
            self.functionName = self.comboBoxFunction.currentText()
            self.samplingRate = int(self.sampleRate.text())
            self.frequency = int(self.frequencySlider.value())
            self.volume = int(self.volumeSlider.value())/100.0
            self.durationValue = int(self.duration.text())
            if self.functionName == "sin":        
                samples = sinWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
            elif self.functionName == "square":
                samples = squareWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
            elif self.functionName == "saw-tooth":
                samples = sawToothWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
            elif self.functionName == "saw-tooth":
                samples = sawToothWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)        
            self.p = pyaudio.PyAudio()
            self.stream = (self.p).open(format=pyaudio.paFloat32,channels=1,rate=self.samplingRate,output=True)
            self.stream.write(samples)
            self.stream.close()
            self.p.terminate()        
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_() 

    def updateGraph(self):
        self.functionName = self.comboBoxFunction.currentText()
        self.samplingRate = int(self.sampleRate.text())
        self.frequency = int(self.frequencySlider.value())
        self.volume = int(self.volumeSlider.value())/100.0
        self.durationValue = int(self.duration.text())
        self.currentFrequencyLabel.setText(str(self.frequencySlider.value())+"Hz")
        self.currentVolume.setText(str(self.volumeSlider.value())+"%")
        if self.functionName == "sin":        
            samples = sinWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
        elif self.functionName == "square":
            samples = squareWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
        elif self.functionName == "saw-tooth":
            samples = sawToothWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)
        elif self.functionName == "saw-tooth":
            samples = sawToothWave(frequency=self.frequency,duration=self.durationValue,samplingRate=self.samplingRate,amplitude=self.volume)        
        self.mplWidget.canvas.axes.clear()
        self.mplWidget.canvas.axes.plot(np.arange(self.samplingRate * self.durationValue)[:200],samples[:200])
        self.mplWidget.canvas.draw()           
      
  

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())