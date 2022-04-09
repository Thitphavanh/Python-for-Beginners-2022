# GUI-calculate.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Program shipping cost')
GUI.geometry('600x550')


bg = PhotoImage(file='phenomenal_logistic_icon.png')

BG = Label(GUI, image=bg)
BG.pack(pady=5)

label = Label(GUI, text='Please entry kilo (Kg) in this field',
              font=(None, 18))
label.pack(pady=5)

v_quantity = StringVar()  # ເປັນໂຕແປທີ່ໃຊ້ເກັບຂໍ້ຄວາມເມື່ອພິມແລ້ວ
Entry1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 18))
Entry1.pack(pady=5)


def Calculate():
    try:
        quantity = float(v_quantity.get())
        calculate = quantity * 15000
        messagebox.showinfo(
            'Total value', 'Total value {} LAK'.format(calculate))
        v_quantity.set('')
        Entry1.focus()
    except:
        messagebox.showerror('You filled in wrong', 'Only fill in quantity')
        v_quantity.set('')
        Entry1.focus()


Button1 = ttk.Button(GUI, text='Calculate', command=Calculate)
Button1.pack(ipadx=20, ipady=10, pady=10)

GUI.mainloop()
