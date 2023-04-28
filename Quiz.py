import tkinter as tk

def quizz_function():
    user_ans = input_area.get(0.0,tk.END)
    if user_ans.lower() == 'print function\n':
        result_label.config(text="CORRECT",bg='green',padx=10,pady=8,fg='white')
    else:
        result_label.config(text="INCORRECT",bg='red',padx=10,pady=8,fg='white')

root = tk.Tk()
root.title('Quizz App')
root.geometry('500x550')
root.config(bg='#5E716A')
root.resizable(0,0) # type: ignore

heading = tk.Label(text='Quizz App',font=('Lucida Handwriting',35),bg='#5E716A',fg='white')
heading.pack(pady=10)

ques_label = tk.Label(text='Q) Which function is use to show output in pyton?',fg='white',font=('Havana',15),bg='#5E716A')
ques_label.pack()

input_area = tk.Text(width=50,height=3,font=('Havana',13),padx=5,pady=5)
input_area.pack(pady=20)

submit = tk.Button(text="Submit",font=('Havana',20),padx=10,pady=8,relief='ridge',bg='#666666',fg='WHITE',command=quizz_function)
submit.pack()

result_label = tk.Label(text="",font=('Havana',20),fg='WHITE',bg='#5E716A')
result_label.pack(pady=20)

root.mainloop()