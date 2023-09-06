from datetime import datetime
import os

file_path = r'C:\Users\mishen\Downloads\Systile - Artificial.webm'  # Replace with the path to your file

# Get the file's modification time (you can also use getctime or getatime)
timestamp = os.path.getmtime(file_path)
print(timestamp)

# Convert the timestamp to a datetime object
date_time = datetime.fromtimestamp(timestamp)

# Format the datetime object as a string
formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

print("File's modification time:", formatted_date_time)