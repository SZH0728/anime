# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: introduce界面的逻辑模块
# ======================================================================================================================

from windows.intro import Ui_Form
from PyQt5 import QtCore, QtWidgets


class introduce(Ui_Form, QtWidgets.QDialog):
    def __init__(self, content):
        super(introduce, self).__init__()
        self._content = content

    def setupUi(self, Form):
        super(introduce, self).setupUi(Form)
        self.pushButton.clicked.connect(lambda: QtWidgets.QDialog.close(self))
        self.plainTextEdit.setPlainText(self._content)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = introduce('a')
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
