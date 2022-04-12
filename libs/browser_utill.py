from loguru import logger
from sys import platform

import webbrowser
import os

class open_browser(object):

    def __init__(self):
        self.url_web = ""

    def open_browser(self, url_input):
        url = url_input

        browser_enable = False
        round_search_browser = 0
        try:
            while browser_enable == False:
                browser_enable = webbrowser.open(url)

                round_search_browser += 1
                if round_search_browser == 3:
                    logger.error("can't open browser")
                    break
        except Exception as e:
            logger.error("can't open browser : {}".format(e)) 
