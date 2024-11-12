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


# Open a new window for descriptive analysis
def open_analysis_window():
    if df is not None:
        analysis_window = Toplevel(root)
        analysis_window.title("Descriptive Statistics Analysis")
        analysis_window.geometry("500x400")

        # Dropdown for selecting the type of analysis
        tk.Label(analysis_window, text="Select Analysis:").pack(pady=5)
        analysis_dropdown = ttk.Combobox(analysis_window, state="readonly", values=[
            "Mean", "Median", "Mode", "Standard Deviation", "Variance", "Min", "Max", "Range"
        ])
        analysis_dropdown.pack()

        # Dropdown for selecting the column
        tk.Label(analysis_window, text="Select Column:").pack(pady=5)
        column_dropdown = ttk.Combobox(analysis_window, state="readonly", values=df.columns.tolist())
        column_dropdown.pack()

        # Calculate button
        calculate_button = tk.Button(analysis_window, text="Calculate",
                                     command=lambda: perform_analysis(analysis_dropdown.get(), column_dropdown.get(),
                                                                      analysis_window))
        calculate_button.pack(pady=10)

        # Text box to display results
        result_text = tk.Text(analysis_window, height=10, width=50)
        result_text.pack(pady=10)


# Perform analysis based on dropdown selections
def perform_analysis(selected_analysis, selected_column, window):
    if not selected_column:
        messagebox.showwarning("Warning", "Please select a column.")
        return

    result = None
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

    # Display result in result_text box
    result_text = window.winfo_children()[-1]  # Last widget in the analysis window
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{selected_analysis} of {selected_column}: {result}\n")


# Individual descriptive analysis functions
def calculate_mean(column):
    return df[column].mean()


def calculate_median(column):
    return df[column].median()


def calculate_mode(column):
    mode_values = df[column].mode()
    return mode_values[0] if not mode_values.empty else "No mode"


def calculate_std_dev(column):
    return df[column].std()


def calculate_variance(column):
    return df[column].var()


def calculate_min(column):
    return df[column].min()


def calculate_max(column):
    return df[column].max()


def calculate_range(column):
    return df[column].max() - df[column].min()


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
