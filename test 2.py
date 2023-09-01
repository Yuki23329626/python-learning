from io import StringIO  # Python 3
import sys

# Create a variable to capture stdout
stdout_backup = sys.stdout
output = ""

try:
    # Redirect stdout to the variable
    sys.stdout = StringIO()
    print("Helloa, Woirld!")
    print("Hellob, World!")
    print("Helloc, Worild!")
    print("Hellod, World!")
    print("Helloe, Worlid!")
    output = sys.stdout.getvalue()
finally:
    # Restore stdout to its original value
    sys.stdout = stdout_backup
    
for string in output.split('\n'):
    if 'i' in string:
        print(string)
