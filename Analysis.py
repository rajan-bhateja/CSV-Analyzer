import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import Welcome
import sys

# Ensure there is a file path passed as an argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]  # The file path is passed as the first argument
    try:
        df = pd.read_csv(file_path)
        print(df.head())

    except Exception as e:
        print(f"Error occurred while processing the file: {e}")
else:
    print("No file path provided.")