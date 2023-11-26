from dotenv import load_dotenv
from lib.Crypt import Crypt
from lib.Decrypt import Decrypt
load_dotenv()

encrypted=Crypt().encrypt("¿Cómo estas?")
print("Encriptado: " + encrypted)

decrypt = Decrypt()
print("Decriptado: " + decrypt.decrypt(message=encrypted))

encryptedHash = encrypted.split("###")[1]
changed = Crypt().step3("Otro mensaje")
print("Decriptado2: " + decrypt.decrypt(message=changed + "###" + encryptedHash))
