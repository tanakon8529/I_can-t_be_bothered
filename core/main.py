# dev on win10/ubuntu 20.04 LTS - python 3.10.0
from libs.browser_utill import open_browser

from loguru import logger
from datetime import datetime
import os

path_log = r'log'

real_path_log = os.path.realpath(path_log)

today = datetime.now().strftime("%Y%m%d")

if not os.path.exists(real_path_log):
    os.makedirs(real_path_log)



logger.add("{}/{}.log".format(real_path_log, today), enqueue=True, retention="30 days")

def process_run():

    url_input = "https://meet.google.com/nht-zaia-ygc"
    web = open_browser()
    web.open_browser(url_input)