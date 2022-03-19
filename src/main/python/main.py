import sys, os

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene, QFileDialog
)

from PyQt5.QtCore import ( 
    QRectF, QSettings
)

from PyQt5 import uic
from compiler import Compiler

DEBUG = True
debug_text = \
"""[Courtyard]sw-->?
[Courtyard]e-->*(Special)
[Courtyard]se-->*(Special)
[Plain Hall]s<->[Courtyard]
[Plain Hall]n<->[Rec Area]
[Plain Hall]ne<->[Rec Corridor]
[Courtyard]w<->[West Wing]
[Rec Area]e<->[Rec Corridor]
[Rec Corridor]e<->[Mess Corridor]
[Mess Corridor]s<->[Mess Hall]
[Mess Hall]s<->[Kitchen]
[Mess Corridor]n<->[Storage West]
[Mess Corridor]e<->[Dorm Corridor]
[Rec Corridor]n<->[Dorm B]<
[Rec Corridor]s<->[Dorm A]<
[Dorm A]s<->[SanFac A]<
[Dorm B]n<->[SanFac B]<
[Dorm Corridor]n<->[Dorm D]<
[Dorm D]n<->[SanFac D]<
[Dorm Corridor]s<->[Dorm C]<
[Dorm C]s<->[SanFac C]<
[Dorm Corridor]e<->[Corridor Junction]
[Corridor Junction]n<->[Admin Corridor South]
[Admin Corridor South]e<->[SanFac E]
[Admin Corridor South]n<->[Admin Corridor]
[Corridor Junction]s<->[Mech Corridor North]
[Corridor Junction]e<->[Elevator Lobby]
[Elevator Lobby]e<->[Booth 2]
[Elevator Lobby]n<->[Upper Elevator]<
[Elevator Lobby]s<->[Lower Elevator]<
[Admin Corridor]n<->[Admin Corridor North]
[Admin Corridor]w<->[Systems Monitors]
[Mech Corridor North]e<->[Storage East]
[Mech Corridor North]w<->ne[Physical Plant]
[Mech Corridor North]s<->[Mech Corridor]
[Physical Plant]se<->w[Mech Corridor]
[Mech Corridor]e<->[Reactor Control]
[Mech Corridor]s<->[Mech Corridor South]
[Mech Corridor South]sw<->[Tool Room]
[Tool Room]e<->[Machine Shop]
[Mech Corridor South]s<->[Machine Shop]
[Mech Corridor South]se<->[Robot Shop]
[Machine Shop]e<->[Robot Shop]
[Reactor Control]e<->[Reactor Elevator]<
[Reactor Control]d-->?
[Admin Corridor North]w<->[Small Office]
[Admin Corridor North]n-->?
[Admin Corridor North]e<->[Plan Room]
[Small Office]w<->[Large Office]
[Booth 1]s<->[Conference Room]
[Conference Room]s<->[Rec Area]
[Conference Room]nw-->?
"""

settings = None
scene = None
win = None
zmap_compiler = Compiler()

current_filename = None

def compile(*args):
    scene.clear()
    map_names = zmap_compiler.compile(win.plainTextEdit.toPlainText())
    current_rendered_map = win.graphChooser.currentText()
    win.graphChooser.clear()
    win.graphChooser.addItems(map_names)
    if current_rendered_map in map_names:
        win.graphChooser.setCurrentIndex(map_names.index(current_rendered_map))

def display(*args):    
    scene.clear()
    zmap_compiler.display(win.graphChooser.currentText(), scene)        

def save_zmap(*args):
    if current_filename:
        with open(current_filename, 'w') as word_file:
            word_file.write(win.plainTextEdit.toPlainText())
    else:
        filedir = settings.value("file/dir", os.path.expanduser("~"))
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(win, "Saving zmap file", filedir, "zmap Files (*.zmap);;All Files (*)", options=options)
        if filename:
            dirname = os.path.dirname(filename)
            settings.setValue("file/dir", dirname)
            with open(filename, 'w') as word_file:
                word_file.write(win.plainTextEdit.toPlainText())

def open_zmap(*args):
    global current_filename
    filedir = settings.value("file/dir", os.path.expanduser("~"))
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(win, "Opening zmap file", filedir, "zmap Files (*.zmap);;All Files (*)", options=options)
    if filename:
        dirname = os.path.dirname(filename)
        settings.setValue("file/dir", dirname)
        with open(filename, 'r') as word_file:
            mapstring = word_file.read()
            win.plainTextEdit.setPlainText(mapstring)
            compile()
            current_filename = filename


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    win = QMainWindow()
    win.setWindowTitle("zmap")
    win.show()

    rsrc = appctxt.get_resource('zmap.ui')
    print(rsrc)

    settings = QSettings("Brainfreeze", "zmap")
    
    uic.loadUi(rsrc, win)
    if DEBUG:
        win.plainTextEdit.setPlainText("")

    win.splitter.setSizes([200, 400])

    scene = QGraphicsScene()
    win.graphicsView.setScene(scene)
    win.actionCompile.triggered.connect(compile)
    win.actionSave.triggered.connect(save_zmap)
    win.actionOpen.triggered.connect(open_zmap)

    win.graphChooser.currentIndexChanged.connect(display)

    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    settings.sync()
    sys.exit(exit_code)