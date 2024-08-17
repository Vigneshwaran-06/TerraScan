import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from PIL import Image, ImageTk

# Save data to CSV
def save_to_csv():
    # Get values from inputs
    texture_value = texture.get()
    moisture_value = moisture.get()
    ph_value = ph.get()
    soil_color_value = Soil_color.get()
    n_value = nitrogen.get()
    p_value = phosphorus.get()
    k_value = potassium.get()
    salinity_value = salinity.get()
    pesticide_value = pesticide.get()
    metal_value = metal.get()

    # Validate required fields
    if not (texture_value and moisture_value and ph_value and soil_color_value and n_value and p_value and k_value and salinity_value and pesticide_value and metal_value):
        messagebox.showerror("Input Error", "All fields are required")
        return

    # Validate numeric fields
    try:
        ph_value = float(ph_value)
        n_value = float(n_value)
        p_value = float(p_value)
        k_value = float(k_value)
        salinity_value = float(salinity_value)
        pesticide_value = float(pesticide_value)
        metal_value = float(metal_value)
    except ValueError:
        messagebox.showerror("Input Error", "Numeric fields must contain valid numbers")
        return

    # Prepare data to save
    data = {
        "Soil Type": [texture_value], 
        "Moisture": [moisture_value], 
        "pH": [ph_value], 
        "Soil Color": [soil_color_value],
        "Nitrogen (N)": [n_value],
        "Phosphorus (P)": [p_value],
        "Potassium (K)": [k_value],
        "Salinity": [salinity_value],
        "Pesticides": [pesticide_value],
        "Metal Content": [metal_value]
    }
    
    df = pd.DataFrame(data)
    
    # Save data to CSV
    try:
        df.to_csv('Soil_Record.csv', mode='a', header=not pd.io.common.file_exists('Soil_Record.csv'), index=False)
        messagebox.showinfo("Success", "Data has been saved to Soil_Record.csv")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    # Clear inputs
    texture.set('')
    moisture.delete(0, tk.END)
    ph.delete(0, tk.END)
    Soil_color.set('')
    nitrogen.delete(0, tk.END)
    phosphorus.delete(0, tk.END)
    potassium.delete(0, tk.END)
    salinity.delete(0, tk.END)
    pesticide.delete(0, tk.END)
    metal.delete(0, tk.END)
    texture.focus()

# Main Tkinter window
a = tk.Tk()
a.title('Soil Fertility Analyzer')
b = "#7469B6"
a.geometry("450x450+600+300")
a.config(bg=b)
si = 11

# Labels
tk.Label(a, text="SOIL FERTILITY", padx=10, pady=7, font=('cambria', si+2, "bold"), bg=b, fg='white').place(x=15, y=0)
tk.Label(a, padx=10, pady=7, text='Soil Type', font=('cambria', si), bg=b).grid(row=2, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Moisture Content in %', font=('cambria', si), bg=b).grid(row=3, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='pH Level', font=('cambria', si), bg=b).grid(row=4, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Soil Color', font=('cambria', si), bg=b).grid(row=5, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Nitrogen (N) in %', font=('cambria', si), bg=b).grid(row=6, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Phosphorus (P) in %', font=('cambria', si), bg=b).grid(row=7, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Potassium (K) in %', font=('cambria', si), bg=b).grid(row=8, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Salinity in dS/m', font=('cambria', si), bg=b).grid(row=9, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Pesticides in ppm', font=('cambria', si), bg=b).grid(row=10, column=0, sticky='w')
tk.Label(a, padx=10, pady=7, text='Metal Content in ppm', font=('cambria', si), bg=b).grid(row=11, column=0, sticky='w')

# Input fields
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

nitrogen = tk.Entry(a, width=width, border=0, font=('cambria', si))
nitrogen.grid(row=6, column=1)

phosphorus = tk.Entry(a, width=width, border=0, font=('cambria', si))
phosphorus.grid(row=7, column=1)

potassium = tk.Entry(a, width=width, border=0, font=('cambria', si))
potassium.grid(row=8, column=1)

salinity = tk.Entry(a, width=width, border=0, font=('cambria', si))
salinity.grid(row=9, column=1)

pesticide = tk.Entry(a, width=width, border=0, font=('cambria', si))
pesticide.grid(row=10, column=1)

metal = tk.Entry(a, width=width, border=0, font=('cambria', si))
metal.grid(row=11, column=1)

# Buttons
tk.Button(a, text="Add Record", font=('cambria', si), bg='#C1FA4A', border=0, width=15, command=save_to_csv).place(x=30, y=400)

a.mainloop()
