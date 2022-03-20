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


class ZApp:
    def __init__(self):
        self.appctxt = ApplicationContext()
        self.current_filename = None
        self.zmap_compiler = Compiler()

    def setup(self):
        self.win = QMainWindow()
        self.win.setWindowTitle("zmap")
        self.win.show()

        self.settings = QSettings("Brainfreeze", "zmap")

        rsrc = self.appctxt.get_resource('zmap.ui')
        uic.loadUi(rsrc, self.win)

        self.win.splitter.setSizes([200, 400])

        self.scene = QGraphicsScene()
        self.win.graphicsView.setScene(self.scene)
        self.win.actionCompile.triggered.connect(self.compile)
        self.win.actionSave.triggered.connect(self.save_zmap)
        self.win.actionOpen.triggered.connect(self.open_zmap)

        self.win.graphChooser.currentIndexChanged.connect(self.display)

    def run(self):
        exit_code = self.appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
        self.settings.sync()
        sys.exit(exit_code)

    def compile(self, *args):
        self.scene.clear()
        map_names = self.zmap_compiler.compile(self.win.plainTextEdit.toPlainText())
        current_rendered_map = self.win.graphChooser.currentText()
        self.win.graphChooser.clear()
        self.win.graphChooser.addItems(map_names)
        if current_rendered_map in map_names:
            self.win.graphChooser.setCurrentIndex(map_names.index(current_rendered_map))

    def display(self, *args):    
        self.scene.clear()
        self.zmap_compiler.display(self.win.graphChooser.currentText(), self.scene)        

    def save_zmap(self, *args):
        if self.current_filename:
            with open(self.current_filename, 'w') as word_file:
                word_file.write(self.win.plainTextEdit.toPlainText())
        else:
            filedir = self.settings.value("file/dir", os.path.expanduser("~"))
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(self.win, "Saving zmap file", filedir, "zmap Files (*.zmap);;All Files (*)", options=options)
            if filename:
                dirname = os.path.dirname(filename)
                self.settings.setValue("file/dir", dirname)
                with open(filename, 'w') as word_file:
                    word_file.write(self.win.plainTextEdit.toPlainText())

    def open_zmap(self, *args):
        filedir = self.settings.value("file/dir", os.path.expanduser("~"))
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self.win, "Opening zmap file", filedir, "zmap Files (*.zmap);;All Files (*)", options=options)
        if filename:
            dirname = os.path.dirname(filename)
            self.settings.setValue("file/dir", dirname)
            with open(filename, 'r') as word_file:
                mapstring = word_file.read()
                self.win.plainTextEdit.setPlainText(mapstring)
                self.compile()
                self.current_filename = filename


if __name__ == '__main__':
    zapp = ZApp()
    zapp.setup()
    zapp.run()