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

## ==========

from easygui import fileopenbox

path_files = fileopenbox("Welcome", "COPR", filetypes= "*.txt", multiple=True)

print(path_files)

# import openpyxl
# import csv
import pandas as pd

df_result = pd.DataFrame(columns=['TYPE', 'NE', 'Severity', 'ALARM NUMBER', 'Alarm History', 'Alarm List', 'abormal alarm in weekend', 'NOTE'])

for csv_file in path_files:
    df = pd.read_csv(csv_file)
    
    if("tas" in csv_file):
        df_temp  = pd.DataFrame({
            'TYPE': ['NTAS'],
            'NE': [''],
            'Severity': [''],
            'ALARM NUMBER': [''],
            'Alarm History': [''],
            'Alarm List': [''],
            'abormal alarm in weekend': [''],
            'NOTE': ['']
            })
    df_result = pd.concat([df_temp, df_result], ignore_index = True, axis = 0)
    
    df_temp  = pd.DataFrame({
            'TYPE': ['NTAS'],
            'NE': [csv_file.split(".")[-1]],
            'Severity': [''],
            'ALARM NUMBER': [''],
            'Alarm History': [''],
            'Alarm List': [''],
            'abormal alarm in weekend': [''],
            'NOTE': ['']
            })
    df_result = pd.concat([df_temp, df_result], ignore_index = True, axis = 0)

    for index, row in df.iterrows():
        df_temp  = pd.DataFrame({
            'TYPE': ['NTAS'],
            'NE': [''],
            'Severity': [df.iloc[index]['Severity']],
            'ALARM NUMBER': [df.iloc[index]['Alarm Number']],
            'Alarm History': ['v'],
            'Alarm List': [''],
            'abormal alarm in weekend': [df.iloc[index]['Alarm Text']],
            'NOTE': ['']
            })
        df_result = pd.concat([df_temp, df_result], ignore_index = True, axis = 0)

print(df_result)