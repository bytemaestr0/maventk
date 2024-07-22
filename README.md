Maven Toolkit
Description

Maven Toolkit is a command-line tool designed for various penetration testing and security assessment tasks. It provides a menu-driven interface to easily navigate through different functionalities ranging from reconnaissance to exploitation.

Usage:

    python3 mtk.py

Installation:
  Manual:
    Install python using your python manager, then:
    
    pip install -r requirements.txt
    python3 mtk.py
  
  Automatic(might not work on some distros):
  
    ./install.sh
  

Features:

    Reconnaissance
        Domain to IP conversion
        Scan open port
        Scan all devices on own network

    Password Cracking
        Create a password dictionary (KWBDC)

    Wireless Hacking
        Find and crack nearby WiFi networks

    Exploitation
        Automatic SQL Injection Testing (ASQLmap)
        Scan open ports

    Web Hacking
        Find all directories for a website (dirb)
        Find all open ports for a website (nmap)

    Reverse Shells
        Listen with ncat for an incoming reverse shell

    Settings
        Configuration options for Maven Toolkit
