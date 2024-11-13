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
file_path = sys.argv[1]
file_name = os.path.basename(file_path)
df = pd.read_csv(file_path)
Welcome.welcome.destroy()

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

    # File information
    info_labels = {
        'Name': file_name,
        'Location': file_path,
        'Size (in KBs)': round((os.path.getsize(file_path)) / 1024, 2),
        'Column Count': len(df.columns),
        'Columns': ", ".join(df.columns.values)
    }

    for i, (label, info) in enumerate(info_labels.items()):
        Label(frame1, text=label + ':', font=('Helvetica', 12), anchor="w", justify=RIGHT).grid(row=i, column=0)
        Label(frame1, text=str(info), font=('Helvetica', 12)).grid(row=i, column=1, sticky='w')

    # Add scrollbar for column names
    column_scrollbar = Scrollbar(frame1, orient=HORIZONTAL)
    column_scrollbar.grid(row=4, column=1, sticky="we")
    columns_info = Text(frame1, wrap=NONE, height=1, font=('Helvetica', 12))
    columns_info.insert(1.0, ", ".join(df.columns.values))
    columns_info.configure(xscrollcommand=column_scrollbar.set, state=DISABLED)
    columns_info.grid(row=4, column=1, sticky="w")
    column_scrollbar.config(command=columns_info.xview)

    # Numeric statistics
    numeric_df = df.select_dtypes(include=[np.number])
    stats_df = pd.DataFrame({
        'Mean': round(numeric_df.mean(), 2),
        'Min': round(numeric_df.min(), 2),
        'Max': round(numeric_df.max(), 2),
        'Standard Deviation': round(numeric_df.std(), 2),
        'Variance': round(numeric_df.var(), 2),
        'Range': round(numeric_df.max() - numeric_df.min(), 2),
        'Skewness': round(numeric_df.skew(), 2),
        'Kurtosis': round(numeric_df.kurtosis(), 2),
        'Sum': round(numeric_df.sum(), 2),
        'Mode': round(numeric_df.mode().iloc[0], 2),
        'Q1 (25%)': round(numeric_df.quantile(0.25), 2),
        'Median (50%)': round(numeric_df.median(), 2),
        'Q3 (75%)': round(numeric_df.quantile(0.75), 2),
        'IQR': round(numeric_df.quantile(0.75) - numeric_df.quantile(0.25), 2),
    }).reset_index()
    stats_df.rename(columns={'index': 'Column'}, inplace=True)

    # Display stats in a Treeview table with a horizontal scrollbar
    tree_frame = Frame(stats_tab)
    tree_frame.pack(fill='both', expand=True)
    tree = ttk.Treeview(tree_frame, columns=list(stats_df.columns), show='headings')
    for col in stats_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=150)
    for _, row in stats_df.iterrows():
        tree.insert('', 'end', values=list(row))
    h_scrollbar = Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
    tree.configure(xscrollcommand=h_scrollbar.set)
    h_scrollbar.pack(side='bottom', fill='x')
    tree.pack(fill='both', expand=True)

    # Add covariance and correlation options
    Label(stats_tab, text="Select Columns for Covariance/Correlation:", font=('Helvetica', 12)).pack()
    col1, col2 = StringVar(), StringVar()
    column_options = df.columns.tolist()
    OptionMenu(stats_tab, col1, *column_options).pack()
    OptionMenu(stats_tab, col2, *column_options).pack()


    def calculate_stats():
        try:
            c1, c2 = df[col1.get()], df[col2.get()]
            cov = np.cov(c1, c2)[0][1]
            corr = np.corrcoef(c1, c2)[0][1]
            result_label.config(text=f"Covariance: {cov:.2f}, Correlation: {corr:.2f}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")


    Button(stats_tab, text="Calculate Covariance & Correlation", command=calculate_stats).pack(pady=5)
    result_label = Label(stats_tab, text="", font=('Helvetica', 12))
    result_label.pack()

    # Visualization tab: Axis selection and plotting options
    Label(viz_tab, text="Select X and Y Axes for Plotting:", font=('Helvetica', 12)).pack()
    x_axis, y_axis = StringVar(), StringVar()
    OptionMenu(viz_tab, x_axis, *column_options).pack()
    OptionMenu(viz_tab, y_axis, *column_options).pack()

    plot_type = StringVar(value="Scatter Plot")
    plot_choices = ["Scatter Plot", "Line Plot", "Bar Plot"]
    OptionMenu(viz_tab, plot_type, *plot_choices).pack()


    def show_visualization():
        plt.figure(figsize=(10, 6))
        x_col, y_col = x_axis.get(), y_axis.get()
        if plot_type.get() == "Scatter Plot":
            sns.scatterplot(x=x_col, y=y_col, data=df)
            plt.xticks(rotation=90)
        elif plot_type.get() == "Line Plot":
            sns.lineplot(x=x_col, y=y_col, data=df)
            plt.xticks(rotation=90)
        elif plot_type.get() == "Bar Plot":
            sns.barplot(x=x_col, y=y_col, data=df)
            plt.xticks(rotation=90)

        plt.title(f"{plot_type.get()} of {x_col} vs {y_col}")
        plt.show()


    Button(viz_tab, text="Show Visualization", command=show_visualization, font=('Helvetica', 12)).pack(pady=10)

    window.mainloop()

except Exception as e:
    print(f"Error occurred while processing the file: {e}")
