import random




#fonction qui genere la clé
def Gen3(): 
    for x in range(26):
        k = [random.randint(0, 26) for _ in range(32)]
        return k
    

def E3(k, m):
    c = ""
    for i in range(32): 
        if m[i].isalpha():
            if m[i].islower(): 
                lettre_encrypted = chr(((ord(m[i]) - 97 + k[i]) % 26) + 97)
            
            else:
                lettre_encrypted = chr(((ord(m[i]) - 65 + k[i]) % 26) + 65)

            c = c + lettre_encrypted

        else: 
            c = c + m[i]

    return c

def D3(k,c): 
    m_decrypted = ""
    for i in range(32): 
        if c[i].isalpha():
            if c[i].islower(): 
                lettre_decrypted = chr(((ord(c[i]) - 97 + k[i]) % 26) + 97)
            
            else:
                lettre_decrypted = chr(((ord(c[i]) - 65 + k[i]) % 26) + 65)

            m_decrypted = m_decrypted + lettre_decrypted

        else: 
            m_decrypted = m_decrypted + c[i]

    return c