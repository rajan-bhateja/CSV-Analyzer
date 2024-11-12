import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter import ttk
import matplotlib.pyplot as plt

# Global DataFrame variable
df = None

# Function to open file dialog and load CSV file
def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", f"File loaded: {file_path}")
            open_distribution_analysis_window()  # Open distribution analysis window after loading CSV
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

# Open a new window for distribution analysis
def open_distribution_analysis_window():
    if df is not None:
        distribution_window = Toplevel(root)
        distribution_window.title("Data Distribution Analysis")
        distribution_window.geometry("500x500")

        # Dropdown for selecting the type of distribution analysis
        tk.Label(distribution_window, text="Select Distribution Analysis:").pack(pady=5)
        distribution_dropdown = ttk.Combobox(distribution_window, state="readonly", values=[
            "Frequency Distribution", "Skewness", "Kurtosis"
        ])
        distribution_dropdown.pack()

        # Dropdown for selecting the column
        tk.Label(distribution_window, text="Select Column:").pack(pady=5)
        column_dropdown = ttk.Combobox(distribution_window, state="readonly", values=df.columns.tolist())
        column_dropdown.pack()

        # Run analysis button
        calculate_button = tk.Button(distribution_window, text="Run Analysis", command=lambda: perform_distribution_analysis(
            distribution_dropdown.get(), column_dropdown.get(), distribution_window))
        calculate_button.pack(pady=10)

        # Text box to display results
        global result_text
        result_text = tk.Text(distribution_window, height=10, width=60)
        result_text.pack(pady=10)

# Perform analysis based on dropdown selections
def perform_distribution_analysis(selected_analysis, selected_column, window):
    if not selected_column:
        messagebox.showwarning("Warning", "Please select a column.")
        return

    if selected_analysis == "Frequency Distribution":
        result = calculate_frequency_distribution(selected_column)
    elif selected_analysis == "Skewness":
        result = calculate_skewness(selected_column)
    elif selected_analysis == "Kurtosis":
        result = calculate_kurtosis(selected_column)
    else:
        result = "Invalid selection."

    # Display the result in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Individual Data Distribution Functions
def calculate_frequency_distribution(column):
    freq_dist = df[column].value_counts()
    return f"Frequency Distribution for {column}:\n{freq_dist.to_string()}"

def calculate_skewness(column):
    skew_value = df[column].skew()
    return f"Skewness of {column}: {skew_value}"

def calculate_kurtosis(column):
    kurtosis_value = df[column].kurt()
    return f"Kurtosis of {column}: {kurtosis_value}"

# Tkinter welcome page setup
root = tk.Tk()
root.title("CSV Analyzer - Welcome")
root.geometry("400x200")

# Welcome page label
welcome_label = tk.Label(root, text="Welcome to the CSV Analyzer", font=("Arial", 16))
welcome_label.pack(pady=20)

# Load CSV Button
load_button = tk.Button(root, text="Choose CSV File", command=load_csv)
load_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
