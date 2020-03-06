#!usr/bin/env python
#coding=utf-8

import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

    # Create and launch a thread



import sys
from PySide import QtGui, QtCore
import pyautogui

import mytree_test
# import mat_stuff as sounddata

import pyaudio
import wave

class SoundData:
    def __init__(self):
        self.filepath = ''
        self.file_loaded = False
        self.data = None
        self.raw_data = None
        self.playing = False
        self.stopPlayback = False

        from threading import Thread
        self.play_thread = None
        self.play_thread = Thread()

    def load_file(self, fpath):
        f = open(fpath, "r")
        self.raw_data = f.read()
        print type(self.raw_data)

        # open a wav format music
        self.data = wave.open(fpath, "r")

    def playloop(self, ch, dt, sw, chan, rt, stop):
        p = pyaudio.PyAudio()
        data = dt.readframes(ch)
        stream = p.open(format=p.get_format_from_width(sw),
                        channels=chan,
                        rate=rt,
                        output=True)
        # play stream
        while data:
            stream.write(data)
            data = dt.readframes(ch)
            if stop():
                break

        self.playing = False
        self.stopPlayback = False
        stream.stop_stream()
        stream.close()
        p.terminate()

    def play(self):
        # define stream chunk
        chunk = 1024

        # open stream


        self.playing = True
        data = self.data.readframes(chunk)
        sample_width = self.data.getsampwidth()
        channels = self.data.getnchannels()
        rate = self.data.getframerate()

        from threading import Thread
        self.play_thread = Thread(target=self.playloop, args=(chunk, self.data, sample_width, channels, rate, lambda: self.stopPlayback))
        self.play_thread.run()

    def stop(self):
        if self.playing:
            self.stopPlayback = True
            # close PyAudio



class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.sound_data = None
        self.sound_data = SoundData()

    def do_file(self):
        fpath, filters = QtGui.QFileDialog.getOpenFileName()
        print fpath
        self.sound_data.load_file(fpath)

    def play(self):
        self.sound_data.play()

    def stop(self):
        self.sound_data.stop()

    def initUI(self):

        # LAYOUT CONFIG
        lo = QtGui.QVBoxLayout()
        self.setLayout(lo)

        # TOOLTIPSGui
        QtGui.QToolTip.setFont(QtGui.QFont('Times New Roman', 12))
        self.setToolTip('this is a <b> QWidget </b> widget')

        self.screenWidth, self.screenHeight = pyautogui.size()

        # SIZING
        size_x = 1024
        size_y = 356

        # MAIN WINDOW GEOMETRY
        # self.setStyleSheet('QWidget {background-color: #37375A; color: white;}')
        self.setGeometry(( self.screenWidth-size_x)/2, (self.screenHeight-size_y) /2, size_x, size_y)
        self.setWindowTitle('TESTING')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        # TOP WIDGET
        topwid = QtGui.QWidget(self)
        topwid.setLayout(QtGui.QVBoxLayout())
        topwid_font = QtGui.QFont('Arial Black', 20)

        project = QtGui.QLabel(topwid)
        user = QtGui.QLabel(topwid)
        topwid.layout().addWidget(project)
        topwid.layout().addWidget(user)

        project.setFont(topwid_font)
        user.setFont(topwid_font)
        topwid.setFont(topwid_font)

        button = QtGui.QPushButton('LOAD FILE', self)
        button.setToolTip('specify a file to be <b> loaded </b>')
        button.resize(button.sizeHint())
        button.clicked.connect(self.do_file)

        button2 = QtGui.QPushButton('PLAY', self)
        button2.setToolTip('this is a <b> BUTTON </b>')
        button2.resize(button.sizeHint())
        button2.clicked.connect(self.play)

        button3 = QtGui.QPushButton('STOP', self)
        button3.setToolTip('this is a <b> BUTTON </b>')
        button3.resize(button.sizeHint())
        button3.clicked.connect(self.stop)

        buttonLo = QtGui.QHBoxLayout()
        lo.addLayout(buttonLo)
        buttonLo.addWidget(button, 3, alignement=QtCore.Qt.AlignRight)
        buttonLo.addWidget(button2, 6, alignement=QtCore.Qt.AlignRight)
        buttonLo.addWidget(button3, 10, alignement=QtCore.Qt.AlignRight)

        project.setFont('Sans Serif')
        user.setFont('Sans Serif')
        project.setText('<b> PROJECT: <b/> PlayStation')
        user.setText('<b> USER: <b/> Animation')

        button.setStyleSheet('QPushButton {background-color: #C50000; color: #0DFFFF;}')

        # SPLITTER
        splitter = QtGui.QSplitter(self)
        self.layout().addWidget(splitter, 100)


        # DETAILS TAB
        detlo = QtGui.QVBoxLayout()
        details = QtGui.QWidget(splitter)
        details.resize(200, 700)
        details.setAutoFillBackground(True)
        details.setLayout(detlo)

        det_name = QtGui.QLabel()
        det_name.setText('DETAIL VIEW')
        det_name.setFont(QtGui.QFont('Arial',pointSize = 24))
        det_name.resize(det_name.sizeHint())
        detlo.addWidget(det_name, 0, QtCore.Qt.AlignCenter)

        # COMMENT EDIT
        txtedit = QtGui.QTextEdit(details)
        txtedit.setMinimumWidth(details.width())
        txtedit.setStyleSheet('QTextEdit {background-color #FFFFFF; color black}')
        detlo.addWidget(txtedit, 1, QtCore.Qt.AlignCenter)
        txtedit.show()

        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Background,QtGui.qRed(255))

        label = QtGui.QLabel(details)
        label.setText('This Is Sample Details Widget')
        label.move(0,210)
        label.resize(300,50)
        detlo.addWidget(label, 10, QtCore.Qt.AlignCenter)
        label.setPalette(pallete)

        model = QtGui.QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())

        #
        #TODO Change to QTreeWidget with items added by user
        tree = mytree_test.MyTree(splitter)

        #
        splitter.addWidget(tree)
        splitter.addWidget(details)


        self.show()




class Project():
    """ PROJECT CLASS
    is used to store simple data to be displayed in GUI and to store the path to the project
    """
    def __init__(self, project = 'test'):
        if project == 'test':
            self.init_sample()

        (' INIT_SAMPLE\n'
         '        used only for development and testing purposes\n'
         '        ')
    def init_sample(self):
        print '>>>>>>> LOADING THE TEST PROJECT'
        self.name = 'test project'
        self.type = 'test type'
        self.project_path = 'D:\DEV\sample_project'



def main():
    app = QtGui.QApplication(sys.argv)
    proj = Project()
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


