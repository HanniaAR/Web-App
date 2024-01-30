"""
The program may conatin:
- Window
- Size
- No resize
- Menu (Init, add, info, exit)
- Diferent windows
- Froms to add a product
- Save data
- Show data list in home
- Exit option
"""

from tkinter import *

window = Tk()

window.geometry('400x400')
window.title('Tkinter Project')
window.resizable(0,0)

home_label = Label(window, text='Home')
add_label = Label(window, text='Add product')
info_label = Label(window, text='Information')
data_label = Label(window, text='Created by Hannia Arias - 2024')

def home():
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial',30),
        padx=150,
        pady=20
    )
    home_label.grid(row=0, column=0)

    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


def add():
    add_label.config(
        fg='white',
        bg='black',
        font=('Arial',30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0, column=0)

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    info_label.config(
        fg='white',
        bg='black',
        font=('Arial',30),
        padx=100,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    add_label.grid_remove()
    home_label.grid_remove()

menu_sup = Menu(window)
menu_sup.add_command(label='Home', command=home)
menu_sup.add_command(label='Add', command=add)
menu_sup.add_command(label='Information', command=info)
menu_sup.add_command(label='Exit', command=window.quit)
window.config(menu=menu_sup)

window.mainloop()