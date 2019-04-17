# -*- coding: utf-8 -*-
# _author_ = 'nsy1994'
# _date_ = '2018/4/27 9:51'

import sys
import hashlib
import time
import threading
from PySide.QtGui import *
from PySide.QtCore import *
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 当下拉框当前选择项发生变化时，发出信号，槽为QPlainTextEdit自带的清除显示内容
        self.comboBox.currentIndexChanged.connect(self.plainTextEdit.clear)
        self.toolButton.clicked.connect(self.select_file)  # '文件'按钮信号
        self.pushButton.clicked.connect(self.file_hash)  # '查询'按钮信号

    def select_file(self):
        """
        '文件'按钮槽
        :return:
        """
        self.file_name = QFileDialog.getOpenFileName(self.centralwidget, caption=u"请选择文件", dir=r"C:\Users\admin")[0]
        self.lineEdit.setText(self.file_name)
        self.plainTextEdit.clear()

    def file_hash(self):
        """
        '查询'按钮槽
        :return:
        """
        try:
            file_name = self.lineEdit.displayText()
            if not file_name:
                self.label_4.setText(u"请选择一个文件！")
            else:
                self.plainTextEdit.clear()
                if self.comboBox.currentText() == u'MD5':
                    f_hash = hashlib.md5()
                    with open(file_name, 'rb') as files:
                        for f in files:
                            f_hash.update(f)
                    self.label_3.setText(u"该文件的hash(MD5)值为")
                elif self.comboBox.currentText() == u'SHA1':
                    f_hash = hashlib.sha1()
                    with open(file_name, 'rb') as files:
                        for f in files:
                            f_hash.update(f)
                    self.label_3.setText(u"该文件的hash(SHA1)值为")
                elif self.comboBox.currentText() == u'SHA256':
                    f_hash = hashlib.sha256()
                    with open(file_name, 'rb') as files:
                        for f in files:
                            f_hash.update(f)
                    self.label_3.setText(u"该文件的hash(SHA256)值为")
                file_hash = f_hash.hexdigest()
                self.plainTextEdit.setPlainText(file_hash)
                self.label_4.clear()
        except:
            self.label_4.setText(u"文件名不正确！")


if __name__ == '__main__':
    program = QApplication(sys.argv)
    app = MainWindow()
    app.show()
    program.exec_()