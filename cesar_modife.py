import random
import string

def Gen3(): 
    for x in range(26):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        k = ''.join(random.choice(letters) for _ in range(32))
        #k = ''.join(random.choice(string.ascii_letters) for _ in range(32))
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
    m = ""
    for i in range(len(c)):
        if c[i].isalpha():
            mi = letters[(letters.index(c[i])+letters.index(k[i])) % 26]
            m = m + mi
        else: 
            m = m + c[i]
        
    return m

print(E3("afejlm","jinane")) #resultat khass ikoun "jdjrcs"
print(D3("afejlm","jdjrcs"))