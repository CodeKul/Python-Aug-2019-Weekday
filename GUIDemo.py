from tkinter import *  

def buttonClick(event):
    l['text'] = e.get()
    print('buttonClick called')

win = Tk()  
win.geometry("200x100")  

l = Label(win, text= "")
e = Entry(win)
b = Button(win,text = "GO")  

l.pack()  
e.pack()  
b.pack()  

b.bind('<Button-1>', buttonClick)

win.mainloop()  