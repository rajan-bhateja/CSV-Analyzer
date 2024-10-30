import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tkinter import *
from tkinter import ttk

import Welcome
import sys
import os

# Ensure there is a file path passed as an argument
file_path = sys.argv[1]  # The file path is passed as the first argument
file_name = os.path.basename(file_path)     # retrieving the file name from file path
df = pd.read_csv(file_path)
Welcome.welcome.destroy()       # destroying the welcome window to fix the looping issue

try:
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

    Label(tab1, text=f"Statistics for {file_name}", font=('Arial', 14)).pack()
    Label(tab2, text=f"Visualizations for {file_name}", font=('Arial', 14)).pack()

    # contains the stats details
    frame1 = Frame(tab1)
    frame1.pack()

    # file name information
    name = Label(frame1, text='Name:', font=('Arial', 12), anchor="w", justify=RIGHT)
    name.grid(row=0, column=0)
    name_info = Label(frame1, text=file_name, font=('Arial', 12))
    name_info.grid(row=0, column=1, sticky='w')

    # file location information
    location = Label(frame1, text='Location:', font=('Arial', 12), anchor="w", justify=RIGHT)
    location.grid(row=1, column=0)
    path = Label(frame1, text=file_path, font=('Arial', 12))
    path.grid(row=1, column=1, sticky='w')

    # file size information
    size = Label(frame1, text='Size (in KBs):', font=('Arial', 12), anchor="w", justify=RIGHT)
    size.grid(row=2, column=0)
    size_info = Label(frame1, text=round((os.path.getsize(file_path))/1024, 2), font=('Arial', 12))
    size_info.grid(row=2, column=1, sticky='w')

    # columns count information
    column_count = Label(frame1, text='Column Count:', font=('Arial', 12), anchor="w", justify=RIGHT)
    column_count.grid(row=3, column=0)
    column_count_info = Label(frame1, text=len(df.columns), font=('Arial', 12))
    column_count_info.grid(row=3, column=1, sticky='w')

    # columns information
    columns = Label(frame1, text='Columns:', font=('Arial', 12), anchor="w", justify=RIGHT)
    columns.grid(row=4, column=0)
    columns_info = Label(frame1, text=df.columns.values, font=('Arial', 12))
    columns_info.grid(row=4, column=1, sticky='w')

    # columns mean information


    window.mainloop()

except Exception as e:
    print(f"Error occurred while processing the file: {e}")