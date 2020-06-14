from musicface import Ui_Form
from splder import Music
import sys, requests, time, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import PyQt5
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class DetailUI(Ui_Form, QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.line_return()
        self.Next_page()
        self.Up_page()

        self.RedioButton13()
        self.RedioButton14()
        self.RedioButton15()
        self.RedioButton16()
        self.RedioButton17()
        self.RedioButton18()
        self.click_play_120()
        self.click_play_124()
        self.click_play_128()
        self.click_play_132()
        self.click_play_136()
        self.click_play_140()
        self.click_play_144()
        self.click_play_148()
        self.click_play_152()
        self.click_play_156()
        self.signal_init()
        self.click_putton_168()
        # self.player = QMediaPlayer()
        # self.horizontalSlider.sliderMoved[int].connect(lambda: self.player.setPosition(self.horizontalSlider.value()))

    def search_music(self, num=1):
        music_name = self.lineEdit.text()
        if self.radioButton_13.isChecked() == True:
            type_num = 1
            return music_name, type_num, num
        if self.radioButton_14.isChecked() == True:
            type_num = 2
            return music_name, type_num, num
        if self.radioButton_15.isChecked() == True:
            type_num = 3
            return music_name, type_num, num
        if self.radioButton_16.isChecked() == True:
            type_num = 4
            return music_name, type_num, num
        if self.radioButton_17.isChecked() == True:
            type_num = 5
            return music_name, type_num, num
        if self.radioButton_18.isChecked() == True:
            type_num = 6
            return music_name, type_num, num

    def Return_datas(self, num=1):
        music_name, type_num, num = self.search_music(num)
        music = Music()
        datas = music.run(music_name, type_num, num)
        return datas

    def show_music(self, num=1):
        datas = self.Return_datas(num)
        platforms = {"netease": "网易云音乐", "qq": "QQ音乐", "kugou": "酷狗音乐", "kuwo": "酷我音乐", "ximalaya": "喜马拉雅",
                     "kg": "全名K歌"}
        if len(datas) == 0:
            pass
        if len(datas) < 10:
            self.pushButton_119.setText('')
            self.pushButton_120.setText('无资源')
            self.pushButton_121.setText('')

            self.pushButton_123.setText('')
            self.pushButton_124.setText('')
            self.pushButton_125.setText('')

            self.pushButton_127.setText('')
            self.pushButton_128.setText('')
            self.pushButton_129.setText('')

            self.pushButton_131.setText('')
            self.pushButton_132.setText('')
            self.pushButton_133.setText('')

            self.pushButton_135.setText('')
            self.pushButton_136.setText('')
            self.pushButton_137.setText('')

            self.pushButton_139.setText('')
            self.pushButton_140.setText('')
            self.pushButton_141.setText('')

            self.pushButton_143.setText('')
            self.pushButton_144.setText('')
            self.pushButton_145.setText('')

            self.pushButton_147.setText('')
            self.pushButton_148.setText('')
            self.pushButton_149.setText('')

            self.pushButton_151.setText('')
            self.pushButton_152.setText('')
            self.pushButton_153.setText('')

            self.pushButton_155.setText('')
            self.pushButton_156.setText('')
            self.pushButton_157.setText('')

            self.lineEdit_3.setText('页数:1')

        if len(datas) >= 10:
            music1 = datas[0]
            music2 = datas[1]
            music3 = datas[2]
            music4 = datas[3]
            music5 = datas[4]
            music6 = datas[5]
            music7 = datas[6]
            music8 = datas[7]
            music9 = datas[8]
            music10 = datas[9]
            self.pushButton_119.setText(music1['author'])
            self.pushButton_120.setText(music1['title'])
            self.pushButton_121.setText(platforms.get(music1['type']))

            self.pushButton_123.setText(music2['author'])
            self.pushButton_124.setText(music2['title'])
            self.pushButton_125.setText(platforms.get(music2['type']))

            self.pushButton_127.setText(music3['author'])
            self.pushButton_128.setText(music3['title'])
            self.pushButton_129.setText(platforms.get(music3['type']))

            self.pushButton_131.setText(music4['author'])
            self.pushButton_132.setText(music4['title'])
            self.pushButton_133.setText(platforms.get(music4['type']))

            self.pushButton_135.setText(music5['author'])
            self.pushButton_136.setText(music5['title'])
            self.pushButton_137.setText(platforms.get(music5['type']))

            self.pushButton_139.setText(music6['author'])
            self.pushButton_140.setText(music6['title'])
            self.pushButton_141.setText(platforms.get(music6['type']))

            self.pushButton_143.setText(music7['author'])
            self.pushButton_144.setText(music7['title'])
            self.pushButton_145.setText(platforms.get(music7['type']))

            self.pushButton_147.setText(music8['author'])
            self.pushButton_148.setText(music8['title'])
            self.pushButton_149.setText(platforms.get(music8['type']))

            self.pushButton_151.setText(music9['author'])
            self.pushButton_152.setText(music9['title'])
            self.pushButton_153.setText(platforms.get(music9['type']))

            self.pushButton_155.setText(music10['author'])
            self.pushButton_156.setText(music10['title'])
            self.pushButton_157.setText(platforms.get(music10['type']))
            self.lineEdit_3.setText('页数:{}'.format(num))

    def line_return(self):
        self.lineEdit.returnPressed.connect(self.show_music)

    def Next_music(self):
        try:
            page = self.lineEdit_3.text()
            page_num = page.split(':')
            num = page_num[1]
            if num == 'True':
                num = 1
                new_num = int(num) + 1
                self.show_music(num=new_num)
            else:
                new_num = int(num) + 1
                self.show_music(num=new_num)
        except:
            pass

    def up_music(self):
        try:
            page = self.lineEdit_3.text()
            page_num = page.split(':')
            num = page_num[1]
            new_num = int(num) - 1
            if new_num < 1:
                pass
            else:
                self.search_music(num=new_num)
                self.show_music(num=new_num)
        except:
            pass

    def Next_page(self):
        self.pushButton_170.clicked.connect(self.Next_music)

    def Up_page(self):
        self.pushButton_171.clicked.connect(self.up_music)

    def RedioButton13(self):
        self.radioButton_13.clicked.connect(self.show_music)

    def RedioButton14(self):
        self.radioButton_14.clicked.connect(self.show_music)

    def RedioButton15(self):
        self.radioButton_15.clicked.connect(self.show_music)

    def RedioButton16(self):
        self.radioButton_16.clicked.connect(self.show_music)

    def RedioButton17(self):
        self.radioButton_17.clicked.connect(self.show_music)

    def RedioButton18(self):
        self.radioButton_18.clicked.connect(self.show_music)

    def signal_init(self):
        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.get_position_func)
        self.horizontalSlider.sliderMoved.connect(self.update_position_func)

    def get_duration_func(self, d):
        self.horizontalSlider.setRange(0, d)
        self.horizontalSlider.setEnabled(True)
        self.get_time_func(d)

    def get_time_func(self, d):
        seconds = int(d / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        if minutes == 0 and seconds == 0:
            self.label1.setText('00:00')
            # self.play_pause_btn.setIcon(QIcon('images/play.png'))
        else:
            self.label1.setText('{}:{}'.format(minutes, seconds))

    def get_position_func(self, p):
        self.horizontalSlider.setValue(p)

    def update_position_func(self, v):
        self.player.setPosition(v)
        d = self.horizontalSlider.maximum() - v
        self.get_time_func(d)

    def play_music(self, music1):
        music_url = music1['url']
        author = music1['author']
        title = music1['title']
        music_title = author + '-' + title
        res = requests.get(music_url)
        music = res.content
        if music_url == None or music_url == 'http://None' or len(music) < 100:
            self.player.pause()
            self.lineEdit_2.setPlaceholderText("暂无资源")
            self.frame.setStyleSheet("background-image:url(\"./mp3_img/None.jpg\")")
        else:
            path = './mp3/{}.mp3'.format(music_title)
            isExists = os.path.exists(path)
            if not isExists:
                self.lineEdit_2.setPlaceholderText("{}".format(music_title))
                with open('./mp3/{}.mp3'.format(music_title), 'ab') as fd:
                    fd.write(music)
                music_play_url = './mp3/{}.mp3'.format(music_title)
                url = PyQt5.QtCore.QUrl.fromLocalFile(music_play_url)
                content = PyQt5.QtMultimedia.QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("./icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_168.setIcon(icon3)
            else:
                music_play_url = './mp3/{}.mp3'.format(music_title)
                url = PyQt5.QtCore.QUrl.fromLocalFile(music_play_url)
                content = PyQt5.QtMultimedia.QMediaContent(url)
                self.player.setMedia(content)
                self.player.play()
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("./icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton_168.setIcon(icon3)
            img_path = './mp3_img/{}.jpg'.format(music_title)
            isExists_jpg = os.path.exists(img_path)
            if not isExists_jpg:
                try:
                    music_pic = music1['pic']
                    res_img = requests.get(url=music_pic)
                    with open('./mp3_img/{}.jpg'.format(music_title), 'wb') as f:
                        f.write(res_img.content)
                    im = Image.open('./mp3_img/{}.jpg'.format(music_title))
                    imBackground = im.resize((121, 100))
                    imBackground.save('./mp3_img/{}.jpg'.format(music_title), 'JPEG')
                    self.frame.setStyleSheet("background-image:url(\"./mp3_img/{}.jpg\")".format(music_title))
                except:
                    self.frame.setStyleSheet("background-image:url(\"./mp3_img/None.jpg\")")
            else:
                self.frame.setStyleSheet("background-image:url(\"./mp3_img/{}.jpg\")".format(music_title))

    def download_play_120(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[0]
            self.play_music(music1=music1)

    def click_play_120(self):
        self.pushButton_120.clicked.connect(self.download_play_120)

    def download_play_124(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[1]
            self.play_music(music1=music1)

    def click_play_124(self):
        self.pushButton_124.clicked.connect(self.download_play_124)

    def download_play_128(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[2]
            self.play_music(music1=music1)

    def click_play_128(self):
        self.pushButton_128.clicked.connect(self.download_play_128)

    def download_play_132(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[3]
            self.play_music(music1=music1)

    def click_play_132(self):
        self.pushButton_132.clicked.connect(self.download_play_132)

    def download_play_136(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[4]
            self.play_music(music1=music1)

    def click_play_136(self):
        self.pushButton_136.clicked.connect(self.download_play_136)

    def download_play_140(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[5]
            self.play_music(music1=music1)

    def click_play_140(self):
        self.pushButton_140.clicked.connect(self.download_play_140)

    def download_play_144(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[6]
            self.play_music(music1=music1)

    def click_play_144(self):
        self.pushButton_144.clicked.connect(self.download_play_144)

    def download_play_148(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[7]
            self.play_music(music1=music1)

    def click_play_148(self):
        self.pushButton_148.clicked.connect(self.download_play_148)

    def download_play_152(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[8]
            self.play_music(music1=music1)

    def click_play_152(self):
        self.pushButton_152.clicked.connect(self.download_play_152)

    def download_play_156(self):
        page = self.lineEdit_3.text()
        page_num = page.split(':')
        num = page_num[1]
        if num == 'True' or '1':
            num = 1
            datas = self.Return_datas(num=int(num))
            music1 = datas[9]
            self.play_music(music1=music1)

    def click_play_156(self):
        self.pushButton_156.clicked.connect(self.download_play_156)

    def putton_168(self):
        if self.player.isMuted():
            self.player.setMuted(False)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("./icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_168.setIcon(icon4)
        else:
            self.player.setMuted(True)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("./icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_168.setIcon(icon4)

        # self.player.pause()
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap("./icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_168.setIcon(icon4)

    def click_putton_168(self):
        self.pushButton_168.clicked.connect(self.putton_168)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    sys.exit(app.exec_())
