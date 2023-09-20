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

def e2( message,key):
    c = []
    i=0
    for caractere in message: 
        if caractere.isalpha():
            # Generer le message chiffré à partir de key xor message
            lettre= int(key[i]) ^ ord(caractere)
            i=i+1
            c.append(format(lettre, '08b'))
        else: 
            c = c

    return c

def d2( key, cryptogramme):
    c=""
    i=0
    for caractere in cryptogramme: 
            # Recuperer le message à partir de key xor chiffré
            lettre= key[i] ^ int(caractere, 2)  
            i=i+1
            c = c + chr(lettre)
    return c

#--------------------------------question a-------------------------------------------

def main():
    for i in range(3):
        print("\n-------------------------scenario",i+1,"---------------")
        print("----------------------------ALICE--------------------")
        print("Salut! je suis Alice voici le message que je veux envoyer a Bob")
        message = "ceciestlemessageclairadechiffrer"
        print("m = ", message)
        key,key_binaire = gen2(message)
        print("Voici la cle generer par l'algorithme GEN2 : ", key_binaire)
        cryptogramme = e2(message,key)
        print("Voici le message chiffré par l'algorithme GEN2 : ", cryptogramme)

        print("---------------------EVE---------------------------")    
        print(" Salut! je suis EVE l'espionne, voila le cryptogramme que j'ai recu : ", cryptogramme)
        print("puisque j'ai pas de cle , je ne peux pas devinner le message !!")

        print("---------------------BOB---------------------------")
        print("Salut! je suis Bob, j'ai recu de la part d'ALICE le cryptogramme : ", cryptogramme)
        print("puisque j'ai le meme cle que ALICE : " ,key_binaire,"\t je peux donc dechiffrer ce message ")
        message_dechiffre = d2(key, cryptogramme)
        print("apres le dechiffrage j'ai eu ce message : " , message_dechiffre )

        print("--------------------------------------------------")
        print("testons la conformité du message : ", message_dechiffre == message )

main()    

