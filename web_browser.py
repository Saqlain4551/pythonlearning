import webbrowser

chrome_path = "C:\\Users\\mohd saqlain\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
browser = webbrowser.get('chrome')

while True:
    url = input('Enter the URL: ')
    browser.open_new_tab(url)