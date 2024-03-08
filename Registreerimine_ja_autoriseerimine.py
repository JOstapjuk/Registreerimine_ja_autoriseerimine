from MyModule import * 
nimed=[]
paroolid=[]
salasonad=[]
while True:
    operatsioon=print("Registreerimine(R)\nAutoriseerimine(A)\nNime või parooli muutmine(M)\nUnustanud parooli taastamine(U)\nLõpetamine(L)")
    vastus=str(input()).capitalize()
    if vastus=="R":
        uus_nimi,uus_parool,uus_salasona=registreerimine(nimed,paroolid,salasonad)
        print(nimed,paroolid,salasonad)
        print("")
    elif vastus=="A":
        autoriseerimine(nimed,paroolid)
    elif vastus=="M":
        muuda_parool(nimed,paroolid)
        print(nimed,paroolid)
    elif vastus=="U":
        unustatud_parool(nimed,paroolid,salasonad)
    elif vastus=="L":
        break
    else:
        print("Palun vali toiming siit nimekirjast")
