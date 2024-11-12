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
    window.config()
    window.title("CSV Analyzer")
    window.geometry('1200x700')

    notebook = ttk.Notebook(window)

    stats_tab = Frame(notebook)
    viz_tab = Frame(notebook)

    notebook.add(stats_tab, text="Statistics", padding=10)
    notebook.add(viz_tab, text="Visualizations", padding=10)
    notebook.pack(expand=True, fill='both')

    Label(stats_tab, text=f"Statistics for {file_name}", font=('Helvetica', 14)).pack()
    Label(viz_tab, text=f"Visualizations for {file_name}", font=('Helvetica', 14)).pack()

    # Contains the stats details
    frame1 = Frame(stats_tab)
    frame1.pack(fill='x')

    # File name information
    name = Label(frame1, text='Name:', font=('Helvetica', 12), anchor="w", justify=RIGHT)
    name.grid(row=0, column=0)
    name_info = Label(frame1, text=file_name, font=('Helvetica', 12))
    name_info.grid(row=0, column=1, sticky='w')

    # File location information
    location = Label(frame1, text='Location:', font=('Helvetica', 12), anchor="w", justify=RIGHT)
    location.grid(row=1, column=0)
    path = Label(frame1, text=file_path, font=('Helvetica', 12))
    path.grid(row=1, column=1, sticky='w')

    # File size information
    size = Label(frame1, text='Size (in KBs):', font=('Helvetica', 12), anchor="w", justify=RIGHT)
    size.grid(row=2, column=0)
    size_info = Label(frame1, text=round((os.path.getsize(file_path)) / 1024, 2), font=('Helvetica', 12))
    size_info.grid(row=2, column=1, sticky='w')

    # Columns count information
    column_count = Label(frame1, text='Column Count:', font=('Helvetica', 12), anchor="w", justify=RIGHT)
    column_count.grid(row=3, column=0)
    column_count_info = Label(frame1, text=len(df.columns), font=('Helvetica', 12))
    column_count_info.grid(row=3, column=1, sticky='w')

    # Columns information
    columns = Label(frame1, text='Columns:', font=('Helvetica', 12), anchor="w", justify=RIGHT)
    columns.grid(row=4, column=0)
    columns_info = Label(frame1, text=", ".join(df.columns.values), font=('Helvetica', 12))
    columns_info.grid(row=4, column=1, sticky='w')

    # Numeric statistics
    numeric_df = df.select_dtypes(include=[np.number])  # Filter numeric columns
    stats_df = pd.DataFrame({
        # Stats with rounded values upto 2 digits
        'Mean': round(numeric_df.mean(), 2),
        'Min': round(numeric_df.min(), 2),
        'Max': round(numeric_df.max(), 2),
        'Standard Deviation': round(numeric_df.std(), 2),
        'Variance': round(numeric_df.var(), 2),
        'Range': round(numeric_df.max() - numeric_df.min(), 2),
        'Skewness': round(numeric_df.skew(), 2),
        'Kurtosis': round(numeric_df.kurtosis(), 2),
        'Sum': round(numeric_df.sum(), 2),
        'Mode': round(numeric_df.mode().iloc[0], 2),  # First mode if multiple
        'Q1 (25%)': round(numeric_df.quantile(0.25), 2),
        'Median (50%)': round(numeric_df.median(), 2),
        'Q3 (75%)': round(numeric_df.quantile(0.75), 2),
        'IQR': round(numeric_df.quantile(0.75) - numeric_df.quantile(0.25), 2),
    }).reset_index()
    stats_df.rename(columns={'index': 'Column'}, inplace=True)

    # Display stats in a Treeview table
    tree_frame = Frame(stats_tab)
    tree_frame.pack(fill='both', expand=True)

    tree = ttk.Treeview(tree_frame, columns=list(stats_df.columns), show='headings')
    for col in stats_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=150)

    for _, row in stats_df.iterrows():
        tree.insert('', 'end', values=list(row))

    # Add horizontal scrollbar
    h_scrollbar = Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
    tree.configure(xscrollcommand=h_scrollbar.set)
    h_scrollbar.pack(side='bottom', fill='x')

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

    btn_hist = Button(viz_tab, text="Show Histograms", command=plot_histogram, font=('Helvetica', 12))
    btn_hist.pack(pady=10)

    btn_scatter = Button(viz_tab, text="Show Scatter Matrix", command=plot_scatter_matrix, font=('Helvetica', 12))
    btn_scatter.pack(pady=10)

    window.mainloop()

except Exception as e:
    print(f"Error occurred while processing the file: {e}")
