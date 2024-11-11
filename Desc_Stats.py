import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


# Function to open file dialog and load CSV file
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            global df
            df = pd.read_csv(file_path)
            file_label.config(text=f"Loaded: {file_path}")
            update_column_dropdown()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")


# Function to update the column dropdown with column names
def update_column_dropdown():
    if df is not None:
        column_dropdown['values'] = df.columns.tolist()


# Function to handle analysis based on user selection
def perform_analysis():
    selected_analysis = analysis_dropdown.get()
    selected_column = column_dropdown.get()

    if not selected_column:
        messagebox.showwarning("Warning", "Please select a column.")
        return

    if selected_analysis == "Mean":
        result = calculate_mean(selected_column)
    elif selected_analysis == "Median":
        result = calculate_median(selected_column)
    elif selected_analysis == "Mode":
        result = calculate_mode(selected_column)
    elif selected_analysis == "Standard Deviation":
        result = calculate_std_dev(selected_column)
    elif selected_analysis == "Variance":
        result = calculate_variance(selected_column)
    elif selected_analysis == "Min":
        result = calculate_min(selected_column)
    elif selected_analysis == "Max":
        result = calculate_max(selected_column)
    elif selected_analysis == "Range":
        result = calculate_range(selected_column)
    else:
        result = "Invalid selection."

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{selected_analysis} of {selected_column}: {result}\n")


# Individual descriptive analysis functions
def calculate_mean(column):
    return round(df[column].mean(), 2)


def calculate_median(column):
    return round(df[column].median(), 2)


def calculate_mode(column):
    mode_values = df[column].mode()
    return round(mode_values[0] if not mode_values.empty else "No mode", 2)


def calculate_std_dev(column):
    return round(df[column].std(), 2)


def calculate_variance(column):
    return round(df[column].var(), 2)


def calculate_min(column):
    return round(df[column].min(), 2)


def calculate_max(column):
    return round(df[column].max(), 2)


def calculate_range(column):
    return round(df[column].max() - df[column].min(), 2)


# Tkinter window setup
root = tk.Tk()
root.title("CSV Analyzer - Descriptive Statistics")
root.geometry("500x400")

# Load CSV Button
load_button = tk.Button(root, text="Load CSV", command=load_csv)
load_button.pack(pady=10)

# Label to show the loaded file
file_label = tk.Label(root, text="No CSV loaded")
file_label.pack()

# Dropdown for selecting the column
tk.Label(root, text="Select Column:").pack(pady=5)
column_dropdown = ttk.Combobox(root, state="readonly")
column_dropdown.pack()

# Dropdown for selecting the type of analysis
tk.Label(root, text="Select Analysis:").pack(pady=5)
analysis_dropdown = ttk.Combobox(root, state="readonly", values=[
    "Mean", "Median", "Mode", "Standard Deviation", "Variance", "Min", "Max", "Range"
])
analysis_dropdown.pack()


# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_analysis)
calculate_button.pack(pady=10)

# Text box to display results
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
