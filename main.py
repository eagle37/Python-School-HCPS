import sys
import os
import time
import colorama
from colorama import Fore, Style

os.system("title Python Is Fun!")

sys.dont_write_bytecode = True

class Normal:
    

    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    def write(text):
        for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.01)
        
    def ask():
        Color = f'{Fore.CYAN}{Style.BRIGHT}'
        Normal.write(f"{Color}> Your Name?: {Fore.RESET}")
        Name = input()
        Normal.clear()
        Normal.write(f"{Color}> Your Age?: {Fore.RESET}")
        Age = input()
        Normal.clear()
        if not Age.isdigit():
            Normal.write(f'{Color}{Fore.RESET} Age must be a number.\n')
            os._exit[0]
        Normal.write(f"{Color}> Your Hobby?: {Fore.RESET}")
        Hobby = input()
        Normal.clear()
        Normal.write(f"{Color}> Your Weight [KG]?: {Fore.RESET}")
        Weight = input()
        Normal.clear()
        Normal.write(f"{Color}Getting Results! Wait For 3 Seconds Only!")
        time.sleep(3)
        if int(Weight) > 60 and int(Age) in (14, 15, 16):
        
            Normal.write(f"\n{Color}Here are the results!\nYour Name: {Name}\nYour Age: {Age}\nYour Hobby: {Hobby}\nYour Weight: {Weight} (You Are Over Weighted According To Your Age!:(){Fore.RESET}\n\n\n{Fore.GREEN}Made With HardWork By Prateek Aggarwal!\nHope You Liked It!{Fore.RESET}")

        elif int(Weight) in (55, 56, 57, 58, 59, 60) and int(Age) in (14, 15, 16):
            Normal.write(f"\n{Color}Here are the results!\nYour Name: {Name}\nYour Age: {Age}\nYour Hobby: {Hobby}\nYour Weight: {Weight} (You Are Fit According To Your Age! :)){Fore.RESET}\n\n\n{Fore.GREEN}Made With HardWork By Prateek Aggarwal!\nHope You Liked It!{Fore.RESET}")
        elif int(Weight) < 55 and int(Age) in (14, 15, 16):
            Normal.write(f"\n{Color}Here are the results!\nYour Name: {Name}\nYour Age: {Age}\nYour Hobby: {Hobby}\nYour Weight: {Weight} (You Are Low Weighted According To Your Age!:(){Fore.RESET}\n\n\n{Fore.GREEN}Made With HardWork By Prateek Aggarwal!\nHope You Liked It!{Fore.RESET}")
        else:
            Normal.write(f"\n{Color}Here are the results!\nYour Name: {Name}\nYour Age: {Age}\nYour Hobby: {Hobby}\nYour Weight: {Weight}{Fore.RESET}\n\n\n{Fore.GREEN}Made With HardWork By Prateek Aggarwal!:)\nHope You Liked It!:){Fore.RESET}")
        
        
if __name__ == "__main__":
        Normal.ask()
 
