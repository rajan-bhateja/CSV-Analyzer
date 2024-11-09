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
file_name = os.path.basename(file_path)  # retrieving the file name from file path
df = pd.read_csv(file_path)
Welcome.welcome.destroy()  # destroying the welcome window to fix the looping issue

try:
    window = Tk()
    window.config(bg='white')
    window.title("CSV Analyzer")
    window.geometry('1200x700')

    notebook = ttk.Notebook(window)

    stats_tab = Frame(notebook, bg='white')
    viz_tab = Frame(notebook, bg='white')

    notebook.add(stats_tab, text="Statistics", padding=10)
    notebook.add(viz_tab, text="Visualizations", padding=10)
    notebook.pack(expand=True, fill='both')

    Label(stats_tab, text=f"Statistics for {file_name}", font=('Helvetica', 14), bg='white').pack()
    Label(viz_tab, text=f"Visualizations for {file_name}", font=('Helvetica', 14), bg='white').pack()

    # Contains the stats details
    frame1 = Frame(stats_tab, bg='white')
    frame1.pack(fill='x')

    # File name information
    name = Label(frame1, text='Name:', font=('Helvetica', 12), bg='white', anchor="w", justify=RIGHT)
    name.grid(row=0, column=0)
    name_info = Label(frame1, text=file_name, font=('Helvetica', 12), bg='white')
    name_info.grid(row=0, column=1, sticky='w')

    # File location information
    location = Label(frame1, text='Location:', font=('Helvetica', 12), bg='white', anchor="w", justify=RIGHT)
    location.grid(row=1, column=0)
    path = Label(frame1, text=file_path, font=('Helvetica', 12), bg='white')
    path.grid(row=1, column=1, sticky='w')

    # File size information
    size = Label(frame1, text='Size (in KBs):', font=('Helvetica', 12), bg='white', anchor="w", justify=RIGHT)
    size.grid(row=2, column=0)
    size_info = Label(frame1, text=round((os.path.getsize(file_path)) / 1024, 2), font=('Helvetica', 12), bg='white')
    size_info.grid(row=2, column=1, sticky='w')

    # Columns count information
    column_count = Label(frame1, text='Column Count:', font=('Helvetica', 12), bg='white', anchor="w", justify=RIGHT)
    column_count.grid(row=3, column=0)
    column_count_info = Label(frame1, text=len(df.columns), font=('Helvetica', 12), bg='white')
    column_count_info.grid(row=3, column=1, sticky='w')

    # Columns information
    columns = Label(frame1, text='Columns:', font=('Helvetica', 12), bg='white', anchor="w", justify=RIGHT)
    columns.grid(row=4, column=0)
    columns_info = Label(frame1, text=", ".join(df.columns.values), font=('Helvetica', 12), bg='white')
    columns_info.grid(row=4, column=1, sticky='w')

    # Numeric statistics
    numeric_df = df.select_dtypes(include=[np.number])  # Filter numeric columns
    stats_df = pd.DataFrame({
        'Mean': numeric_df.mean(),
        'Min': numeric_df.min(),
        'Max': numeric_df.max(),
        'Q1 (25%)': numeric_df.quantile(0.25),
        'Median (50%)': numeric_df.median(),
        'Q3 (75%)': numeric_df.quantile(0.75)
    }).reset_index()
    stats_df.rename(columns={'index': 'Column'}, inplace=True)

    # Display stats in a Treeview table
    tree_frame = Frame(stats_tab, bg='white')
    tree_frame.pack(fill='both', expand=True)

    tree = ttk.Treeview(tree_frame, columns=list(stats_df.columns), show='headings')
    for col in stats_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=150)

    for _, row in stats_df.iterrows():
        tree.insert('', 'end', values=list(row))

    tree.pack(fill='both', expand=True)

    # Visualization tab with basic plots
    def plot_histogram():
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if not numeric_columns.empty:
            plt.figure(figsize=(10, 6))
            df[numeric_columns].hist(bins=15)
            plt.suptitle("Histograms of Numeric Columns")
            plt.show()

    def plot_scatter_matrix():
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) >= 2:
            sns.pairplot(df[numeric_columns])
            plt.show()

    btn_hist = Button(viz_tab, text="Show Histograms", command=plot_histogram, font=('Helvetica', 12), bg='white')
    btn_hist.pack(pady=10)

    btn_scatter = Button(viz_tab, text="Show Scatter Matrix", command=plot_scatter_matrix, font=('Helvetica', 12), bg='white')
    btn_scatter.pack(pady=10)

    window.mainloop()

except Exception as e:
    print(f"Error occurred while processing the file: {e}")
