from tkinter import*
import datetime
root=Tk()
root.configure(bg='black')
root.geometry('960x540')
root.resizable(0,0)
root.title('Python Clock')
Label(root, text='Digital Clock', font='arial 20 bold').pack(side=TOP)

def clock():
    date_time= datetime.datetime.now().strftime("%A:%d-%b-%Y %H:%M:%S%p")
    date,time= date_time.split()
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)

time_label=Label(root, font="calibri 90 bold", foreground='green', background='black')
time_label.pack(anchor='center')
date_label= Label(root, font="calibri 50 bold", foreground='green', background='black')
date_label.pack(anchor='s')

clock()
mainloop()