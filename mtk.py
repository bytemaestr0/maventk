#!/usr/bin/env python3

from functions.mtk_functions import *

os.system('clear')

configuration = get_config()

first_time = configuration['firsttime']
nmap_timing = configuration['nmap_timing']
nmap_stealth = configuration['nmap_stealth']
default_interface = configuration['default_wireless']
proxychains_preference = configuration['proxychains_default']
web_wordlist = configuration['web_wordlist']
file_extensions = configuration['file_extensions']

options_general = r'''
{1}---Reconnaissance
{2}---Password Cracking
{3}---Wireless Hacking
{4}---Exploitation
{5}---Web Hacking
{6}---Reverse Shells
{7}---Settings
{99}---Exit
'''
menu_recon = r'''
{1}---Domain to IP
{2}---Scan open ports
{3}---Scan all devices on own network
{99}---Go Back
'''
menu_pass = r'''
{1}---Create a password dictionary(KWBDC)
{99}---Go Back
'''

menu_wireless = r'''
{1}---Find and crack nearby wifi networks
{99}---Go Back
'''

menu_exploit = r'''
{1}---Automatic Sql Injection Testing(SQLmap)
{2}---Scan open ports
{99}---Go Back
'''
menu_web = r'''
{1}---Find all directories for a website(dirb)
{2}---Find all open ports for a website(nmap)
{99}---Go Back
'''
menu_shells = r'''
{1}---Listen with ncat for an incoming reverse shell
{99}---Go Back
'''

mtk_logo = r'''
   _____                              ___________           .__   ____  __.__  __   
  /     \ _____ ___  __ ____   ____   \__    ___/___   ____ |  | |    |/ _|__|/  |_ 
 /  \ /  \\__  \\  \/ // __ \ /    \    |    | /  _ \ /  _ \|  | |      < |  \   __\
/    Y    \/ __ \\   /\  ___/|   |  \   |    |(  <_> |  <_> )  |_|    |  \|  ||  |  
\____|__  (____  /\_/  \___  >___|  /   |____| \____/ \____/|____/____|__ \__||__|  
        \/     \/          \/     \/                                     \/         

    '''
recon = r'''
__________                            
\______   \ ____   ____  ____   ____  
 |       _// __ \_/ ___\/  _ \ /    \ 
 |    |   \  ___/\  \__(  <_> )   |  \
 |____|_  /\___  >\___  >____/|___|  /
        \/     \/     \/           \/
'''

pass_crack = r'''
__________                                               .___ _________                       __   .__                
\______   \_____    ______ ________  _  _____________  __| _/ \_   ___ \____________    ____ |  | _|__| ____    ____  
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  /    \  \/\_  __ \__  \ _/ ___\|  |/ /  |/    \  / ___\ 
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  \     \____|  | \// __ \\  \___|    <|  |   |  \/ /_/  >
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   \______  /|__|  (____  /\___  >__|_ \__|___|  /\___  / 
                \/     \/     \/                          \/          \/            \/     \/     \/       \//_____/  
'''

wireless = r'''
 __      __.__               .__                            _____   __    __                 __            
/  \    /  \__|______   ____ |  |   ____   ______ ______   /  _  \_/  |__/  |______    ____ |  | __  ______
\   \/\/   /  \_  __ \_/ __ \|  | _/ __ \ /  ___//  ___/  /  /_\  \   __\   __\__  \ _/ ___\|  |/ / /  ___/
 \        /|  ||  | \/\  ___/|  |_\  ___/ \___ \ \___ \  /    |    \  |  |  |  / __ \\  \___|    <  \___ \ 
  \__/\  / |__||__|    \___  >____/\___  >____  >____  > \____|__  /__|  |__| (____  /\___  >__|_ \/____  >
       \/                  \/          \/     \/     \/          \/                \/     \/     \/     \/
'''

exploitation = r'''
___________              .__         .__  __          __  .__               
\_   _____/__  _________ |  |   ____ |__|/  |______ _/  |_|__| ____   ____  
 |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\__  \\   __\  |/  _ \ /    \ 
 |        \>    < |  |_> >  |_(  <_> )  ||  |  / __ \|  | |  (  <_> )   |  \
/_______  /__/\_ \|   __/|____/\____/|__||__| (____  /__| |__|\____/|___|  /
        \/      \/|__|                             \/                    \/
'''

web_hacking = r'''
 __      __      ___.       ___ ___                __   .__                
/  \    /  \ ____\_ |__    /   |   \_____    ____ |  | _|__| ____    ____  
\   \/\/   // __ \| __ \  /    ~    \__  \ _/ ___\|  |/ /  |/    \  / ___\ 
 \        /\  ___/| \_\ \ \    Y    // __ \\  \___|    <|  |   |  \/ /_/  >
  \__/\  /  \___  >___  /  \___|_  /(____  /\___  >__|_ \__|___|  /\___  / 
       \/       \/    \/         \/      \/     \/     \/       \//_____/  
'''
shells = r'''
__________                                           _________.__           .__  .__          
\______   \ _______  __ ___________  ______ ____    /   _____/|  |__   ____ |  | |  |   ______
 |       _// __ \  \/ // __ \_  __ \/  ___// __ \   \_____  \ |  |  \_/ __ \|  | |  |  /  ___/
 |    |   \  ___/\   /\  ___/|  | \/\___ \\  ___/   /        \|   Y  \  ___/|  |_|  |__\___ \ 
 |____|_  /\___  >\_/  \___  >__|  /____  >\___  > /_______  /|___|  /\___  >____/____/____  >
        \/     \/          \/           \/     \/          \/      \/     \/               \/ 
'''
settings = r'''
  _________          __     __   .__                          
 /   _____/  ____  _/  |_ _/  |_ |__|  ____     ____    ______
 \_____  \ _/ __ \ \   __\\   __\|  | /    \   / ___\  /  ___/
 /        \\  ___/  |  |   |  |  |  ||   |  \ / /_/  > \___ \ 
/_______  / \___  > |__|   |__|  |__||___|  / \___  / /____  >
        \/      \/                        \/ /_____/       \/
'''
exitting = r'''
___________        .__   __     __   .__                  
\_   _____/___  ___|__|_/  |_ _/  |_ |__|  ____     ____  
 |    __)_ \  \/  /|  |\   __\\   __\|  | /    \   / ___\ 
 |        \ >    < |  | |  |   |  |  |  ||   |  \ / /_/  >
/_______  //__/\_ \|__| |__|   |__|  |__||___|  / \___  / 
        \/       \/                           \/ /_____/  
'''
mtk_prompt = f'''
┌(maven@toolkit)--[{location}] 
└$ '''
if first_time == True:
    answer_prereq = input('''This seems to be your first time.
    To work, this toolkit needs some prerequisites.
    To continue, you have to install them.
    Continue?(Default = Yes)''')
    if answer_prereq in positive_answers or answer_prereq == '':
        if get_prerequisites() == True:
            replace_value('firsttime', False)
        else:
            pass
    elif answer_prereq == 'n' or answer_prereq == 'no':
        print("\nSee you.")
        os.system("clear")
        exit()
    else:
        get_prerequisites()
        replace_value('firsttime', False)
elif first_time != False: 
    repair_answer = input("Broken config file, replace it?")
    if repair_answer == '':
        exit() # TODO make it so that it grabs the default config file from github
    else:
        print("\nSee you")
        os.system("clear")
        exit()
else:
    pass
def main():
    while True:
        print(mtk_logo)
        answer_prompt = show_options(options_general)
        if answer_prompt == '1':
            while True:
                print(recon)
                answer_prompt = show_options(menu_recon)
                if answer_prompt == '1':
                    got_domain, got_ip = use_program('dig')
                    os.system("clear")
                    print(f"{got_domain} has an ip of {got_ip}")
                elif answer_prompt == '2':
                    use_program('nmap')
                elif answer_prompt == '3':
                    use_program('nmap_network')
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '2':
            while True:
                print(pass_crack)
                answer_prompt = show_options(menu_pass)
                if answer_prompt == '1':
                    os.system("python3 apps/kwbdc/main.py")
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '3':
            while True:
                print(wireless)
                answer_prompt = show_options(menu_wireless)
                if answer_prompt == '1':
                    os.system("sudo apps/airgeddon/airgeddon.sh")
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '4':
            while True:
                print(exploitation)
                answer_prompt = show_options(menu_exploit)
                if answer_prompt == '1':
                    use_program('asqlmap') 
                elif answer_prompt == '2':
                    use_program('nmap')
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '5':
            while True:
                print(web_hacking)
                answer_prompt = show_options(menu_web)
                if answer_prompt == '1':
                    use_program('dirb') 
                elif answer_prompt == '2':
                    use_program('nmap')
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '6':
            while True:
                print(shells)
                answer_prompt = show_options(menu_shells)
                if answer_prompt == '1':
                    use_program('ncat')
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '7':
            while True:
                configuration = get_config()
                first_time = configuration['firsttime']
                nmap_timing = configuration['nmap_timing']
                nmap_stealth = configuration['nmap_stealth']
                default_interface = configuration['default_wireless']
                proxychains_preference = configuration['proxychains_default']
                web_wordlist = configuration['web_wordlist']
                file_extensions = configuration['file_extensions']
                menu_setting = f'''
{{1}}---Change nmap timing - higher = faster, but riskier (Now = {nmap_timing})
{{2}}---Activate nmap stealth(requires sudo permissions) (Now = {nmap_stealth})
{{3}}---Change default wireless interface (Now = {default_interface})
{{4}}---Enable/Disable proxychains by default for tools like nmap/dirb, etc. (Now = {proxychains_preference})
{{5}}---Change the default dirb wordlist (Now = {web_wordlist})
{{6}}---Set the default file extension for dirb (Now = {file_extensions})
{{99}}---Go Back
                '''
                print(settings)
                answer_prompt = show_options(menu_setting)
                if answer_prompt == '1':
                    os.system("clear")
                    print(settings)
                    print('')
                    print("Set timing(1-5): ")
                    print('')
                    timing_new = ''
                    while timing_new == '':
                        timing_new = input(mtk_prompt)
                        replace_value("nmap_timing", timing_new)
                        os.system("clear")
                elif answer_prompt == '2':
                    os.system("clear")
                    print(settings)
                    print('')
                    print("Set stealth(True/False): ")
                    print('')
                    stealth_new = ''
                    while stealth_new == '':
                        temp_stealth = input(mtk_prompt)
                        if temp_stealth == "true" or temp_stealth == "True":
                            stealth_new = True
                        elif temp_stealth == "false" or temp_stealth == "False":
                            stealth_new = False
                        else:
                            continue
                    replace_value("nmap_stealth", stealth_new)
                    os.system("clear")
                elif answer_prompt == '3':
                    os.system("clear")               
                    print(settings)
                    print('')
                    print("Set wireless interface(example: wlan0/wlan3): ")
                    print('')
                    interface_new = ''
                    while interface_new == '':
                        interface_new = input(mtk_prompt)
                        replace_value("default_wireless", interface_new)
                        os.system("clear")
                elif answer_prompt == '4':
                    os.system("clear")
                    print(settings)
                    print('')
                    print('Enable proxychains(True/False): ')  
                    proxychains_new = ''
                    while proxychains_new == '':
                        temp_prox = input(mtk_prompt)
                        if temp_prox == "true" or temp_prox == "True":
                            proxychains_new = True
                        elif temp_prox == "false" or temp_prox == "False":
                            proxychains_new = False
                        else:
                            continue
                    replace_value("proxychains_default", proxychains_new)
                    os.system("clear")
                elif answer_prompt == '5':
                    os.system("clear")
                    print('')
                    print('New wordlist location for dirb?: ')  
                    web_word_new = ''
                    while web_word_new == '':
                        web_word_new = input(mtk_prompt)
                    replace_value("web_wordlist", web_word_new)
                elif answer_prompt == '6':
                    os.system("clear")
                    print('')
                    print('New file extensions for dirb?: ')  
                    file_extension_new = ''
                    while file_extension_new == '':
                        file_extension_new = input(mtk_prompt)
                    replace_value("file_extensions", file_extension_new)
                elif answer_prompt == '99':
                    break
        elif answer_prompt == '99':
            print(exitting)
            print("\nSee you")
            sleep(1)
            os.system("clear")
            exit()
if __name__ == "__main__":
    main()
