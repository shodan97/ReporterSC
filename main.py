import time,os,platform
try:from prettytable import PrettyTable
except:os.system("pip install prettytable")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'

def clear_console():
    
    os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    clear_console()
    
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
           {lrd}REPORTER 1.0{k}     -*%.   {g}PulseScope{k}   .%+    {be}TELEGRAM      {k}       
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
                      %@.    {cn}@Skeleton_Realm{k}    .@%                    
                      :+@:               =@+:                    
                        =@:             :@-                      
                         -%.           .%:                       
                          .#           #.                        
                            +         +                          
                             -       -                     
"""

re(banner)
re("Внимание! Это тестовая версия репортера PulseScope 1.0, ответственность за любые нарушения лежит на пользователе!")
print (f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}',f'{cn}info{lrd}'])
t.add_row([f'{lgn}1{lrd}',f'{gn}Reporter Account{lrd}'])
t.add_row([f'{lgn}2{lrd}',f'{gn}Reporter Channel{lrd}'])
t.add_row([f'{lgn}3{lrd}',f'{gn}Reporter Group [Updating]{lrd}'])
print (t)

number = input(f"{gn}Enter Number : {cn}")
if number == "1":
    os.system("python report/report_account.py")
if number == "2":
	os.system("python report/report_channel.py")
elif number == "3":
    print ("Раздел обновляется и скоро будет добавлен \n\nКанал : @Skeleton_Realm")
