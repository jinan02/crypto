import random


#fonction qui genere la clé
def Gen3(): 
    for x in range(26):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        k = ''.join(random.choice(letters) for _ in range(32))
        return k
    

def E3(k, m): 
    letters = "abcdefghijklmnopqrstuvwxyz"
    c = ""

    for i in range(len(m)):
        if m[i].isalpha():
            ci = letters[(letters.index(m[i])-letters.index(k[i])) % 26]
            c = c + ci
        else: 
            c = c + m[i]
        
    return c

def D3(k, c): 
    letters = "abcdefghijklmnopqrstuvwxyz"
    m_decrypted = ""
    for i in range(len(c)):
        if c[i].isalpha():
            mi = letters[(letters.index(c[i])+letters.index(k[i])) % 26]
            m_decrypted = m_decrypted + mi
        else: 
            m_decrypted = m_decrypted + c[i]
        
    return m_decrypted

print(E3("afejlm","jinane")) #resultat khass ikoun "jdjrcs"
print(D3("afejlm","jdjrcs"))