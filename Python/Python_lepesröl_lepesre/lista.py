import random
def listabejaras():
    # lista azonos típusú elemek halmaza, melyek adott sorrendben vannak
    # lista megadása:
    lista_nev = ["Éva", "Géza"]
    lista_szam = [1, 4, 3, 6]
    #Hivatkozás a lista elemeire az indexükkel lehet.
    # A számozás 0-tól kezdődik:
    print(lista_nev[1]) #Géza
    print(lista_szam[0]) #1
    #a lista hossza a benne lévő elemek száma
    print(len(lista_nev)) # 2, mert két elem van benne
    #lista elemeinek megváltoztatása:
    lista_nev[0] = "Juli"
    # listaelemek hozzáadása
    lista_nev.append("Elemér")


def lottoszamok():
    #generáljunk 5 lottószámot! [1,90]
    lotto_lista = [] # kezdetben üres a lista, itt fogom tárolni a lottószámokat
    i = 1 #ciklusváltozó
    while i <= 5:
        vel = int(random.random()*89)+1
        lotto_lista.append(vel) # véletlen szám hozzáadása a listához
        # lotto_lista.append(int(random.random()*89)+1)
        i += 1
    #ciklus vége

def megszamlalas():
    # Adott egy lista, hány páros szám van benne?
    lista = [ 12, 32, 45, 21, 34]
    i = 0  # ciklusváltozó
    db = 0  # gyűjtőváltozó
    while i < len(lista):
        if (lista[i] % 2 == 0):
            db += 1
        i += 1
    # ciklus vége
    print(f"A lista = [ 12, 32, 45, 21, 34] listában  {db} db páros szám van!")

def osszegzes():
    # Egy listában adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a számok összege a listában?
    lista = [12, 32, 45, 21, 34]
    i = 0 # ciklusváltozó
    ossz = 0 # gyűjtóváltozó
    while i < len(lista):
        ossz += lista[i] # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"lista = [12, 32, 45, 21, 34] számok összege: {ossz } ")


def maximumkivalasztas():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Hol van a legnagyobb szám, és mennyi az értéke?
    lista = [12, 32, 45, 21, 34]
    i = 0 # ciklusváltozó
    max_ertek = 0 # gyűjtóváltozó
    max_hely = 0
    while i < len(lista):
        if (lista[i] >max_ertek):
           max_ertek = lista[i]
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f" lista = [12, 32, 45, 21, 34] legnagyobb száma: {max_ertek }, a helye: {max_hely}")


def eldontes():
    # Adott egy lista, döntsük el, hogy van-e benne páros szám!
    lista = [12, 32, 45, 21, 34]
    i = 0  # ciklusváltozó
    while i < len(lista) and lista[i] % 2 == 1:  # fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    if (i < len(lista)):
        print(f"Van páros szám, az {i}. helyen.")
    else:
        print("Nincs páros szám!")


def nyert_e_lotto():
    # Adott 5 lottószám!
    lotto = [12, 32, 45, 21, 34]
    # Kérjünk be a felhasználótól egy tippet és
    # döntsük el, hogy benne van-e a lottószámok között?
    tipp = int(input("Kérek egy számot 1 és 90 között! "))
    i = 0  # ciklusváltozó
    while i < len(lotto) and lotto[i] != tipp:  # fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    if (i < len(lotto)):
        print(f"Nyert, az {i}. helyen.")
    else:
        print("Nem nyert!")

def hanytalalat_lotto():
    # Adott 5 lottószám!
    lotto = [12, 32, 45, 21, 34]
    # Kérjünk be a felhasználótól 5 tippet és
    # Hány találata lett a lottón?
    ## Tippek bekérése
    tipp = [] # itt tárolom a felhasználó tippjeit
    i = 0  # ciklusváltozó
    while i < 5:
        tipp.append(int(input(f"Kérem az {i+1}. számot 1 és 90 között! ")))
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    print(tipp)
    i = 0  # külső ciklusváltozó
    talalat_db = 0 # a találatok száma gyűjtőváltozoó
    while i < len(lotto):
        j = 0  # belső ciklusváltozó
        while j < len(tipp):
            if (tipp[j] == lotto [i]):
                talalat_db += 1
                print(tipp[j])
            #elágazás vége
            j += 1 # belső ciklusváltozó értékét növelem
        i += 1  # külső ciklusváltozó értékét növelem
    # ciklus vége

    print(f"A találatok száma: {talalat_db}")


def abetuk_szama():
    # A szövegek karakterekből álló listák. Az egyes betűkre az indexükkel tudunk hivatkozni.
    # Adott egy szöveg. Hány 'a' betű van a szövegben?
    szoveg = " Indul a kutya és a tyúk aludni!"
    i = 0
    a_db = 0
    while i < len(szoveg):
        if (szoveg[i] == 'a'):
            a_db += 1
        #elágazás vége
    #ciklus vége
    print(f"A {szoveg} - ben {a_db} 'a' betű van")

def megszamlalas_szoveg():
    # Adott egy lista, hány a betűvel kezdődő szó van benne?
    lista = ["alma", "béka" , "Anna", "nyak"]
    i = 0  # ciklusváltozó
    db = 0  # gyűjtőváltozó
    while i < len(lista):
        if (lista[i][0] == "a"):
            db += 1
        i += 1
    # ciklus vége
    print(f"A {lista} listában  {db} db a betűs szó van!")

def osszegzes_szoveg():
    # Egy listában adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a szavak összhossza?
    lista = ["alma", "béka", "Anna", "nyak"]
    i = 0 # ciklusváltozó
    ossz = 0 # gyűjtóváltozó
    while i < len(lista):
        ossz += len(lista[i]) # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"A {lista} lista összhossza:   {ossz} ")


def maximumkivalasztas_szoveg():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Mekkora a leghosszabb szöveg hossza?
    lista = ["alma-ata", "béka", "Anna", "nyak"]
    i = 0 # ciklusváltozó
    max_ertek = 0 # gyűjtóváltozó
    max_hely = 0
    while i < len(lista):
        if (len(lista[i]) >max_ertek):
           max_ertek = len(lista[i])
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f" {lista} leghosszabb szava: {lista[max_hely]}, hossza:  {max_ertek }, a helye: {max_hely}")
