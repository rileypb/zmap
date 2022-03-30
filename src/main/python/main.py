import sys, os, datetime

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtWidgets import (
    QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
)

from PyQt5.QtCore import ( 
    QSettings
)
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat, QCloseEvent

from PyQt5 import uic
from compiler import Compiler
from highlight import SyntaxHighlighter

from display import Display
from arrange import Arranger
from layout import Layout

class ZApp:
    def __init__(self):
        self.appctxt = ApplicationContext()
        self.current_filename = None
        self.zmap_compiler = Compiler()
        self.display = Display()
        self.arranger = Arranger()
        self.layout = Layout()
        self.original_text = ""

    def closeEvent(self, event:QCloseEvent):
        confirmation = self.confirm_destructive_action("quitting")
        cancel = confirmation & QMessageBox.Cancel
        if cancel:
            event.ignore()
        else:
            event.accept()

    def setup(self):
        self.win = QMainWindow()
        self.win.setWindowTitle("zmap")
        self.win.show()

        self.settings = QSettings("Brainfreeze", "zmap")

        rsrc = self.appctxt.get_resource('zmap.ui')
        uic.loadUi(rsrc, self.win)

        background_img_rsrc = self.appctxt.get_resource('vellum1.jpeg')
        self.display.background_image = background_img_rsrc

        self.win.splitter.setSizes([200, 400])

        self.win.actionCompile.triggered.connect(self.compile)
        self.win.actionNew.triggered.connect(self.new_zmap)
        self.win.actionSave.triggered.connect(self.save_zmap)
        self.win.actionSave_As.triggered.connect(self.save_as)
        self.win.actionOpen.triggered.connect(self.open_zmap)
        self.win.actionOneStep.triggered.connect(self.do_layout)

        self.win.graphChooser.currentIndexChanged.connect(self.display_map)

        self.highlighter = SyntaxHighlighter(self.win.plainTextEdit.document())
        self.win.plainTextEdit.document().contentsChange.connect(self.textChanged)

        self.win.closeEvent = self.closeEvent
        

    def do_layout(self):
        map = self.maps[self.win.graphChooser.currentText()]
        
        self.scene.clear()
        self.layout.one_step(map)
        self.display.display(map, self.scene)    

    def textChanged(self, *args):
        if self.highlighter and self.highlighter.is_highlighted():
            self.highlighter.clear_highlight()

    def run(self):
        exit_code = self.appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
        self.settings.sync()
        sys.exit(exit_code)

    def highlight_error(self, line):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor("red"))
        self.highlighter.clear_highlight()
        self.highlighter.highlight_line(line-1, fmt)
        self.win.plainTextEdit.update();

    def compile(self, *args):
        self.maps, exc = self.zmap_compiler.compile(self.win.plainTextEdit.toPlainText())
        
        if exc:
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            self.win.outputFrame.append(f'{time} {exc.args[0][2]}')
            self.highlight_error(exc.args[0][0])
        else:
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            self.win.outputFrame.append(f'{time} compilation successful')
            current_rendered_map = self.win.graphChooser.currentText()
            self.win.graphChooser.clear()
            map_names = list(self.maps.keys())
            self.win.graphChooser.addItems(map_names)
            if current_rendered_map in map_names:
                self.win.graphChooser.setCurrentIndex(map_names.index(current_rendered_map))

    def display_map(self, *args):    
        if not self.win.graphChooser.currentText():
            return
        map = self.maps[self.win.graphChooser.currentText()]
        if not map.arranged:
            self.arranger.arrange(map)
            
        self.scene = QGraphicsScene()
        self.win.graphicsView.setScene(self.scene)

        for i in range(200):
            self.layout.one_step(map)

        self.display.display(map, self.scene)    
        
         

    def confirm_destructive_action(self, action):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Continue {action}?")
        msg.setInformativeText("You will lose your current progress")
        msg.setWindowTitle("Continue?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msg.exec_()

    def new_zmap(self, *args):
        if self.win.plainTextEdit.toPlainText() != self.original_text:
            confirmation = self.confirm_destructive_action("creating new file")
            cancel = confirmation & QMessageBox.Cancel
            if cancel:
                return
        self.win.plainTextEdit.setPlainText("")
        self.original_text = ""
        self.current_filename = None

    def save_zmap(self, *args, do_save_as=False):
        if self.current_filename and not do_save_as:
            with open(self.current_filename, 'w') as word_file:
                word_file.write(self.win.plainTextEdit.toPlainText())
            self.original_text = self.win.plainTextEdit.toPlainText()
        else:
            filedir = self.settings.value("file/dir", os.path.expanduser("~"))
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(self.win, "Saving zmap file", filedir, "zmap Files (*.zmap);;All Files (*)", options=options)
            if filename:
                dirname = os.path.dirname(filename)
                self.settings.setValue("file/dir", dirname)
                with open(filename, 'w') as word_file:
                    word_file.write(self.win.plainTextEdit.toPlainText())
                self.current_filename = filename
                self.original_text = self.win.plainTextEdit.toPlainText()

    def save_as(self, *args) :
        self.save_zmap(do_save_as=True)

    def open_zmap(self, *args):
        if self.win.plainTextEdit.toPlainText() != self.original_text:
            confirmation = self.confirm_destructive_action("opening file")
            cancel = confirmation & QMessageBox.Cancel
            if cancel:
                return
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
                self.original_text = self.win.plainTextEdit.toPlainText()


if __name__ == '__main__':
    import menu_icons
    zapp = ZApp()
    zapp.setup()
    zapp.run()