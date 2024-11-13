from tkinter import *
from tkinter import filedialog
import subprocess


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if file_path:
        # Pass the selected file to the 'Analysis.py' script
        subprocess.run(['python', 'Analysis.py', file_path])


# Basic Welcome page GUI window stuff
welcome = Tk()  # creating a GUI window
welcome.geometry("400x550")  # Setting the resolution
welcome.title("CSV Analyzer - Welcome")  # Setting the title
welcome.config(bg='white')
icon = PhotoImage(file="Logo no_background 147_200.png")
welcome.iconphoto(True, icon)  # Setting the GUI logo
welcome.config(background='#FFFFFF')  # Setting the background color

# Label stuff
logo = PhotoImage(file="Logo no_background 147_200.png")
icon = logo
label = Label(welcome, text="CSV Analyzer", bg='#FFFFFF', fg='#000000', font=('Helvetica', 40, 'bold'),
              padx=20, pady=20, image=icon, compound='top')
label.pack()

# intro to CSV Analyzer
text = Label(text="A simple application to\n"
                  "display some statistics.",
             bg='#FFFFFF', fg='#000000', font=('Helvetica', 16), padx=20, pady=20)
text.pack()  # display the text

# click to analyze button
open_btn = Button(welcome, text="Select CSV file", font=("Helvetica", 12),
                  border=2, bg='#FFFFFF', fg='#000000', padx=10, compound='bottom',
                  command=open_file)
open_btn.pack()  # display the button

if __name__ == "__main__":
    welcome.mainloop()  # Display the GUI window
