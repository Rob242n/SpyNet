from colorama import Fore, Back, Style
import os
import nmap
import socket

#loading screen












import time
import sys
print("Loading:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
def Loading():

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(1.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")











#This function to clear the screen
def Clear_Screen():
    os.system("clear")

nocolor = "\033[0;37;10m"
azul = "\033[0;34;10m"
amarillo = "\033[1;33;10m"

#Main Menu class with the Banar and the choice of the first begin
class MainMenu:
    def Baner(self):
        baner = (azul + r"""   _____             _   __     __ 
  / ___/____  __  __/ | / /__  / /_
  \__ \/ __ \/ / / /  |/ / _ \/ __/
 ___/ / /_/ / /_/ / /|  /  __/ /_  
/____/ .___/\__, /_/ |_/\___/\__/  
    /_/    /____/                  """)
        print(baner)
        
        print( "****************************************")

    def Explain(self):
        print(amarillo + r"""THIS PROJECT UNDER  *GNU LICENSE*
IF THERE IS ANY ISSUE PLEASE CONTENT WITH US ON:
spynet4sc@gmail.com
READ MORE ON https://github.com/hotdeth/SpyNet 
****************************************      
""")
     
#Ask the user to Run or exit or show the requirements
    def choice(self):
        UserChoice = input(nocolor + """1-Run program
2-Show the requirement 
3-Exit
Input:""")
        return UserChoice
    def choice2(self):
        choice2 = input(nocolor + """1-Port checkout
2-Network Discover
Input:""")
        return choice2










class Discover:
   
    def __init__(self):
        self.ip = ''

    
    

    def NetworkScan(self):
        ip = input("Your ip address(press enter to detect automaticlly):")
        self.ip = ip
        if len(self.ip) == 0:
            network = socket.gethostbyname(socket.gethostname())
            network = network + '/24'
        else:
            network = self.ip + '/24'

        print("Scanning Please Wait!")
        nm = nmap.PortScanner()
        Loading()
        nm.scan(hosts=network,arguments='-sn')
        host_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
        for host,status in host_list:
    
            print(f"Host\t{host}\tMAC:")
         


class Port:
    pass



class Run:
    def __init__(self):
        self.menu = MainMenu()
        self.port = Port()
        self.Discover = Discover()




    def Start(self):
        self.menu.Baner()
        self.menu.Explain()
        
        choice = self.menu.choice()


        if choice == '1':
            Clear_Screen()
            self.menu.Baner()
            choice2 = self.menu.choice2()
            if choice2 == '1':
                #port checkout 
                pass
            elif choice2 == '2':
               self.Discover.NetworkScan()
              
            


        elif choice == '2':
            Clear_Screen()
            self.menu.Baner()
            self.Show_file_content()
    
        elif choice == '3':
            self.exit()
        else:
            self.exit()




    def Show_file_content(self):
        pass




    def exit(self):
        print(azul + "-----------------------------")
        print(azul + "Thank you for use SpyNet")
        print(azul + "See you late")
       
User = Run()
User.Start()