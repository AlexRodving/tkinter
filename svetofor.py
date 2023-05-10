from tkinter import *

root = Tk()
root.geometry('200x119+1000+300')
root.resizable(0,0)
root.title('Светофор')

def red():
    lab['text'] = 'Красный'
    entr.delete(0, END)
    entr.insert(0, '#ff0000')

def yellow():
    lab['text'] = 'Желтый'
    entr.delete(0, END)
    entr.insert(0, 'ffff00')

def green():
    lab['text'] = 'Зеленый'
    entr.delete(0, END)
    entr.insert(0, '00ff00')

lab = Label(root)
lab.pack(fill=X)
entr = Entry(root, justify='center')
entr.pack(fill=X)

btn1= Button(root, bg="#ff0000", command=red)
btn1.pack(fill=X)
btn2= Button(root, bg="#ffff00", command=yellow)
btn2.pack(fill=X)
btn3= Button(root, bg="#00ff00", command=green)
btn3.pack(fill=X)

root.mainloop()