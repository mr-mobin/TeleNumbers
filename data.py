import requests as req
from colorama import Fore
from time import sleep
print(Fore.CYAN+"""
  _______ ______ _      ______                       _               
 |__   __|  ____| |    |  ____|                     | |              
    | |  | |__  | |    | |__   _ __  _   _ _ __ ___ | |__   ___ _ __ 
    | |  |  __| | |    |  __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
    | |  | |____| |____| |____| | | | |_| | | | | | | |_) |  __/ |   
    |_|  |______|______|______|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
____________________________
+Join=@Termux_learning
+We Love You ;)
""")
Mr_ngrok=input(Fore.GREEN+"Enter"+Fore.RED+"USERid"+Fore.GREEN+"=>")
print(Fore.GREEN+"start.")
sleep(0.4)
print(Fore.CYAN+"start..")
sleep(0.4)
print(Fore.RED+"start....")
url=str("http://turk-hack1.tk/shkar/?UseriD="+Mr_ngrok)
r=req.get(url).text
r3=r.replace("@TurkHack1","@termux_learning").replace("Nima Dark or Mehrdad Ziro","Mobin-Dan")
r4=r3.replace('"username": "@0"',"")
print(Fore.CYAN+r4)
