from tkinter import *
from tkinter import ttk
from compiler import Compiler

DEBUG = True

zmap_compiler = Compiler()
text = None
canvas = None

def get_text():
    return text.get("1.0", END)


def setup():
    global text
    global canvas
    root = Tk()
    root.geometry('1200x600')

    style = ttk.Style()
    style.configure("Horizontal.TScrollbar", foreground="red", background="white")

    container = ttk.Frame(root, width=4)
    container.pack(fill=BOTH, expand=1)

    text = Text(container, width=60)
    text.pack(fill=BOTH, expand=0, side=LEFT)

    canvas_container = ttk.Frame(container, width=60)
    canvas_container.pack(fill=BOTH, expand=1, side=RIGHT)
    
    canvas = Canvas(canvas_container, width=4)
    scrollbar_x = ttk.Scrollbar(canvas_container, orient="horizontal", command=canvas.xview)
    scrollbar_y = ttk.Scrollbar(canvas_container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set)
    canvas.configure(xscrollcommand=scrollbar_x.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar_x.pack(side=BOTTOM, fill=X)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    if DEBUG:
        text.insert(1.0, """[Courtyard]d<->[Winding Stair]
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
""")
    return root


def compile(event):
    if event.state == 4: # control
        canvas.delete("all")
        zmap_compiler.compile(get_text(), canvas)


def save(event):
    if event.state == 4: # control
        pass


def load(event):
    if event.state == 4: # control
        pass


if __name__ == '__main__':
    print("Welcome to zmap!")

    root = setup()

    root.bind('k', lambda event: compile(event))
    root.bind('s', lambda event: save(event))
    root.bind('l', lambda event: load(event))

    root.mainloop()