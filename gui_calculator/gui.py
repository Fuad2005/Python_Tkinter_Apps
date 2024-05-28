import customtkinter as ctk
import tkinter.messagebox as messagebox

# Root Widget Setup
root = ctk.CTk()
root.geometry('400x500')
root.title("Calculator")
root.resizable(False, False)

input_text = ctk.StringVar()

# Algorithm
def get_input(value):
    global input_text
    input_text.set(input_text.get() + value)



def delete(all=False):
    global input_text
    if all:
        input_text.set('')
    else:
        input_text.set(input_text.get()[:-1])


def calculate(expression):
    global input_text
    try:
        input_text.set(eval(expression.get()))
    except SyntaxError:
        messagebox.showerror("Error", "Invalid input")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by 0!")


def key_input(e):
    if e.char in '1234567890.+-*/':
        get_input(e.char)
    elif e.char == '=' or e.keysym == 'Return':
        calculate(input_text)
    elif e.keysym == 'BackSpace':
        delete()
    elif e.keysym == 'Del':
        delete(all=True)



root.bind('<Key>', key_input)


# Widgets
screen = ctk.CTkFrame(root)  
screen.pack(fill='x')

text = ctk.CTkLabel(screen, textvariable=input_text, font=('Calibri', 30))
text.pack(side='right', padx=(0, 20), pady=30)

controls = ctk.CTkFrame(root, height=400)
controls.pack(fill='x')

b1 = ctk.CTkButton(controls, text='1',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('1'))
b1.pack()
b1.place(relx = 0, rely = 3/5, relwidth = 1/4, relheight = 1/5)

b2 = ctk.CTkButton(controls, text='2',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('2'))
b2.pack()
b2.place(relx = 1/4, rely = 3/5, relwidth = 1/4, relheight = 1/5)

b3 = ctk.CTkButton(controls, text='3',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('3'))
b3.pack()
b3.place(relx = 2/4, rely = 3/5, relwidth = 1/4, relheight = 1/5)

b4 = ctk.CTkButton(controls, text='4',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('4'))
b4.pack()
b4.place(relx = 0, rely = 2/5, relwidth = 1/4, relheight = 1/5)

b5 = ctk.CTkButton(controls, text='5',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('5'))
b5.pack()
b5.place(relx = 1/4, rely = 2/5, relwidth = 1/4, relheight = 1/5)

b6 = ctk.CTkButton(controls, text='6',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('6'))
b6.pack()
b6.place(relx = 2/4, rely = 2/5, relwidth = 1/4, relheight = 1/5)

b7 = ctk.CTkButton(controls, text='7',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('7'))
b7.pack()
b7.place(relx = 0, rely = 1/5, relwidth = 1/4, relheight = 1/5)

b8 = ctk.CTkButton(controls, text='8',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('8'))
b8.pack()
b8.place(relx = 1/4, rely = 1/5, relwidth = 1/4, relheight = 1/5)

b9 = ctk.CTkButton(controls, text='9',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('9'))
b9.pack()
b9.place(relx = 2/4, rely = 1/5, relwidth = 1/4, relheight = 1/5)

b0 = ctk.CTkButton(controls, text='0',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('0'))
b0.pack()
b0.place(relx = 1/4, rely = 4/5, relwidth = 1/4, relheight = 1/5)

bpoint = ctk.CTkButton(controls, text='.',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('.'))
bpoint.pack()
bpoint.place(relx = 2/4, rely = 4/5, relwidth = 1/4, relheight = 1/5)


bequals = ctk.CTkButton(controls, text='=',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: calculate(input_text))
bequals.pack()
bequals.place(relx = 3/4, rely = 4/5, relwidth = 1/4, relheight = 1/5)

bplus = ctk.CTkButton(controls, text='+',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('+'))
bplus.pack()
bplus.place(relx = 3/4, rely = 3/5, relwidth = 1/4, relheight = 1/5)

bminus = ctk.CTkButton(controls, text='-',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('-'))
bminus.pack()
bminus.place(relx = 3/4, rely = 2/5, relwidth = 1/4, relheight = 1/5)

bmul = ctk.CTkButton(controls, text='*',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('*'))
bmul.pack()
bmul.place(relx = 3/4, rely = 1/5, relwidth = 1/4, relheight = 1/5)

bdiv = ctk.CTkButton(controls, text='/',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: get_input('/'))
bdiv.pack()
bdiv.place(relx = 3/4, rely = 0, relwidth = 1/4, relheight = 1/5)


bback = ctk.CTkButton(controls, text='<',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: delete())
bback.pack()
bback.place(relx = 2/4, rely = 0, relwidth = 1/4, relheight = 1/5)

bdel = ctk.CTkButton(controls, text='C',  border_width=1, border_color='#2b2b2b', font=('Calibri', 20), command=lambda: delete(all=True))
bdel.pack()
bdel.place(relx = 1/4, rely = 0, relwidth = 1/4, relheight = 1/5)





# Running the Application
root.mainloop()