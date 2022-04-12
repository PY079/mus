import urllib.request, os, requests, re, time, datetime, sys, random
from playsound import playsound
from bs4 import BeautifulSoup
from fake_useragent import UserAgent # новое
from colorama import Fore, Style, init
from os import environ, getcwd
import fake_useragent
init()


def да():
    playsound('C:/Users/'+user+'/Jarvis/da.wav')
    
def загружаю():
    playsound('C:/Users/'+user+'/Jarvis/Загружаю сэр.wav')
    
def есть():
    playsound('C:/Users/'+user+'/Jarvis/Есть.wav')

def чего():
    playsound('C:/Users/'+user+'/Jarvis/Чего вы пытаетесь добиться сэр.wav')

def мы():
    playsound('C:/Users/'+user+'/Jarvis/Мы подключены и готовы.wav')

def как_пож():
    playsound('C:/Users/'+user+'/Jarvis/Как пожелаете.wav')

def перез():            # новое
    playsound('C:/Users/'+user+'/Jarvis/Я перезагрузился сэр.wav')

def усл():            # новое
    playsound('C:/Users/'+user+'/Jarvis/К вашим услугам сэр.wav')

def rand():
    a = random.randint(1,3)
    if a == 1:
        да()
    if a == 2:
        загружаю()
    if a == 3:
        есть()



while True:
    global noh
    noh = 1
    
    
    
    user = fake_useragent.UserAgent().random
    
    headers = {
        'user-agent': user
    }
    
    
    def res():
        print(Style.RESET_ALL)
    
    
    
    getUser = lambda: environ['USERNAME']
    user = getUser()
    global d
    
    def dat():
        while True:
            today = datetime.datetime.today()
            global d
            d = today.strftime("%Y-%m-%d-%H.%M.%S")
            break
        
    
    os.system('cls')
    print('\n\n',headers,'\n\n\n')
    dat()
    print(Fore.CYAN+Style.BRIGHT+'  Время: ',d)
    res()
    print('\n\n  Чтобы выйти введите - '+Fore.RED+Style.BRIGHT+'0\n'+Style.RESET_ALL)
    isp = input("\n\n  Введите исполнителя --> ")
    if isp == '0':
        os.system('cls')
        усл()
        break
    track = input("\n    Введите трек --> ")
    if track == '0':
        os.system('cls')
        усл()
        break
    print('\n\n\n')
    url = 'https://ru.hitmotop.com/search?q='+isp+'+-+'+track
    
    
    if isp == '' and track == '':
        print(Fore.RED+Style.BRIGHT+'\n\n     Вы ввели ничего\n\n'), чего()
        res()
        noh = 0
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'10с\r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'9с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'8с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'7с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'6с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'5с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'4с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'3с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'2с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'1с \r'+Style.RESET_ALL)
        time.sleep(1)
        sys.stdout.write('  Перезапуск через '+Fore.GREEN+Style.BRIGHT+'0с \r'+Style.RESET_ALL)
        перез()
        print('\n\n')
        
    if noh == 1:
        if track == '':
            url = 'https://ru.hitmotop.com/search?q='+isp
            print('  Исходная ссылка:  ',url)
            
        
        
        
        
        track2 = re.sub(" ", "+", url)
        
        print('    Изменённая ссылка:  ',track2)
        
        
        
        req = requests.get(url, headers)
        
        
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        
        naz_track = soup.find_all('div', class_='track__title')
        musikant_track = soup.find_all('div', class_='track__desc')
        count = 0
        coun = 0
        
        
        print('\n\n\n')
        na = []
        for i in naz_track:
            coun +=1
            global i_text
            i_text = i.text
            i_text = i_text.lstrip()
            print(Fore.GREEN+Style.BRIGHT+f"  {coun}  "+Fore.CYAN+'Трек: '+Style.RESET_ALL+f"{musikant_track[count].text} - {i_text}")
            na.append(i_text)
        
        
        
        
            
        items = soup.find_all('ul', class_='tracks__list')
        
        
        print('\n\n\n')
        #               ссылка
        
        
        
        global nm
        nm = 0
        sp = []
        print('\n\n')
        for uro in soup.find_all('a', class_='track__download-btn'):
            global abn
            abn = uro.get('href')
            sp.append(abn)
            nm+=1
            print(Fore.GREEN,Style.BRIGHT,f'  {nm}',Fore.CYAN+Style.BRIGHT+'  Ссылка: ',Style.RESET_ALL,'    ',f'{abn}','\n')
            #print('    ',f'{abn}','\n')
            
        
        
        
        
        
        print('\n\n\n')
        
        while True:
            
           
            
            
            print('\n Выйти из скачки - '+Fore.RED+Style.BRIGHT+'0'+Style.RESET_ALL)
            ap = int(input('\n\n Что скачать --> '))
            if ap == 0:
                os.system('cls')
                break
            
            if ap <= 48:
                nm = sp[ap-1]
                print(nm)

                rand()
                try:
                    global ab
                    ab = 'hitmotop' 
                    df = 'c:/Users/'+user+'/'+ab
                    os.mkdir(df)
                    print('\n         Папка hitmotop создана в '+ df)
                except FileExistsError:
                    print("\n      Папка hitmotop"+ Fore.CYAN+ ' уже '+ Style.RESET_ALL +'создана в '+df+'\n')
                    time.sleep(3)
            
            
                url2 = abn
                        
                if track == '':
                    dat()
                    urllib.request.urlretrieve(nm, 'c:/Users/'+user+'/'+ab+'/'+isp+'_'+d+'.mp3')
                    print('     Файл '+isp+' ' + d + Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
              
                else:
                    urllib.request.urlretrieve(nm, 'c:/Users/'+user+'/'+ab+'/'+isp+'_'+track+'.mp3')
                    print('     Файл '+isp+' ' + track + Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)