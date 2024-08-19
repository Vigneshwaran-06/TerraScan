import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def graph():
    df = pd.read_csv('Soil_Record.csv')
    date=df['Date']
    texture=df['Soil Texture']
    plt.figure(figsize=(10, 6))
    plt.plot(date,texture, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Texture')
    plt.title('Texture vs Date')
    plt.grid(True)
    plt.show()
def save_to_csv(cal):
    texture_value = texture.get()
    moisture_value = moisture.get()
    ph_value = ph.get()
    soil_color_value = Soil_color.get()
    cal=cal
    if not texture_value or not moisture_value or not ph_value or not soil_color_value:
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    try:
        ph_value = float(ph_value)
    except ValueError:
        messagebox.showerror("Input Error", "pH must be a number")
        return

    data = {"Date":[cal], "Soil Texture": [texture_value], "Moisture": [moisture_value], "pH": [ph_value], "Soil Color": [soil_color_value]}
    df = pd.DataFrame(data)
    try:
        df.to_csv('Soil_Record.csv', mode='a', header=not pd.io.common.file_exists('Soil_Record.csv'), index=False)
        messagebox.showinfo("Success", "Data has been saved to Soil_Record.csv")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    texture.set('')
    moisture.delete(0, tk.END)
    ph.delete(0, tk.END)
    Soil_color.set('')
    texture.focus()
a = tk.Tk()
a.title('Soil Fertility Analyze')
b = "#7469B6"
a.geometry("400x270+600+300")
a.config(bg=b)
si = 11
tk.Label(a,text="SOIL FERTILITY",padx=10,pady=7,font=('cambria',si+2,"bold"),bg=b,fg='white').place(x=15,y=0)
tk.Label(a, padx=10, pady=7, text='', font=('cambria', si), bg=b).grid(row=1, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Soil Texture', font=('cambria', si), bg=b).grid(row=2, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Moisture Content in %', font=('cambria', si), bg=b).grid(row=3, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='pH Level', font=('cambria', si), bg=b).grid(row=4, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Soil Colour', font=('cambria', si), bg=b).grid(row=5, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Date', font=('cambria', si), bg=b).grid(row=6, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='', font=('cambria', si), bg=b).grid(row=7, column=0, sticky='w')

width = 20
soil_texture = ["Sandy", "Sandy-Loamy", "Loam", "Silty-Loam", "Clay", "Heavy Clay"]
texture = ttk.Combobox(a, values=soil_texture, state="readonly", width=width, font=('cambria', si-1))
texture.grid(row=2, column=1)

moisture = tk.Spinbox(a, from_=0, to=100, width=width-16, border=0, font=('cambria', si))
moisture.grid(row=3, column=1, sticky="w")

ph = tk.Entry(a, width=width, border=0, font=('cambria', si))
ph.grid(row=4, column=1)

soil_colors = ["Red", "Yellow", "Brown", "Black", "Gray"]
Soil_color = ttk.Combobox(a, values=soil_colors, state="readonly", width=width, font=('cambria', si-1))
Soil_color.grid(row=5, column=1)
tk.Button(a, text="Add Record", font=('cambria', si), bg='#C1FA4A', border=0, width=15, command=lambda : save_to_csv(cal.get())).place(x=30, y=220)
tk.Button(a, text="Data Visualization", font=('cambria', si), bg='#DB66F4', border=0, width=15, command=graph).place(x=200, y=220)
cal = DateEntry(a, width=23, background=b,
                foreground='yellow', borderwidth=0, date_pattern='dd/MM/yyyy')
cal.grid(row=6, column=1)
a.mainloop()
