from tkinter import *
from tkinter import ttk

# Create the main window
root = Tk()
root.geometry("500x500")

# Set the theme to 'classic'
#style = ttk.Style()
#style.theme_use('classic')

# Create a sample widget to demonstrate the theme change
label = ttk.Label(root, text="This is a label with the 'classic' theme.")
label.pack(pady=20)

button = ttk.Button(root, text="Click Me")
button.pack(pady=20)

# Run the main loop
root.mainloop()
