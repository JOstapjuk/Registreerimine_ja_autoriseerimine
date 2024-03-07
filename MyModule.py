import random

def registreerimine(n:list,p:list,s:list)->any:
    """ 
    Funktsioon lisab uue kasutaja
    :param list n: Nimi j�rjend
    :param list p: Parool j�rjend
    :param list p: Salas�na j�rjend
    :rtype: any
    """
    while True:
        nimi=input("Nimi: ").capitalize()
        if nimi=="":
            print("Nimi ei saa olla t�hi.")
            print("")
        elif nimi in n:
            print("See nimi on juba registreeritud.")
            print("")
        else:
            break
    
    while True:
        valik=input("Kas soovite sisestada oma parooli v�i genereerida �he? (Sisesta/Gener): ").capitalize()
        if valik=="Sisesta":
            parool=input("Parool: ")
        elif valik=="Gener":
            str0=".,:;!_*-+()/#�%&"
            str1='0123456789'
            str2='qwertyuiopasdfghjklzxcvbnm'
            str3=str2.upper()
            str4=str0 + str1 + str2 + str3
            ls=list(str4)
            random.shuffle(ls)
            parool=''.join([random.choice(ls) for x in range(12)])
        else:
            print("Palun vali 'sisesta' v�i 'genereri'")
            print("")
            continue
        
        if parool=="":
            print("Parool ei saa olla t�hi.")
            print("")
        else:
            break
    
    while True:
        salas�na=input("Sisesta salas�na: ")
        if salas�na=="":
            print("Salas�na ei saa olla t�hi.")
            print("")
        else:
            print("Te olete edukalt registreerunud")
            n.append(nimi)
            p.append(parool)
            s.append(salas�na)
            return nimi, parool, salas�na
def autoriseerimine(n: list, p: list) -> bool:
    """
    Autoriseerib kasutaja s�steemi.

    :param list n: Nimi j�rjend
    :param list p: Parool j�rjend
    :rtype: bool
    """
    while True:
        nimi=input("Sisesta kasutajanimi: ").capitalize()
        parool=input("Sisesta parool: ")
        if nimi in n and parool==p[n.index(nimi)]:
            print("Autentimine �nnestus!")
            print("")
            return True
        else:
            print("Vigane kasutajanimi v�i parool!")
            print("")

def muuda_parool(n:list,p:list)->any:
    """
    Muudab kasutaja parooli.

    :param list n: Nimi j�rjend
    :param list n: Parool j�rjend
    :rtype: any
    """
    while True:
        nimi=input("Sisesta oma kasutajanimi: ").capitalize()
        if nimi not in n:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index=n.index(nimi)
            break

    while True:
        muutmine=input("Kas soovid muuta nime (N) v�i parooli (P)?: ").capitalize()
        if muutmine=="N":
            uus_nimi=input("Sisesta uus nimi: ").capitalize()
            if uus_nimi=="":
                print("Nimi ei saa olla t�hi.")
                print("")
                continue
            elif uus_nimi in n:
                print("See nimi on juba kasutusel.")
                print("")
                continue
            else:
                n[index]=uus_nimi
                print("Nimi edukalt muudetud.")
                print("")
                break
        elif muutmine=="P":
            uus_parool=input("Sisesta uus parool: ")
            if uus_parool=="":
                print("Parool ei saa olla t�hi.")
                print("")
                continue
            else:
                p[index]=uus_parool
                print("Parool edukalt muudetud.")
                print("")
                break
        else:
            print("Vigane valik. Palun vali 'N' v�i 'P'.")
            print("")  

def unustatud_parool(n: list, p: list, s: list) -> any:
    """
    Taastab unustatud parooli, kasutades eelnevalt sisestatud salas�na.

    :param list n: Nimi j�rjend
    :param list p: Parool j�rjend
    :param list s: Salas�na j�rjend
    :rtype: any
    """
    while True:
        kasutajanimi=input("Sisesta oma kasutajanimi: ").capitalize()
        if kasutajanimi not in n:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            break

    salasona=input("Sisesta salas�na: ")
    if salasona in s:
        index=s.index(salasona)
        if n[index]==kasutajanimi:
            print(f"Kasutaja {kasutajanimi} parool on: {p[index]}")
            print("")
        else:
            print("Vale kasutajanimi.")
            print("")
    else:
        print("Vale salas�na.")
        print("")