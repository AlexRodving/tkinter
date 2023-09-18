from tkinter import *
from tkinter import ttk # для системных кнопок
import time


#-------------------- Окно ----------------------------
root = Tk()   #создать окно

root.title('TestTK')

#root.iconbitmap('путь') #иконка

root.geometry('400x400+1000+300') #размер окна, место появления

root.resizable(0,0) #разрешить/запретить растягивать окно

root.config(bg='black') #фон окна

#------------------- Функции -----------------------------

def check_time():          #command для кнопки btn_tm
    # print(time.strftime('%H:%M:%S'))
    btn_tm['text'] = time.strftime('%H:%M:%S')


def click():                #command для кнопки btn
    print('Click!')
    
count = 0                   
def counter():              #command для кнопки btn_count
    global count
    count += 1
    root.title(f'Counter: {count}')
    
count_txt = 0               
def counter_txt():           #command для кнопки btn_txt
    global count_txt
    count_txt += 1
    txt['text'] = count_txt
    
def add_str():                 #command для кнопки btn_add
    e.insert(END, 'Hello!')
    
def delete_str():               #command для кнопки btn_del
    e.delete(0, END)
    
def get_str():                  #command для кнопки btn_get
    txt2['text'] = e.get()

#-------------------- Кнопки ------------------------------

btn = Button(root, text="Кнопка", command=click, width=10, 
             font=("Comics Sans MS", 20, "italic")).pack() 
#кнопка Tkinter + упаковка
#переменая = Кнопка Tk(окно, текст на кнопке, функция, ширина, 
# шрифт).запаковать/отрисовать

btn2 = ttk.Button(root, text="Кнопка2",) #кнопка системная
btn2.pack() #Упаковка кнопки

btn3 = Button(root, text="Кнопка3")
btn3.configure(width=10, height=2)
btn3['font'] = "Arial 15"
btn3.pack()

btn_tm = Button(root, text='Time', command=check_time)
btn_tm.pack()

btn_count = Button(root, text="Counter", command=counter)
btn_count.pack()

btn_txt = Button(root, text="Counter_TXT", command=counter_txt)
btn_txt.pack()

btn_add = Button(root, text="Add",command=add_str).pack()
btn_del = Button(root, text="Delete",command=delete_str).pack()
btn_get = Button(root, text="Get", command=get_str).pack()

#--------------------- Label ----------------------------------

txt = Label(root, text='Текст')
txt.pack()

txt2 = Label(root, bg="black", fg="white")
txt2.pack(fill=X,)
print("hello")
 
#---------------------- IMG ------------------------------------

# img = PhotoImage(file='путь')   #Достать картинку
# l_img = Label(root, image=img)  #Положить в Label
# l_img.pack()                    #Отрисовать

#---------------------- Entry ----------------------------------

e = Entry(root)                #Создать поле ввода
#e.insert(0, 'Hello')           #Добавить в начало 
# e.insert(6,'World')          #Добавить в опред.позицию(посимвольно)
#e.insert(END, ' world')        #Добавить в конец
e.pack(fill=X)                       #Отрисовать

#--------------------- Главный цикл ----------------------------
root.mainloop() #метод - главный цикл обработки окна