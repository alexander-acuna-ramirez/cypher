from dotenv import load_dotenv
from lib.Crypt import Crypt
from lib.Decrypt import Decrypt
load_dotenv()

encrypted=Crypt().encrypt("{¿Cómo esta?ñ] é()/&%$#!|¡¬°*¨´}-_.:,;~`^@😀")
print("Encriptado: " + encrypted)
decrypt = Decrypt()
print("Decriptado: " + decrypt.decrypt(message=encrypted))


primer = decrypt.step2(message='l¿Kká& }aú{?')
segundo = decrypt.step3(message=primer)
print(segundo)