#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 09, 2018 06:06:25 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import PaintWithFriends_support

top = None
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = Tk()
    top = New_Toplevel (root)
    PaintWithFriends_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    PaintWithFriends_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None

#Drawing line code starts here ***************************************************************
# color = "black"
b1 = "up"
xold, yold = None, None
input_user = ''

def Enter_pressed(event):
    from PaintWithFriends_support import client
    global input_user
    input_get = event.widget.get()
    if ('|' not in input_get):
        client.toSend += input_get.lower()
    input_user = ''
    input_get = ''
    event.widget.delete(0,END)
    return "break"

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    from PaintWithFriends_support import color, thicc, toolType, client
    if b1 == "down" and client.isClientConnected:
        global xold, yold, color
        if xold is not None and yold is not None:
            if toolType == 1: #line
                client.toSend += "$Line|{0}|{1}|{2}|{3}|{4}|{5}$".format(xold,yold,event.x,event.y,color,thicc)
                event.widget.create_line(
                    xold,
                    yold,
                    event.x,
                    event.y,
                    smooth=1,
                    fill=color,
                    width= thicc
                )
                          # here's where you draw it. smooth. neat.
            elif toolType == 2: #circle
                # print(event.x)
                # print(event.y)
                # print(thicc)
                client.toSend += "$Circle|{0}|{1}|{2}|{3}|{4}|{5}$".format(xold,yold,event.x,event.y,color,thicc)
                event.widget.create_oval(event.x - thicc, event.y - thicc, event.x + thicc, event.y + thicc, fill= color, width = "0")
        xold = event.x
        yold = event.y

def main():
    
    # root = Tk()
    # my_gui = GUI(root)  #my_gui needed???
    # frame = Tk.Frame()
    drawing_area = Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    print("drawing test")
    root.mainloop()
    
#Drawing code ends here ********************************************************************


#Circle tool********************************************************************************
#t= ttk.Tk()

# def createCircle(self, x, y, r, **kwargs):
    
#     return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
#     Canvas.create_circle = createCircle

#Circle ends here **************************************************************************

#Draw line
# def drawLine():
#     Canvas1 = Canvas()
#     Canvas1.create_line(15, 25, 200, 25, color = "red")
#     print("draw line")

class New_Toplevel:
    global input_user    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("800x450+629+228")
        top.title("Paint With Friends")
        top.configure(highlightcolor="black")

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=PaintWithFriends_support.connect,
                font="TkMenuFont",
                foreground="#000000",
                label="Connect")
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=PaintWithFriends_support.quit,
                font="TkMenuFont",
                foreground="#000000",
                label="Disconnect")
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=PaintWithFriends_support.clean,
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Clear Canvas")

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.23, rely=0.13, relheight=0.85, relwidth=0.71)
        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(cursor="pencil")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=511)
        # self.Canvas1.pack()
        self.Canvas1.bind("<Motion>", motion)
        self.Canvas1.bind("<ButtonPress-1>", b1down)
        self.Canvas1.bind("<ButtonRelease-1>", b1up)
        print("drawing test")

        #Color Buttons ***************************************************************

        self.ButtonWhite = Button(top)
        self.ButtonWhite.place(relx=0.95, rely=0.14, height=26, width=26)
        self.ButtonWhite.configure(activebackground="#d9d9d9")
        self.ButtonWhite.configure(background="#ffffff")
        self.ButtonWhite.configure(command=PaintWithFriends_support.changeWhite)
        
        self.ButtonBlack = Button(top)
        self.ButtonBlack.place(relx=0.95, rely=0.21, height=26, width=26)
        self.ButtonBlack.configure(activebackground="#d9d9d9")
        self.ButtonBlack.configure(background="#000000")
        self.ButtonBlack.configure(command=PaintWithFriends_support.changeBlack)
        
        self.ButtonRed = Button(top)
        self.ButtonRed.place(relx=0.95, rely=0.28, height=26, width=26)
        self.ButtonRed.configure(activebackground="#d9d9d9")
        self.ButtonRed.configure(background="#d90000")
        self.ButtonRed.configure(command=PaintWithFriends_support.changeRed)

        self.ButtonBlue = Button(top)
        self.ButtonBlue.place(relx=0.95, rely=0.35, height=26, width=26)
        self.ButtonBlue.configure(activebackground="#d9d9d9")
        self.ButtonBlue.configure(background="#0000ff")
        self.ButtonBlue.configure(command=PaintWithFriends_support.changeBlue)

        self.ButtonGreen = Button(top)
        self.ButtonGreen.place(relx=0.95, rely=0.42, height=26, width=26)
        self.ButtonGreen.configure(activebackground="#d9d9d9")
        self.ButtonGreen.configure(background="#00ff00")
        self.ButtonGreen.configure(command=PaintWithFriends_support.changeGreen)
        
        self.ButtonYellow = Button(top)
        self.ButtonYellow.place(relx=0.95, rely=0.49, height=26, width=26)
        self.ButtonYellow.configure(activebackground="#d9d9d9")
        self.ButtonYellow.configure(background="#ffff00")
        self.ButtonYellow.configure(command=PaintWithFriends_support.changeYellow)

        self.ButtonCyan = Button(top)
        self.ButtonCyan.place(relx=0.95, rely=0.56, height=26, width=26)
        self.ButtonCyan.configure(activebackground="#d9d9d9")
        self.ButtonCyan.configure(background="cyan")
        self.ButtonCyan.configure(command=PaintWithFriends_support.changeCyan)

        self.ButtonMagenta = Button(top)
        self.ButtonMagenta.place(relx=0.95, rely=0.63, height=26, width=26)
        self.ButtonMagenta.configure(activebackground="#d9d9d9")
        self.ButtonMagenta.configure(background="magenta")
        self.ButtonMagenta.configure(command=PaintWithFriends_support.changeMagenta)

        #Scale Slider Widget ******************************************************
        self.ScaleSize = Scale(top)
        self.ScaleSize.place(relx=0.78, rely=0.0, relwidth=0.13, relheight=0.0
                , height=55)
        self.ScaleSize.configure(activebackground="#d9d9d9")
        self.ScaleSize.configure(command=PaintWithFriends_support.scaleSize)
        self.ScaleSize.configure(font="TkTextFont")
        self.ScaleSize.configure(cursor="sb_h_double_arrow")
        self.ScaleSize.configure(from_="1.0")
        self.ScaleSize.configure(label="Size")
        self.ScaleSize.configure(orient="horizontal")
        self.ScaleSize.configure(troughcolor="#d9d9d9")

        #Brush Type Widgets ********************************************************
        self.BrushType = LabelFrame(top)
        self.BrushType.place(relx=0.23, rely=0.01, relheight=0.11, relwidth=0.19)
        self.BrushType.configure(relief=GROOVE)
        self.BrushType.configure(text='''Brush Type''')
        self.BrushType.configure(width=150)

        self.Line = Button(top)
        self.Line.place(relx=0.33, rely=0.05, height=26, width=59)
        self.Line.configure(activebackground="#d9d9d9")
        self.Line.configure(text='''Line''')
        self.Line.configure(command=PaintWithFriends_support.lineTool)

        self.Circle = Button(top)
        self.Circle.place(relx=0.24, rely=0.05, height=26, width=59)
        self.Circle.configure(activebackground="#d9d9d9")
        self.Circle.configure(text='''Circle''')
        self.Circle.configure(command=PaintWithFriends_support.circleTool)

        #Shape Widgets **************************************************************
        self.Shapes = LabelFrame(top)
        self.Shapes.place(relx=0.45, rely=0.01, relheight=0.11, relwidth=0.3)
        self.Shapes.configure(relief=GROOVE)
        self.Shapes.configure(text='''Shapes''')
        self.Shapes.configure(width=150)

        #Chat Widgets ****************************************************************
        self.ChatLabel = Label(top)
        self.ChatLabel.place(relx=0.01, rely=0.09, height=18, width=36)
        self.ChatLabel.configure(text='''Chat''')

        self.ChatBox = Text(top)
        self.ChatBox.place(relx=0.01, rely=0.13, relheight=0.8, relwidth=0.2)
        self.ChatBox.configure(background="white")
        self.ChatBox.configure(font="TkTextFont")
        self.ChatBox.configure(selectbackground="#c4c4c4")
        self.ChatBox.configure(width=146)
        self.ChatBox.configure(wrap=WORD) 

        self.Entry1 = Entry(top, text=input_user)
        self.Entry1.place(relx=0.01, rely=0.93,height=20, relwidth=0.2)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=156)
        self.Entry1.bind("<Return>", Enter_pressed)




if __name__ == '__main__':
    vp_start_gui()
    # drawLine()
    #main()
    # PaintWithFriends_support.main()


