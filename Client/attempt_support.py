#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 09, 2018 06:06:13 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#default color
color = "black"

def changeRed():
    global color
    color = "red"
    print('attempt_support.changeRed')
    sys.stdout.flush()

def changeBlack():
    global color
    color = "black"
    print('attempt_support.changeBlack')
    sys.stdout.flush()

def changeBlue():
    global color
    color = "blue"
    print('attempt_support.changeBlue')
    sys.stdout.flush()

def changeWhite():
    global color
    color = "white"
    print('attempt_support.changeWhite')
    sys.stdout.flush()

def changeGray():
    global color
    color = "gray"
    print('attempt_support.changeGray')
    sys.stdout.flush()

def changeYellow():
    global color
    color = "yellow"
    print('attempt_support.changeYellow')
    sys.stdout.flush()

def connect():
    print('attempt_support.connect')
    sys.stdout.flush()

def quit():
    print('attempt_support.quit')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import attempt
    attempt.vp_start_gui()


