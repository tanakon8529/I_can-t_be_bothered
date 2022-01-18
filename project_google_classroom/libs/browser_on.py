import webbrowser

def open_browser():
    url = 'https://www.google.com/'

    # MacOS
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


    # Windows
    chrome_path_1 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    chrome_path_2 = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'


    res = webbrowser.get(chrome_path_1).open(url)
    if res == False:
        res = webbrowser.get(chrome_path_2).open(url)

    print(res)