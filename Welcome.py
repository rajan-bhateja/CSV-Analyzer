from tkinter import *

# Basic Welcome page GUI window stuff
welcome = Tk()                                      # creating a GUI window
welcome.geometry("400x600")                         # Setting the resolution
welcome.title("CSV Analyzer - Welcome")             # Setting the title
icon = PhotoImage(file="Logo no_background 147_200.png")
welcome.iconphoto(True, icon)                       # Setting the GUI logo
welcome.config(background='#FFFFFF')                # Setting the background color

# Label stuff
logo = PhotoImage(file="Logo no_background 147_200.png")
icon = logo
label = Label(welcome, text="CSV Analyzer", bg='#FFFFFF', fg='#000000', font=('Arial', 40, 'bold'),
              padx=20, pady=20, image=icon, compound='top')
label.pack()

# intro to CSV Analyzer
text = Label(text="CSV Analyzer is a simple GUI application\n"
                  "to display some stats about\n"
                  "the opened .csv file",
             bg='#FFFFFF', fg='#000000', font=('Arial', 12), padx=20, pady=20)

text.pack()
print("Hello world")
welcome.mainloop()                                  # Display the GUI window
