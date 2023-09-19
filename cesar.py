import random

#-----------------------------------question1------------------------------------

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
                lettre_encrypted = chr(((ord(caractere) - 97 + k) % 26) + 97)
            
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



#-----------------------------------question2------------------------------------

# Répétons le scénario trois fois de manière indépendante
m = "ceciestlemessageclairadechiffrer"

#1er scenario
print('************************************1er scenario************************************')
k1 = Gen1() #generation de la clé k1
c1 = E1(k1, m) #Alice chiffre le message m en utilisant la clé k1
print("****Pour Alice:\n => le message est: ", m, "\n => la clé est: ", k1, "\n => le cryptogramme est: ", c1, "\n" )
m_eve1 = c1 #le message chiffré vu par Eve 
print("****Pour Eve:\n  => le cryptogramme est: ", m_eve1, "\n" )
c1_decrypted = D1(k1, c1) #bob dechiffre le message m en utilisant la clé k1
print("****Pour Bob:\n => le cryptogramme est: ", c1, "\n => la clé est: ", k1, "\n => le message dechiffré est: ", c1_decrypted, "\n")

#2eme scenario
print('************************************2eme scenario************************************')
k2 = Gen1() #generation de la clé k2
c2 = E1(k2, m) #Alice chiffre le message m en utilisant la clé k2
print("****Pour Alice:\n => le message est: ", m, "\n => la clé est: ", k2, "\n => le cryptogramme est: ", c2 ,"\n" )
m_eve2 = c2 #le message chiffré vu par Eve
print("****Pour Eve:\n  => le cryptogramme est: ", m_eve2, "\n")
c2_decrypted = D1(k2, c2) #bob dechiffre le message m en utilisant la clé k2
print("****Pour Bob:\n => le cryptogramme est: ", c2, "\n => la clé est: ", k2, "\n => le message dechiffré est: ", c2_decrypted, "\n")

#3eme scenario
print('************************************3eme scenario************************************')
k3 = Gen1() #generation de la clé k3
c3 = E1(k3, m) #Alice chiffre le message m en utilisant la clé k3
print("****Pour Alice:\n => le message est: ", m, "\n => la clé est: ", k3, "\n => le cryptogramme est: ", c3, "\n" )
m_eve3 = c3 #le message chiffré vu par Eve
print("****Pour Eve:\n  => le cryptogramme est: ", m_eve3, "\n" )
c3_decrypted = D1(k3, c3) #bob dechiffre le message m en utilisant la clé k3
print("****Pour Bob:\n => le cryptogramme est: ", c3, "\n => la clé est: ", k3, "\n => le message dechiffré est: ", c3_decrypted, "\n")




#-----------------------------------question3------------------------------------


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

