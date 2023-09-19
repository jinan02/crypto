import random

def main():
    print("--------------------ALICE--------------------")
    print("Salut! je suis Alice voici le message que je veux envoyer à Bob \n   ")
    m = "ceciestlemessageclairadechiffrer"
    print("m = ", m , "\n")
    k = Gen1()
    print("Voici la clé generée par l'algorithme Gen1 : ", k)
    c = E1(k,m)
    print("Voici le message chiffré par l'algorithme E1 : ", c)

    print("---------------------EVE---------------------------")    
    print(" Salut! je suis EVE l'espionne, voila le cryptogramme que j'ai recu : ", c)
    print("puisque j'ai pas de clé , je ne peux pas devinner le message !!")

    print("---------------------BOB---------------------------")
    print("Salut! je suis Bob, j'ai recu de la part d'ALICE le cryptogramme : ", c)
    print("puisque j'ai la meme clé que ALICE : " ,k,"\t je peux donc dechiffrer ce message ")
    c_decrypted = D1(k,c)
    print("apres le dechiffrage j'ai eu ce message : " , c_decrypted )

    print("--------------------------------------------------")

    print("testons la conformité du message : ", c_decrypted == m )



#fonction qui genere la clé
def Gen1(): 
    return random.randint(0, 26)


def E1(k, m):
    c = ""
    for caractere in m: 
        #on verifie si le caractere est une lettre
        if caractere.isalpha():
            #on verifie par la suite si elle est minuscule
            if caractere.islower(): 
                #on chiffre le caractere en calculant la distance entre la valeur ASCII du caractere et la valeur ASCII de la lettre 'a'(qui est égale à 97)
                #on ajoute la valeur de notre clé et ensuite la valeur 97 pour rester dans la plage des valeures ASCII des lettres miniscules 
                lettre_encrypted = chr(((ord(caractere) - 97 + k) % 26)+ 97)
            
            else:
                #Si la lettre est majuscule on refait la meme chose en utilisant, cette fois-ci la valeur ASCII de la lettre 'A'
                lettre_encrypted = chr(((ord(caractere) - 65 + k) % 26) + 65)

            c = c + lettre_encrypted

        else: 
            #si le caractere n'est pas une lettre on le conserve comme il est
            c = c + caractere

    return c


#D1 est la fonction inverse de E1
def D1(k, c):
    m = ""
    for caractere in c: 
        if caractere.isalpha():
            if caractere.islower():         
                lettre_decrypted = chr(((ord(caractere) - 97 - k) % 26)+ 97)
            
            else:
                lettre_encrypted = chr(((ord(caractere) - 65 - k) % 26) + 65)

            m = m + lettre_decrypted

        else: 
            #si le caractere n'est pas une lettre on le conserve comme il est
            m = m + caractere

    return m


#on pourrait aussi l'ecrire de cette manière
def D1(k,c): 
    return E1(-k,c)


#eve(c): fonction qui va permettre à Eve de trouver la clé secrete en essayant les 26 clés possibles
def eve(c): 
    for k in range(26): 
        m = ""
        for caractere in c: 
            if caractere.isalpha():
                if caractere.islower(): 
                    m_dec = chr(((ord(caractere) - 97 - k) % 26) + 97)
                
                else:
                    m_dec = chr(((ord(caractere) - 65 - k) % 26) + 65)

                m = m + m_dec
            else: 
                m = m + caractere
        print(f"Clé {k}: {m}")


main()