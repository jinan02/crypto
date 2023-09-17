import random

def main():
    print("----------------------------ALICE--------------------")
    print("Salut! je suis Alice voici le message que je veux envoyer a Bob \n   ")
    message = "ceciestlemessageclairadechiffrer"
    print("m = ", message , "\n")
    key = Gen1()
    print("Voici la cle generer par l'algorithme GEN1 : ", key)
    cryptogramme = E1(message,key)
    print("Voici le message chiffré par l'algorithme GEN1 : ", cryptogramme)

    print("---------------------EVE---------------------------")    
    print(" Salut! je suis EVE l'espionne, voila le cryptogramme que j'ai recu : ", cryptogramme)
    print("puisque j'ai pas de cle , je ne peux pas devinner le message !!")

    print("---------------------BOB---------------------------")
    print("Salut! je suis Bob, j'ai recu de la part d'ALICE le cryptogramme : ", cryptogramme)
    print("puisque j'ai le meme cle que ALICE : " ,key,"\t je peux donc dechiffrer ce message ")
    message_dechiffre = D1(cryptogramme,key)
    print("apres le dechiffrage j'ai eu ce message : " , message_dechiffre )

    print("--------------------------------------------------")

    print("testons la conformité du message : ", message_dechiffre == message )


def Gen1():
    k = random.randint(0, 26)
    return k

def E1(message, key):
    c = ''
    for caractere in message:
        # Obtention du code ASCII du caractère
        code_ascii = ord(caractere)

        if code_ascii >= 97 and code_ascii <= 122:
            nouveau_code_ascii = (code_ascii - 97 + key) % 26 + 97
            lettre = chr(nouveau_code_ascii)
            
        elif code_ascii >= 65 and code_ascii <= 90:
            nouveau_code_ascii = (code_ascii - 65 + key) % 26 + 65
            lettre = chr(nouveau_code_ascii)

        else :
            # Si le caractère n'est pas une lettre minuscule, ne le modifiez pas
            lettre = caractere

        c = c + lettre

    return c

def D1(cryptogramme , key):
    m = ''
    for caractere in cryptogramme:
        # Obtention du code ASCII du caractère
        code_ascii = ord(caractere)

        if code_ascii >= 97 and code_ascii <= 122:
            nouveau_code_ascii = (code_ascii - 97 - key) % 26 + 97
            lettre = chr(nouveau_code_ascii)
            
        elif code_ascii >= 65 and code_ascii <= 90:
            nouveau_code_ascii = (code_ascii - 65 - key) % 26 + 65
            lettre = chr(nouveau_code_ascii)

        else :
            # Si le caractère n'est pas une lettre minuscule, ne le modifiez pas
            lettre = caractere

        m = m + lettre

    return m



    

main()    
