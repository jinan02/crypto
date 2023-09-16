import random

def gen1(): 
    return random.randint(0, 26)

def E1(k, m): 
    c = ""
    for i in m: 
        if i.isalpha():
            if i.islower(): 
                c_i = chr(((ord(i)-97+ k)%26)+97)
            
            else:
                c_i = chr(((ord(i)-65+ k)%26)+65)

            c = c + c_i
        else: 
            c = c + i

    return c


def D1(k,c): 
    return E1(-k,c)



def eve(c): 
    for k in range(26): 
        m = ""
        for i in c: 
            if i.isalpha():
                if i.islower(): 
                    m_i = chr(((ord(i)- 97 - k)%26) + 97)
                
                else:
                    m_i = chr(((ord(i)-65 - k)%26) + 65)

                m = m + m_i
            else: 
                m = m + i
        print(f"Clé {k}: {m}")


print(eve('rtrxthiatbthhpvtrapxgpstr'))