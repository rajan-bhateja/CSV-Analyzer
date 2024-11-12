import pandas as pd
import numpy as np
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
            open_outlier_detection_window()  # Open outlier detection window after loading CSV
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

# Open a new window for outlier detection
def open_outlier_detection_window():
    if df is not None:
        outlier_window = Toplevel(root)
        outlier_window.title("Outlier Detection")
        outlier_window.geometry("500x500")

        # Dropdown for selecting the outlier detection method
        tk.Label(outlier_window, text="Select Outlier Detection Method:").pack(pady=5)
        outlier_dropdown = ttk.Combobox(outlier_window, state="readonly", values=[
            "Z Score", "IQR"
        ])
        outlier_dropdown.pack()

        # Dropdown for selecting the column
        tk.Label(outlier_window, text="Select Column:").pack(pady=5)
        column_dropdown = ttk.Combobox(outlier_window, state="readonly", values=df.columns.tolist())
        column_dropdown.pack()

        # Run analysis button
        calculate_button = tk.Button(outlier_window, text="Run Detection", command=lambda: perform_outlier_detection(
            outlier_dropdown.get(), column_dropdown.get(), outlier_window))
        calculate_button.pack(pady=10)

        # Text box to display results
        global result_text
        result_text = tk.Text(outlier_window, height=15, width=60)
        result_text.pack(pady=10)

# Perform outlier detection based on dropdown selections
def perform_outlier_detection(selected_method, column, window):
    if not column:
        messagebox.showwarning("Warning", "Please select a column.")
        return

    if selected_method == "Z Score":
        result = detect_outliers_z_score(column)
    elif selected_method == "IQR":
        result = detect_outliers_iqr(column)
    else:
        result = "Invalid selection."

    # Display the result in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Individual Outlier Detection Functions
def detect_outliers_z_score(column):
    threshold = 3  # Z-score threshold
    z_scores = (df[column] - df[column].mean()) / df[column].std()
    outliers = df[column][np.abs(z_scores) > threshold]
    return f"Outliers detected using Z Score method in {column}:\n{outliers.to_string(index=False)}"

def detect_outliers_iqr(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[column][(df[column] < lower_bound) | (df[column] > upper_bound)]
    return f"Outliers detected using IQR method in {column}:\n{outliers.to_string(index=False)}"

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
