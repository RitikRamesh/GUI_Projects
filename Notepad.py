import tkinter as tk
from tkinter import filedialog

class Notepad():
    def __init__(self,window):
        self.file_path = None
        print(self.file_path)
        self.window = window
        window.title('Notepad')
        window.geometry('817x472')
        window.config(bg='#FFC700')
        window.resizable(0,0)
    
        open_btn = tk.Button(text='Open',font=('Futura',15),highlightbackground='#4267B2',fg='Black',command=self.file_open)
        save_btn = tk.Button(text='Save',font=('Futura',15),highlightbackground='#FFD700',fg='Black',command=self.save_file)
        saveas_btn = tk.Button(text='Save As',font=('Futura',15),highlightbackground='#FF9500',fg='Black',command=self.save_as_file)
        clear_btn = tk.Button(text='Clear',font=('Futura',15),highlightbackground='#FF5100',fg='Black',command=self.clear)
        help_btn = tk.Button(text='Help',font=('Futura',15),highlightbackground='#6D00C9',fg='Black',command=self.help)
        
        self.text_area = tk.Text(width=80,height=20,font=('Futura',15),bg='#1F1F21',fg='#D4D4D2',relief='ridge',borderwidth=5)

        open_btn.grid(row=1,column=1,padx=10,pady=12)
        save_btn.grid(row=1,column=2,padx=10,pady=12)
        saveas_btn.grid(row=1,column=3,padx=10,pady=12)
        clear_btn.grid(row=1,column=4,padx=10,pady=12)
        help_btn.grid(row=1,column=5,padx=10,pady=12)
    
        self.text_area.grid(row=2,column=1,columnspan=5)

    def file_open(self):
        self.file_path = filedialog.askopenfilename()
        print(self.file_path)
        with open(self.file_path,'r')as f:
            file_text=f.read()
        self.text_area.insert(0.0,file_text)
        self.window.title(f'Notepad - {self.file_path}')
    
    def clear(self):
        self.text_area.delete(0.0,tk.END)
        
    def help(self):
        help_text = '''Find that one note when you really need to\n
                        With gallery view, you can see all your notes as thumbnails,\n 
                        and easily scan the images in them to find the note you want. \n
                        Or use powerful search features to find objects in attached images, \n
                        text in a scanned document, and more.'''
        self.text_area.insert(0.0,help_text)
    
    def save_file(self):
        if self.file_path == None:
            self.save_as_file()
        else:
            with open(self.file_path,'w') as f:
                file_text = self.text_area.get(0.0,tk.END)
                f.write(file_text)
    
    def save_as_file(self):
        options = [('.txt','*.txt'),('.bat','*.bat'),('All files','*.*')]
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=options)
        with open(file_path,'w') as f:
                file_text = self.text_area.get(0.0,tk.END)
                f.write(file_text)
                                
root = tk.Tk()
obj=Notepad(root)
root.mainloop()