import random

def registreerimine(n:list,p:list,s:list)->any:
    """ 
    Funktsioon lisab uue kasutaja
    :param list n: Nimi järjend
    :param list p: Parool järjend
    :param list p: Salasõna järjend
    :rtype: any
    """
    while True:
        nimi=input("Nimi: ").capitalize()
        if nimi=="":
            print("Nimi ei saa olla tühi.")
            print("")
        elif nimi in n:
            print("See nimi on juba registreeritud.")
            print("")
        else:
            break
    
    while True:
        valik=input("Kas soovite sisestada oma parooli või genereerida ühe? (Sisesta/Gener): ").capitalize()
        if valik=="Sisesta":
            parool=input("Parool: ")
        elif valik=="Gener":
            str0=".,:;!_*-+()/#¤%&"
            str1='0123456789'
            str2='qwertyuiopasdfghjklzxcvbnm'
            str3=str2.upper()
            str4=str0 + str1 + str2 + str3
            ls=list(str4)
            random.shuffle(ls)
            parool=''.join([random.choice(ls) for x in range(12)])
        else:
            print("Palun vali 'sisesta' või 'genereri'")
            print("")
            continue
        
        if parool=="":
            print("Parool ei saa olla tühi.")
            print("")
        else:
            break
    
    while True:
        salasõna=input("Sisesta salasõna: ")
        if salasõna=="":
            print("Salasõna ei saa olla tühi.")
            print("")
        else:
            print("Te olete edukalt registreerunud")
            n.append(nimi)
            p.append(parool)
            s.append(salasõna)
            return nimi, parool, salasõna
def autoriseerimine(n: list, p: list) -> bool:
    """
    Autoriseerib kasutaja süsteemi.

    :param list n: Nimi järjend
    :param list p: Parool järjend
    :rtype: bool
    """
    while True:
        nimi=input("Sisesta kasutajanimi: ").capitalize()
        parool=input("Sisesta parool: ")
        if nimi in n and parool==p[n.index(nimi)]:
            print("Autentimine õnnestus!")
            print("")
            return True
        else:
            print("Vigane kasutajanimi või parool!")
            print("")

def muuda_parool(n:list,p:list)->any:
    """
    Muudab kasutaja parooli.

    :param list n: Nimi järjend
    :param list n: Parool järjend
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
        muutmine=input("Kas soovid muuta nime (N) või parooli (P)?: ").capitalize()
        if muutmine=="N":
            uus_nimi=input("Sisesta uus nimi: ").capitalize()
            if uus_nimi=="":
                print("Nimi ei saa olla tühi.")
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
                print("Parool ei saa olla tühi.")
                print("")
                continue
            else:
                p[index]=uus_parool
                print("Parool edukalt muudetud.")
                print("")
                break
        else:
            print("Vigane valik. Palun vali 'N' või 'P'.")
            print("")  

def unustatud_parool(n: list, p: list, s: list) -> any:
    """
    Taastab unustatud parooli, kasutades eelnevalt sisestatud salasõna.

    :param list n: Nimi järjend
    :param list p: Parool järjend
    :param list s: Salasõna järjend
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

    salasona=input("Sisesta salasõna: ")
    if salasona in s:
        index=s.index(salasona)
        if n[index]==kasutajanimi:
            print(f"Kasutaja {kasutajanimi} parool on: {p[index]}")
            print("")
        else:
            print("Vale kasutajanimi.")
            print("")
    else:
        print("Vale salasõna.")
        print("")