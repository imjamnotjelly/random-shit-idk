# bad
"""
class CaesarCipher(object):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        encoded_st = ""
        for c in st.upper():
            if not c.isalpha():
                encoded_st += c
                continue
            alphabet_index = self.alphabet.index(c)+self.shift
            if alphabet_index > 25:
                alphabet_index %= 26
            encoded_st += self.alphabet[alphabet_index]
        return encoded_st
        
    def decode(self, st):
        decoded_st = ""
        for c in st.upper():
            if not c.isalpha():
                decoded_st += c
                continue
            alphabet_index = self.alphabet.index(c)-self.shift
            if alphabet_index < 0:
                alphabet_index %= 26
            decoded_st += self.alphabet[alphabet_index]
        return decoded_st
"""

# okay
class CaesarCipher(object):
    def __init__(self, shift):
        self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shift_alph = self.alph[shift:] + self.alph[:shift]
        
    def encode(self, st):
        encoded_st = ""
        for c in st.upper():
            if not c.isalpha():
                encoded_st += c
                continue
            encoded_st += self.shift_alph[self.alph.index(c)]
        return encoded_st
        
    def decode(self, st):
        decoded_st = ""
        for c in st.upper():
            if not c.isalpha():
                decoded_st += c
                continue
            decoded_st += self.alph[self.shift_alph.index(c)]
        return decoded_st
      
  
# ill probably come back to this in the future and use translations or ascii values like a big boy
