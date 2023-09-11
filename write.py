import os 
import sys

# Get the path of the current Python script
script_dir = os.path.dirname(sys.argv[0])
# os.chdir(script_path)

print(os.getcwd())

if getattr(sys, 'frozen', False):
    # The script is running as an executable (e.g., using PyInstaller or cx_Freeze)
    print("Running as an executable")
    executable_path = sys.executable
    print("Executable path:", executable_path)
else:
    # The script is running as a regular Python script
    print("Running as a Python script")
    script_name = sys.argv[0]
    print("Script name:", script_name)


with open(os.path.join(script_dir, 'output.txt'), 'w') as fd:
    fd.write('test')

with open('output.txt', 'r') as fd:
    input_data = fd.read()
    print(input_data)

os.system("pause")