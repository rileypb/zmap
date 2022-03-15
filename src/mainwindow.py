"""
ZetCode Tkinter tutorial

The example draws lines on the Canvas.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from textwrap import fill
from tkinter import VERTICAL, Y, Tk, Canvas, Text, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        textbox = Text(self, wrap='word', height=0, width=0)
        textbox.pack(fill=BOTH, expand=True, side="left")

        canvas = Canvas(self, bg="blue", height=0, width=0)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=True, side="right")


def main():

    root = Tk()
    ex = Example()
    root.geometry("800x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()