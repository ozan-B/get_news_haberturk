# :inbox_tray:İndirme ve Kurulum   :inbox_tray:

>- git clone https://github.com/ozan-B/get_news_haberturk.git
>- cd get_news_haberturk/project
>- python3 setup.py
>- python3 main.py

>**Not1:** Bilgisayarınızda chrome browser olmalı
>**Not2:** main.py dosyasındaki driver path değişkenini kendi driverınızın yolu olarak değiştirmeyi unutmayın
---

# :snowflake: Aracın amacı ve ne yaptığı hakkında ön bilgi :snowflake:

Program **[habertürkün sağlık haberleri](https://www.haberturk.com/saglik)** domainini ve bu domainin subdomainlerini tarar istediğimiz verileri **bozkurt.db** adlıveri tabanına kaydeder . Daha sonra bu haber verileri üzerinde bize çeşitli seçenekler sunar bu seçenekler :

- **Tüm haberleri göster**
- **Haberi aç**
- **Haberin özetini aç**
- **Son bir günde çıkan haberleri göster**
- **Verdiğim tarihte çıkan haberleri göster**

---

# :snowflake: Kullanılan kütüphaneler ve modüller :snowflake:
>from **selenium** import **webdriver**
from **selenium.webdriver.common.by** import **By**
from **selenium.webdriver.common.keys** import **Keys**
from **selenium.webdriver.chrome.service** import **Service**
from **selenium.webdriver.chrome.options** import **Options**
from **bs4** import **BeautifulSoup**
import **time**
import **sqlite3** as **sql**
import **re**
from **prettytable** import **PrettyTable**
from **colorama** import **Fore ,Back, Style**
import **requests**
import **subprocess**
import **json**
from **sumy.parsers.plaintext** import **PlaintextParser**
from **sumy.nlp.tokenizers** import **Tokenizer**
from **sumy.summarizers.lsa** import **LsaSummarizer**
import **datetime**
import **sys**
import **os**


## 1-selenium.webdriver:

**webdriver:** Web tarayıcılarını otomatik olarak kontrol etmek için kullanılır. Otomatik testler, web scraping ve tarayıcıda insan etkileşimini taklit etmek için kullanılır.
**By:** HTML öğelerini bulmak için kullanılan konum belirleyici stratejileri sağlar (örneğin, ID, sınıf adı).
**Keys:** Klavye tuşlarını simüle etmek için kullanılır (örneğin, ENTER, TAB).
**Service:** WebDriver servislerini yönetmek için kullanılır (örneğin, ChromeDriver servisleri).
**Options:** WebDriver için özel tarayıcı ayarları belirlemek için kullanılır (örneğin, başlık modu, tarayıcı seçenekleri).

## 2- BeautifulSoup:

HTML ve XML dosyalarını ayrıştırmak ve bunlardan veri çekmek için kullanılır. Web scraping işlemlerinde yaygın olarak kullanılır.

## 3-time:
Zamanla ilgili işlemler yapmak için kullanılır (örneğin, bekleme süreleri eklemek, zaman damgası almak).

## 4-sqlite3 as sql:

SQLite veritabanı yönetim sistemi ile etkileşim kurmak için kullanılır. Veritabanı işlemleri yapmak için kullanılır (örneğin, veri eklemek, sorgulamak).

## 5- re:
Düzenli ifadeler kullanarak metinleri işlemek ve desen eşleştirme yapmak için kullanılır.

## 6-prettytable:

Verileri tablo formatında görselleştirmek ve yazdırmak için kullanılır.

## 7-colorama:

**Fore, Back, Style:** Terminal çıktısında metinleri renklendirmek ve stil vermek için kullanılır.

## 8-requests:
HTTP istekleri yapmak için kullanılır (örneğin, web sayfalarına GET ve POST istekleri göndermek).

## 9- subprocess:

Yeni süreçler başlatmak ve bu süreçlerle etkileşimde bulunmak için kullanılır. Sistem komutlarını çalıştırmak için kullanılır.

## 10- json:
JSON (JavaScript Object Notation) verilerini işlemek için kullanılır. JSON verilerini Python veri yapılarına dönüştürmek ve tam tersi işlemi yapmak için kullanılır.

## 11- sumy.parsers.plaintext, sumy.nlp.tokenizers, sumy.summarizers.lsa:

**PlaintextParser:** Düz metin dosyalarından veri ayrıştırmak için kullanılır.

**Tokenizer:** Metinleri belirli dil kurallarına göre tokenlere (kelimelere) ayırmak için kullanılır.

**LsaSummarizer:** LSA (Latent Semantic Analysis) algoritmasını kullanarak metin özetleri oluşturmak için kullanılır.

## 12- datetime:

Tarih ve saat ile ilgili işlemler yapmak için kullanılır.

## 13- sys:

Python yorumlayıcısı ile ilgili çeşitli işlevlere erişim sağlar (örneğin, komut satırı argümanlarını almak, sistemden çıkmak).

## 14- os

İşletim sistemi ile etkileşim kurmak için kullanılır (örneğin, dosya ve dizin işlemleri, çevre değişkenlerine erişim).

---
---

# :pencil: Class'ın fonksiyonlarının açıklamaları :pencil:

# 1- _init_ :

![init](/img/init.png)

##### Bu fonksiyon Selenium ile Chrome tarayıcısını başlatmak ve bu tarayıcıyı arka planda çalıştırmak için gereken ayarları ve yapılandırmayı yapar.

- __init__ metodu, sınıfın yapıcı metodudur ve sınıf örneği oluşturulduğunda çalışır.

- **self.veritabani_bozkurt** değişkeni, SQL veritabanı bağlantısı için yer tutucu olarak **sql.Connection** ile başlatılmış.

- **self.driver_path değişkeni**, ChromeDriver'ın dosya yolunu saklar.
- **Service** sınıfı kullanılarak ChromeDriver servisi başlatılır. 

- **--headless** argümanı eklenerek tarayıcının arka planda (görünmez) çalışması sağlanır.
- **webdriver.Chrome** kullanılarak Chrome tarayıcısı başlatılır. 

# 2- banner :
![banner](/img/banner.png)

- Bu fonksiyon slowprint fonksiyonu kulllanılarak bannerımız ekrana yazılır.

# 3- slowprint:
![slowprint](/img/slow_print.png)
- Bu fonksiyon verilen bir metni **(s)** ekrana yavaş yavaş, karakter karakter yazdırır. 

# 4- back:
![back](/img/back.png)

- Kullanıcının bir seçim yapmasını sağlayan ve bu seçimi geri döndüren bir kullanıcı arayüzü işlevidir .

# 5- scrape_and_save:
![scrape_and_save_1](/img/scrape_and_save_1.png)
![scrape_and_save_2](/img/scrape_and_save_2.png)

##### belirli bir URL'den web sayfasını çeker, belirli bir tabloya verileri kaydeder ve ardından belirli bir desene göre sayfanın içeriğini tarar. İşte kodun kısa açıklaması:

- **self.driver.get(url):** Selenium kullanarak belirtilen URL'ye tarayıcıyı yönlendirir.
- Tarayıcıda sayfa yüklenmesi için **time.sleep(3)** kullanılır.
- Sayfanın sonuna kadar kaydırma işlemi yapılır. Bu, sayfanın içeriğinin tamamını almak için gerekli olabilir.
- BeautifulSoup kütüphanesi kullanılarak sayfanın HTML içeriği parse edilir.
- Tüm `<a>` etiketleri bulunur.
- Her bir `<a>` etiketi için belirli kriterlere göre  bazı veriler alınır **(örneğin, URL, başlık, resim URL'si).**
- Elde edilen veriler, bir desenle **(regex)** karşılaştırılarak belirli bir formata uygun olup olmadığı kontrol edilir.
- Veritabanında daha önce kaydedilip kaydedilmediğini kontrol etmek için elde edilen URL veritabanında aranır.
- Eğer URL veritabanında yoksa, bu veriler veritabanına kaydedilir.

# 6- connect_veritabani_bozkurt:
![connect_veritabani_bozkurt](/img/connect_veritabani_bozkurt.png)
- Bozkurt adlı sqlite veri tabanımıza bağlanmamızı sağlayan fonksiyondur kendisi .

# 7- get_the_all_news:
![get_the_all_news_1](/img/get_the_all_news_1.png)
![baget_the_all_news_2](/img/get_the_all_news_2.png)

##### Bu fonksiyon, veritabanından belirli bir tarih aralığındaki haberleri çeker ve bu haberleri bir tablo formatında ekrana yazar. Kullanıcıya bu haberlerden birini seçmesi için bir haber ID'si girmesini sağlar.

- **self.connect_veritabani_bozkurt():** Veritabanına bağlanır.
- Belirtilen tarihte kaydedilmiş haber başlıklarını ve kısaltılmış URL'leri veritabanından alır.
- Aldığı verileri bir tablo formatında düzenler ve ekrana yazar.
- Kullanıcıdan bir haber ID'si alır.
- Kullanıcının girdiği ID'ye karşılık gelen haber bilgilerini (başlık ve URL) yine tablo halinde ekrana yazdırır.
- Bu seçilen haberin URL'sini bir değişkene atar ve bu değeri döndürür.


# 8- control_saved_domain_database:
![control_saved_domain_database](/img/control_saved_domain_database.png)

##### Bu fonksiyon, verilen bir domain değerini alır ve bu domain değerini belirtilen bir tablodaki diğer domain değerleriyle karşılaştırarak veritabanında mevcut olup olmadığını kontrol eder.
##### Bu fonksiyon, veritabanında bir domain değerinin tekrarlanmasını engellemek için kullanılır. Eğer verilen bir domain değeri zaten veritabanında bulunuyorsa, bu değerin tekrar kaydedilmesini engeller.

- **cursor.execute(f"SELECT Domain FROM {Table_name}"):** Belirtilen tablodan **(Table_name)** tüm domain değerlerini alır.
- Veritabanındaki tüm domain değerleriyle verilen domain değerini karşılaştırır.
- Eğer verilen domain değeri veritabanında bulunursa, **found değişkeni True olarak ayarlanır.**
- Eğer verilen domain değeri veritabanında bulunmazsa, **found değişkeni False olarak kalır.**
- Son olarak, fonksiyon, veritabanında verilen domain değerinin bulunup bulunmadığını belirten bir **boolean** değer döndürür.




# 9- save_to_database:
![save_to_database](/img/save_to_database.png)

##### Bu fonksiyon, verilen bir domain, başlık, resim URL'si, tarih ve tablo adıyla birlikte veritabanına veri ekler.

##### verilen verileri belirtilen bir tabloya ekler ve ekleme işlemi başarılı olursa kullanıcıya geri bildirim sağlar.


- **self.url_shorter(domain):** Verilen domain değerini kısaltır ve kısaltılmış URL'yi döndürür. Bu işlem, kullanıcıya URL'yi daha anlaşılır ve kısa bir şekilde göstermek için kullanılır.
- **sql_query** adında bir SQL sorgusu oluşturulur. Bu sorgu, belirtilen tabloya **(Table_name)** verilen değerlerin eklenmesini sağlar.
- SQL sorgusu, **cursor.execute()** ile çalıştırılır. **execute()** metodu, SQL sorgusunu çalıştırarak veritabanına veri ekler.
- Veritabanındaki değişiklikler, **self.veritabani_bozkurt.commit()** ile kaydedilir.
- Eğer işlem başarılı olursa, kullanıcıya **"Veritabanına başarıyla eklendi."** şeklinde bir mesaj gösterilir.
- Eğer bir hata oluşursa, kullanıcıya **"Veritabanına ekleme yapılırken bir hata oluştu:"** şeklinde bir hata mesajı ve hatanın detayları gösterilir.




# 10- url_shorted:
![url_shorter](/img/url_shorter.png)
- Verilen url 'i tinyurl apisi yardımı ile kısaltır .
  
# 11- get_news_or_my_custom_news:

#### Bu fonksiyon, kullanıcıya haberin orijinal sitesine gitme veya özetini kendi yerel sitesinde görüntüleme imkanı tanır. 
  
#### 1. seçenekte Veritabanından gerekli bilgileri alır ve bir bash script yardımı ile web sitesini yeni bir chrome sekmesinde açar.

#### 2. seçenekta Veritabanından gerekli bilgileri alır ve bu bilgileri kullanarak HTML dosyası oluşturur ve kullanıcıya sunar.

#### Fonksiyon iki parametre alıyor .
- **new_url:** Kullanıcının ilgilendiği haberin URL'si.
- **Table_name:** Veritabanındaki tablonun adı.

#### Adımlar :

##### 1- ANSI Kaçış Dizilerini Kaldırma

##### 2- Kullanıcı Seçenekleri Menüsü

##### 3-Seçenek 1: *Haberi Aç*

![get_news_or_my_custom_news](/img/get_news_or_my_custom_news.png)
![url_shget_news_or_my_my_custom_newsorter_2](/img/get_news_or_my_my_custom_news_2.png)


- Eğer kullanıcı "1" seçeneğini seçerse:
    - Ekranı temizliyoruz.
    - Kullanıcıya web sitesinin açılacağını bildiriyoruz.
    - Küçük bir bekleme süresinden sonra **(time.sleep(2))**, subprocess.run komutuyla **clean_url**'yi **open_the_url.sh** bashini kullanarak açıyoruz.
    - Döngüyü kırarak işlemden çıkıyoruz.

##### 4-Seçenek 2: *Haberin Özetini Aç*

- Eğer kullanıcı "2" seçeneğini seçerse:
    - Ekranı temizliyoruz.
    - Aşağıdaki işlemleri sırasıyla yapacağız:
  
      - **1- Haber Sitesine Gidip İçeriği Alma**
        - Haber sitesine gidip içeriği almak ve özetini çıkartmak için news_summary fonksiyonunu kullanıyoruz.
      - **2-Veritabanından Resim ve Başlık Bilgilerini Alma**
           - clean_url'yi kullanarak veritabanından resim ve başlık bilgilerini sorguluyoruz.
           - SQL sorgusu yaparak **(SELECT Resim, Title FROM {Table_name} WHERE Short_url="{clean_url}")**, **img_result** ve **header_result** değişkenlerini alıyoruz.
      - **3- HTML Dosyası Oluşturma ve Yerel Sunucuyu Başlatma**
          - create_html fonksiyonunu kullanarak özet, resim ve başlık bilgilerini HTML dosyasına yazıyoruz.
          - Kullanıcıya işlemin başarılı olduğunu bildiriyoruz.

          - Küçük bir bekleme süresinden sonra **(time.sleep(2))**, subprocess.run komutuyla yerel sunucudaki **(http://0.0.0.0:1234)** web sitemizi open_the_url.sh betiği kullanarak açıyoruz.
          - Döngüyü kırarak işlemden çıkıyoruz.

##### 5- Hatalı Giriş

- Eğer kullanıcı geçersiz bir seçenek girerse, **"hatalı giriş"** mesajını yazdırıyoruz ve döngüyü kırarak işlemden çıkıyoruz.





# 12- news_summary:
![news_summary](/img/news_summary.png)

##### Bu fonksiyon, bir web sayfasından haber metinlerini çekerek, gereksiz `<p>` etiketlerini filtreleyip, sadece gerekli olan metinleri alır ve bu metni özetler.

### Haber Özeti Fonksiyonunun Adımları

#### Haber Sitesine Gitme
1. Selenium sürücüsünü kullanarak `news_url` adresine gidiyoruz (`self.driver.get(news_url)`).
2. Sayfanın tam olarak yüklenmesini beklemek için kısa bir süre duraklıyoruz (`time.sleep(2)`).

#### Sayfanın HTML İçeriğini Alma
1. Sayfanın HTML içeriğini `page_source` aracılığıyla alıyoruz ve `html` değişkenine atıyoruz.

#### HTML İçeriğini İşleme
1. `BeautifulSoup` kütüphanesini kullanarak HTML içeriğini parse ediyoruz (`soup = BeautifulSoup(html, 'html.parser')`).

#### `<p>` Etiketlerini Bulma
1. Sayfadaki tüm `<p>` etiketlerini buluyoruz (`p_tags = soup.find_all('p')`).

#### İlgili `<p>` Etiketlerini Filtreleme
1. Bizim için yalnızca sınıf (`class`) özelliği olmayan `<p>` etiketleri önemlidir. Çünkü bu etiketler haberin asıl metnini içerir.
2. Boş bir `content` stringi oluşturuyoruz.
3. Tüm `<p>` etiketlerini döngüyle kontrol ediyoruz.
4. Eğer `<p>` etiketinin sınıf (`class`) özelliği yoksa, o etiketin metin içeriğini (`tag.text.strip()`) `content` stringine ekliyoruz.
5. Bu sayede sadece metin içeren `<p>` etiketlerini almış oluyoruz.

#### Metni Özetleme
1. `content` stringindeki metni özetlemek için `metin_ozet_al` fonksiyonunu çağırıyoruz ve sonucu `summary` değişkenine atıyoruz.

#### Özeti Döndürme
1. `summary` değişkenini fonksiyonun sonucu olarak döndürüyoruz.


# 13- main_processes
![main_processes_1](/img/main_processes_1.png)
![main_processes_2](/img/main_processes_2.png)

#### Bu fonksiyon, kullanıcının belirli bir tarih aralığına göre haberleri getirmesine ve bu haberlerle ilgili işlemler yapmasına olanak tanır.

## Fonksiyon Adımları

#### Seçenek Menüsü Gösterme
Kullanıcıya üç seçenek sunar:
1. Tüm haberleri getirmek.
2. Son bir günde çıkan haberleri getirmek.
3. Belirli bir tarihteki haberleri getirmek.

### Kullanıcı Seçimine Göre İşlem

##### Seçenek 1: Tüm Haberleri Getir
1. Sabit bir tarih (`date=20`) belirler.
2. `get_the_all_news` fonksiyonuyla belirtilen tarihteki tüm haberlerin URL'lerini alır.
3. `get_news_or_my_custom_news` fonksiyonunu çağırarak haberi açar veya özetini gösterir.

##### Seçenek 2: Son Bir Günde Çıkan Haberleri Getir
1. Şu anki tarih bilgisini alır.
2. Tarihi uygun formata (`%Y/%m/%d`) çevirir.
3. `get_the_all_news` fonksiyonuyla bu tarihteki tüm haberlerin URL'lerini alır.
4. `get_news_or_my_custom_news` fonksiyonunu çağırarak haberi açar veya özetini gösterir.

##### Seçenek 3: Belirli Bir Tarihteki Haberleri Getir
1. Kullanıcıdan belirli bir tarih girmesini ister.
2. Girdiyi kontrol ederek doğru formatta olup olmadığını doğrular.
3. `get_the_all_news` fonksiyonuyla belirtilen tarihteki tüm haberlerin URL'lerini alır.
4. `get_news_or_my_custom_news` fonksiyonunu çağırarak haberi açar veya özetini gösterir.




# 14- metin_ozet_al
![main_ozet_al](/img/metin_ozet_al.png)

#### - Bu fonksiyon, uzun bir metni daha kısa bir özet haline getirir.
#### - Önce metni parse eder, sonra LSA algoritmasıyla özetler ve sonunda özetlenmiş metni bir string olarak döndürür.

#### Kısaca Bu fonksiyon, verilen metni özetlemek için Latent Semantic Analysis (LSA) algoritmasını kullanır ve özetlenmiş metni döndürür. 

## metin_ozet_al Fonksiyonunun Adımları

#### Metni Parse Etme
1. `PlaintextParser.from_string(content, Tokenizer("turkish"))` kullanarak, verilen metni (`content`) parse eder.
2. Türkçe metinleri tokenize etmek için `Tokenizer("turkish")` kullanılır.

#### LSA Özeti Oluşturma
1. `LsaSummarizer()` kullanarak bir LSA özetleyici oluşturur.
2. `summarizer(parser.document, sentences_count=10)` ile parse edilen metni kullanarak 10 cümlelik bir özet oluşturur.

#### Özeti Birleştirme
1. `summarized_text` değişkenini tanımlar ve boş bir string olarak başlatır.
2. Özetlenmiş cümleleri döngüyle (`for sentence in summary`) tek bir stringde birleştirir.

#### Özeti Döndürme
1. Birleştirilen özetlenmiş metni (`summarized_text`) döndürür.



# 15- create_html:
![create_html](/img/create_html.png)

# template html koduna fonksiyona verilen değişiklikleri ekler ve bu html kodunu  index.html dosyasına kaydeder .


# 16- all_scrap_data:
![all_scrap_data](/img/all_scrap_data.png)

- #### Bu fonksiyon, belirtilen sağlık kategorilerindeki web sayfalarını tarar ve istenen dataları veritabanına kaydeder.

- #### Fonksiyon, belirtilen sekiz farklı sağlık kategorisinden verileri çekip, her biri için uygun tabloya kaydeder. Her bir kategori için işlemler arasında 10 saniye bekler.

# 17- main:

![main_1](/img/main_1.png)
![main_2](/img/main_2.png)
![main_3](/img/main_3.png)
![main_4](/img/main_4.png)
![main_5](/img/main_5.png)
![main_6](/img/main_6.png)


## -Bu Python kodu, bir haber toplama ve işleme uygulamasının ana işlevini tanımlar. İşlev, belirli sağlık konularındaki haberleri web'den toplar, veritabanına kaydeder ve kullanıcıya çeşitli seçenekler sunar. 

## main() Fonksiyonu Açıklaması

Bu `main()` fonksiyonu, bir dizi işlemi gerçekleştiren bir programın ana döngüsünü oluşturur. İşlem adımları arasında kullanıcıyla etkileşimde bulunur, verileri çeker ve işler, hataları yönetir.

### İşlem Adımları:

1. **Banner Gösterme:**
   - `banner()` fonksiyonunu çağırarak programın başlangıcında bir banner gösterir.

2. **Veritabanına Bağlanma:**
   - `connect_veritabani_bozkurt()` fonksiyonunu çağırarak veritabanına bağlanır.

3. **Python Sunucusunu Başlatma:**
   - `subprocess.Popen()` ile bir Python sunucusu başlatır ve arka planda çalışmasını sağlar.
   - Başlangıç için bir saniye bekleme süresi tanımlar.
   - Başlatılan sunucunun adresini ve port numarasını kullanıcıya gösterir.

4. **Haber Verilerini Çekme:**
   - Kullanıcıya, mevcut veritabanının güncellenip güncellenmeyeceğini sorar.
   - Eğer kullanıcı "y" veya "Y" girerse, `all_scrap_data()` fonksiyonunu çağırarak haber verilerini çeker ve veritabanına kaydeder.
   - Eğer kullanıcı "n" veya "N" girerse, geçerli veritabanındaki işlemlere devam eder.
   - Kullanıcının yanlış bir giriş yapması durumunda uygun bir mesaj gösterir.

5. **Kullanıcı İşlemleri:**
   - Kullanıcıya, çeşitli işlem seçeneklerini sunar.
   - Seçeneklere göre ilgili işlevleri çağırır ve işlem sonunda kullanıcıya geri dönüş seçenekleri sunar.
   - Kullanıcı geri dönüş seçeneklerinden birini seçene kadar bu işlemi tekrarlar.
   - Kullanıcı "a" veya "A" girerse, ana menüye geri döner.
   - Kullanıcı "b" veya "B" girerse, programı sonlandırır.
   - Yanlış bir seçenek girilirse, kullanıcıya bir hata mesajı gösterir ve işlemi tekrarlar.

6. **Hata Yönetimi:**
   - `try-except` bloğu içinde program çalıştırılır.
   - Eğer herhangi bir hata oluşursa, Python sunucusunu kapatır ve hatayı kullanıcıya gösterir.

Bu fonksiyon, kullanıcı ile etkileşime geçerek haber verilerini çeker, işler ve kullanıcının taleplerine göre işlem yapar. Hataları yönetir ve programın akışını kontrol eder.

