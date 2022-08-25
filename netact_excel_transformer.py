# import win32com.client

# # Open up Excel and make it visible
# excel = win32com.client.Dispatch('Excel.Application')
# excel.Visible = True

# # Select a file and open it
# file = r"C:\Users\mishen\Documents\python-learning\s3tas01(0815-0821).csv"
# workbook = excel.Workbooks.Open(file)

# # Wait before closing it
# _ = input("Press enter to close Excel")
# excel.Quit()

# from tkinter import filedialog
# from tkinter import *

# root = Tk()
# root.filename =  filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"), ("csv files","*.csv"),("excel files","*.xlsx")))
# print (root.filename)

from easygui import fileopenbox

path_files = fileopenbox("Welcome", "COPR", filetypes= "*.txt", multiple=True)

print(path_files)

import openpyxl

for file in path_files:
    