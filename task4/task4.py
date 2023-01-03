from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox
import json
import requests

file = ''

def download():
    filename = txt.get().split('/')[-1]
    r = requests.get(txt.get(), allow_redirects=True)
    open(filename, "wb").write(r.content)
    messagebox.showinfo('Внимание!','Файл установлен')
    opfile(filename)
    

def wrfile():
    data = text.get(1.0, END)
    try:
        json.loads(data)
    except:
        messagebox.showinfo('Внимание!','Файл json не корректен')
        return
    file_name = filedialog.asksaveasfilename(title='Сохранение json файла', filetype = [("Json file","*.json")])
    f = open(file_name, 'w')
    f.write(data)
    f.close

def leave():
    quit()

def opfile(filename = ''):
    if filename == '':
        file = filedialog.askopenfilename(title='Открытие json файла', filetype = [("Json file","*.json")])
    else:
        file = filename
    with open(file,'r') as read_file:
        data = json.load(read_file)
    text.config(state=NORMAL)
    if text.get(1.0, END)!='':
        text.delete(1.0, END)
    text.insert(1.0, json.dumps(data, indent=2))

        
    
window = Tk()

file_menu = Menu()
main_menu = Menu()

file_menu.add_command(label='Edit', command = opfile)
file_menu.add_command(label='Save', command = wrfile)
file_menu.add_separator()
file_menu.add_command(label='Close', command = leave)

main_menu.add_cascade(label='File', menu=file_menu)

window.title('Редактор JSON')

text = Text(bg='#BABABA', fg='#000000', state=DISABLED)
txt=Entry(width=100)
btn=Button(text='скачать', command=download)

txt.pack(side=TOP)
btn.pack(side=TOP)
text.pack(expand = True, fill=BOTH, side=BOTTOM)

window.config(menu=main_menu)
window.mainloop()
