

def test():
    QMessageBox.warning(self, '错误', '用户名和密码不匹配', QMessageBox.Yes, QMessageBox.Yes)


if __name__ == "__main__":
    import sys
    import main
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QDialog

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    myshow = Ui_MainWindow()
    myshow.show()
    sys.exit(app.exec_())


