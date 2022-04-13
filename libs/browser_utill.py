from loguru import logger

import webbrowser
import pyautogui
import time
import os



class open_browser(object):

    def __init__(self):
        # create folder resource
        path_resource = r'resource'
        self.real_path_resource = os.path.realpath(path_resource) 
        if not os.path.exists(self.real_path_resource):
            os.makedirs(self.real_path_resource)

        self.blabla = ""

    def click_button_join(self):
        try:
            button_join = pyautogui.locateOnScreen(self.real_path_resource+'\join_class.png' , confidence=0.9)
            time.sleep(2)
            pyautogui.click(button_join)
        except Exception as e:
            logger.error("can't join class : {}".format(e)) 

    def turn_off_mic_and_cam(self):
        try:
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'e')
            pyautogui.hotkey('ctrl', 'd')
        except Exception as e:
            logger.error("can't turn off : {}".format(e)) 

    def open_browser(self, url_input):
        url = url_input

        browser_enable = False
        round_search_browser = 0
        try:
            while browser_enable == False:
                browser_enable = webbrowser.open(url, autoraise=False)

                self.turn_off_mic_and_cam()
                self.click_button_join()
                logger.info("open : {}".format(url))


                round_search_browser += 1
                if round_search_browser == 3:
                    logger.error("can't open browser")
                    break
        except Exception as e:
            logger.error("can't open browser : {}".format(e)) 
