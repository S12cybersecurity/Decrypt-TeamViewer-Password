from itertools import product
from Crypto.Cipher import AES
import sys

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


IV = b"\x01\x00\x01\x00\x67\x24\x4F\x43\x6E\x67\x62\xF2\x5E\xA8\xD7\x04"
key = b"\x06\x02\x00\x00\x00\xa4\x00\x00\x52\x53\x41\x31\x00\x04\x00\x00"

ciphertext= bytes([ADD HERE])
decipher = AES.new(key,AES.MODE_CBC,IV)
plaintext = decipher.decrypt(ciphertext).decode()

print(f"{bcolors.OK}[+] Password: {bcolors.RESET}"+plaintext)
