import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


# Function to open file dialog and load CSV file
def load_csv():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            global df
            df = pd.read_csv(file_path)
            file_label.config(text=f"Loaded: {file_path}")
            display_columns()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")


# Function to display the columns of the loaded CSV
def display_columns():
    if df is not None:
        column_menu['values'] = df.columns.tolist()


# Function for Mean
def calculate_mean():
    selected_column = column_menu.get()
    if selected_column:
        mean_value = df[selected_column].mean()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Mean: {mean_value}\n")


# Function for Median
def calculate_median():
    selected_column = column_menu.get()
    if selected_column:
        median_value = df[selected_column].median()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Median: {median_value}\n")


# Function for Mode
def calculate_mode():
    selected_column = column_menu.get()
    if selected_column:
        mode_value = df[selected_column].mode().values[0] if not df[selected_column].mode().empty else "No mode"
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Mode: {mode_value}\n")


# Function for Standard Deviation
def calculate_std_dev():
    selected_column = column_menu.get()
    if selected_column:
        std_dev_value = df[selected_column].std()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Standard Deviation: {std_dev_value}\n")


# Function for Variance
def calculate_variance():
    selected_column = column_menu.get()
    if selected_column:
        variance_value = df[selected_column].var()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Variance: {variance_value}\n")


# Function for Min
def calculate_min():
    selected_column = column_menu.get()
    if selected_column:
        min_value = df[selected_column].min()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Min: {min_value}\n")


# Function for Max
def calculate_max():
    selected_column = column_menu.get()
    if selected_column:
        max_value = df[selected_column].max()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Max: {max_value}\n")


# Function for Range
def calculate_range():
    selected_column = column_menu.get()
    if selected_column:
        range_value = df[selected_column].max() - df[selected_column].min()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Range: {range_value}\n")


# Tkinter window setup
root = tk.Tk()
root.title("CSV Analyzer - Descriptive Statistics")
root.geometry("600x500")

# CSV Load Button
load_button = tk.Button(root, text="Load CSV", command=load_csv)
load_button.pack(pady=10)

# Label to show the loaded file
file_label = tk.Label(root, text="No CSV loaded")
file_label.pack()

# Dropdown for column selection
column_menu_label = tk.Label(root, text="Select a column:")
column_menu_label.pack()

column_menu = ttk.Combobox(root, state="readonly")
column_menu.pack(pady=5)

# Buttons for each descriptive statistic
mean_button = tk.Button(root, text="Calculate Mean", command=calculate_mean)
mean_button.pack(pady=5)

median_button = tk.Button(root, text="Calculate Median", command=calculate_median)
median_button.pack(pady=5)

mode_button = tk.Button(root, text="Calculate Mode", command=calculate_mode)
mode_button.pack(pady=5)

std_dev_button = tk.Button(root, text="Calculate Standard Deviation", command=calculate_std_dev)
std_dev_button.pack(pady=5)

variance_button = tk.Button(root, text="Calculate Variance", command=calculate_variance)
variance_button.pack(pady=5)

min_button = tk.Button(root, text="Calculate Min", command=calculate_min)
min_button.pack(pady=5)

max_button = tk.Button(root, text="Calculate Max", command=calculate_max)
max_button.pack(pady=5)

range_button = tk.Button(root, text="Calculate Range", command=calculate_range)
range_button.pack(pady=5)

# Text box to display results
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
