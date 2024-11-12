import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter import ttk

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
            open_analysis_window()  # Open analysis window after loading CSV
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

# Open a new window for analysis (Correlation and Covariance)
def open_analysis_window():
    if df is not None:
        analysis_window = Toplevel(root)
        analysis_window.title("Correlation and Covariance Analysis")
        analysis_window.geometry("500x500")

        # Dropdown for selecting the type of analysis
        tk.Label(analysis_window, text="Select Analysis Type:").pack(pady=5)
        analysis_dropdown = ttk.Combobox(analysis_window, state="readonly", values=[
            "Correlation", "Covariance"
        ])
        analysis_dropdown.pack()

        # Dropdowns for selecting the columns
        tk.Label(analysis_window, text="Select First Column:").pack(pady=5)
        column1_dropdown = ttk.Combobox(analysis_window, state="readonly", values=df.columns.tolist())
        column1_dropdown.pack()

        tk.Label(analysis_window, text="Select Second Column:").pack(pady=5)
        column2_dropdown = ttk.Combobox(analysis_window, state="readonly", values=df.columns.tolist())
        column2_dropdown.pack()

        # Run analysis button
        calculate_button = tk.Button(analysis_window, text="Run Analysis", command=lambda: perform_analysis(
            analysis_dropdown.get(), column1_dropdown.get(), column2_dropdown.get(), analysis_window))
        calculate_button.pack(pady=10)

        # Text box to display results
        global result_text
        result_text = tk.Text(analysis_window, height=10, width=60)
        result_text.pack(pady=10)

# Perform analysis based on dropdown selections
def perform_analysis(selected_analysis, column1, column2, window):
    if not column1 or not column2:
        messagebox.showwarning("Warning", "Please select both columns.")
        return

    if selected_analysis == "Correlation":
        result = calculate_correlation(column1, column2)
    elif selected_analysis == "Covariance":
        result = calculate_covariance(column1, column2)
    else:
        result = "Invalid selection."

    # Display the result in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Individual Analysis Functions
def calculate_correlation(column1, column2):
    correlation_value = df[column1].corr(df[column2])
    return f"Correlation between {column1} and {column2}: {correlation_value}"

def calculate_covariance(column1, column2):
    covariance_value = df[column1].cov(df[column2])
    return f"Covariance between {column1} and {column2}: {covariance_value}"

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
