class Transform:
    def __init__(self):
        self._transformation_map = {"a": "{", "e": "}", "i": "@", "o": "&", "u": "]","{":"a","}":"e","@":"i","&":"o","]":"u","ñ":"a"}
        self._inverse_map = {v: k for k, v in self._transformation_map.items()}

    def crypt(self, message):
        transformed_message = ""
        for char in message:
            if char in self._transformation_map:
                transformed_message += self._transformation_map[char]
            else:
                transformed_message += char
        return transformed_message
    
    def decrypt(self, message):
        transformed_message = ""
        for char in message:
            if char in self._inverse_map:
                transformed_message += self._inverse_map[char]
            else:
                transformed_message += char
        return transformed_message