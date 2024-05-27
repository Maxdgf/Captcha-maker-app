from tkinter import *
from captcha.image import ImageCaptcha
from random import randint
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk




def captcha():
    pattern = a.get()
    save = b.get()
    captcha = ImageCaptcha(width=300, height=100)
    captcha.write(pattern, save + '.png')


def quit():
    root.destroy()



def show_captcha():
     global img, img_tk, draw
     filename = filedialog.askopenfilename()
     img = Image.open(filename)
     img_tk = ImageTk.PhotoImage(img)
     window.config(width=img.width, height=img.height)
     window.create_image(0, 0, anchor=tk.NW, image=img_tk)
     draw = ImageDraw.Draw(img)




root = Tk()
root.title('Captcha Maker')
root.geometry('800x500')
root.resizable(0,0)
root.iconbitmap('LOGO32.ico')
window = Canvas(root, width=300, height=100, bg='white', highlightbackground='black')
window.place(x=245, y=100)

Button(root, text='Создать капчу', width=15, height=5, bg='orange', font='Verdana 10 bold', command=captcha).place(x=25, y=380)
Button(root, text='Выйти', width=10, bg='red', command=quit).place(x=0, y=0)
Label(root, text='Создать свой тескт для капчи:').place(x=320, y=300)
Button(root, text='Просмотреть капчу\nпапка Captcha maker',width=17, font='Italic 10 bold', bg='yellow', command=show_captcha).place(x=25, y=300)
Button(root, text='Добавить текст для капчи', width=25, font='Italic 10 bold').place(x=320, y=400)
Label(root, text='Добавить имя сохраняемого файла:').place(x=580, y=70)
Button(root, text='Добавить имя', width=15, font='Italic 10 bold', command=captcha).place(x=620, y=130)
b = Entry(root, width=20)
b.place(x=620, y=100)
a = Entry(root, width=65)
a.place(x=320, y=350)

root.mainloop()
