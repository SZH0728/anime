# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 主程序
# ======================================================================================================================

from windows import *
import sys
import data
import setting
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import network
import qt_thread
from analysis import *


class Ui_Form(main_window.Ui_Form, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.research = data.research(5)
        self.detail = data.detail()
        self.set = setting.setting()
        bro = network.broswer.broswer_option(True)
        dri = network.broswer.driver_option()
        self.analysis = qt_thread.analysis(bro, dri)
        self.analysis.start()

    def setupUi(self, form):
        super(Ui_Form, self).setupUi(form)
        self.label.setScaledContents(True)
        self.label_8.setText(self.set.save_path)
        self.comboBox.addItems(['所有网站', '所有勾选', '所有未勾选'])
        self.pushButton_12.clicked.connect(self.name_change)
        self.pushButton_13.clicked.connect(self.show_introduce)
        self.pushButton_5.clicked.connect(self.window_change)
        self.pushButton_2.clicked.connect(self.research_checkbox_setchecked_true)
        self.pushButton_3.clicked.connect(self.research_checkbox_setchecked_false)
        self.pushButton_14.clicked.connect(self.choose_save_root)
        self.pushButton_10.clicked.connect(self.picture_save)
        self.pushButton_9.clicked.connect(self.information_save)
        self.pushButton.clicked.connect(self.research_click)
        self.listWidget.itemClicked.connect(self.set_research_show)
        self.listWidget_2.itemClicked.connect(self.detail_click)
        self.analysis.research.connect(self.add_research_result)
        self.analysis.detail.connect(self.detail_load)
        self.comboBox_2.activated.connect(self.play_list_change)

    def closeEvent(self, event):
        QtWidgets.QDialog.close(self)
        self.research.stop()
        self.analysis.quit()

    def name_change(self):
        text, flag = QtWidgets.QInputDialog.getText(self, '名称修改', '请输入修改后名称',
                                                    QtWidgets.QLineEdit.Normal, self.label_2.text())
        if flag:
            self.label_2.setText(text)

    def show_introduce(self):
        w = intro_logic.introduce(self.detail.introduce)
        w.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        w.setupUi(w)
        w.show()

    def window_change(self):
        i = self.stackedWidget.currentIndex()
        if i == 0:
            self.stackedWidget.setCurrentIndex(1)
        elif i == 1:
            self.stackedWidget.setCurrentIndex(0)

    def research_checkbox_setchecked_true(self):
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        self.checkBox_5.setChecked(True)
        self.checkBox_6.setChecked(True)

    def research_checkbox_setchecked_false(self):
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)

    @staticmethod
    def all_true(*args):
        for i in args:
            if i is False:
                return False
        return True

    @staticmethod
    def all_false(*args):
        for i in args:
            if i is True:
                return False
        return True

    def choose_save_root(self):
        f = QtWidgets.QFileDialog()
        f.setFileMode(QtWidgets.QFileDialog.Directory)
        f.setFilter(QtCore.QDir.Files)
        if f.exec_():
            p = f.selectedFiles()[0]
            self.label_8.setText(p)
            self.set.save_path = p
            self.set.save()

    def picture_save(self):
        if self.detail.picture == '':
            QtWidgets.QMessageBox.critical(self, 'Anime', '图片未加载！',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            if os.path.exists(os.path.join(self.set.save_path, self.detail.name)):
                path = os.path.join(self.set.save_path, self.detail.name)
                with open(os.path.join(path, self.detail.name + self.detail.fmat), 'wb') as p:
                    p.write(self.detail.picture)
                    p.close()
            elif os.path.exists(self.set.save_path):
                with open(os.path.join(self.set.save_path, self.detail.name + self.detail.fmat), 'wb') as p:
                    p.write(self.detail.picture)
                    p.close()
            else:
                QtWidgets.QMessageBox.critical(self, 'Anime', '保存路径不存在！',
                                               QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def information_save(self):
        if self.detail.introduce == '':
            QtWidgets.QMessageBox.critical(self, 'Anime', '信息未加载！',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            infor = [self.detail.name, self.detail.auther, self.detail.time, self.detail.type,
                     self.detail.url, self.detail.picture_url, self.detail.from_, self.detail.introduce]
            title = ['名称', '作者', '时间', '分类', '网址', '图片网址', '来源', '简介']
            w = ''
            for key, value in dict(zip(title, infor)).items():
                w += str(key) + '：' + str(value) + '\n'
            if os.path.exists(os.path.join(self.set.save_path, self.detail.name)):
                path = os.path.join(self.set.save_path, self.detail.name)
                with open(os.path.join(path, self.detail.name + '.txt'), 'w') as p:
                    p.write(w)
                    p.close()
            elif os.path.exists(self.set.save_path):
                with open(os.path.join(self.set.save_path, self.detail.name + '.txt'), 'w') as p:
                    p.write(w)
                    p.close()
            else:
                QtWidgets.QMessageBox.critical(self, 'Anime', '保存路径不存在！',
                                               QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def research_click(self):
        if self.lineEdit.text() != self.research.key_word and self.lineEdit.text() != '':
            self.research.key_word = self.lineEdit.text()
            self.research.clear()
            self.listWidget.clear()
            self.listWidget.addItems(['「全部」', '「匹配」', '「包含」'])
            self.listWidget.setCurrentItem(self.listWidget.item(0))
            self.listWidget_2.clear()
            self.analysis.add_research(self.research.key_word, ['fcdm', 'ttt'])

    def add_research_result(self, value):
        li = []
        for item in range(self.listWidget.count()):
            li.append(self.listWidget.item(item).text())
        if public.web_name_change(value[0]['from']) not in li:
            self.listWidget.addItem(public.web_name_change(value[0]['from']))
        for i in value:
            self.research.add_result(i['name'], i['url'], i['pic_url'], i['from'])
        self.set_research_show(self.listWidget.currentItem())

    def set_research_show(self, item):
        text = item.text()
        self.listWidget_2.clear()
        if text == '「全部」':
            for i in self.research.result:
                photo = QtGui.QPixmap()
                photo.loadFromData(i.pic)
                item = QtWidgets.QListWidgetItem(self.listWidget_2)
                item.setText(i.name)
                item.setWhatsThis(i.url)
                item.setIcon(QtGui.QIcon(photo))
                item.setToolTip('来源：' + public.web_name_change(i.from_))
        elif text == '「匹配」':
            for i in self.research.result:
                if i.name != self.research.key_word:
                    continue
                photo = QtGui.QPixmap()
                photo.loadFromData(i.pic)
                item = QtWidgets.QListWidgetItem(self.listWidget_2)
                item.setText(i.name)
                item.setWhatsThis(i.url)
                item.setIcon(QtGui.QIcon(photo))
                item.setToolTip('来源：' + public.web_name_change(i.from_))
        elif text == '「包含」':
            for i in self.research.result:
                if self.research.key_word not in i.name:
                    continue
                photo = QtGui.QPixmap()
                photo.loadFromData(i.pic)
                item = QtWidgets.QListWidgetItem(self.listWidget_2)
                item.setText(i.name)
                item.setWhatsThis(i.url)
                item.setIcon(QtGui.QIcon(photo))
                item.setToolTip('来源：' + public.web_name_change(i.from_))
        else:
            for i in self.research.search_all_by_from(public.web_name_change(text)):
                photo = QtGui.QPixmap()
                photo.loadFromData(i.pic)
                item = QtWidgets.QListWidgetItem(self.listWidget_2)
                item.setText(i.name)
                item.setWhatsThis(i.url)
                item.setIcon(QtGui.QIcon(photo))
                item.setToolTip('来源：' + public.web_name_change(i.from_))

    def detail_click(self, item):
        r = self.research.search_by_url(item.whatsThis())
        self.analysis.add_detail(r.url, r.from_)
        self.label_10.setText('正在加载')
        self.label_2.setText(r.name)
        photo = QtGui.QPixmap()
        photo.loadFromData(r.pic)
        self.label.setPixmap(photo)
        self.detail.put_research_result(r)
        self.comboBox_2.clear()
        self.comboBox_2.addItem('所有列表')
        self.listWidget_3.clear()
        self.label_4.setText('')
        self.label_3.setText('')
        self.label_5.setText('')
        self.label_6.setText('')

    def detail_load(self, value):
        li = []
        for index, i in enumerate(value['play']):
            li.append(data.download_list('下载列表'+str(index+1), i))
        self.detail.set_download_list(value['auther'], value['time'], value['type'], value['info'], li)
        self.label_10.setText('')
        self.label_4.setText(value['auther'])
        self.label_3.setText(value['time'])
        self.label_5.setText(value['type'])
        self.label_6.setText(value['info'])
        if len(self.detail.clear_download_list) != 1:
            self.comboBox_2.addItems(self.detail.clear_download_list.keys())
        for key, value in self.detail.clear_download_list.items():
            for i in value:
                item = QtWidgets.QListWidgetItem(self.listWidget_3)
                item.setText(i['name']+'    '+i['url'])
                item.setWhatsThis(i['url'])
                item.setToolTip('来源：'+key)

    def play_list_change(self):
        li = self.comboBox_2.currentText()
        self.listWidget_3.clear()
        if li == '所有列表':
            for key, value in self.detail.clear_download_list.items():
                for i in value:
                    item = QtWidgets.QListWidgetItem(self.listWidget_3)
                    item.setText(i['name'] + '    ' + i['url'])
                    item.setWhatsThis(i['url'])
                    item.setToolTip('来源：' + key)
        else:
            for key, value in self.detail.clear_download_list.items():
                if key != li:
                    continue
                for i in value:
                    item = QtWidgets.QListWidgetItem(self.listWidget_3)
                    item.setText(i['name'] + '    ' + i['url'])
                    item.setWhatsThis(i['url'])
                    item.setToolTip('来源：' + key)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_Form()
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
