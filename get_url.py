from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request 
from bs4 import BeautifulSoup

def get_url(ill,rem):

    driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
    driver.get('http://www.google.com/')
    content_fin = []

    ingredient = "Turmeric"
    illness = ill
    for ingredient in rem:
        search_box = driver.find_element(by = By.NAME, value = 'q')
        
        search_box.clear()
        search_box.send_keys(f"can \"{ingredient}\" cure \"{illness}\"")

        search_box.submit()
        time.sleep(1)

        headings = driver.find_elements(by = By.TAG_NAME,value = 'a')
        links = []
        for i in headings:
            
            a = str(i.get_attribute('href'))
            if 'google' not in a and a!='None':
                if '#' in a:
                    a = a[:a.index('#')]
                links.append(a)
        links = list(set(links))
        print(links)
        content = []
        sites = []
        for url in links:
            print(url)
            try:
                
                html = urllib.request.urlopen(url)
                content.append(list())
                # parsing the html file
                htmlParse = BeautifulSoup(html, 'html.parser')
                sites.append(url)
                # getting all the paragraphs
                for para in htmlParse.find_all("p"):
                    if len(para.get_text()) != 0:
                        content[-1].append(para.get_text())
            except:
                pass
            finally:
                pass
        content_fin+=[content]
    driver.quit()
    return content_fin,sites