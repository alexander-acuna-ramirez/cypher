from dotenv import load_dotenv
from lib.Crypt import Crypt
from lib.Decrypt import Decrypt
load_dotenv()

encrypted=Crypt().encrypt("¿Cómo estás?")
print("Encriptado: " + encrypted)
decrypt = Decrypt()
print("Decriptado: " + decrypt.decrypt(message=encrypted))