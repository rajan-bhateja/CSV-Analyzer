import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
import Welcome
import sys
import Welcome

# Ensure there is a file path passed as an argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]  # The file path is passed as the first argument
    try:
        df = pd.read_csv(file_path)
        Welcome.welcome.destroy()

        window = Tk()
        window.config(bg='#ffffee')
        #window.geometry('500x500')

        frame1 = Frame(window)
        frame1.pack()
        location = Label(frame1, text='File Location:', font=('Arial', 14))
        location.pack()
        label = Label(frame1, text=file_path, font=('Arial', 14))
        label.pack()
        #fvfvfsvfs
        window.mainloop()
        print(df.head())

    except Exception as e:
        print(f"Error occurred while processing the file: {e}")
else:
    print("No file path provided.")