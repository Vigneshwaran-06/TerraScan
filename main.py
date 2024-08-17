import tkinter as tk
from tkinter import ttk
from soil_analysis import create_main_window  # Import the function from soil_analysis.py

def main():
  app_window = create_main_window()
  app_window.mainloop()

if __name__ == "__main__":
    main()
