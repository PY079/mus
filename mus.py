import urllib.request, os, requests, re, time, datetime, sys, random, pathlib
from playsound import playsound
from bs4 import BeautifulSoup
from fake_useragent import UserAgent # новое
from colorama import Fore, Style, init
from os import environ, getcwd
import fake_useragent
init()

getUser = lambda: environ['USERNAME']
user = getUser()


def col():
    global w
    ih = random.randint(1,5)
    if ih == 1:
        w = Fore.WHITE

    if ih == 2:
        w = Fore.GREEN

    if ih == 3:
        w = Fore.YELLOW

    if ih == 4:
        w = Fore.RED
 
    if ih == 5:
        w = Fore.CYAN

    



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

os.system('cls')
print('\n\n')
def res():
    print(Style.RESET_ALL)

mus = ['Alan Walker - Alone','Alan Walker - Sing Me to Sleep','Alan Walker - Live Fast',
       'Alan Walker - Sweet Dreams','Alan Walker - Sorry','CHVRCHS - Miracle','Clandestina','Eminem - Rap God','Eva Simons - Bludfire','Hans Zimmer - End Credits','Katy Perry - Dark Horse',
       'Alan Walker - Legends Never Die','Leonid Rudenko, ARITMIYA - Rain Sun','Minelli - Rampampam','Nessa Barrett - la di die',
       'Parah Dice - Hot','Alan Walker - Are You Lonely','TOMYGONE Amvis - What More','Оксимирон - Цунами','Annodomini - Никто не Нужен','AC_DC - WAR MACHINE','AC_DC - T_N_T',
       'AC_DC - Thunderstruck','AC_DC - Highway to Hell','AC_DC - Back in Black','Ghostemane - Fed Up','Ghostemane - Venom','uicedeboy - LTE','uicideboy - Paris','Lil Peep - Star Shopping',
       'Король и Шут - Лесник','Lost Frequencies - Reality','The Score - Head Up','Disturbed - Old Friend','Король и Шут - Кукла колдуна','БИ-2, oxxxymiron - Пора возвращаться домой',
       'Blues Saraceno - Dogs of War','БИ-2 - Большие города','Thousand Foot Krutch - Take It Out On Me','Skillet - Back to Life','K.Flay - High Enough','Three Days Grace - So Called Life',
       'Chvrches, Matt Berninger - My Enemy','Bishop Briggs - River','Disturbed - Liberate','Oxxxymiron, Porchy - Earth Burns','Papa Roach - Last Resort','Slipknot - Dead Memories',
       'Dope - Die MF Die','Slipknot - Before I Forget','Александр Пушной - Всё идёт по плану','Би-2 - Чёрное солнце','Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)',
       'Oxxxymiron - Дело нескольких минут (3 раунд, 17 ib)','Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)','Oxxxymiron - В долгий путь (1 раунд 17ib)',
       'Oxxxymiron - До зимы','Oxxxymiron - Не от мира сего','Oxxxymiron - Признаки жизни','Oxxxymiron - Детектор лжи','Oxxxymiron - Хитиновый покров',
       'Oxxxymiron - Волапюк','Oxxxymiron - Больше Бена','Oxxxymiron - Цифры и цвета','Oxxxymiron - Где нас нет','Oxxxymiron - Башня из слоновой кости','Oxxxymiron - Слово мэра',
       'Oxxxymiron - Накануне','Oxxxymiron - Полигон','Oxxxymiron - Колыбельная','Oxxxymiron - Переплетено','Oxxxymiron - Всего лишь писатель','Oxxxymiron - Кем ты стал',
       'Oxxxymiron - Город под подошвой','Oxxxymiron - Reality','Oxxxymiron, Markul - Fata Morgana',
       'Saliva - They Dont Care About Us','Bullet For My Valentine - All These Things I Hate','Jonas Blue and Rita Ora - Ritual','Travis Scott and Hvme - Goosebumps',
       'BLIND CHANNEL - Dark Side','onepunchman - Opening 1','Oxxxymiron - Хоп-механика','Oxxxymiron - Мы все умрем','Annodomini - Не надо слов','Fivefold - Fading Away',
       'Renegade Five - When Youre Gone','Alan Walker, Torine - Hello World','Don Omar, Lucenzo - Danza Kuduro','Linkin Park - Faint','Linkin Park - Numb','Linkin Park - From The Inside',
       'Three Days Grace - I Hate Everything About You',"The Offspring - You're Gonna Go Far, Kid",'Thousand Foot Krutch - War of Change',
       'Skillet - Hero','All Time Low, blackbear - Monsters','From Ashes to New - Blind','RADIO TAPOK - Feel Invincible - Skillet','RADIO TAPOK - The Offspring - The Kids Arent Alrigh',
       "Airbourne - Breakin' Outta Hell"
       
       ]


    
 

while True:
    a = 0
    print(Fore.GREEN+   ' ╔════════════════════════════════════════════════════════════════════════════════╗')
    for i in mus:
        a += 1
        col()
        print(Fore.GREEN,'║',Style.RESET_ALL,a,'Музыка:',Style.BRIGHT,w,i,Style.RESET_ALL)
        if a <101:
            print(Fore.GREEN+' ╠════════════════════════════════════════════════════════════════════════════════╣')
        if a == 101:
            print(Fore.GREEN+ ' ╚════════════════════════════════════════════════════════════════════════════════╝')


    try:
        col()
        res()
        ap = int(input('\n\n Что включить --> '))
    

    
        if ap == 0:
            как_пож()
            print(Fore.CYAN+'       Выхожу')
            time.sleep(2.5)
            os.system('cls')
            break
        
        
        if ap <= 101:
            nm = mus[ap-1]
            print(nm)
            rand()
            path = pathlib.Path('C:/Users/'+ user +'/01/'+nm+'.mp3')
            if path.exists() == True:
                os.startfile('C:/Users/'+ user +'/01/'+nm+'.mp3')
                os.system('cls')
                time.sleep(1)  
            else:
               print('Ошибка')
                            
    except ValueError:
        os.system('cls')
        pass
    
    except KeyboardInterrupt:
        pass