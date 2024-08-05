import os, platform, json, time, re, subprocess, psutil, ipaddress, itertools

location = "~"
mtk_prompt = f'''
┌(maven@toolkit)--[{location}] 
└$ '''
positive_answers = ['Yes', 'yes', 'ye', 'y', 'yea', 'Y', 'yeah', 'yah'] 
answer_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '99']
apps = ['dig', 'nmap', 'nmap_network', 'asqlmap', 'dirb', 'ncat', 'setookit']
top_level_domains = ['.com', '.net', '.org', '.gov', '.edu', '.co', '.io', '.biz', '.ro', '.md', '.uk', '.shop']

def get_config():
    config = open('config/mtk_config.json', 'r')
    return json.load(config)
configuration = get_config()
first_time = configuration['firsttime']
nmap_timing = configuration['nmap_timing']
nmap_stealth = configuration['nmap_stealth']
default_interface = configuration['default_wireless']
proxychains_preference = configuration['proxychains_default']
default_listening_port = configuration['listen_port']
if proxychains_preference == True:
    proxychains = "proxychains "
else:
    proxychains = ""
# Get The Distro (To Know The Package Manager)
def get_distro():
    distro = platform.freedesktop_os_release()['ID_LIKE']
    return distro

def get_subnets():
    subnets = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == 2:  # AF_INET (IPv4)
                ip = ipaddress.IPv4Address(addr.address)
                netmask = ipaddress.IPv4Address(addr.netmask)
                network = ipaddress.IPv4Network(f'{ip}/{netmask}', strict=False)
                subnets.append(str(network))
    return subnets

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip()

def get_package_manager(distro):
    if distro == "arch":
        return "pacman -S --noconfirm"
    elif distro == "debian" or distro == "ubuntu" or distro == "debian ubuntu" or distro == "ubuntu debian":
        return "apt install -y"
    else:
        return "unknown"

# Check If The Selected Program Is Installed
def check_install(program):
    # Checks If The Program Is Installed 
    if os.path.isfile(f"/usr/bin/{program}"):
        return True
    else:
        # Prompts The User If They Want To Install The Program Or Not
        return prompt_install(program)

def sleep(ammount):
    time.sleep(ammount)

def prompt_install(program):
    install = get_package_manager(get_distro())
    answer_install = None
    answer_install = input(f"{program} not found. Would you like to install it?(Default = Yes)")
    if answer_install in positive_answers or answer_install == "" :
        os.system(f"sudo {install} {program}")
        return True
    elif answer_install == "n" or answer_install == "no": 
        print("Not Installing")
        return False

def get_interface():
    # Get the list of interfaces from ifconfig
    try:
        result = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Extract interface names
        interfaces = re.findall(r'^(\S+):', output, re.MULTILINE)
        
        # Exclude 'lo' interface and return the first available one
        for iface in interfaces:
            if iface != 'lo':
                return iface
    except subprocess.CalledProcessError:
        pass

    # If no suitable interface is found with ifconfig, use iwconfig
    try:
        result = subprocess.run(['iwconfig'], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Extract interface names
        interfaces = re.findall(r'^(\S+)\s+IEEE', output, re.MULTILINE)
        
        if interfaces:
            return interfaces[0]
    except subprocess.CalledProcessError:
        pass

    return None

def get_main_subnet(interface):
    try:
        result = subprocess.run(['ip', 'addr', 'show', interface], capture_output=True, text=True, check=True)
        output = result.stdout
        
        match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)/(\d+)', output)
        
        if match:
            ip_address = match.group(1)
            subnet_mask = int(match.group(2))
            
            ip_bin = ''.join(format(int(octet), '08b') for octet in ip_address.split('.'))

            network_bin = ip_bin[:subnet_mask] + '0' * (32 - subnet_mask)
            network_address = '.'.join(str(int(network_bin[i:i+8], 2)) for i in range(0, 32, 8))
            
            return f"{network_address}/{subnet_mask}"
        
        else:
            return None
    except subprocess.CalledProcessError:
        return None

print()

def use_program(app):
    if app == apps[0]:
        if check_install("dig") != True:
            pass
        else:
            domain = ''
            while domain == '':
                domain = input("Enter the domain to find the ip of: ")
            dig_output = run_command(f"dig {domain}")
            ip = re.search(r"ANSWER SECTION:\n(?:.*\n)*?.*?\s+IN\s+A\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", dig_output)
            return domain, ip.group(1)
    elif app == apps[1]:
        if check_install("nmap") != True:
            pass
        else:
            ip = ''
            while ip == '':
                ip = input("Enter the ip of the device to scan: ")
            if nmap_stealth == False:
                stealth = ""
            else:
                stealth = "sudo "
            os.system(f"{stealth}{proxychains}nmap -T{nmap_timing} {ip}")
    elif app == apps[2]:
        if check_install("nmap") != True:
            pass
        else:
            subnet = get_main_subnet(get_interface())
            os.system(f"nmap -T{nmap_timing} {subnet}")
    elif app == apps[3]:
        if os.path.exists("apps/asqlmap") != True:
            print("The app asqlmap isn't installed. Want to install it?(Default = Yes)")
            ans_inst = input(mtk_prompt)
            if ans_inst in positive_answers or ans_inst == '':
                os.system("git clone https://github.com/Gualty/asqlmap > apps/asqlmap")
                os.system('clear')
                pass
            else:
                pass
        else:
            asqlmap_url = input("Which url to scan? ")
            os.system(f"./apps/asqlmap/asqlmap.sh {asqlmal_url}")
    elif app == apps[4]:
        if check_install("dirb") != True:
            print("The app dirb isn't installed. Quitting")
        else:
            os.system('clear')
            print("Which url to scan? ")
            base_url = ''
            while base_url == '':
                base_url = input(mtk_prompt)
            tld_in_url = False
            for tld in top_level_domains:
                if tld in base_url:
                    tld_in_url = True
                else:
                    pass 
            if tld_in_url == False:
                base_url += ".com"
            if 'http://' not in base_url or 'https://' not in base_url:
                dirb_url = f"https://{base_url}"
                os.system('clear')
            print("Use default file extensions and wordlist?(Default = Yes)")
            answer_default = input(mtk_prompt)
            if answer_default in positive_answers or answer_default == '':
                file_extension = configuration['file_extensions']
                extension_final = f"-X {file_extension}"
                web_wordlist = configuration['web_wordlist']
            else:
                print("Which file extension to use? ")
                while file_extension == '':
                    file_extension = input(mtk_prompt)
                extension_final = f"-X {file_extension}"
                print("Which wordlist to use?(Enter the file location) ")
                while web_wordlist == '':
                    web_wordlist = input(mtk_prompt)
            os.system('clear')
            os.system(f"{proxychains} dirb {dirb_url} {web_wordlist} {extension_final}")
            print("")
            print("")
            temp_var = input(mtk_prompt)
            os.system("clear")
    elif app == apps[5]:
        if check_install('netcat') != True:
            print("The app netcat isn't installed. Quitting")
        else:
            os.system('clear')
            print(f"Listen on default port set in configuration?(Default = {default_listening_port})")
            answer_port = input(mtk_prompt)
            if answer_port in positive_answers or answer_port == '':
                listen_port = configuration['listen_port']
            else:
                os.system('clear')
                print("Which port to listen on?")
                final_answer_port = ''
                while final_answer_port == '':
                    final_answer_port = input(mtk_prompt)
                listen_port = final_answer_port
            os.system("clear")
            replace_value('listen_port', listen_port)
            os.system(f"netcat -lnvp {listen_port}")
    elif app == apps[6]:
        if check_install('setoolkit') != True:
            pass
def replace_value(key, value):
    full_config = get_config()
    full_config[key] = value
    with open("config/mtk_config.json", "w") as config_file:
        json.dump(full_config, config_file, indent=4)

def get_prerequisites():
    install = get_package_manager(get_distro())
    os.system(f"sudo {install} proxychains")
    os.system(f"sudo {install} nmap sqlmap")
    # for airgeddon:
    os.system(f"sudo {install} iw awk airmon-ng xterm ip lspci ps")

def show_options(menu_name):
    print(menu_name)
    answer = ''
    while answer not in answer_choices:
        answer = input(mtk_prompt)
    os.system('clear')
    return answer
