from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import sqlite3 as sql
import re
from prettytable import PrettyTable
from colorama import Fore
import requests
import subprocess
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer






# ChromeDriver yolunu belirtin
driver_path = '/home/boewolf/Desktop/Tengri/pythonProjects/web_ozan_bozkurt_odev/chromedriver-linux64/chromedriver'
service = Service(driver_path)

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome(service=service)


def news_summary(news_url):

    # Siteye git ve haber içeriğini çek
    driver.get(news_url)
    time.sleep(5)
    # Sayfanın HTML içeriğini alın
    html = driver.page_source

    time.sleep(10)
    # Beautiful Soup ile HTML içeriğini parse edin
    soup = BeautifulSoup(html, 'html.parser')

    p_tags=soup.find_all('p')
    #Şimdi burada "p" taglarımızı çektiğimizde bize iki çeşit "p" tagı geliyor aşağıda örneğini bırakıyorum

    '''
    1 = <p>haber metni<p>
    2 = <p>class = "" , metin<p>
    '''

    # Bizim burada işimize yarayanlar içinde sadece netin olan "p" taglarıdır , içinde class isimleri vesaire olan taglar bizim işimize yaramıyor . O yüzden bunları filtrelemeliyiz .

    
    
    # Her bir "p" tag'ini kontrol et
    i=0 # bu değer işimize yarar kaç tane p tagı var onun sayısını almak için kullanılacak 
    # Boş bir liste oluştur
    content = ""
    for tag in p_tags:
        
        # Tag'ın "class" özelliğini kontrol et 
        if not tag.has_attr("class"):
            # "class" özelliği yoksa tag'ın içeriğini yazdır
            content = str(content) + str(tag.text.strip())
            
            #print(content)
            # content değerini listeye ekle
            #contents.append(content)
    print("\n")
    print("CONTENT : ",content)
    print("\n")
    

    summary=metin_ozet_al(content)
    print("SUMMARY",summary)

    driver.quit()
    #return summary


def metin_ozet_al(ozan):#bunu devam ettir text ve img değerleri döndürsün ve create_html fonksiyonunu burada çalıştırsın .

    # Parse the input text
    parser = PlaintextParser.from_string(ozan, Tokenizer("turkish"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=5)  # You can adjust the number of sentences in the summary

    time.sleep(3)
   # Output the summary
    summarized_text = ""
    for sentence in summary:
        summarized_text += str(sentence) + " "  # Her cümleyi özette birleştir
    return summarized_text  # Tüm özetlenmiş metni döndür

url = "https://tinyurl.com/24e9lmku"
news_summary(url)