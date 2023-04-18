class CaesarCipher:
    """
    A class to represent a Caesar Cipher.
    Args:
        alphabet (str): The alphabet taken from the user.
        shift (int): The shift chosen by the user to encrypt or decrypt alphabet.
    """
    def __init__(self, alphabet, shift):
        self.alphabet = alphabet
        self.shift = shift

    @property
    def cipher(self):
        """Returns encrypted alphabet."""
        new_alphabet = ''
        for letter in self.alphabet:
            new_idx = (
                              self.alphabet.index(letter) + self.shift
                      ) % len(self.alphabet)
            new_alphabet += self.alphabet[new_idx]
        return new_alphabet

    def encrypt(self, message):
        """Takes normal message and returns encrypted message. """
        encrypted_message = ''
        for letter in message:
            if letter not in self.alphabet:
                encrypted_message += letter
            else:
                encrypted_message += self.cipher[self.alphabet.index(letter)]
        return encrypted_message

    def decrypt(self, message):
        """Takes encrypted message and returns decrypted message."""
        decrypted_message = ''

        for letter in message:
            if letter not in self.cipher:
                decrypted_message += letter
            else:
                decrypted_message += self.alphabet[self.cipher.index(letter)]
        return 