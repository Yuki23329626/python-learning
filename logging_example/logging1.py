# learn how to use logging in python
import sys
import logging
import os

# Get the path of the current Python script
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.logging', encoding='utf-8')], format=FORMAT, level=logging.INFO, datefmt = '%Y-%m-%d %H:%M:%S')


count = 0
while(count < 10):
    count = count + 1
    logging.info("this is an info")
    if((count % 3) ==0):
        try:
            error
        except Exception as e:
            logging.exception(e)