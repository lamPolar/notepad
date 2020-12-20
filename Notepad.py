import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QCursor, QFont
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QFileDialog, QTextEdit, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QFontDialog, QStatusBar, QLabel


class QNotepad(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(830, 450)
        self.setTitle()
        self.setWindowIcon(QIcon(os.path.join('image', 'notepad.jpg')))
        menubar = self.menuBar()
       # elf.status.showMessage("{}%".format(self.size))
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.size = 100
        self.label = QLabel("{}%".format(self.size), self)
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.status.addWidget(self.label,2)

        Filemenu = menubar.addMenu("파일")
        Filemenu1 = menubar.addMenu("편집")
        Filemenu2 = menubar.addMenu("서식")
        Filemenu3 = menubar.addMenu("보기")
        zoom = Filemenu3.addMenu("확대/축소")
        Filemenu4 = menubar.addMenu("도움")

        newfile = QAction("새파일", self)
        newfile.setShortcut('Ctrl+N')
        openfile = QAction('열기', self)
        openfile.setShortcut('Ctrl+O')
        savefile = QAction('저장', self)
        savefile.setShortcut('Ctrl+N')
        saveasfile = QAction('다른 이름으로 저장',self)
        printfile = QAction('출력',self)
        exit = QAction('끝내기', self)

        undo = QAction("실행취소", self)
        undo.setShortcut('Ctrl+Z')
        redo = QAction("재실행", self)
        redo.setShortcut('Ctrl+X')
        cut = QAction("잘라내기", self)
        cut.setShortcut('Ctrl+T')
        copy = QAction("복사",self)
        copy.setShortcut('Ctrl+C')
        paste = QAction("붙여넣기", self)
        paste.setShortcut('Ctrl+V')
        delete = QAction("삭제",self)
        delete.setShortcut("Del")
        find = QAction("찾기",self)
        find.setShortcut("Ctrl+F")

        autoenter = QAction("자동 줄 바꿈",self)
        autoenter.setCheckable(True)
        autoenter.setChecked(False)
        font = QAction("글꼴", self)

        zoomin = QAction("확대",self)
        zoomout = QAction("축소",self)
        statusbar = QAction("상태표시줄",self)
        statusbar.setCheckable(True)
        statusbar.setChecked(True)

        autoenter.triggered.connect(self.format_autoenter)
        font.triggered.connect(self.format_font)
        Filemenu2.addAction(autoenter)
        Filemenu2.addAction(font)

        zoomin.triggered.connect(self.view_zoomin)
        zoomout.triggered.connect(self.view_zoomout)
        statusbar.triggered.connect(self.view_status)
        zoom.addAction(zoomin)
        zoom.addAction(zoomout)
        Filemenu3.addAction(statusbar)

        info = QAction("메모장 정보", self)
        info.triggered.connect(self.help_info)
        Filemenu4.addAction(info)

        newfile.triggered.connect(self.file_new)
        openfile.triggered.connect(self.file_open)
        savefile.triggered.connect(self.file_save)
        saveasfile.triggered.connect(self.file_saveas)
        printfile.triggered.connect(self.file_print)
        exit.triggered.connect(qApp.quit)
        Filemenu.addAction(newfile)
        Filemenu.addAction(openfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(saveasfile)
        Filemenu.addSeparator()
        Filemenu.addAction(printfile)
        Filemenu.addSeparator()
        Filemenu.addAction(exit)

        undo.triggered.connect(self.edit_undo)
        redo.triggered.connect(self.edit_redo)
        cut.triggered.connect(self.edit_cut)
        copy.triggered.connect(self.edit_copy)
        paste.triggered.connect(self.edit_paste)
        delete.triggered.connect(self.edit_delete)
        find.triggered.connect(self.edit_find)
        Filemenu1.addAction(undo)
        Filemenu1.addSeparator()
        Filemenu1.addAction(redo)
        Filemenu1.addAction(cut)
        Filemenu1.addAction(copy)
        Filemenu1.addAction(paste)
        #Filemenu1.addAction(delete)
        Filemenu1.addSeparator()
        Filemenu1.addAction(find)

        self.text1 = QTextEdit(self)
        self.text1.setAcceptRichText(True)
        #self.buffer = ""
        self.text1.setLineWrapMode(0)
        self.text1.default_font = QFont()
        self.setCentralWidget(self.text1)
        self.show()

    def view_zoomin(self):
        self.text1.zoomIn()
        self.size += 10

    def view_zoomout(self):
        self.text1.zoomOut()
        self.size -= 10

    def view_status(self):
        if self.status.isHidden():
            self.status.show()
        else: self.status.hide()

    def help_info(self):
        dial = QMessageBox(self)
        dial.setText("\n B6110054 김희선 작성\t\n")
        dial.setWindowTitle("메모장 정보")
        dial.show()

    def edit_undo(self):
        self.text1.undo()
    def edit_redo(self):
        self.text1.redo()
    def edit_cut(self):
        self.text1.cut()
    def edit_copy(self):
        self.text1.copy()
    def edit_paste(self):
        self.text1.paste()
    def edit_delete(self):
        pass
        #self.text1.setText(self.text1.toPlainText())
        #self.text1.clear()
    def edit_find(self):
        pass
        #QFindDialog
        #self.text1.find()


    def file_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, '파일 열기', './')
        if FileOpen[0]:
            f = open(FileOpen[0], 'r')
            textcontent = f.read()
            self.text1.setText(textcontent)
            self.setTitle(FileOpen[0])
            f.close()
            self.setWindowFilePath(FileOpen[0])

    def file_saveas(self):
        FileSaveas = QFileDialog.getSaveFileName(self, '파일 저장', './')
        if FileSaveas[0]:
            textcontent = self.text1.toPlainText()
            f = open(FileSaveas[0], 'w')
            f.write(textcontent)
            self.setTitle(FileSaveas[0])
            f.close()
            self.setWindowFilePath(FileSaveas[0])

    def file_new(self):
        self.file_save()
        self.text1.setText("")
        self.setTitle()

    def file_save(self):
        FileSave = self.windowFilePath()
        textcontent = self.text1.toPlainText()
        if FileSave:
            f = open(FileSave, 'w')
            f.write(textcontent)
            self.setTitle(FileSave)
            f.close()
        else:
            dial = QMessageBox(self)
            dial.setText("저장가능한 경로가 없습니다")
            dial.setWindowTitle("저장 오류 발생")
            dial.show()

    def file_print(self):
        dial = QPrintDialog()
        if dial.exec_():
            self.text1.print(dial.printer())

    def setTitle(self, title="제목없음"):
        self.setWindowTitle(os.path.basename(title) + " - 메모장")

    def format_autoenter(self):
        if self.text1.lineWrapMode() == 1 :
            self.text1.setLineWrapMode(0)
        else:
            self.text1.setLineWrapMode(1)

    def format_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text1.setCurrentFont(font)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '메모장 종료', '저장하지 않고 종료하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = QNotepad()
    app.exec_()
