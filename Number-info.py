from rich.console import Console;from rich.table import Table
from requests import get,post
from collections import Counter
from time import sleep
import os,re


console=Console()
NAME=list()


def header():
    os.system('cls' if os.name == 'nt' else 'clear');console.print("""
███╗   ██╗██╗   ██╗███╗   ███╗      ██╗███╗   ██╗███████╗ ██████╗ 
████╗  ██║██║   ██║████╗ ████║      ██║████╗  ██║██╔════╝██╔═══██╗
██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║██║ ╚████║██║     ╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝  
                                                                                                                  
                   By @TweakPY - @vv1ck
""",style='bold dark_red',justify='left')


def Main():
    header()
    num=input("[+] Enter a Phone Number : ")#966 505555555
    if '+' in num:num=num.replace("+","")
    try:
        code=num.split(' ')[0]
        number=num.split(' ')[1]
    except:
        console.print('[!] Error Invalid Number, Example : [ 966 505555555 ]');exit()
    header()
    Search_1(number,code)


def Search_1(number,code):
    try:
        if code=='20':country="EG"
        elif code=='98':country="IR"
        elif code=='212':country="MA"
        elif code=='213':country="DZ"
        elif code=='216':country="TN"
        elif code=='249':country="SD"
        elif code=='252':country="SO"
        elif code=='961':country="LB"
        elif code=='962':country="JO"
        elif code=='963':country="SY"
        elif code=='964':country="IQ"
        elif code=="965":country="KW"
        elif code=='966':country="SA"
        elif code=='967':country="YE"
        elif code=='968':country="OM"
        elif code=='970':country="PS"
        elif code=='971':country="AE"	
        elif code=='972':country="ISR"
        elif code=='973':country="BH"
        elif code=='974':country="QA"
        else:
            country='default'#You can try to modify that to a 2-digit or 3-digit country code if you don't know, look at https://laendercode.net/en/2-letter-list.html or https://laendercode.net/en/3-letter-list.html I don't know, follow, or sponsored by this site, but I want to help you
            if country=='default':
                console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 1 : Country Code Not Supported ');country=None
            else:
                console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 1 : Country Code Not Supported, But we will Try ')
        r=get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={number}&country_code={country}",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX1821) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4660.11 Mobile Safari/537.36"})
        try:
            name=r.json()['result'][0]['name']
            if name=='':name=None
            NAME.append(name)   
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 1 : [bold green1]success[/bold green1] ') 
        except KeyError:
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 1 : No information Found For [ +{code}{number} ] ')
    except Exception as e:
        console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 1 : [bold red]Error[/bold red] ')
    Search_2(country,number,code)
        
def Search_2(country,number,code):
    try:
        rq=get(f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={country}')
        if 'No recourd found.' in rq.text:
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 2 : No information Found For [ +{code}{number} ] ')
        else:
            try:
                for JQ in rq.json()['result']:
                    NAME.append(JQ["name"]) 
                console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 2 : [bold green1]success[/bold green1] ') 
            except Exception as e:
                console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 2 : [bold red]Error[/bold red] Number [ 1 ] ')
    except Exception as e:
        console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 2 : [bold red]Error[/bold red] Number [ 2 ] ')
    Search_3(country,number,code)
    
def Search_3(country,number,code):
    try:
        r=post(f'https://devappteamcall.site/data/search_name?country={country}',data=f'&phoneNumber={number}',headers={'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)','Host': 'devappteamcall.site','Connection': 'close','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '23'})
        if r.json()["errorDesc"]=="no data found":
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 3 : No information Found For [ +{code}{number} ] ')
        else:
            for ED in re.findall('"Name":"(.*?)",',str(r.json())):
                NAME.append(ED)    
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 3 : [bold green1]success[/bold green1] ') 
    except Exception as e:
        console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 3 : [bold red]Error[/bold red] ')
    Search_4(country,number,code)
    
def Search_4(country,number,code):
    try:
        r=post('http://86.48.0.204:919/main',data={"number": str(code+number)},headers={"Content-Type": "application/x-www-form-urlencoded; charset=utf-8","User-Agent": "نمبربوك الخليج 1/3.3 CFNetwork/1240.0.4 Darwin/20.5.0".encode('UTF-8'),"Accept-Encoding": "gzip, deflate","Host": "86.48.0.204:919","Accept": "*/*","Accept-Language": "ar","Authorization": "Basic aW9zYWRtaW46cGFzc3BvcmQ=","token": "pcfgv64567ko1","Content-Length": "19"})
        try:
            for FZ in r.json():
                NAME.append(FZ["name"]) 
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 4 : [bold green1]success[/bold green1] ') 
        except:
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 4 : [bold red]Error[/bold red] Number [ 1 ] ')
    except Exception as e:
        console.print(f'[bold red]Root@Num-Info[/bold red]:-# Search 4 : [bold red]Error[/bold red] Number [ 2 ] ')
    Number_info(country,number,code)
    
def Number_info(country,number,code):
    try:
        if len(NAME)==0:console.print(f'[bold red]Root@Num-Info[/bold red]:-# Numebr-Info : No information Found For [ +{code}{number} ] ');exit()
        sleep(2);header()
        console.print(f"[bold bright_white] Number information  [ +{code}{number} {country} ] [/bold bright_white] ")
        table=Table(show_header=True,header_style="bold bright_blue")
        table.add_column("ID",style="bold dim",width=6)
        table.add_column("Name",style="bold red",min_width=20,justify="left")
        for id,data in enumerate(NAME,start=1):
            Name=str(data).split(":")[0]
            table.add_row(f'{id}',f'{str(Name)}')
        console.print(table)
        try:
            console.print(f'[bold red]Root@Num-Info[/bold red]:-# [ [bold dark_orange3]INFO[/bold dark_orange3] ] We Have Found That The Most Common Names in The list are ')
            for i in Counter(str(NAME).replace("'",'').replace(",","").split()).most_common(4):
                console.print(f'- [ {i[0]} ] It has been repeated about [ {i[1]} ] Times ')
        except Exception as e:pass
        console.print('\n')
    except Exception as e:
        console.print(f'\n[bold red]Root@Num-Info[/bold red]:-# Number-Info [bold red]Error[/bold red] !')
        
      
      
      
        
Main()