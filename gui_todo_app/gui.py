import customtkinter as ctk

# Root Widget Setup
root = ctk.CTk()
root.geometry('850x650')
root.title("Todo App")

# Functions
def remove_todo(frame):
    frame.destroy()


def add_todo():
    todo = entry.get()
    if todo == '':
        pass
    else:
        todo_frame = ctk.CTkFrame(scrollable_frame, bg_color='#D3D3D3')
        todo_frame.pack(fill='x', padx=40, pady=10)
        label = ctk.CTkLabel(todo_frame, text=todo, font=ctk.CTkFont(size=15, family='Calibri'))
        label.pack(side='left')
        entry.delete(0, ctk.END)
        remove_button = ctk.CTkButton(todo_frame, text="Remove", command=lambda: remove_todo(todo_frame))
        remove_button.pack(side='right')






# Widgets
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight='bold', family='Calibri'))
title_label.pack(pady=(20, 20))

entry = ctk.CTkEntry(root, placeholder_text="Add Task", width=500, height=40, font=ctk.CTkFont(size=18, family='Calibri'))
entry.pack(pady=(10, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=250)
scrollable_frame.pack()

add_button = ctk.CTkButton(root, text="Add", width=500, height=50, command=add_todo)
add_button.pack(pady=20)




# Running the Application
root.mainloop()