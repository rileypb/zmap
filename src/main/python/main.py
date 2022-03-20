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