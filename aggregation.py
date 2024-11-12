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
            open_data_aggregation_window()  # Open data aggregation window after loading CSV
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

# Open a new window for data aggregation (Group By or Pivot Table)
def open_data_aggregation_window():
    if df is not None:
        aggregation_window = Toplevel(root)
        aggregation_window.title("Data Aggregation")
        aggregation_window.geometry("500x500")

        # Dropdown for selecting the type of aggregation
        tk.Label(aggregation_window, text="Select Aggregation Method:").pack(pady=5)
        aggregation_dropdown = ttk.Combobox(aggregation_window, state="readonly", values=[
            "Group By", "Pivot Table"
        ])
        aggregation_dropdown.pack()

        # Dropdowns for selecting the columns for aggregation
        tk.Label(aggregation_window, text="Select Column to Aggregate:").pack(pady=5)
        column_dropdown = ttk.Combobox(aggregation_window, state="readonly", values=df.columns.tolist())
        column_dropdown.pack()

        # Dropdown for selecting the grouping or pivoting column
        tk.Label(aggregation_window, text="Select Grouping or Pivoting Column:").pack(pady=5)
        group_column_dropdown = ttk.Combobox(aggregation_window, state="readonly", values=df.columns.tolist())
        group_column_dropdown.pack()

        # Run aggregation button
        calculate_button = tk.Button(aggregation_window, text="Run Aggregation", command=lambda: perform_aggregation(
            aggregation_dropdown.get(), column_dropdown.get(), group_column_dropdown.get(), aggregation_window))
        calculate_button.pack(pady=10)

        # Text box to display results
        global result_text
        result_text = tk.Text(aggregation_window, height=15, width=60)
        result_text.pack(pady=10)

# Perform aggregation based on dropdown selections
def perform_aggregation(selected_method, column, group_column, window):
    if not column or not group_column:
        messagebox.showwarning("Warning", "Please select both columns.")
        return

    if selected_method == "Group By":
        result = perform_group_by(column, group_column)
    elif selected_method == "Pivot Table":
        result = perform_pivot_table(column, group_column)
    else:
        result = "Invalid selection."

    # Display the result in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Individual Aggregation Functions

# Group by function
def perform_group_by(column, group_column):
    grouped = df.groupby(group_column)[column].agg(['sum', 'mean', 'count', 'min', 'max'])
    return f"Group By Result for {group_column}:\n{grouped.to_string()}"

# Pivot Table function
def perform_pivot_table(column, group_column):
    pivot_table = df.pivot_table(values=column, index=group_column, aggfunc=['sum', 'mean', 'count'])
    return f"Pivot Table Result for {group_column}:\n{pivot_table.to_string()}"

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
