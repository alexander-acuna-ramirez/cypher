class Vigenere:
    def __init__(self, _key):
        self.key = _key
        #self.abc = "abcdefghijklmnñopqrstuvwxyz"
        self.abc = "abcdefghijklmnñopqrstuvwxyzáéíóú"

    def crypt(self, message):  # ENCRYPTION FUNCTION
        encrypted_text = ""
        i = 0
        for char in message:
            if char.isalpha():
                is_upper = char.isupper()
                char_index = self.abc.upper().find(char.upper())
                key_index = self.abc.upper().find(self.key[i % len(self.key)].upper())
                sum_value = char_index + key_index
                modulo = sum_value % len(self.abc)
                encrypted_char = self.abc[modulo]
                encrypted_text += encrypted_char.upper() if is_upper else encrypted_char.lower()
                i += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, message):
        decrypted_text = ""
        i = 0
        for char in message:
            if char.isalpha():
                is_upper = char.isupper()
                char_index = self.abc.upper().find(char.upper())
                key_index = self.abc.upper().find(self.key[i % len(self.key)].upper())
                sum_value = char_index - key_index
                modulo = sum_value % len(self.abc)
                decrypted_char = self.abc[modulo]
                decrypted_text += decrypted_char.upper() if is_upper else decrypted_char.lower()
                i += 1
            else:
                decrypted_text += char
        return decrypted_text
