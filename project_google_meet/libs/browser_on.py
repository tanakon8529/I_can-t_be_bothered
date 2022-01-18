import webbrowser
from sys import platform
import os

class open_browser(object):

    def __init__(self):
        self.url_web = 'https://www.google.com/'

    def check_os(self):
        my_os =""
        if platform == "linux" or platform == "linux2":
            my_os = "linux"
        elif platform == "darwin":
            my_os = "OS_X"
        elif platform == "win32":
            my_os = "Windows"

        return my_os

    def close_browser(self, brow):
        task_success = False

        if brow == 'chrome':
            os.system("taskkill /im chrome.exe /f")
            task_success = True

        if brow == 'firefox':
            os.system("taskkill /im firefox.exe /f")
            task_success = True

        return task_success

    def open_browser(self):
        url = self.url_web
        browser_name = None
        os_found = self.check_os()

        if os_found == "linux":
            # Linux
            chrome_path = '/usr/bin/google-chrome %s'
            browser_name = 'chrome'

        if os_found == "OS_X":
            # MacOS
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            browser_name = 'chrome'

        if os_found == "Windows":
            # Windows
            chrome_path_1 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            chrome_path_2 = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            browser_name = 'chrome'

        browser_enable = False
        round_search_browser = 0
        while browser_enable == False:
            browser_enable = webbrowser.open(url)
            if browser_enable == False:
                browser_enable = webbrowser.get(chrome_path_1).open(url)
                if browser_enable == False:
                    browser_enable = webbrowser.get(chrome_path_2).open(url)

            round_search_browser += 1
            if round_search_browser == 3:
                break

        print(browser_enable, round_search_browser)
