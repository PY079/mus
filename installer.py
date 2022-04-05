import urllib.request, os, requests, re, time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Style, init
init()

os.system('cls')

isp = input("\n\n  Введите исполнителя --> ")
track = input("\n    Введите трек --> ")
url = 'https://ru.hitmotop.com/search?q='+isp+'+-+'+track

if track == '':
    url = 'https://ru.hitmotop.com/search?q='+isp
    print(url)
    
print(url)



track2 = re.sub(" ", "+", url)

print('      '+track2)


headers = {"user-agent:":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.360"}
req = requests.get(url, headers)



response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


naz_track = soup.find_all('div', class_='track__title')
musikant_track = soup.find_all('div', class_='track__desc')
count = 0
coun = 0

for i in naz_track:
    coun +=1
    i_text = i.text
    i_text = i_text.lstrip()
    print(f"  {coun}  Трек: {musikant_track[count].text} - {i_text}")


    
items = soup.find_all('ul', class_='tracks__list')


print('\n\n\n')
#               ссылка

def itn():   
    for item in items:
        global abn
        abn = item.find('a',  class_='track__download-btn').get('href')
        print('      ',abn)
itn()










# скачивание

ipnn = input('\n\n   Скачивать [y/n] -->   ')



if ipnn == 'y':

    try:
        global ab
        ab = 'hitmotop' 
        df = 'c:/Users/User/'+ab
        os.mkdir(df)
        print('\n         Папка hitmotop создана в '+ df)
    except FileExistsError:
        print("\n      Папка hitmotop"+ Fore.CYAN+ ' уже '+ Style.RESET_ALL +'создана в '+df+'\n')
        time.sleep(3)


    url2 = abn
    urllib.request.urlretrieve(url2, 'c:/Users/User/'+ab+'/'+isp+'_'+track+'.mp3')
    print('     Файл '+isp+' ' + track + Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)

if ipnn == 'n':
    pass
    



   
