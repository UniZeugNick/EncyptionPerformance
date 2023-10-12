from Cryptodome.Cipher import Blowfish
from random import randbytes

key = randbytes(56)
data = b"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "

def Blowfish_en():
    cipher = Blowfish.new(key=key, mode= Blowfish.MODE_CBC)
    ciphertext = cipher.encrypt(data)    