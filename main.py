import sys
import s2_ui
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindows(QMainWindow,s2_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_11.clicked.connect(s2053)
        self.radioButton_12.clicked.connect(s2052)
        self.radioButton_10.clicked.connect(s2048)
        self.radioButton_9.clicked.connect(s2045)
        self.radioButton.clicked.connect(s2037)
        self.radioButton_2.clicked.connect(s2032)
        self.radioButton_3.clicked.connect(s2devmode)
        self.radioButton_4.clicked.connect(s2019)
        self.radioButton_5.clicked.connect(s2016)
        self.radioButton_6.clicked.connect(s2013)
        self.radioButton_7.clicked.connect(s2009)
        self.radioButton_8.clicked.connect(s2005)
        self.radioButton_13.clicked.connect(s2003)
        self.radioButton_14.clicked.connect(s2001)

        self.pushButton.clicked.connect(Tab1_Getinfo)
        self.pushButton_2.clicked.connect(Tab1_Saveinfo)
        self.pushButton_3.clicked.connect(Tab1_Clear)

        self.comboBox.currentIndexChanged.connect(UA_Changed)
        self.comboBox_2.currentIndexChanged.connect(Http_Mathod_Changed)
        self.comboBox_3.currentIndexChanged.connect(Encode_Changed)



class Current_Payload:
    name = ""
    UserAgent = "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"
    HttpMathod = "POST"
    Encode = "UTF-8"
    Get_Info = ""
    Cmd_Exec = ""



def s2053():
    Current_Payload.name = "s2053"
    print(Current_Payload.name)


def s2052():
    Current_Payload.name = "s2052"
    print(Current_Payload.name)


def s2048():
    Current_Payload.name = "s2048"
    print(Current_Payload.name)


def s2045():
    Current_Payload.name = "s2045"
    print(Current_Payload.name)

def s2037():
    Current_Payload.name = "s2037"
    print(Current_Payload.name)


def s2032():
    Current_Payload.name = "s2032"
    print(Current_Payload.name)


def s2devmode():
    Current_Payload.name = "s2devmode"
    print(Current_Payload.name)


def s2019():
    Current_Payload.name = "s2019"
    print(Current_Payload.name)


def s2016():
    Current_Payload.name = "s2016"
    print(Current_Payload.name)


def s2013():
    Current_Payload.name = "s2013"
    print(Current_Payload.name)


def s2009():
    Current_Payload.name = "s2009"
    print(Current_Payload.name)


def s2005():
    Current_Payload.name = "s2005"
    print(Current_Payload.name)


def s2003():
    Current_Payload.name = "s2003"
    print(Current_Payload.name)


def s2001():
    Current_Payload.name = "s2001"
    print(Current_Payload.name)


def Tab1_Getinfo():
    print("test")
    mainWindow.textEdit.append(mainWindow.comboBox.currentText())
def Tab1_Saveinfo():
    print("test")

def Tab1_Clear():
    mainWindow.textEdit.clear()

def UA_Changed():
    mainWindow.textEdit.append(mainWindow.comboBox.currentText())
    c_payload.UserAgent = mainWindow.comboBox.currentText()


def Http_Mathod_Changed():
    mainWindow.textEdit.append(mainWindow.comboBox_2.currentText())
    c_payload.HttpMathod = mainWindow.comboBox_2.currentText()


def Encode_Changed():
    mainWindow.textEdit.append(mainWindow.comboBox_3.currentText())
    c_payload.Encode = mainWindow.comboBox_3.currentText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = s2_ui.Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    mainWindow = MainWindows()
    mainWindow.show()
    c_payload = Current_Payload()
    sys.exit(app.exec_())