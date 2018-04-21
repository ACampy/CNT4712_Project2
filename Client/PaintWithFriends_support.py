#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 09, 2018 06:06:13 PM


import sys
import threading
import select
from socket import *
import ChatClient as clientClass
import BaseDialog as dialog

try:
    import Tkinter as tk
    import tkSimpleDialog as simpledialog
    import tkColorChooser as colorchooser
except ImportError:
    import tkinter as tk
    import tkinter.messagebox
    import tkinter.simpledialog as simpledialog
    import tkinter.colorchooser as colorchooser

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



color = "black"     #default color
thicc = 1           #default thiccness
toolType = 1        #default line
spinbox = 1
client = clientClass.Client()

class ChatDialog(dialog.BaseDialog):
    def body(self, master):
        tk.Label(master, text="Enter host:").grid(row=0, sticky="w")
        tk.Label(master, text="Enter port:").grid(row=1, sticky="w")

        self.hostEntryField = tk.Entry(master)
        self.portEntryField = tk.Entry(master)

        self.hostEntryField.grid(row=0, column=1)
        self.portEntryField.grid(row=1, column=1)
        return self.hostEntryField

    def validate(self):
        host = str(self.hostEntryField.get())

        try:
            port = int(self.portEntryField.get())

            if(port >= 0 and port < 65536):
                self.result = (host, port)
                return True
            else:
                tkinter.messagebox.showwarning("Error", "The port number has to be between 0 and 65535. Both values are inclusive.")
                return False
        except ValueError:
            tkinter.messagebox.showwarning("Error", "The port number has to be an integer.")
            return False


def send():
    global client
    # clear send buffer on new connection
    # client.toSend = ""
    while True:
        if client.isClientConnected and client.toSend != "":
            client.send(client.toSend)
            client.toSend = ""

def receive():
    global client, top_level, w, root
    while True:
        if client.isClientConnected: 
            message = client.receive(4096)
            # print(message)
            commands = message.split("$")
            for command in commands:
                if command != "" and command != "\n":
                    args = command.split("|")
                    tool = args[0]
                    if tool == "Line" or tool == "Circle" or "S" in tool:
                        try:
                            xold = int(args[1])
                            yold = int(args[2])
                            eventx = int(args[3])
                            eventy = int(args[4])
                            color = args[5]
                            thick = int(args[6])
                            if(tool == "Line"):
                                w.Canvas1.create_line(xold, yold, eventx, eventy, smooth=1, fill=color, width=thick)
                            elif (tool == "Circle"):
                                w.Canvas1.create_oval(eventx - thick, eventy - thick, eventx + thick, eventy + thick, fill=color, width = "0")
                            elif (tool == "SCircle"):
                                w.Canvas1.create_oval(xold, yold,eventx,eventy, fill = color,width = "0")
                            elif (tool == "SRect"):
                                w.Canvas1.create_rectangle(xold, yold,eventx,eventy, fill = color,width = '0')
                            elif (tool == "SLine"):
                                w.Canvas1.create_line(xold, yold, eventx, eventy, fill = color,width = thick)
                        except (ValueError, IndexError):
                            pass
                    elif tool == "Clear":
                        target = args[1]
                        if target == "Chat":
                            w.ChatBox.delete('1.0', tk.END)
                        elif target == "Canvas":
                            culprit = args[2]
                            w.Canvas1.delete("all")
                            w.ChatBox.insert(tk.INSERT, "\n>{0} has cleared the canvas!\n".format(culprit))
                    elif tool == "QUIT":
                        shutdown()
                    elif "Line" not in command and "Circle" not in command and '|' not in command and "S" not in command:
                        w.ChatBox.insert(tk.INSERT, command)
                        w.ChatBox.see(tk.END)

# def set_Tk_var():
#     global spinbox
#     spinbox = StringVar()

def lineTool():
    global toolType
    toolType = 1
    print('PaintWithFriends_support.lineTool')
    sys.stdout.flush()

def circleTool():
    global toolType
    toolType = 2
    print('PaintWithFriends_support.circleTool')
    sys.stdout.flush()

def sCircleTool():
    global toolType
    toolType = 3
    print('PaintWithFriends_support.SCircleTool')
    sys.stdout.flush()

def sCircleTool2():
    global toolType
    toolType = 4
    print('PaintWithFriends_support.SCircleTool2')
    sys.stdout.flush()

def sRectTool():
    global toolType
    toolType = 5
    print('PaintWithFriends_support.sRectTool')
    sys.stdout.flush()

def sRectTool2():
    global toolType
    toolType = 6
    print ('PaintWithFriends_support.sRectTool2')
    sys.stdout.flush()

def sLineTool():
    global toolType
    toolType = 7
    print('PaintWithFriends_support.sLineTool')
    sys.stdout.flush()

def sLineTool2():
    global toolType
    toolType = 8
    print('PaintWithFriends_support.sLineTool2')
    sys.stdout.flush()

def changeRed():
    global color
    color = "red"
    print('PaintWithFriends_support.changeRed')
    sys.stdout.flush()

def changeBlack():
    global color
    color = "black"
    print('PaintWithFriends_support.changeBlack')
    sys.stdout.flush()

def changeBlue():
    global color
    color = "blue"
    print('PaintWithFriends_support.changeBlue')
    sys.stdout.flush()

def changeWhite():
    global color
    color = "white"
    print('PaintWithFriends_support.changeWhite')
    sys.stdout.flush()

def changeGreen():
    global color
    color = "#00ff00"
    print('PaintWithFriends_support.changeGreen')
    sys.stdout.flush()

def changeYellow():
    global color
    color = "yellow"
    print('PaintWithFriends_support.changeYellow')
    sys.stdout.flush()

def changeCyan():
    global color
    color = "cyan"
    print('PaintWithFriends_support.changeCyan')
    sys.stdout.flush()

def changeMagenta():
    global color
    color = "magenta"
    print('PaintWithFriends_support.changeMagenta')
    sys.stdout.flush()

def changePick():
    global color
    _, color = colorchooser.askcolor()
    print('PaintWithFriends_support.changeMagenta')
    sys.stdout.flush()

def scaleSize(*args): 
    global thicc
    print('PaintWithFriends_support.scaleSize')
    thicc = int(args[0])
    sys.stdout.flush()

sendThread = threading.Thread(target=send)
recvThread = threading.Thread(target=receive)
sendThread.start()
recvThread.start()
def connect():
    print('PaintWithFriends_support.connect')
    global client, root, w, top_level, recvThread, sendThread
    if client.isClientConnected:
        tkinter.messagebox.showwarning("Error", "Already connected to a server!\nPlease disconnect first and try again.")
    else:
        # client.connect('localhost',50000)
        dialogResult = ChatDialog(root).result
        if dialogResult:
            result = client.connect(dialogResult[0], dialogResult[1])

            if result:
                answer = simpledialog.askstring("Input", "Please provide a nickname", parent=root)
                while answer is None:
                    answer = simpledialog.askstring("Input", "Please provide a nickname", parent=root)
                client.toSend = answer

            else:
                tkinter.messagebox.showwarning("Error", "Unable to connect to the server.")
    sys.stdout.flush()

def quit():
    global w, recvThread, sendThread
    print('PaintWithFriends_support.quit')
    if client.isClientConnected and tkinter.messagebox.askyesno("Disconnect", "Are you sure you want to disconnect?"):
        client.send("/Quit")
        w.Canvas1.delete("all")
        w.ChatBox.delete('1.0', tk.END)
        client.disconnect()
    elif not client.isClientConnected:
        tkinter.messagebox.showwarning("Error", "You are not connected to a server.")
    sys.stdout.flush()

def shutdown():
    global w
    print('PaintWithFriends_support.shutdown')
    w.Canvas1.delete("all")
    w.ChatBox.delete('1.0', tk.END)
    client.disconnect()
    tkinter.messagebox.showinfo("Server Disconnect", "This server has been shut down remotely.")
    sys.stdout.flush()

def clean():
    global client
    print('attempt_support.clean')
    if client.isClientConnected and tkinter.messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the canvas?\nThis cannot be undone!"):
        w.Canvas1.delete("all")
        client.toSend += "$Clear$"
    elif not client.isClientConnected:
        tkinter.messagebox.showwarning("Error", "You must be connected to a server to preform this action.")
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level, w, root, sendThread, recvThread
    if client.isClientConnected:
        try:
            client.send("/Quit")
        except ConnectionAbortedError:
            pass
        client.disconnect()
    recvThread.join(1)
    sendThread.join(1)
    root.destroy()
    top_level = None


if __name__ == '__main__':
    import PaintWithFriends
    PaintWithFriends.vp_start_gui()
    #main()

