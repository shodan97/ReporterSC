import os,time,platform
try:from telethon.sync import TelegramClient
except:os.system("pip install telethon")
from telethon.tl import types
from telethon import functions
from prettytable import PrettyTable
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  
        
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
print (f"{lrd}")
t = PrettyTable([f'{cn}Число{lrd}',f'{cn}Метод{lrd}'])
t.add_row([f'{lgn}1{lrd}',f'{gn}Спам{lrd}'])
t.add_row([f'{lgn}2{lrd}',f'{gn}Другое{lrd}'])
t.add_row([f'{lgn}3{lrd}',f'{gn}Насилие{lrd}'])
t.add_row([f'{lgn}4{lrd}',f'{gn}Порно{lrd}'])
t.add_row([f'{lgn}5{lrd}',f'{gn}Авторские права{lrd}'])
t.add_row([f'{lgn}6{lrd}',f'{gn}Фейки{lrd}'])
t.add_row([f'{lgn}7{lrd}',f'{gn}Нерелевантное гео{lrd}'])
t.add_row([f'{lgn}8{lrd}',f'{gn}Драгсы (нарко){lrd}'])
t.add_row([f'{lgn}9{lrd}',f'{gn}Персональные данные{lrd}'])
def clear():
    if 'Windows' in platform.uname():
    	try:from colorama import init
    	except:os.system("pip install colorama")
    	init()
    	os.system("cls")
    elif 'Windows' not in platform.uname():
        os.system("clear")
clear()
re(f"""{g}
  _____      __      _   _________     ____    
 (_   _)    /  \    / ) (_   _____)   / __ \   
   | |     / /\ \  / /    ) (___     / /  \ \  
   | |     ) ) ) ) ) )   (   ___)   ( ()  () ) 
   | |    ( ( ( ( ( (     ) (       ( ()  () ) 
  _| |__  / /  \ \/ /    (   )       \ \__/ /  
 /_____( (_/    \__/      \_/         \____/
""")
account = f"""{k}
 ____                             _               
|  _ \   ___  _ __    ___   _ __ | |_   ___  _ __ 
| |_) | / _ \| '_ \  / _ \ | '__|| __| / _ \| '__|
|  _ < |  __/| |_) || (_) || |   | |_ |  __/| |    {cn}АВТОР{k}
|_| \_\ \___|| .__/  \___/ |_|    \__| \___||_|   
             |_|	

	{lrd}[{lgn}+{lrd}] {gn}АВТОРСТВО : {lgn}t.me/Skeleton_Realm
			"""	 
			
class TelegramReporter:
    def __init__(self):
        self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api id аккаунта: {g}")
        self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api hash аккаунтаt: {g}")
        self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите номер телефона аккаунта:{g} ")
        clear()
        re(account)
        print (f"{lrd}")
        print (t)
        self.method = input(f"{lrd}[{lgn}?{lrd}] {gn}Выберите метод: {k}")
        self.channel_username = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите юзернейм канала: {k}")
        self.number = input(f"{lrd}[{lgn}+{lrd}] {gn}Кол-во жалоб : {k}")
        self.client = TelegramClient('session', self.api_id, self.api_hash)
    def report_channel(self):
        with self.client as client:
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(self.phone_number)
                client.sign_in(self.phone_number, input('Введите код: '))
            try:channel_entity = client.get_entity(self.channel_username)
            except:print (f"{lrd}Юзер не доступен !")
            if self.method == "1":
                message = "This channel contains spam content."
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonSpam(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о спаме отправлена")
            elif self.method == "2":
                message = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите свое сообщение: {g}")
                for _ in range(0,int(self.number)): 
                     result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonOther(),
                    message=message
                ))
                     print (f"\{lrd}[{lgn}+{lrd}] {gn}Жалоба о Другом отправлена")
            elif self.method == "3":
                message = "Images of brutally murdered people, blood, and the generally unthinkable nature of this publication on the channel. Block it!"
                for _ in range(0,int(self.number)): 
                     result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonViolence(),
                    message=message
                ))
                     print (f"\{lrd}[{lgn}+{lrd}] {gn}Жалоба о насилии отправлена")
            elif self.method == "4":
                message = "This channel has pornographic content"
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonPornography(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о порнографии отправлена")
            elif self.method == "5":
                message = "Block this channel due to copyright"            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonCopyright(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о нарушении авторского права отправлена")
            elif self.method == "6":
                message = "This channel spreads fake news, misleading citizens, which leads to destabilization in the country"
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonFake(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о фейках отправлена ")
            elif self.method == "7":
                message = "Block this channel due to irrelevant geo "            
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonGeoIrrelevant(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о нерелевантном географическом положении отправлена ")
            elif self.method == "8":
                message = " "
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonIllegalDrugs(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о наркотиках отправлена")
            elif self.method == "9":
                message = "Dissemination of personal information, threats to people and calls for violence. Delete it! "
                for _ in range(0,int(self.number)): 
                    result = client(functions.messages.ReportRequest(
                    peer=channel_entity,
                    id=[42],
                    reason=types.InputReportReasonPersonalDetails(),
                    message=message
                ))
                    print (f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о персональных данных отправлена")
                print (f"\n\n{k}Жалобы отправлены успешно !")
reporter = TelegramReporter()
reporter.report_channel()
