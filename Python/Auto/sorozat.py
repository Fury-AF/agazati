import random



def lottoszamok(kiirás_db):
    #generáljunk 5 lottószámot! [1,90]
    lotto_lista = []
    i = 1
    while i <= kiirás_db:
        vel = int(random.random()*89)+1

        lotto_lista.append(vel)
        i += 1
    return lotto_lista

def kiir(lista,szeparator):
    lista_v=''
    i=0
    while i<len(lista):
        if lista[i] != lista[-1]:
            a=(str(lista[i])+szeparator)
            lista_v+=a
        else: lista_v+=str(lista[i])
        i+=1
    return [lista_v]

def kiir2(lista,szeparator):
    lista_v=[]
    i=0
    while i<len(lista):
        if lista[i] != lista[-1]:
            a=(str(lista[i])+szeparator)
            lista_v.append(a)
        else: lista_v.append(lista[i])
        i+=1
    return lista_v

def egyjegyu(nyero_szamok):
    i=0
    e_szam=0
    while i  <len(nyero_szamok):
        if ( nyero_szamok[i] / 10 ) < 1:
         e_szam +=1
        i+=1
    return e_szam

def konzol_kiir(feladat,kiirando):
    return print(f"{feladat} feladat, eredménye a következő : {kiirando}")


def file_kiir(kiiratando):
    f = open('szamok.txt', "w", encoding='utf8')
    f.write(str(kiiratando))
    f.close()