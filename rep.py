import hashlib
import subprocess
import os

hashed_password = '0bdb052c7849d33bf29db0a647606fbb8f517f7ce613e079a6756c9b5a767ee6'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def clear_console():
    
    os.system('clear' if os.name == 'posix' else 'cls')


def ask_password():
    entered_password = input("Пожалуйста, введите пароль: ")
    return entered_password


if __name__ == "__main__":
    clear_console()
    entered_password = ask_password()
    if hash_password(entered_password) == hashed_password:
        print("Пароль верный, запуск скрипта...")
        
        import time,os,platform
try:from prettytable import PrettyTable
except:os.system("pip install prettytable")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  
if 'Windows' in platform.uname():
    from colorama import init
    init()
else:
    pass
banner = f"""
                                                                 
{k}                                                                
                              -     -                            
                            .+       +.                          
                           :#         #:                         
                          =%           %-                        
           {lrd}РЕПОРТЁР{k}     -*%.   {g}SKELETON_REALM{k}   .%+    {be}ТЕЛЕГРАМ      {k}
                        #@:             -@#                      
                     :  #@:             :@*  :                   
                    -=  *@:             -@*  =-                  
                   -%   *@-             =@+   %-                 
                  -@=  .*@+             +@+.  =@-                
                 =@%   .+@%-    :.:    -@@+.   #@:               
                =@@#:     =%%-+@@@@@+-%%=     .#@@=              
                 .+%@%+:.   -#@@@@@@@#-   .:=#@%=                
                    -##%%%%%#*@@@@@@@*#%%%%%##-                  
                  .*#######%@@@@@@@@@@@%#######*.                
               .=#@%*+=--#@@@@@@@@@@@@@@@#--=+*%@#=.             
            .=#@%+:     *@@@@@+.   .+@@@@@*     :+%@#=.          
          :*@@=.    .=#@@@@@@@       @@@@@@@#=.    .=@@*.        
            =@+    .%@@*%@@@@@*     *@@@@@%*@@%.    +@=          
             :@=    +@# :@@@@@#     #@@@@%. #@+    =@:           
              .#-   :@@  .%@@#       #@@#.  @@:   -#.            
                +:   %@:   =%         %=   :@%   -+              
                 -.  +@+                   +@+  .-               
                  .  :@#                   #@:  .                
                      %@.    {cn}t.me/Skeleton_Realm{k}    .@%
                      :+@:               =@+:                    
                        =@:             :@-                      
                         -%.           .%:                       
                          .#           #.                        
                            +         +                          
                             -       -                     
"""

re(banner)
re("ЭТО БЕТА-ВЕРСИЯ РЕПОРТЁРА, @SKELETON_REALM НЕ ОБЛАДАЕТ ОТВЕТСТВЕННОСТЬЮ ЗА ДЕЙСТВИЯ ПОЛЬЗОВАТЕЛЕЙ !")
print (f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}',f'{cn}info{lrd}'])
t.add_row([f'{lgn}1{lrd}',f'{gn}Разъебать канал{lrd}'])
t.add_row([f'{lgn}2{lrd}',f'{gn}Разъебать аккаунт{lrd}'])
# t.add_row([f'{lgn}3{lrd}',f'{gn}Разъебать чат{lrd}'])
print (t)

number = input(f"{gn}Выберите что хотите разъебать : {cn}")
if number == "1":
    os.system("python report/reporter.py")
if number == "2":
	os.system("python report/report.py")
else:
    print("ОПЦИЯ НЕ ИДЕНТИФИЦИРОВАНА !")