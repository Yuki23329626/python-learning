from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.resources import path
from easygui import fileopenbox
import pandas as pd
from datetime import date
import os
from plyer import notification

# Matching file names and categorize them with a proper function name
def match_stirng(csv_file):
    if("titan" in csv_file):
        return "NETNUMBER(ENUM)"
    if("mrf" in csv_file):
        return "MRF"
    if("sub" in csv_file):
        return "SUBPROV"
    if("asbc" in csv_file):
        return "A-SBC"
    if("cscf" in csv_file):
        return "CFX-5000"
    if("tas" in csv_file):
        return "NTAS"
    if("mgcf" in csv_file):
        return "MGCF"
    if("mw" in csv_file):
        return "OMGW"
    return ""

# Get files path into list
path_files = fileopenbox("Welcome", "COPR", filetypes= "*.txt", multiple=True)
path_files.sort()
print(path_files)
    

df_result = pd.DataFrame(columns=['TYPE', 'NE', 'Severity', 'ALARM NUMBER', 'Alarm History', 'Alarm List', 'abormal alarm in weekend', 'NOTE'])


for csv_file in path_files:
    df = pd.read_csv(csv_file)

    # Get the duplicated index of the same function
    duplicated_index = df_result[df_result['TYPE'] == match_stirng(csv_file)].index.values
    
    if(duplicated_index.size == 0):
        df_temp  = pd.DataFrame({
            'TYPE': [match_stirng(csv_file)],
            'NE': [''],
            'Severity': [''],
            'ALARM NUMBER': [''],
            'Alarm History': [''],
            'Alarm List': [''],
            'abormal alarm in weekend': [''],
            'NOTE': ['']
            })
        
        df_temp2  = pd.DataFrame({
                'TYPE': [''],
                'NE': [csv_file.split(".")[-2].split("\\")[-1]],
                'Severity': [''],
                'ALARM NUMBER': [''],
                'Alarm History': [''],
                'Alarm List': [''],
                'abormal alarm in weekend': [''],
                'NOTE': ['']
                })
        df_temp = pd.concat([df_temp, df_temp2], ignore_index = True, axis = 0)

        for index, row in df.iterrows():
            df_temp2  = pd.DataFrame({
                'TYPE': [''],
                'NE': [''],
                'Severity': [df.iloc[index]['Severity']],
                'ALARM NUMBER': [df.iloc[index]['Alarm Number']],
                'Alarm History': ['v'],
                'Alarm List': [''],
                'abormal alarm in weekend': [df.iloc[index]['Alarm Text']],
                'NOTE': ['']
                })
            df_temp = pd.concat([df_temp, df_temp2], ignore_index = True, axis = 0)
        df_result = pd.concat([df_result, df_temp], ignore_index = True, axis = 0)
    else:
        df_temp  = pd.DataFrame({
                'TYPE': [''],
                'NE': [csv_file.split(".")[-2].split("\\")[-1]],
                'Severity': [''],
                'ALARM NUMBER': [''],
                'Alarm History': [''],
                'Alarm List': [''],
                'abormal alarm in weekend': [''],
                'NOTE': ['']
                })

        for index, row in df.iterrows():
            df_temp2  = pd.DataFrame({
                'TYPE': [''],
                'NE': [''],
                'Severity': [df.iloc[index]['Severity']],
                'ALARM NUMBER': [df.iloc[index]['Alarm Number']],
                'Alarm History': ['v'],
                'Alarm List': [''],
                'abormal alarm in weekend': [df.iloc[index]['Alarm Text']],
                'NOTE': ['']
                })
            df_temp = pd.concat([df_temp, df_temp2], ignore_index = True, axis = 0)
        
        insertion_point = duplicated_index[0]+1
        df_result = pd.concat([df_result.iloc[:insertion_point], df_temp, df_result.iloc[insertion_point:]]).reset_index(drop=True)

# print(df_result)

# Generate excel file with proper file name
today = date.today()
current_date = today.strftime("%Y%m%d")
print("current_date =", current_date)

path_save = csv_file.split(".")[-2][0:len(csv_file.split(".")[-2])-len(csv_file.split(".")[-2].split("\\")[-1])] + "CIMS_NE_alarm_" + current_date + ".xlsx"
path_temp = path_save

i = 1
while os.path.exists(path_temp):
    path_temp = path_save.split(".")[-2] + " - (" + str(i) + ").xlsx"
    i = i + 1
    print("revised path: ", path_temp)

df_result.to_excel(path_temp, index=False)
print(path_temp)


# # history
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

# notification.notify(
#     title='Task has done.',
#     message='The result has been saved to \n' + path_temp + '.',
#     app_name='NetAct Excel Transformer'
# )

# from win10toast import ToastNotifier

# toast = ToastNotifier()
# toast.show_toast(
#     "Task has done.",
#     'The result has been saved to \n' + path_temp + '.',
#     duration = 20,
#     threaded = True,
# )