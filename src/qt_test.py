import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene
)

from PyQt5.QtCore import ( 
    QRectF 
)

from PyQt5 import uic
from compiler import Compiler

DEBUG = True
debug_text = """[Courtyard]d<->[Winding Stair]
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
"""

scene = None
win = None
zmap_compiler = Compiler()

def compile(*args):
    scene.clear()
    zmap_compiler.compile(win.plainTextEdit.toPlainText(), scene)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = QMainWindow()
    win.show()
    uic.loadUi('zmap.ui', win)
    if DEBUG:
        win.plainTextEdit.setPlainText(debug_text)

    win.splitter.setSizes([200, 400])

    scene = QGraphicsScene()
    scene.addText("Hello, World!")
    win.graphicsView.setScene(scene)
    win.actionCompile.triggered.connect(compile)

    app.exec()