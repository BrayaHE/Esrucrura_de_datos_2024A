from ListaDinamicaCompleta import ListaDinamica
from string import ascii_lowercase as def_alph

class Caesar:
    def _init_(self, alphabet: str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self._set_alphabet: ListaDinamica = self._set_alphabet(alphabet)

    def encrypt(self, msg: str, key: int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
        result = ''
        for char in msg:
            if char.isalpha():
                index = self.__set_alphabet.index(char.lower())
                if inverse:
                    index = (index - key) % len(self.__set_alphabet)
                else:
                    index = (index + key) % len(self.__set_alphabet)
                result += self.__set_alphabet[index]
            else:
                result += char
        return result

    def multiple_decrypt(self, msg: str) -> str:
        ''' Herramienta interactiva para múltiples desencriptaciones '''
        for key in range(len(self.__set_alphabet)):
            decrypted_msg = self.encrypt(msg, key, inverse=True)
            print(f"Key {key}: {decrypted_msg}")
        return "Multiple decryption completed"

    def __set_alphabet(self, alphabet: str) -> ListaDinamica:
        ''' Definir alfabeto de la herramienta '''
        alph = ListaDinamica(len(alphabet))
        for e in alphabet:
            alph.append(e)
        return alph

if __name__ == '__main__':
    ''' Incluye aquí tus casos de prueba '''
    caesar_cipher = Caesar(def_alph)
    key = 2
    encrypted_une = caesar_cipher.encrypt("UNE", key=10)
    encrypted_guadalajara = caesar_cipher.encrypt("GuAdAlAjArA", key=10)
    encrypted_mexico = caesar_cipher.encrypt("MexicO", key=10)
    encrypted_names = caesar_cipher.encrypt("(Tú primer nombre y primer apellido separados por un espacio)", key=10)
    
    print(f'UNE encriptado: {encrypted_une}')
    print(f'GuAdAlAjArA encriptado: {encrypted_guadalajara}')
    print(f'MexicO encriptado: {encrypted_mexico}')
    print(f'Nombres encriptados: {encrypted_names}')

    caesar_cipher.multiple_decrypt("Rfgehpghen qr qngbf")
    caesar_cipher.multiple_decrypt("Dbx mn urbcjb")
    caesar_cipher.multiple_decrypt("Fkdbkfbox bk zljmrqxzflk")
    caesar_cipher.multiple_decrypt("Ozmyzmcn") 