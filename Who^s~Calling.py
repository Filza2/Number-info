
import phonenumbers
from os import system
from phonenumbers import carrier
from requests import get,post
def n1():
	try:system("cls")
	except:
		try:system("clear")
		except:pass
	phon=input("\n[+] Enter Phone Number: ")
	code=phon.split(' ')[0]
	try:phone=phon.split(' ')[1]
	except IndexError:exit('[-] You must type the country code, then a space, and then the phone number.. \nExample[ 974 52947429 ]')
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
	send=get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phone}&country_code={countr}",headers={"User-Agent":"8Y/69"})
	try:
		name=send.json()['result'][0]['name']
		if name=='':name='nothing'
		nump=send.json()['result'][0]['number']
		pho=phonenumbers.parse('+'+phon)
		qtr=carrier.name_for_number(pho,'en')
		print(f'\n[+] phone : {nump}\n[+] country : {countr2}\n[+] ZIP code : {countr}\n[+] name : {name}\n[+] number type : {qtr}')
	except KeyError:print('[-] No leaked information found')
def n2():
	try:system("cls")
	except:
		try:system("clear")
		except:pass
	res=get('http://ipinfo.io/json').json()
	c=res["country"]
	n=input("[+] Enter number : ")
	r=post(f'https://devappteamcall.site/data/search_name?country={c}',data=f'&phoneNumber={n}',headers={'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)','Host': 'devappteamcall.site','Connection': 'close','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '23'},verify=False).json()
	if r["errorDesc"]=="no data found":print("[-] There is no information on the number at the moment")
	else:print(r)
print("""
██╗    ██╗██╗  ██╗ ██████╗ ███████╗     ██████╗ █████╗ ██╗     ██╗     ██╗███╗   ██╗ ██████╗     ██████╗ 
██║    ██║██║  ██║██╔═══██╗██╔════╝    ██╔════╝██╔══██╗██║     ██║     ██║████╗  ██║██╔════╝     ╚════██╗
██║ █╗ ██║███████║██║   ██║███████╗    ██║     ███████║██║     ██║     ██║██╔██╗ ██║██║  ███╗      ▄███╔╝
██║███╗██║██╔══██║██║   ██║╚════██║    ██║     ██╔══██║██║     ██║     ██║██║╚██╗██║██║   ██║      ▀▀══╝ 
╚███╔███╔╝██║  ██║╚██████╔╝███████║    ╚██████╗██║  ██║███████╗███████╗██║██║ ╚████║╚██████╔╝      ██╗   
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝       ╚═╝                                                                                                            
By @TweakPY - @vv1ck - @EDISONpy - @8Y""")
try:
	b=int(input('1- Number info\n2- Number info\n:'))
	if b==1:n1()
	elif b==2:n2()
	else:exit('\n- By @TweakPY - @vv1ck - @EDISONpy - @8Y .. ')
except KeyboardInterrupt:exit(2030)
except:exit('\n- By @TweakPY - @vv1ck - @EDISONpy - @8Y .. ')
