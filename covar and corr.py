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
        column_menu_x['values'] = df.columns.tolist()
        column_menu_y['values'] = df.columns.tolist()

# Function to calculate correlation
def calculate_correlation():
    selected_column_x = column_menu_x.get()
    selected_column_y = column_menu_y.get()
    if selected_column_x and selected_column_y:
        correlation_value = df[selected_column_x].corr(df[selected_column_y])
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Correlation between {selected_column_x} and {selected_column_y}: {correlation_value}\n")
    else:
        messagebox.showwarning("Warning", "Please select both columns to calculate correlation.")

# Function to calculate covariance
def calculate_covariance():
    selected_column_x = column_menu_x.get()
    selected_column_y = column_menu_y.get()
    if selected_column_x and selected_column_y:
        covariance_value = df[selected_column_x].cov(df[selected_column_y])
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Covariance between {selected_column_x} and {selected_column_y}: {covariance_value}\n")
    else:
        messagebox.showwarning("Warning", "Please select both columns to calculate covariance.")

# Tkinter window setup
root = tk.Tk()
root.title("CSV Analyzer - Correlation and Covariance")
root.geometry("600x500")

# CSV Load Button
load_button = tk.Button(root, text="Load CSV", command=load_csv)
load_button.pack(pady=10)

# Label to show the loaded file
file_label = tk.Label(root, text="No CSV loaded")
file_label.pack()

# Dropdowns for column selection for Correlation and Covariance
column_menu_x_label = tk.Label(root, text="Select Column X:")
column_menu_x_label.pack()

column_menu_x = ttk.Combobox(root, state="readonly")
column_menu_x.pack(pady=5)

column_menu_y_label = tk.Label(root, text="Select Column Y:")
column_menu_y_label.pack()

column_menu_y = ttk.Combobox(root, state="readonly")
column_menu_y.pack(pady=5)

# Buttons for Correlation and Covariance
correlation_button = tk.Button(root, text="Calculate Correlation", command=calculate_correlation)
correlation_button.pack(pady=5)

covariance_button = tk.Button(root, text="Calculate Covariance", command=calculate_covariance)
covariance_button.pack(pady=5)

# Text box to display results
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
