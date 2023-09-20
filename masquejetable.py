import random
"------------------------------------2. Masque jetable-----------------------------------"

def gen2(message):
    key= []
    key_binaire= []
    for i in message:
       # Générer un nombre aléatoire entre 0 et 255 (8 bits)
       n = random.randint(0, 255)
       key.append(n)
       # Convertir le nombre en binaire (8 bits)
       key_binaire.append(format(n, '08b'))

    return key,key_binaire

def e2( message):
    c = []
    key,_ =gen2(message)
    i=0
    for caractere in message: 
        if caractere.isalpha():
            # Generer le message chiffré à partir de key xor message
            lettre= int(key[i]) ^ ord(caractere)
            i=i+1
            c.append(format(lettre, '08b'))
        else: 
            c = c

    return key,c

def d2( key, cryptogramme):
    c=""
    i=0
    for caractere in cryptogramme: 
            # Recuperer le message à partir de key xor chiffré
            lettre= key[i] ^ int(caractere, 2)  
            i=i+1
            c = c + chr(lettre)
    return c

