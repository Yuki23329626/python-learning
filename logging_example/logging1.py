# learn how to use logging in python
import sys
import logging
import os

# Get the path of the current Python script
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)

FORMAT = '%(levelname)-5s %(asctime)s %(message)s'
logging.basicConfig(
    handlers=[logging.FileHandler(filename=os.path.join(
        script_dir, 'log_logging.log'), encoding='utf-8')],
    format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

count = 0
while(count < 10):
    count = count + 1
    logging.info("this is an info")
    if((count % 3) ==0):
        try:
            error
        except Exception as e:
            logging.exception(e)