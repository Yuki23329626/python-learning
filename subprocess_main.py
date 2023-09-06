import subprocess
import sys
import os
import logging

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.subprocess_main', encoding='utf-8')], format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
# message = "https://www.youtube.com/watch?v=9n1aOSXX180&format=bestaudio"
message = "https://www.youtube.com/watch?v=PRoCvsJTnCI&format=bestaudio"
try:
    subprocess_args = ["python", "subprocess_sub.py"]  # Command to run the subprocess
    subprocess_obj = subprocess.Popen(subprocess_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False)

    # Communicate with the subprocess
    stdout_byte, stderr_byte = subprocess_obj.communicate(input=message.encode('utf-8'))

    # It is only recommended to cancel the following comment when debugging
    print('output_data:', stdout_byte.decode("utf-8"))
except Exception as e:
    logging.exception(e)