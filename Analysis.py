import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tkinter import *
from tkinter import ttk

import Welcome
import sys

# Ensure there is a file path passed as an argument
file_path = sys.argv[1]  # The file path is passed as the first argument
try:
    df = pd.read_csv(file_path)
    Welcome.welcome.destroy()

    window = Tk()
    window.config(bg='white')
    window.title("CSV Analyzer")
    window.geometry('1200x700')

    notebook = ttk.Notebook(window)

    tab1 = Frame(notebook)
    tab2 = Frame(notebook)

    notebook.add(tab1, text="Statistics", padding=10)
    notebook.add(tab2, text="Visualizations", padding=10)
    notebook.pack(expand=True, fill='both')

    Label(tab1, text="Stats", font=('Arial',14)).pack()
    Label(tab2, text="Visualizations", font=('Arial', 14)).pack()

    #frame1 = Frame(window)
    #frame1.pack()
    #location = Label(frame1, text='File Location:', font=('Arial', 14))
    #location.pack()
    #label = Label(frame1, text=file_path, font=('Arial', 14))
    #label.pack()

    window.mainloop()
    print(file_path)

except Exception as e:
    print(f"Error occurred while processing the file: {e}")