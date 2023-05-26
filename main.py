from colorama import Fore, init
import ctypes
from datetime import datetime
import requests
import aiohttp
import asyncio
import json
from time import sleep
import os
import subprocess, sys
import os#!/bin/python
import optparse
import getpass
import urllib


class colour:
    blue = Fore.BLUE
    green = Fore.GREEN
    red = Fore.RED
    magenta = Fore.MAGENTA
    reset = Fore.RESET

init()

ctypes.windll.kernel32.SetConsoleTitleW(f'[TikTok Username Checker]')
os.system("notification.vbs")

usernames1 = ["admin"]
passwords = ["admin"]

def count():
    namecount = 0
    with open("usernames.txt") as f:
            for namecount, l in enumerate(f):
                pass
            namecount = namecount + 1


    return namecount

def county():
    namecounty = 0
    with open("authhere.txt") as f:
            for namecounty, l in enumerate(f):
                pass
            namecounty = namecounty + 1


    return namecounty


pasteLink = 'https://pastebin.com/raw/ZcpvecyB'

Users = []

with open('authhere.txt', 'r') as f:
    for line in f:
        for user in line.split():
            Users.append(user)    

print(f"[{colour.blue}+{colour.reset}] TikTok Username Checker - ash")

def Auth():
    r = requests.get(pasteLink)
    for i in r.content.decode('utf-8').split():
        if i in Users:
          print(f'[{colour.blue}?{colour.reset}] Auth Status: {colour.blue}Authed{colour.reset}')
          print(f"[{colour.blue}?{colour.reset}] Users Online: [\x1b[32m{county()}\x1b[39m]")
          print("")
          print(f"[{colour.blue}✓{colour.reset}] {count()} Usernames Found In Username Text File")
          print(f"[{colour.blue}-{colour.reset}] Press {colour.blue}Enter{colour.reset} To Login")
          input("")
          username = input (f"[{colour.blue}?{colour.reset}] Please Enter Your {colour.blue}Username{colour.reset}: {colour.blue}")
          print(f'{colour.reset}')
          print(f"[{colour.blue}+{colour.reset}] Login Status: {colour.blue}Successfully logged in...{colour.reset}")
          print (f'[{colour.blue}+{colour.reset}] Welcome User: {colour.blue}{username}{colour.reset}\n')
          sleep(1.5)

if __name__ == '__main__':
    Auth()

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'{colour.red} [!] No usernames found!\n Make sure to paste them into usernames.txt and save.{colour.reset}')
        quit()

async def check():
    session = requests.Session()
    for username in usernames:
        r = session.get(f'https://www.tiktok.com/@{username}/', headers={'Connection': 'keep-alive', 'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 13.6.1; sv_SE) Cronet'}, timeout=60)
        check = r.status_code
        if check == 404:
            print(f"[{colour.green}+{colour.reset}] {username}")
            with open('available.txt', "a") as x:
                x.write(f"{username}\n")
        elif check == 200 or 204:
            print(f"[{colour.red}x{colour.reset}] {username}")
        elif check == 429:
            print(f"\n[{colour.gredreen}x{colour.reset}] Response: Status code: HTTP 429: You are being rate limited by the Instagram API\n")
            sleep(30)
            check()
            return
        else:
            print(f"{colour.red} [?]{colour.reset} Unknown Error . . . - {check}")
    
    print(f"\n[{colour.green}+{colour.reset}] Checked all usernames. Press Enter to exit.\n")
    os.system("finished.vbs")
    input()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check())