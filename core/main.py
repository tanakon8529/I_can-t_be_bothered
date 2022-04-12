# dev on win10/ubuntu 20.04 LTS - python 3.10.0
from libs.browser_utill import open_browser

from loguru import logger
from datetime import datetime
import os

newpath = r'log'
real_path = os.path.realpath(newpath) 

today = datetime.now().strftime("%Y%m%d")

if not os.path.exists(real_path):
    os.makedirs(real_path)

logger.add("{}/{}.log".format(real_path, today), enqueue=True, retention="30 days")

def process_run():
    # url_input = "https://meet.google.com/nht-zaia-ygc"
    # web = open_browser()
    # web.open_browser(url_input)
    print("test")