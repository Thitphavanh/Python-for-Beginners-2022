# GUI-mouse.py
from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Click calendar program')
GUI.geometry('500x300')


def Calendar():
    pg.click(1814, 1062)


Button1 = Button(GUI, text='Calendar1', command=Calendar)
Button1.pack(ipadx=20, ipady=10, pady=20)

Button2 = ttk.Button(GUI, text='Calendar2', command=Calendar)
Button2.pack(ipadx=20, ipady=10, pady=20)


def Google():
    webbrowser.open('https://www.google.com')


Button3 = ttk.Button(GUI, text='Google', command=Google)
Button3.pack(ipadx=20, ipady=10)

GUI.mainloop()
