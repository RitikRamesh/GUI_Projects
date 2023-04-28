import tkinter as tk
from datetime import datetime as dt

def real_clock():
    
    current_time = dt.now().strftime('%H : %M : %S ')
    real_time.config(text=current_time)
    
    current_date = dt.now().strftime('%d-%b-%Y')
    real_date.config(text=current_date)
    
    current_day = dt.now().strftime('%A')
    real_day.config(text=current_day)
    
    root.after(1000,real_clock)

root=tk.Tk()
root.geometry('400x250')
root.resizable(0,0) # type: ignore
root.title('Digital Clock')
# root.config(padx=10,pady=12)

heading_digital = tk.Label(text='Digital Clock', font=('Rockwell',50))

heading_time = tk.Label(text=('Time : '),font=('Menlo',30))
heading_date = tk.Label(text=('Date : '),font=('Menlo',30))
heading_day = tk.Label(text=('Day  : '),font=('Menlo',30))

real_time = tk.Label(text='',font=('Din Condensed',30))
real_date = tk.Label(text='',font=('Din Condensed',30))
real_day = tk.Label(text='',font=('Din Condensed',30))

heading_digital.grid(row=1,column=1,columnspan=2,padx=50,pady=5)

heading_time.grid(row=2,column=1,sticky='w')
heading_date.grid(row=3,column=1,sticky='w')
heading_day.grid(row=4,column=1,sticky='w')

real_time.grid(row=2,column=2,sticky='w')
real_date.grid(row=3,column=2,sticky='w')
real_day.grid(row=4,column=2,sticky='w')

real_clock()
root.mainloop()