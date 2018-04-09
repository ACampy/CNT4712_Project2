from tkinter import *

b1 = "up"
xold, yold = None, None
color = "black"

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        

        self.label = Label(master, text="Paint")
        self.label.grid(columnspan = 2, sticky = W)
        self.label.pack()

        self.buttonRed = Button(master, text="Red", command=changeRed)
        self.buttonRed.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.grid(row = 1, column = 1)
        self.close_button.pack(side = RIGHT)
        


def main():
    
    root = Tk()
    my_gui = GUI(root)  #my_gui needed???
    # frame = Tk.Frame()
    drawing_area = Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

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
    global color
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE, fill=color)
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

def changeRed():
        global color
        color = "red"
        print("Color changed to Red")


if __name__ == "__main__":
    main()