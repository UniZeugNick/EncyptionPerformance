from random import randbytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes, CipherAlgorithm

key = randbytes(16)
data = b"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
iv = randbytes(16)

def SM4_en():
    cipher = Cipher(algorithms.SM4(key),modes.CBC(iv))
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()   