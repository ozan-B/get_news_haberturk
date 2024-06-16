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
from colorama import Fore ,Back, Style
import requests
import subprocess
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import datetime
import sys
import os
import cv2
import numpy as np
import nltk
nltk.download('punkt')




class Program:
    def __init__(self):
        self.veritabani_bozkurt = sql.Connection

        # ChromeDriver yolunu belirtin
        self.driver_path = '/home/boewolf/Desktop/Tengri/pythonProjects/web_ozan_bozkurt_odev/chromedriver-linux64/chromedriver'
        service = Service(self.driver_path)

        # Sessiz mod için seçenekleri ayarlayın
        chrome_options = Options()
        #chrome_options.add_argument("--headless")

        #chrome_options.add_argument('--headless')  # Sessiz modu etkinleştir

        # Chrome WebDriver'ı başlat
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def banner(self):
        self.slowprint("""\033[96m
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣭⣿⣿⣿⠿⢿⣿⠿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣍⡛⢿⣿⣿⡿⣿⢸⣿⣾⣿⣿⡏⢰⡄⠀⠀
        ⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⣆⣉⣵⣶⣿⣿⣿⣿⡇⡉⢝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡾⠃⢋⡿⣸⣿⣿⣿⣿⣿⣿⣶⣀⡀
        ⠀⠀⠀⠀⠀⠀⠈⢦⡄⠀⠀⠀⠀⠀⠀⠉⠉⠓⠛⠻⠗⠻⠿⣷⣷⢲⣶⣾⢰⣿⣿⣿⣿⣿⢿⠺⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣻⠛⣸⣘⠀⠻⠟⣥⡄⣿⣿⣿⣿⣿⣷
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠻⢿⣿⣻⣿⣴⣷⠦⠛⠛⠛⠛⠉⠙⠛⠉⠉⠙⠉⠒⠋⣁⣿⡗⡍⢠⣴⣿⠋⠀⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⠾⠷⠶⠦⠠⠄⠀⡄⠀⠀⠘⠛⠛⠓⠆⠁⠀⠀⠀⠁⠀⠠⢤⡤⣤⣶⡾⣾⡠⢀⡀⠉⠞⠀⣹⡿⢁⢠⠀⣿⣿⣿⣿⣿⡏
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡤⣀⡀⣀⣴⣂⠀⠀⡀⠀⠀⣿⣿⣿⣦⠀⢀⡀⠀⠀⠴⠀⠀⠀⢠⣄⡀⠀⢚⣍⠴⡇⢻⡤⡿⢡⣿⢸⠃⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡄⣿⣷⣄⡀⣰⣬⣛⠒⠖⠀⠙⠋⠀⠱⠀⠀⢰⣿⣿⣿⣿⡄⠀⢹⣾⡾⡋⢑⣐⡒⢛⡿⢂⣷⣂⢴⣶⡆⣼⠄⠀⣾⣿⡆⣴⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠘⣿⣿⣷⡹⣿⣿⣿⣿⣗⣠⠄⡀⠀⡀⠀⠸⣿⣿⣿⣿⣷⡀⠹⣿⢿⡿⢷⡮⢩⣭⣰⣿⣿⣿⣿⣿⠃⣿⠃⣷⣿⣿⠇⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠹⣦⣈⠻⠿⣿⣿⣿⣷⣿⣿⡯⠞⡁⣘⠇⠀⠘⣿⣿⣿⣿⣿⣷⡐⡘⢿⣿⣶⡩⢳⣾⣿⣿⣿⣿⡿⢃⣼⣿⠀⡿⣸⡟⣰⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢿⣿⡶⡶⡶⠭⣭⣵⣶⣶⣾⢿⠘⠉⠀⣸⣿⣿⣿⣿⣿⣿⣷⣌⠒⠬⣙⣛⣛⣛⣛⣋⣉⣥⣶⣿⣿⠏⠀⣴⡿⢰⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⠴⣯⢁⡈⣸⣿⣿⣿⣿⠆⢠⠀⠠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⣸⣏⡄⣿⣿⣿⣿⠏⠋⠛⠟⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣯⣿⣿⣿⣿⠇⠀⠛⠀⠲⣿⣿⣿⣿⣿⣿⠿⠛⡿⡓⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⡿⣡⣿⣿⣿⣿⣧⣀⣀⣸⣾
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢷⣷⣿⣾⡟⢣⡆⠀⠀⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⣼⣷⡩⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣋⣿⣿⡝⠱⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠐⠀⠺⣟⡦⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠀⠀⣩⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠚⣷⡺⣿⣿⣿⣿⣿⣿⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠘⢿⣿⣿⣿⣯⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠰⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣯⣾⠏⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⠶⠖⠲⠦⠦⠶⡾⣶⣾⣴⣦⡄⠀⠀⠀⠀⣿⣻⣿⢛⠉⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⢏⣹⡟⠑
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⣦⢦⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡷⡟⣿⠀⠀⠀⠀⢂⣿⠁⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡣⠀
        ⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢣⡊⠀⠀⠀⠀⠀⣜⠁⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
        ⠀⠀⠀⣶⠦⠚⠀⢠⠶⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠠⠂⠂⠱⡀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡁⠀⠰⢻⡄⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠁⡀⡈⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠉⡀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⢙⡔⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀By Ozan Bozkurt⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⣴⢟⠡⡬⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀W.W⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
        \033[0m""")
    
    
    
    def slowprint(self,s):
        for c in s + '\n': #Metnin sonuna bir yeni satır (\n) eklenir ve her karakter için döngü oluşturulur.
            sys.stdout.write(c) #Geçerli karakter ekrana yazdırılır.
            sys.stdout.flush() # Çıkış tamponu temizlenir, böylece yazılan karakter hemen ekranda görünür.
            time.sleep(0.1 / 100)  # Her karakter yazıldıktan sonra 0.1 milisaniye beklenir, bu da metnin yavaşça yazdırılmasını sağlar.
    
    
    def back(self):
        job = input(f"\n{Fore.BLUE}Press 'e' to exit tool  or Press 'a' use to again tool:    ") 
        return job
    
    
    def scrape_and_save(self, url, Table_name):

        self.driver.get(url)
        time.sleep(6)
        #self.connect_veritabani_bozkurt() #database kayıt için en başta bir kere databese bağlanııyoruz

        # Sayfanın sonuna kadar kaydırma işlemi
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Sayfanın yarısına kaydır
            self.driver.execute_script(f"window.scrollTo(0, {last_height//2});")
            
            # Yeni içeriğin yüklenmesini bekleyin
            time.sleep(4)
            
            # Yeni sayfa yüksekliğini alın
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            #Sayfanın sonuna kaydır
            self.driver.execute_script(f"window.scrollTo(3500, {new_height});")
            time.sleep(4)

            # Eğer yeni yüklenen içerik yoksa, döngüden çıkın
            if new_height == last_height:
                break

            last_height = new_height

        #print(last_height) 15 bin küsür değeri verdi
        self.driver.execute_script(f"window.scrollTo(3500, {last_height//1.5});")
        time.sleep(5)
        
        self.driver.execute_script(f"window.scrollTo(3500, {last_height-3000});")
        
        time.sleep(10)
        # Sayfanın HTML içeriğini alın
        html = self.driver.page_source

        # Beautiful Soup ile HTML içeriğini parse edin
        soup = BeautifulSoup(html, 'html.parser')

        # Tüm <a> etiketlerini bulun
        a_tags = soup.find_all('a')
        i=0
        # <a> etiketlerini  çek ve database e kaydet .
        pattern = r'/\d{4}/\d{2}/\d{2}/'  # Desen: /4 rakam/2 rakam/2 rakam/ .Kendisi tarih kısmını src textinde çıkartmak için kullanılan regex tir.

        for a in a_tags:
            
            new = a.get('data-newscategory')  # haber mi, değil mi kontrol etmek için bu nitelik alınıyor 
  
            if new == 'Sağlık':
                
                href = a.get('href') #haber urlsi seç
                href ="https://www.haberturk.com/" + href
               
                baslik = a.get('title') or a.get_text() # haber başlığını seç
               
                # img etiketini seç
                img_tag = a.select_one('img')
                if img_tag:  # Eğer img etiketi bulunduysa
                    img_src = img_tag.get('src') or img_tag.get_text()

                    if img_src and img_src.startswith("/images/dummy/placeholder-image.gif"):
                        data_src = img_tag.get("data-src") or img_tag.get_text()
                        if data_src:
                            img_src = data_src

                    #resimde insan olup olmaması işleminin başlangıcı


                    boolean_deger = self.detect_humans(img_src)

                    if boolean_deger:
                        Human_value = 1
                    else:
                        Human_value = 0    

                    #resimde insan olup olmaması işleminin bitişi

                    
                    match = re.search(pattern, img_src)  # Deseni metin içinde ara
                    if match:
                        found_text = match.group()  # Eşleşen metni al
                else:
                    img_src = None

               
                    
                '''print(f'{i}Text: {baslik}, Href: {href}, src:{img_src}, tarih: {found_text}')
                print("-" * 40)
                i+=1'''#bu kısım çıktıları ekrana yazdırmak için kullnıldı . Şimdi çıktıları database'e ekleyeceğim için yorum satırına alındı .
       
                # Bu kısma kadar elde etmek istediğimiz domain,title,tarih ve resmin urlsini elde ettik.
                # Artık bu kısımda yapılacak şey domain değerini databesedeki domain değeri ile karşılaştırmak 
                # domain değerimiz databasede yok ise bu domain değeri ve diğer bilgilerini database e kaydetmektir 
                domain_databasede_kiyasla =self.control_saved_domain_database(href, Table_name)
                
                if domain_databasede_kiyasla == False:
                    
                    self.save_to_database(href, baslik, img_src, found_text, Table_name, Human_value)
             

        # Tarayıcıyı kapatın
        #self.driver.close()

    def connect_veritabani_bozkurt(self):
        try:
            self.veritabani_bozkurt = sql.connect("./bozkurt.db")
            print(Fore.GREEN+"Veritabanı bağlantısı başarılı.")
        except:
            print(Fore.RED+"Veritabanı bağlantısında sorun yaşandı.")

    #Bu fonksiyon çekilen bütün haberleri "title -> url" olarak tablo formatında ekrana yazdırır ve kullanıcıdan bir haberi seçmesini ister
    def get_the_all_news(self,date,Table_name,human1,human2):
        
        # Bütün haberleri database den çek ve ekrana yazdır her satırın başında bir id olsun 
        self.connect_veritabani_bozkurt()
        cursor = self.veritabani_bozkurt.cursor()

        try:
            # Veritabanından tüm HABER BAŞLIKLARINI ve KISALTILMIŞ URL leri al
            #cursor.execute(f"SELECT Title,Short_url,Tarih,Human FROM {Table_name} WHERE Tarih LIKE '%{date}%';")
            #aşağıdaki komutta kullanıcı 1,1 girerse sadece insan olanlar gelir::0,0 girerse insan olmayanlar gelir::1,0 girerse tüm sütunlar gelir
            cursor.execute(f"SELECT Title, Short_url, Tarih, Human FROM {Table_name} WHERE Tarih LIKE '%{date}%' AND (Human = {human1} OR Human = {human2});")
            rows = cursor.fetchall()

            # Sonuçları tablo şeklinde görüntülemek için PrettyTable nesnesi oluştur
            result_table = PrettyTable()
            #Her Sütunun başlığını ayarla 
            result_table.field_names = ["ID","TITLE", "LINK"]
            # Her sütunun genişliğini ayarla
            result_table.max_width["ID"] =5
            result_table.max_width["TITLE"] = 96
            result_table.max_width["DOMAIN"] = 30

            # Veritabanındaki tüm domainler ve title bilgisi çekilsin ve tabloya eklenip görüntülensin 
            i=1 #başa gelecek olan id numarasıdır
            for row in rows:

                #time.sleep(1)
                result_table.add_row([Fore.GREEN + f"[{i}]" + Fore.WHITE, Fore.WHITE +row[0], Fore.YELLOW + row[1] + Fore.WHITE])
                result_table.add_row([Fore.WHITE + 5*"-",Fore.WHITE + 96*"-", Fore.WHITE + 30*"-"])
                i+=1

                # Her satır eklendikten sonra çizgi ekle
                
                #print(f"{row[0]} --> {row[1]} ")
            print("\n")
            print(result_table)
            print("\n")

            # Kullanıcıdan haber ID'si al
            option = input(Back.GREEN+Fore.BLACK+"Bir haber ID'si girin: "+Style.RESET_ALL)
            while True:
                #option = input(Back.GREEN+Fore.BLACK+"Bir haber ID'si girin: "+Style.RESET_ALL)
                try:
                    option = int(option)
                    if 1 <= option <= len(rows):
                        # Kullanıcının girdiği ID'ye karşılık gelen satırı yazdır
                        print(result_table[option * 2 - 2])  # Her bir haberin 2 satırı olduğu için, 2'ye bölerek indexleyin
                        
                        #print(result_table[option * 2 - 2].get_string(fields=["LINK"]).split("\n")[3].strip("|").strip()) # BU kod url'yi tablodan düzgün bir şekilde çıkartmak için kulanıldı . Bu değeri "get_new_or_my_custom_new" fonksiyonuna vereceğiz .Bunu return edeceğiz aşağıda

                        url_value = result_table[option * 2 - 2].get_string(fields=["LINK"]).split("\n")[3].strip("|").strip()
                        
                        break
                        
                    else:
                        print(Fore.YELLOW+"Geçersiz ID! Lütfen geçerli bir ID girin.")
                        

                
                except ValueError:
                    print(Fore.RED+"Geçersiz giriş! Lütfen bir sayı girin.")
                    break
                    
            

        except Exception as e:
            # Hata oluşursa ekrana hata mesajı basılır
            print("\033[91mDomain ve mail eşlerinin bulunduğu Veritabanından veri okunurken bir hata oluştu:\033[0m", str(e))

        return url_value


    def control_saved_domain_database(self, domain, Table_name): # bu domain değerini alır ve tüm databasede karşılaştırma yapar bu domain database de varsa onu database e yüklemez, bu fonksiyon tekrarları engellemk için yazılmıştır .
        # Veritabanına bağlan
        #self.connect_veritabani_bozkurt()
        cursor = self.veritabani_bozkurt.cursor()
        found=False

        try:
            # Veritabanından tüm domainleri al
            cursor.execute(f"SELECT Domain FROM {Table_name}")
            rows = cursor.fetchall()

            found = False
            # Veritabanındaki tüm domainlerle karşılaştırma yapılır
            for row in rows:
                if domain == row[0]:
                    # Eğer domain zaten veritabanında varsa, found değişkeni True yapılır
                    found = True
                    break

        except Exception as e:
            # Hata oluşursa ekrana hata mesajı basılır
            print("\033[91mDomain ve mail eşlerinin bulunduğu Veritabanından veri okunurken bir hata oluştu:\033[0m", str(e))

        # Sonuç listesi döndürülür
        return found

    def save_to_database(self, domain, title, img_src, date, Table_name, Human_value):
        try:
            # Veritabanına bağlan
            #self.connect_veritabani_bozkurt()
            cursor = self.veritabani_bozkurt.cursor()

            #Kullaıcıya url'i tablo halinde gösterirken url çok uzun olduğu için görsel olarak kötü gözüküyor o yüzden ekstra olarak url'in kısaltılmış halini de database e kaydedeiyoruz ki diğer fonksiyonlarda bu ksıaltılmış url 'yi kullanıcaz
            short_url = self.url_shorter(domain)
            
            # SQL sorgusu oluştur
            sql_query = f"INSERT INTO {Table_name} (Domain, Title, Resim, Tarih, Short_url, Human) VALUES (?, ?, ?, ?, ?, ? )"
            
            # SQL sorgusunu çalıştır
            cursor.execute(sql_query, (domain, title, img_src, date, short_url, Human_value))

            # Değişiklikleri kaydet
            self.veritabani_bozkurt.commit()

            print("Veritabanına başarıyla eklendi.")
        except Exception as e:
            print(Fore.RED+"Veritabanına ekleme yapılırken bir hata oluştu:", str(e))


    #Bu fonksiyon verilen url'i kısaltır 
    def url_shorter(self,long_url):
        # TinyURL API'si ile URL'i kısalt
        response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
        
        # Kısaltılmış URL'yi al
        short_url = response.text
        return short_url

    #BU fonksiyon iki seçenek sunacak , 1-istenen haberi browserda kullanıcıya açar ,2- istenen haberin özetini kendi web sitemizde açar (Localde)
    def get_news_or_my_custom_news(self,new_url, Table_name):
            
        # ANSI kaçış dizilerini kaldır tabloda yazdırırken urlyi renkli yazdığımız için başında ve sonunda ANSI stringleri var . Url stringimizi bu ANSI stringlerimizden arındırmamız gerekir yoksa url 'miz yanlış olur .
        clean_url = new_url.replace('\x1b[33m', '').replace('\x1b[37m', '') # bu kod new_url içindeki "\x1b[33m" ve "\x1b[37m" stringlerini boş string ile  değiştirerek temiz bir URL oluşturur.


        while True:
            

            print(Fore.BLUE+"""
                  
            1- Haberi aç
            2- Haberin özetini aç
                  
            """+Style.RESET_ALL)

            option =input(Back.GREEN+Fore.BLACK+"Seçeneklerden birini seç"+Style.RESET_ALL)

            if option == "1":
                os.system("clear")
                # URL'yi aç bash script kullanrak yaptım bunu selenium kullanrak url'yi  browserda sürekli açık tutmak programın çalışmasını aksatıyordu .
                print(Fore.GREEN+"İşlem başarılı, web sitesi açılıyor"+Style.RESET_ALL)
                time.sleep(2)
                subprocess.run(["./open_the_url.sh", clean_url])
                
                break

            elif option == "2":
                os.system("clear")
                # Bu kısımda 
                 #1- haber sitesinin içine gidilecek
                  #2- haber içeriği çekilecek
                   #3- içeriği alınan haberin özeti çıkartılacak
                    #4- çıkaetnin ana fikirlerini kapsamaktadır. Uzman tavsiyeleri, karartılan özet ve haberin resmi kendi index.html dosyamıza yazdırılacak
                     #5- programın en başında('https://im.haberturk.com/l/2024/04/30/ver1714476127/3682082/jpg/640x360',) açılan python servırımzda kendi localimizdeki web sitemizin linki kullanılarak sitemiz kullanıcıya sunulacak .
                      #6- Bunların hepsini başka bir fonksiyonda yapmaya karar verdim böyle daha düzenli olucak gibi .
                
                
                #özet değerimize ulaşalım
                summary=self.news_summary(clean_url) 
                
                #image likine ulaşalım,database e şöyle bir sorgu yapacağız clean_url nin olduğu satırdaki resim sütunundaki değeri bize döndür
                cursor = self.veritabani_bozkurt.cursor()
                 # SQL sorgusu oluştur
                sql_query = f'SELECT Resim,Title FROM {Table_name} WHERE Short_url="{clean_url}"' 
                # SQL sorgusunu çalıştır
                cursor.execute(sql_query)
                # Sorgudan dönen sonuçları al
                result = cursor.fetchone() 
                img_result=result[0]
                header_result= result[1] 
                #print(img_result)# bu değer şu formatta çıkıyor ('https://im.haberturk.com/l/2024/04/30/ver1714476127/3682082/jpg/640x360',) bunu düzenlememiz gerek yoksa html koduna yazıldığında düzgün sonuç vermiyor .        
                #img_result = img_result[0].strip("('),") # URL'yi alıyoruz ve gereksiz karakterleri temizliyoruz
                
                
                #print(img_result)
                #print(header_result)
                #header değerimizede ulaşalım
                print(Fore.GREEN+"İşlem başarılı, web sitesi açılıyor"+Style.RESET_ALL)
                time.sleep(2)
                custom_url="http://0.0.0.0:1234"
                subprocess.run(["./open_the_url.sh", custom_url])
 
                
                
                
                self.create_html(summary, img_result, header_result)
                break

            else:
                print(Fore.RED+"hatalı giriş")
                break



    def news_summary(self,news_url):

        # Siteye git ve haber içeriğini çek
        self.driver.get(news_url)
        time.sleep(2)
        # Sayfanın HTML içeriğini alın
        html = self.driver.page_source

        time.sleep(2)
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
        # Boş bir string oluştur
        content = ""
        for tag in p_tags:
            
            # Tag'ın "class" özelliğini kontrol et 
            if not tag.has_attr("class"):
                # "class" özelliği yoksa tag'ın içeriğini yazdır
                content = str(content) + str(tag.text.strip())
                
                #print(content)
                # content değerini listeye ekle
                #contents.append(content)

        

        summary=self.metin_ozet_al(content)

        
        return summary
        
    def main_processes(self, Table_name):
        
        while True:
            print(Fore.BLUE+"""      
                1-Tüm haberleri getir
                
                2-Son bir günde çıkan haberleri getir
                
                3-Verilen tarihteki haberleri getir
                
                4- Haber resminde insan olan haberleri getir
                
                5- Haber resminde insan olmayan haberleri getir
                """+Style.RESET_ALL)           

            option=input(Back.GREEN+Fore.BLACK+"seçimini yap : "+Style.RESET_ALL)
            
            if option == "1":
                while True:
                    try:
                        os.system("clear")
                        date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                        url=self.get_the_all_news(date,Table_name,1,0)
                        self.get_news_or_my_custom_news(url, Table_name)
                    except Exception as e:
                        print(f"Hata: {e}")
                        break

            elif option == "2":

        
                os.system("clear")

                tarih_bilgisi = datetime.datetime.now()#şuanki tarih bilgisini alır 
                #ama şu formatta yazdırır = 2024-05-27 10:04:23.175173 bizim bunu databasede olan foratta yazdırmamız lazım
                # databasedeki format ludur = 2024/25/07
                
                # Tarihi istenen formatta yazdırma
                formatli_tarih = tarih_bilgisi.strftime("%Y/%m/%d") # %Y/%m/%d formatı, yılı dört basamak olarak, ayı iki basamak olarak ve günü iki basamak olarak gösterir ve bu parçalar arasında "/" karakterini kullanır.
                print("Formatlı Tarih:", formatli_tarih)

                date=formatli_tarih # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                url=self.get_the_all_news(date,Table_name,1,0)
                self.get_news_or_my_custom_news(url,Table_name)
                
            elif option == "3":
                
            
                os.system("clear")

                
                print(Fore.BLUE+"""
                    Bu kısımda tarih bilgisini şu formatta vermelisiniz :: yıl/ay/gün 

                """+Style.RESET_ALL)

                value=input(Back.GREEN+Fore.BLACK+"tarihi giriniz"+Style.RESET_ALL)

                # Girdinin istenen formata uyup uymadığını kontrol et
                if value.count('/') == 2:  # Girdide iki tane '/' karakteri olup olmadığını kontrol et
                    parts = value.split('/')  # Girdiyi '/' karakterine göre bölerek parçalarına ayır
                    # Parçaların uzunluklarını ve sayı olup olmadıklarını kontrol et
                    if len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                        print(Fore.GREEN+"Tarih formatı doğru."+Style.RESET_ALL)  # Format doğruysa mesaj yazdır
                        date=value # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                        url=self.get_the_all_news(date,Table_name,1,0)
                        self.get_news_or_my_custom_news(url,Table_name)  
                    else:
                        print(Fore.RED+"Yanlış formatta giriş yaptınız.")  # Parçalar doğru uzunlukta veya sayı değilse mesaj yazdır
            
            
                       
                                    





            elif option == "4":
                os.system("clear")
                date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                url=self.get_the_all_news(date,Table_name,1,1)
                self.get_news_or_my_custom_news(url, Table_name)
                
            
            elif option == "5":
                os.system("clear")
                date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                url=self.get_the_all_news(date,Table_name,0,0)
                self.get_news_or_my_custom_news(url, Table_name)
            
            else:
                print(Fore.RED+"Yanlış formatta giriş yaptınız.")  # '/' karakteri sayısı doğru değilse mesaj yazdır
                
            
                    


    def metin_ozet_al(self,content):#bunu devam ettir text ve img değerleri döndürsün ve create_html fonksiyonunu burada çalıştırsın .

        # Parse the input text
        parser = PlaintextParser.from_string(content, Tokenizer("turkish"))

        # Create an LSA summarizer
        summarizer = LsaSummarizer()

        # Generate the summary
        summary = summarizer(parser.document, sentences_count=10)  

        time.sleep(3)
            
    # Output the summary
        summarized_text = ""
        for sentence in summary:
            summarized_text += str(sentence) + " "  # Her cümleyi özette birleştir
        return summarized_text  # Tüm özetlenmiş metni döndür

    def create_html(self, text, img, header):
        # HTML içeriğini oluştur
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ozan Bozkurt</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <header>
                <nav>
                    <ul>
                        <li><a href="cv-site/index.html">Anasayfa</a></li>
                        <li><a href="https://github.com/ozan-B">İçerik</a></li>
                        <li><a href="https://www.linkedin.com/in/ozan-bozkurt-66742919a/">İletişim</a></li>
                    </ul>
                </nav>
            </header>
            <div class="container">
                <h1>{header}</h1>
                <img src={img} alt="image" class="header-image">

                <div class="content">
                    <p>
                    {text}
                    </p>
                </div>
            </div>
            <footer>
                <p>&copy; 2024 Ozan Bozkurt. Tüm hakları saklıdır.</p>
            </footer>
        </body>
        </html>

        """

        # HTML içeriğini dosyaya yaz
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(html_content)

    def all_scrap_data(self):
        
        #1-Ana domain
        url1="https://www.haberturk.com/saglik"
        data_base_table_name="Odev"
        self.scrape_and_save(url1,data_base_table_name)
        print(Fore.GREEN+"Sağlık verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(10)


        #2- Genel Sağlık

        data_base_table_name_sub="Genel_Saglik"
        url2="https://www.haberturk.com/saglik/genel-saglik"
        self.scrape_and_save(url2, data_base_table_name_sub)
        print(Fore.GREEN+"Genel Sağlık verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(10)

        #3-Anne ve Çocuk
        data_base_table_name_sub="Anne_Cocuk"
        url3="https://www.haberturk.com/saglik/anne-ve-cocuk"
        self.scrape_and_save(url3, data_base_table_name_sub)
        print(Fore.GREEN+"Anne ve Çocuk  verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        #4-Kalp sağlığı
        data_base_table_name_sub="Kalp_Saglik"
        url4="https://www.haberturk.com/saglik/kalp-sagligi"
        self.scrape_and_save(url4, data_base_table_name_sub)
        print(Fore.GREEN+"Kalp sağlığı verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        #5-Beslenme
        data_base_table_name_sub="Beslenme"
        url5="https://www.haberturk.com/saglik/saglikli-beslenme"
        self.scrape_and_save(url5, data_base_table_name_sub)
        print(Fore.GREEN+"Beslenme verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        #6-Kanser
        data_base_table_name_sub="Kanser"
        url6="https://www.haberturk.com/saglik/kanser"
        self.scrape_and_save(url6, data_base_table_name_sub)
        print(Fore.GREEN+"Kanser verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        #7-Cinsel Sağlık
        data_base_table_name_sub="Cinsel_Saglik"
        url7="https://www.haberturk.com/saglik/cinsel-saglik"
        self.scrape_and_save(url7,data_base_table_name_sub)
        print(Fore.GREEN+"Cinsel Sağlık verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        #8-Estetik cerrahi
        data_base_table_name_sub="Estetik_Cerrahi"
        url8="https://www.haberturk.com/saglik/estetik-cerrahi"
        self.scrape_and_save(url8,data_base_table_name_sub)
        print(Fore.GREEN+"Sağlık verileri çekildi ve kaydedildi"+Style.RESET_ALL)
        time.sleep(20)

        
    def main(self):
    
        self.banner()
        try:
            self.connect_veritabani_bozkurt()   
        
            #Program başladığı anda Python server aç arka planda çalışsın
            # Sunucuyu arka planda başlatmak için subprocess.Popen kullandım fonksiyonun bitiminde serverı kapatmalısın
            server_process=subprocess.Popen(["python", "-m", "http.server", "1234"], stderr=subprocess.DEVNULL)#hata çıktıları nulla gitsin
            time.sleep(1)
            print(Fore.GREEN+"Python server çalıştırıldı -> http://0.0.0.0:1234/")
            print("\n")

            #Program çalıştığı an haberler/sağlık ve sağlığın subdomainlerindeki veriler 
            #kazılsın ve ilgili databaselere kaydedilsin.(BU isteğe bağlı olacak kullanıcıya iki soru sor: Database yenilensin mi , yoksa mevcut databasede işlem mi yapılsın.)

            op=input(Back.GREEN +Fore.BLACK + "Database yenilensin mi y/n: "+Style.RESET_ALL)
            
            if op=="y" or op=="Y":
                self.all_scrap_data()
            elif op=="n" or op=="N":
                pass
            else:
                print(Fore.RED+"yanlış seçim yaptınız")


            while True :
                print(Fore.BLUE+"""      
                    1-Tüm haberleri getir
                    
                    2-Son bir günde çıkan haberleri getir
                    
                    3-Verilen tarihteki haberleri getir
                    
                    4-Sağlık subdomainleri haberlerine bak
                    
                    5-Haber resminde insan olan haberleri getir
                      
                    6-Haber resminde insan olmayan haberleri getir
                      
                """)           

                option=input(Back.GREEN +Fore.BLACK +"seçimini yap : "+Style.RESET_ALL)



                if option == "1":

                    while True:
                        try:
                            os.system("clear")
                            Table_name="Odev"

                            date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                            url=self.get_the_all_news(date,Table_name,1,0)
                            self.get_news_or_my_custom_news(url, Table_name)
                        except Exception as e:
                            print(f"Hata: {e}")
                            break

                    #ana menüye dönme veya aracı kullanmaya devam etmek için kontrol mekanizması
                    user_input = self.back()
                    if user_input == 'b' or user_input == 'B':
                        os.system('clear')
                        break
                    elif user_input == 'a' or user_input == 'A':
                        os.system('clear')
                        continue
                    else:
                        print("Good By :)")
                        exit()
                            
                        
            
                elif option == "2":

                    while True:
                        try:
                            os.system("clear")

                            Table_name="Odev"

                            tarih_bilgisi = datetime.datetime.now()#şuanki tarih bilgisini alır 
                            #ama şu formatta yazdırır = 2024-05-27 10:04:23.175173 bizim bunu databasede olan foratta yazdırmamız lazım
                            # databasedeki format ludur = 2024/25/07
                            
                            # Tarihi istenen formatta yazdırma
                            formatli_tarih = tarih_bilgisi.strftime("%Y/%m/%d") # %Y/%m/%d formatı, yılı dört basamak olarak, ayı iki basamak olarak ve günü iki basamak olarak gösterir ve bu parçalar arasında "/" karakterini kullanır.
                            #print("Formatlı Tarih:", formatli_tarih)

                            date=formatli_tarih # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                            url=self.get_the_all_news(date,Table_name,1,0)
                            Table_name="Odev"

                            self.get_news_or_my_custom_news(url,Table_name)

                        except Exception as e:
                                print(f"Hata: {e}")
                                break
                        
                    user_input = self.back()
                    if user_input == 'e' or user_input == 'e':
                        os.system('clear')
                        break
                    elif user_input == 'a' or user_input == 'A':
                        os.system('clear')
                        continue
                    else:
                        print("Good By :)")
                        exit()


                
                elif option == "3":

                    while True:

                        try:
                            os.system("clear")

                            Table_name="Odev"

                            
                            print(Fore.BLUE+"""
                                Bu kısımda tarih bilgisini şu formatta vermelisiniz :: yıl/ay/gün 

                            """+ Style.RESET_ALL)

                            value=input(Back.GREEN+Fore.BLACK+"tarihi giriniz"+Style.RESET_ALL)

                            # Girdinin istenen formata uyup uymadığını kontrol et
                            if value.count('/') == 2:  # Girdide iki tane '/' karakteri olup olmadığını kontrol et
                                parts = value.split('/')  # Girdiyi '/' karakterine göre bölerek parçalarına ayır
                                # Parçaların uzunluklarını ve sayı olup olmadıklarını kontrol et
                                if len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                                    print(Fore.GREEN+"Tarih formatı doğru."+Style.RESET_ALL)  # Format doğruysa mesaj yazdır
                                    date=value # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                                    url=self.get_the_all_news(date,Table_name,1,0)
                                    
                                    Table_name="Odev"
                                    self.get_news_or_my_custom_news(url,Table_name)  
                                
                                else:
                                    print(Fore.RED+"Yanlış formatta giriş yaptınız."+Style.RESET_ALL)  # Parçalar doğru uzunlukta veya sayı değilse mesaj yazdır
                            else:
                                print(Fore.RED+"Yanlış formatta giriş yaptınız."+Style.RESET_ALL)  # '/' karakteri sayısı doğru değilse mesaj yazdır
                        
                        except KeyboardInterrupt:
                            print("\nçıkış yapılıyor")
                            
                            
                            user_input = self.back()
                            if user_input == 'e' or user_input == 'e':
                                os.system('clear')
                                break
                            elif user_input == 'a' or user_input == 'A':
                                os.system('clear')
                                continue
                            else:
                                print("Good By :)")
                                #exit()


                    user_input = self.back()
                    if user_input == 'b' or user_input == 'B':
                        os.system('clear')
                        break
                    elif user_input == 'a' or user_input == 'A':
                        os.system('clear')
                        continue
                    else:
                        print("Good By :)")
                        exit()


                    
                
                elif option == "4":


                    os.system("clear")

                    Table_name="Odev_Sub"
                
                    
                
                    while True:

                        print(Fore.BLUE+"""
                            1- Genel Sağlık
                            2- Anne ve Çocuk
                            3- Kalp sağlığı
                            4- Beslenme
                            5- Kanser
                            6- Cinsel Sağlık
                            7- Estetik cerrahi
                            """+Style.RESET_ALL)
                        
                        option=input(Back.GREEN +Fore.BLACK + "İçeriğine bakmak istediğiniz bir alt başlık seçiniz"+Style.RESET_ALL)


                        if option=="1":
                            
                            try:
                                os.system("clear")
                                Table_name="Genel_Saglik"
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()
                                

                        elif option=="2":
                            os.system("clear")

                            try:
                                Table_name="Anne_Cocuk"
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()


                        elif option=="3":
                            os.system("clear")

                            try:
                                Table_name="Kalp_Saglik"
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()


                        elif option =="4":
                            os.system("clear")

                            try:
                                Table_name="Beslenme"    
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()


                        elif option=="5":
                            os.system("clear")

                            try:
                                Table_name="Kanser"    
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()


                        elif option=="6":
                            os.system("clear")

                            try:
                                Table_name="Cinsel_Saglik"
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()


                        elif option=="7":
                            os.system("clear")

                            try:
                                Table_name="Estetik_Cerrahi"
                                self.main_processes(Table_name)
                            
                            finally:
                                user_input = self.back()
                                if user_input == 'b' or user_input == 'B':
                                    os.system('clear')
                                    break
                                elif user_input == 'a' or user_input == 'A':
                                    os.system('clear')
                                    continue
                                else:
                                    print("Good By :)")
                                    exit()
                        
                            
                        else:
                            print(Fore.RED+"Yanlış tuşladınız tekrar deneyin"+Style.RESET_ALL)
                            continue

                elif option == "5":

                    os.system("clear")
                    Table_name="Odev"
                    date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                    url=self.get_the_all_news(date,Table_name,1,1)
                    self.get_news_or_my_custom_news(url, Table_name)  

                    #ana menüye dönme veya aracı kullanmaya devam etmek için kontrol mekanizması
                    user_input = self.back()
                    if user_input == 'b' or user_input == 'B':
                        os.system('clear')
                        break
                    elif user_input == 'a' or user_input == 'A':
                        os.system('clear')
                        continue
                    else:
                        print("Good By :)")
                        exit()


                elif option == "6":
                    
                    os.system("clear")
                    Table_name="Odev"
                    date=20 # tüm haberleri getirmek için bu değişkeni belirledim tarihin içinde 2024'ün 20'si olan tüm verileri databaseden çekecek
                    url=self.get_the_all_news(date,Table_name,0,0)
                    self.get_news_or_my_custom_news(url, Table_name)     

                    #ana menüye dönme veya aracı kullanmaya devam etmek için kontrol mekanizması
                    user_input = self.back()
                    if user_input == 'b' or user_input == 'B':
                        os.system('clear')
                        break
                    elif user_input == 'a' or user_input == 'A':
                        os.system('clear')
                        continue
                    else:
                        print("Good By :)")
                        exit()



                else:
                    print("byby")       
            
        except Exception as e :
            # Sunucuyu durdur
            server_process.terminate()
            server_process.wait()
            print(Fore.YELLOW+"Server stopped.")

            # Tüm hataları yakala ve göster
            print(f"Hata oluştu: {e}")


    def url_to_image(self,url):  # Verilen URL'deki resmi indiren ve OpenCV formatına dönüştüren fonksiyon
        try:
            # URL'den resmi indir
            response = requests.get(url, stream=True)
            response.raise_for_status()  # HTTP hatalarını kontrol et
            image_data = np.asarray(bytearray(response.raw.read()), dtype="uint8")
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
            if image is None:
                raise ValueError("Resim indirilemedi veya çözülemedi.")
            return image
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return None
    
    def detect_humans(self,url): # resim de insan var ise True dön , yok ise False dön 


            
        image = self.url_to_image(url)

        if image is None or image.size == 0: # bu if clause opencvde error: (-215:Assertion failed) !ssize.empty() in function 'resize' hatasını engellemek için konulmuştur. 
            print("Geçersiz veya boş görüntü.")
            return False

        # YOLOv3 için önceden eğitilmiş model ve konfigürasyon dosyalarını yükle
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        layer_names = net.getLayerNames()
        
        try:
            output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        except:
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        # COCO sınıf isimlerini yükle
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]

        # Resmi blob'a çevir
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Tespit edilen nesneler için bilgi listesi
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and classes[class_id] == "person":
                    # Nesnenin merkezi ve kutusu
                    center_x = int(detection[0] * image.shape[1])
                    center_y = int(detection[1] * image.shape[0])
                    w = int(detection[2] * image.shape[1])
                    h = int(detection[3] * image.shape[0])

                    # Kutunun sol üst köşesi
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        if len(class_ids) > 0:
            return True
        else:
            return False
        
    
    '''# Resim URL'sini buraya girin
    url = "https://im.haberturk.com/l/2024/05/31/ver1717148503/3691280/jpg/640x640"
    image = url_to_image(url)
    contains_human = detect_humans(image)

    if contains_human:
        print("Resimde insan var.")
    else:
        print("Resimde insan yok.")'''

#----------------------------------------------------------------

program = Program()

ozan=program.main()

