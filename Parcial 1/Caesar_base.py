''' Archivo base para cifrado César '''
from ListaDinamicaCompleta_base import ListaDinamica
from string import ascii_lowercase as def_alph

class Caesar:
    def __init__(self, alphabet:str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self.__set_alphabet:ListaDinamica = self.__set_alphabet(alphabet)

    def encrypt(self, msg:str, key:int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
       
    
    def multiple_decrypt(self, msg:str) -> str:
        ''' Herramienta interactiva para múltiples desencriptaciones '''

    def __set_alphabet(self, alphabet:str) -> ListaDinamica:
        ''' Definir alfabeto de la herramienta '''
        alph = ListaDinamica(len(alphabet))
        for e in alphabet:
            alph.append(e)

if __name__ == '__main__':
    ''' Incluye aquí tus casos de prueba '''
    cesar= Caesar(def_alph)
    caso1 = "Une"
    caso2 = "Brayan herrera"
    
    print(cesar.encrypt(caso1, 2))
    encriptado =cesar.encrypt(caso2, 38)
    print(encriptado)
    print(cesar.encrypt(encriptado, 38, inverse=True))
    cesar.multiple_decrypt(encriptado)
    
    
















































































# '''Caso 1'''
# from ListaDinamicaCompleta import ListaDinamica
# from string import ascii_lowercase as def_alph

# class Caesar:
#     def _init_(self, alphabet: str) -> None:
#         ''' Inicializa herramienta criptográfica '''
#         self._set_alphabet: ListaDinamica = self._set_alphabet(alphabet)

#     def encrypt(self, msg: str, key: int, inverse=False) -> str:
#         ''' Des/encriptar un mensaje '''
#         result = ''
#         for char in msg:
#             if char.isalpha():
#                 index = self.__set_alphabet.index(char.lower())
#                 if inverse:
#                     index = (index - key) % len(self.__set_alphabet)
#                 else:
#                     index = (index + key) % len(self.__set_alphabet)
#                 result += self.__set_alphabet[index]
#             else:
#                 result += char
#         return result

#     def multiple_decrypt(self, msg: str) -> str:
#         ''' Herramienta interactiva para múltiples desencriptaciones '''
#         for key in range(len(self.__set_alphabet)):
#             decrypted_msg = self.encrypt(msg, key, inverse=True)
#             print(f"Key {key}: {decrypted_msg}")
#         return "Multiple decryption completed."

#     def __set_alphabet(self, alphabet: str) -> ListaDinamica:
#         ''' Definir alfabeto de la herramienta '''
#         alph = ListaDinamica(len(alphabet))
#         for e in alphabet:
#             alph.append(e)
#         return alph

# if __name__ == '_main_':
#     ''' Casos de prueba '''
#     caesar_cipher = Caesar(def_alph)

#     # Cadenas encriptadas
#     encrypted_une = caesar_cipher.encrypt("UNE", key=10)
#     encrypted_guadalajara = caesar_cipher.encrypt("GuAdAlAjArA", key=10)
#     encrypted_mexico = caesar_cipher.encrypt("MexicO", key=10)
#     encrypted_names = caesar_cipher.encrypt("(Tú primer nombre y primer apellido separados por un espacio)", key=10)
    
#     print(f'UNE encriptado: {encrypted_une}')
#     print(f'GuAdAlAjArA encriptado: {encrypted_guadalajara}')
#     print(f'MexicO encriptado: {encrypted_mexico}')
#     print(f'Nombres encriptados: {encrypted_names}')

#     # Cadenas desencriptadas y llaves
#     caesar_cipher.multiple_decrypt("Rfgehpghen qr qngbf")
#     caesar_cipher.multiple_decrypt("Dbx mn urbcjb")
#     caesar_cipher.multiple_decrypt("Fkdbkfbox bk zljmrqxzflk")
#     caesar_cipher.multiple_decrypt("Ozmyzmcn")




'''Caso 2'''
from ListaDinamicaCompleta_base import ListaDinamica
from string import ascii_lowercase as def_alph

# class Caesar:
#     def _init_(self, alphabet: str) -> None:
#         ''' Inicializa herramienta criptográfica '''
#         self._set_alphabet: ListaDinamica = self._set_alphabet(alphabet)

#     def encrypt(self, msg: str, key: int, inverse=False) -> str:
#         ''' Des/encriptar un mensaje '''
#         result = ''
#         for char in msg:
#             if char.isalpha():
#                 index = self.__set_alphabet.index(char.lower())
#                 if inverse:
#                     index = (index - key) % len(self.__set_alphabet)
#                 else:
#                     index = (index + key) % len(self.__set_alphabet)
#                 result += self.__set_alphabet[index]
#             else:
#                 result += char
#         return result

#     def multiple_decrypt(self, msg: str) -> str:
#         ''' Herramienta interactiva para múltiples desencriptaciones '''
#         for key in range(len(self.__set_alphabet)):
#             decrypted_msg = self.encrypt(msg, key, inverse=True)
#             print(f"Key {key}: {decrypted_msg}")
#         return "Multiple decryption completed."

#     def __set_alphabet(self, alphabet: str) -> ListaDinamica:
#         ''' Definir alfabeto de la herramienta '''
#         alph = ListaDinamica(len(alphabet))
#         for e in alphabet:
#             alph.append(e)
#         return alph

# if __name__ == '_main_':
#     ''' Incluye aquí tus casos de prueba '''
#     caesar_cipher = Caesar(def_alph)
#     message = "Hello, World!"
#     key = 3

#     encrypted_message = caesar_cipher.encrypt(message, key)
#     print(f"Original Message: {message}")
#     print(f"Encrypted Message: {encrypted_message}")

#     decrypted_message = caesar_cipher.encrypt(encrypted_message, key, inverse=True)
#     print(f"Decrypted Message: {decrypted_message}")

#     caesar_cipher.multiple_decrypt(encrypted_message)