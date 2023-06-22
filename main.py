
from bs4 import BeautifulSoup
import requests
import csv 
import datetime
import time
import smtplib


with open('youtube.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    header=['Views','Time Stamp']
    writer.writerow(header)



URL = 'https://www.youtube.com/watch?v=4M60iSPyCwA'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.text, "html.parser")

soup = BeautifulSoup(soup.prettify(), "html.parser")
views_meta = soup.find('meta', {'itemprop': 'interactionCount'})
views = views_meta['content']
views=int(views)
print(type(views))



def send_mail(email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()


    username = 'projectwebscraping@gmail.com'
    password = 'euozacvozfqdtpzj'
    server.login(username, password)

    from_email = username
    to_email = email
    subject = 'ViewerShip Crossed'
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    body = f'The viewership has crossed your limit at {current_time}'
    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(from_email, to_email, message)   

def check_views(URL,threshold,email):
    #URL = 'https://www.youtube.com/watch?v=gk4JTomY6aE'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.text, "html.parser")

    soup = BeautifulSoup(soup.prettify(), "html.parser")
    views_meta = soup.find('meta', {'itemprop': 'interactionCount'})
    views = views_meta['content']
    views=int(views)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    #threshold=103000
    
    data = [views,current_time]

    with open('youtube.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    if views>threshold:
        send_mail(email)
        return 1
    return 0

def main(url,threshold,email):
    while(True):
        check=check_views(url,threshold,email)
        if check==1:
            break
        time.sleep(10)



