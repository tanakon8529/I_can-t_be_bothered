import os
import webbrowser


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


url = 'https://www.google.com/'

result = find('chrome.exe', 'C:/Program Files(x86)/Google/')
if result == [] :
    result = find('chrome.exe', 'C:/Program Files/Google/')

print(result)
current_path = result
res = webbrowser.open(url)
