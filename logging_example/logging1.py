# learn how to use logging in python
import sys
import logging

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='log.comic-downloader', encoding='utf-8')], format=FORMAT, level=logging.WARNING)


count = 0
while(count < 10):
    count = count + 1
    logging.info("this is an info")
    if((count % 3) ==0):
        try:
            error
        except Exception as e:
            logging.error(e)