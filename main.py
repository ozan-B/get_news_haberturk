import os
from colorama import Fore
import time
import sys

def Banner():
    print("""\033[96m
      ooooooo                oooooooo                        oooooooooo  
    o888   888o ooooooooooo         o   oo oooooo            888    888 
    888     888      8888    ooooo888   888   888 ooooooooo 888oooo88  
    888o   o888   8888     888    888   888   888           888    888 
      88ooo88   o888ooooooo 88ooo88 8o o888o o888o         o888ooo888  
\033[0m""")
    

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

def menu():
    slowprint(f'''
                            {Fore.LIGHTRED_EX} [1] Ana sayfadaki tüm haberleri getir . 
                            {Fore.LIGHTGREEN_EX} [2] son 24 saatte yayınlanan haberleri getir .


                            {Fore.RED} [{Fore.BLUE}${Fore.RED}]{Fore.CYAN} Choose one of the options above)

        ''')
    time.sleep(0.2)
    option = input("\n\n \033[93m           Let's Start \033[96m --> --> --> \033[91m ")
    
    return option

def back():
    job = input(f"\n{Fore.BLUE}Press 'b' to go menu  or Press 'a' use to again tool:    ") 
    return job


def infolist2():

    Banner()
    
    


    while True:

        op=menu()
        if op == "1":

            while True:     
                os.system('clear')
                os.system("./project/option1.py") # Error
                
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()


        elif op == "2":

            while True:
                os.system('clear')
                os.system("./mergen/project.py") # Error
                
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()
        elif op == "E" or op== "e":
            print("[INFO] Exitting...")
            break

        else:
            print(f"{Fore.RED}[FAIL] Invalid Command Dedected. Please Input Valid Commands.") # Error
            break




     

        


infolist2()