import tkinter as tk
from tkinter import filedialog
import os

def browse_directory():
    dir_path = filedialog.askdirectory(title="Select a Directory")
    entry_path.delete(0, tk.END)
    entry_path.insert(0, dir_path)

def submit():
    print('submit')

# Create the main tkinter window
root = tk.Tk()
root.title("Lite Youtube Downloader - Setup")

# Create a frame to hold the label and entry
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a label
label = tk.Label(frame, text="Custom install location:")
label.grid(row=0, sticky = 'w', padx=10)

# Create an entry field for path input with default text
DEFAULT_PATH = os.path.expanduser("~")
entry_path = tk.Entry(frame, width=40)
entry_path.insert(0, DEFAULT_PATH)
entry_path.grid(row=1, column=0, padx=10)

# Create a "Browse" button
browse_button = tk.Button(frame, text="Browse", command=browse_directory, width=10)
browse_button.grid(row=1, column=1, padx=10, pady=10)

# Create a "Browse" button
browse_button = tk.Button(frame, text="Install", command=submit, width=10)
browse_button.grid(row=2, column=1, padx=10, sticky = 'e')

# Start the tkinter event loop
root.mainloop()