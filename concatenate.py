# Open a file for reading
file_path = r"C:\Users\mishen\Documents\youtube-downloader-chrome-extension\src_native_app\src_native_app.pem"  # Replace with the path to your file
try:
    with open(file_path, "r") as file:
        # Read the entire file into a string
        file_contents = file.read()
        print("".join(file_contents.split('\n')[1:-2]))
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")