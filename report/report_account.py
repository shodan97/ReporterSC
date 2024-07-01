import os
import time
import platform
import pickle

try:
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")

from telethon.tl import types
from telethon import functions
from prettytable import PrettyTable

def save_login_data(data, filename='login_data.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_login_data(filename='login_data.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'
print(f"{lrd}")
t = PrettyTable([f'{cn}Число{lrd}', f'{cn}Метод{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Спам{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Порно{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Насилие{lrd}'])
t.add_row([f'{lgn}4{lrd}', f'{gn}ЦП{lrd}'])
t.add_row([f'{lgn}5{lrd}', f'{gn}Другое{lrd}'])
t.add_row([f'{lgn}6{lrd}', f'{gn}Авторские права{lrd}'])
t.add_row([f'{lgn}7{lrd}', f'{gn}Фейки{lrd}'])
t.add_row([f'{lgn}8{lrd}', f'{gn}Нерелевантное гео{lrd}'])
t.add_row([f'{lgn}9{lrd}', f'{gn}Драгсы (нарко){lrd}'])
t.add_row([f'{lgn}10{lrd}', f'{gn}Персональные данные{lrd}'])

def clear():
    if 'Windows' in platform.uname():
        try:
            from colorama import init
        except:
            os.system("pip install colorama")
        init()
        os.system("cls")
    else:
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
                                                                 
                    .---:                :---.                   
               .=++*+=+#+                +#*=+*++=.              
             =#*+++=++-=#                #==++=+++*#=            
           =%++**==**-*+#=   {rd}РЕПОРТЕР{k}   =#+*-**==**++%=
         .#*+***=+**-*+##+.   {gn}УЧЁТКИ{k}   .+*%+*-**+=***+*%:
        -%=****-***=+*=%@+=            =+@%=*+=***-****=%-       
       -%=****-****-***++@#.          .#@++***-****-****=%-      
      .%=****=+***+=****-=%@=*:=#%=.*=@%=-****=+***+=****=%.     
      *+*****-****=*****-+=#%*%#@@#%*%#=+-*****=****-*****=#     
     .%=****=+****-*-..::%@@@+@@@@@@*@@@%-:..-*-****+=****=#.    
     ++*****-*+-:::.    @@@@@*%@@@@%*@@@@@    .:::-+*-*****++    
     *=***++-=         :@@@@@@##@@##@@@@@@:         =-++***=#    
     *=+:               %@@%#@@@##@@@##@@%               :+=#    
     +-            .... =@@@+@@@@@@@@+@@@= ....            -*    
     =          *@@@@@@@+@@@=@@@@@@@@=@@@+@@@@@@@*          =    
               :@@@@@@@@+@@%##%@@@@@###@@+@@@@@@@@:              
               .@@@@##%@+@@%*@@@@@@@@*%@@+@%##@@@@.              
                .*@@@@%#*+@@#%@@@@@@%#@@+*#%@@@@#:               
                  .=#@@@@*%@@-*+--+*-@@%*@@@@#=.                 
                      :=*@+@@:.    .-@@+@#=:                     
                          #*@=      =@*#                         
                         :%=@+      +@=%:                        
                       +****%*+=  =+*%****+                      
                        .-.=-        -=.-.                       


	{lrd}[{lgn}+{lrd}] {gn}АВТОР : {lgn} t.me/Skeleton_Realm
			"""	 
class TelegramReporter:
    def __init__(self):
        login_data = load_login_data()
        if login_data:
            use_saved = input(f"{lrd}[{lgn}?{lrd}] {gn}Использовать сохраненные данные для входа? (y/n): {g}").strip().lower()
            if use_saved == 'y':
                self.api_id = login_data['api_id']
                self.api_hash = login_data['api_hash']
                self.phone_number = login_data['phone_number']
                self.password = login_data.get('password', '')
            else:
                self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api id аккаунта: {g}")
                self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api hash аккаунта: {g}")
                self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите номер телефона аккаунта: {g}")
                self.password = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите пароль 2фа: (если нету, нажми Enter) {g}")
                save_login_data({
                    'api_id': self.api_id,
                    'api_hash': self.api_hash,
                    'phone_number': self.phone_number,
                    'password': self.password
                })
        else:
            self.api_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api id аккаунта: {g}")
            self.api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите Api hash аккаунта: {g}")
            self.phone_number = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите номер телефона аккаунта: {g}")
            self.password = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите пароль 2фа: (если нету, нажми Enter) {g}")
            save_login_data({
                'api_id': self.api_id,
                'api_hash': self.api_hash,
                'phone_number': self.phone_number,
                'password': self.password
            })

        clear()
        re(account)
        print(f"{lrd}")
        print(t)
        self.method = input(f"{lrd}[{lgn}?{lrd}] {gn}Выберите метод : {k}")
        self.scammer_id = input(f"{lrd}[{lgn}+{lrd}] {gn}Введите юзер цели : {k}")
        self.number = input(f"{lrd}[{lgn}+{lrd}] {gn}Кол-во жалоб: {k}")

    def report_spam(self):
        with TelegramClient('reporter', self.api_id, self.api_hash) as client:
            client.start(self.phone_number, self.password)

            try:
                user = client.get_entity(self.scammer_id)
                scammer_input_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)
            except ValueError:
                print(f'{lrd}[{rd}!{lrd}] {k}Пользователь не найден')
                client.disconnect()
                return

            if self.method == "1":
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonSpam(),
                        message=''
                    ))
                    print(f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о спаме отправлена: {i}")

            elif self.method == "2":
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonPornography(),
                        message=''
                    ))
                    print(f"{lrd}[{lgn}+{lrd}] {gn}Жалоба о порнографии отправлена: {i}")

            elif self.method == "3":
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonViolence(),
                        message=''
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о насилии отправлена: {i}")

            elif self.method == "4":
                report_message = 'Этот пользователь распространяет материалы, связанные с детским порно, если вы не заблокируете его, я обращусь к Международной конвенции о правах ребенка'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonChildAbuse(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о детской порнографии отправлена: {i}")

            elif self.method == "5":
                message = input(f"{lrd}[{lgn}?{lrd}] {gn}Введите текст жалобы: {k}")
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonOther(),
                        message=message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о другом отправлена: {i}")

            elif self.method == "6":
                report_message = 'Этот пользователь подозревается в нарушении авторских прав'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonCopyright(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба на нарушение авторских прав отправлена: {i}")

            elif self.method == "7":
                report_message = 'Этот пользователь подозревается в распространении фейковой информации'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonFake(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о фейках отправлена: {i}")

            elif self.method == "8":
                report_message = 'Этот пользователь подозревается в нерелевантной географической информации'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonGeoIrrelevant(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о нерелевантной географической информации отправлена: {i}")

            elif self.method == "9":
                report_message = 'Этот пользователь подозревается в распространении наркотиков'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonIllegalDrugs(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о наркотиках отправлена: {i}")

            elif self.method == "10":
                report_message = 'Этот пользователь подозревается в распространении персональных данных'
                for i in range(0, int(self.number)):
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=types.InputReportReasonPersonalDetails(),
                        message=report_message
                    ))
                    print(f"\n{lrd}[{lgn}+{lrd}] {gn}Жалоба о распространении персональных данных отправлена: {i}")

            client.disconnect()

        print(f'\n\n{lrd}[{rd}-{lrd}] {k}Жалобы успешно отправлены!')

reporter = TelegramReporter()
reporter.report_spam()