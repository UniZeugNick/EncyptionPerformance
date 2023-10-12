from Cryptodome.Cipher import Salsa20
from random import randbytes

key = randbytes(32)
data = b"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "

def Salsa20_en():
    cipher = Salsa20.new(key)
    ciphertext = cipher.encrypt(data)