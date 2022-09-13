try:import os,re;from phonenumbers import carrier,parse;from requests import get,post;from time import sleep
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

███╗   ██╗██╗   ██╗███╗   ███╗      ███████╗██╗███╗   ██╗███████╗        
████╗  ██║██║   ██║████╗ ████║      ██╔════╝██║████╗  ██║██╔════╝        
██╔██╗ ██║██║   ██║██╔████╔██║█████╗███████╗██║██╔██╗ ██║█████╗          
██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝╚════██║██║██║╚██╗██║██╔══╝          
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ███████║██║██║ ╚████║██║             
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝   

By @TweakPY - @vv1ck - @EDISONpy """)
def n1():
    banner()
    print('\nNote : Phone Number Must Like This : 966 508551505')
    phon=input("\n[?] Phone Number : ")
    code=phon.split(' ')[0]
    try:phone=phon.split(' ')[1]
    except IndexError:exit('[-] You Must Type The Country Code, Then a space, And Then The Phone Number.. \nExample : [ 974 52947429 ]')
    if code =='20':country="EG:Egypt"
    elif code =='98':country="IR:Iran"
    elif code =='212':country="MA:Morocco"
    elif code =='213':country="DZ:Algeria"
    elif code =='216':country="TN:Tunisia"
    elif code =='249':country="SD:Sudan"
    elif code =='252':country="SO:Somalia"
    elif code =='961':country="LB:Libya"
    elif code =='962':country="JO:Jordan"
    elif code =='963':country="SY:Syria"
    elif code =='964':country="IQ:Iraq"
    elif code =="965":country="KW:Kuwait"
    elif code =='966':country="SA:Saudi Arabia"
    elif code =='967':country="YE:Yemen"
    elif code =='968':country="OM:Oman"
    elif code =='970':country="PS:Palestine"
    elif code =='971':country="AE:Emirates"	
    elif code =='972':country="ISR:Israel"
    elif code =='973':country="BH:Bahrain"
    elif code =='974':country="QA:Qatar"
    else:exit("[¿] The country code is not added for this number, it will be added soon")
    countr=country.split(':')[0]
    countr2=country.split(':')[1]
    rq=get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phone}&country_code={countr}",headers={"User-Agent":"8Y/69"})
    try:
        name=rq.json()['result'][0]['name']
        if name=='':name='nothing'
        nump=rq.json()['result'][0]['number']
        pho=parse('+'+phon)
        qtr=carrier.name_for_number(pho,'en')
        print(f'\n[+] Phone : {nump}\n[+] Country : {countr2}\n[+] ZIP code : {countr}\n[+] Name : {name}\n[+] Number Type : {qtr}')    
    except KeyError:print('[-] No leaked information Found . ');print('\n[!] Moving to Another Tool ..');sleep(5);n2()
def n2():
    banner()
    res=get('http://ipinfo.io/json').json();c=res["country"]
    n=input("\n[?] Phone Number : ")
    rq=post(f'https://devappteamcall.site/data/search_name?country={c}',data=f'&phoneNumber={n}',headers={'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)','Host': 'devappteamcall.site','Connection': 'close','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '23'})
    if rq.json()["errorDesc"]=="no data found":print('[-] No leaked information Found . ');print('\n[!] Moving to Another Tool ..');sleep(5);n3()
    else:
        rea=rq.text.replace('\\',"");spam=re.findall('"itSpam":(.*?),',rea);spam_t=str(spam).split(']')[0].split(',')[1]
        if 'true' in spam_t:print('\n[+] The Number is Flagged under Spam Numbers')
        elif 'false' in spam_t:print('\n[+] The Number is Not Flagged under Spam Numbers')
        else:print('[+] The Number is Flagged under Spam Numbers',spam)
        print(f'\n[+] Records Found :\n')
        for ED in re.findall('"Name":"(.*?)",',rea):print(f'[+] Name : {ED}')       
def n3():
    banner()
    print('\nNote : Phone Number Must Like This : 508551505 SA ')
    n=input("\n\n[?] Phone Number : ")
    nu=n.split(' ')[0]
    try:cc=n.split(' ')[1]
    except IndexError:exit('[-] You Must Type The Phone Number, Then a space, and Then The country code .. \nExample : [ 52947429 SA ]')
    rq=get(f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={nu}&country_code={cc}')
    if 'No recourd found.' in rq.text:exit('[-] No leaked information Found . ')
    else:
        try:
            for JQ in rq.json()['result']:print(f'\n[+] Name : {JQ["name"]}\n[+] Phone : {JQ["number"]}')    
        except:exit('[!] Error .')
n1()
