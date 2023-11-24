from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

class Aes:
    def __init__(self, key):
        # Ensure key is in bytes format
        if isinstance(key, str):
            key = key.encode('utf-8')
        self._key = key

    def crypt(self, message, encode_input=True, decode_output=True):
        if encode_input:
            message = message.encode('utf-8')
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_message = padder.update(message) + padder.finalize()
        cipher = Cipher(algorithms.AES(self._key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_message) + encryptor.finalize()
        if decode_output:
            ciphertext = base64.b64encode(ciphertext).decode('utf-8')
        return ciphertext

    def decrypt(self, message, encode_output=True, decode_input=True):
        if decode_input:
            message = base64.b64decode(message.encode('utf-8'))
        cipher = Cipher(algorithms.AES(self._key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(message) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_message = unpadder.update(decrypted_message) + unpadder.finalize()
        if encode_output:
            unpadded_message = unpadded_message.decode('utf-8')
        return unpadded_message