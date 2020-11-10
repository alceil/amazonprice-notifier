import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Redmi-Note-Pebble-Grey-Storage/dp/B086977TR6/ref=sr_1_2?dchild=1&keywords=REDMI&qid=1605014171&sr=8-2'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56' }
def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    # title = soup.find(id="title").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    print(price[5:8])
    converted_price = float(price[5:8])
    if(converted_price<11000):
            send_mail()
    # print(converted_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # server.login('','')
    subject = 'Price fell down'
    body = 'check the amazon link https://www.amazon.in/Redmi-Note-Pebble-Grey-Storage/dp/B086977TR6/ref=sr_1_2?dchild=1&keywords=REDMI&qid=1605014171&sr=8-2'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'ashishshajisrampickal@gmail.com',
        'asifamalyt@gmail.com',
        msg
    )
    print('Hey dummy email has been sent')
    server.quit()
check_price()    
      
   

