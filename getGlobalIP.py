from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as cs

# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv
load_dotenv()


txtPath = os.getenv('TXTPATH')
URL = 'https://www.cman.jp/network/support/go_access.cgi'
tag = '.outIp'

def openURL():
    options = Options()
    options.add_argument('--headless')

    chrome_servie = cs.Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=chrome_servie, options=options)
    browser.get(URL)
    return browser

def getIP(browser):
    html = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup.select(tag)[0].text

def writeText(ip):
    with open(txtPath,'w') as f:
        f.write(ip)

def main():
    browser = openURL()
    ip = getIP(browser)
    writeText(ip)
    browser.close()

if __name__ == "__main__":
    main()