# NOT FINISHED

import tkinter as tk

# Root Widget Setup
root = tk.Tk()
root.geometry('400x500')
root.title("Unit Convertor")
root.resizable(False, False)

# Algorithm
def raise_frame(frame):
    frame.tkraise()

# Navbar
navbar = tk.Frame(root)
navbar.pack(fill='x')

mass_button = tk.Button(navbar, text="Mass", command=lambda: raise_frame(mass_page)).pack(side="left")

length_button = tk.Button(navbar, text="Length", command=lambda: raise_frame(length_page)).pack(side="left")

time_button = tk.Button(navbar, text="Time", command=lambda: raise_frame(time_page)).pack(side="left")

temperature_button = tk.Button(navbar, text="Temperature", command=lambda: raise_frame(temperature_page)).pack(side="left")

# Pages
mass_page = tk.Frame(root)
length_page = tk.Frame(root)
time_page = tk.Frame(root)
temperature_page = tk.Frame(root)

for frame in (length_page, mass_page, time_page, temperature_page):
    frame.place(x=0, y=30, relwidth=1, relheight=1)

# Length Page
tk.Label(mass_page, text='Mass Unit Conversion').pack()

mass_inner_frame = tk.Frame(mass_page)
mass_inner_frame.pack()


mass_units = ["kilogram", "gram", "milligram", "ton", "pound", "ounce", "carrat", "atomic mass unit"]
selected_mass = tk.StringVar(length_page)
selected_mass.set(mass_units[0])

input_unit = tk.OptionMenu(mass_inner_frame, selected_mass, *mass_units)
input_unit.grid(row=0, column=0)

length_arrow = tk.Label(mass_inner_frame, text="------->")
length_arrow.grid(row=0, column=1)

output_unit = tk.OptionMenu(mass_inner_frame, selected_mass, *mass_units)
output_unit.grid(row=0, column=2)

input_unit_text = tk.Entry(mass_inner_frame)
input_unit_text.grid(row=1, column=0)

length_arrow2 = tk.Label(mass_inner_frame, text="------->")
length_arrow2.grid(row=1, column=1)

output_unit_text = tk.Label(mass_inner_frame, text="100")
output_unit_text.grid(row=1, column=2)

# Running the Application
raise_frame(mass_page)
root.mainloop()