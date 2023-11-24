from utils.Vigenere import Vigenere
from utils.Transform import Transform
from utils.AES import Aes
import re

from dotenv import load_dotenv
import os

class Decrypt:
    def __init__(self):
        try:
            load_dotenv()
            vk = os.getenv('VIGENERE_KEY')
            if not vk:
                raise ValueError("Error: La clave de Vigenere no puede estar vacía.")
            elif not re.match("^[a-zA-Z]+$", vk):
                raise ValueError("Error: La clave de Vigenere solo puede contener letras.")
            
            ak = os.getenv('AESKEY')

            if not ak:
                raise ValueError("Error: La clave de AES no puede estar vacía.")
            elif len(ak) != 16:  # 16 bytes es igual a 128 bits
                raise ValueError("Error: La clave de AES debe tener una longitud de 128 bits (16 bytes).")
            
            self._vk = vk 
            self._ak = ak

            self._vgc = Vigenere(vk)
            self._tgc = Transform()
            self._agc = Aes(ak)
        except ValueError as ve:
            print(ve)
            exit(1)

    def step1(self, message):
        return self._agc.decrypt(message=message)
    def step2(self, message):
        return self._vgc.decrypt(message=message)
    def step3(self, message):
        return self._tgc.decrypt(message=message)
    

    def decrypt(self, message):
        result = self.step1(message)
        result = self.step2(result)
        result = self.step3(result)
        return result