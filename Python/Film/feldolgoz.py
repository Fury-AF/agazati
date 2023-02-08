from film import Film
filmek_lista=[]
def beolvas(fajnev):
    """Beolvassuk az adatokat a fő fájlból"""
    my_file = open(fajnev,"r",encoding='utf8')
    fejlec=my_file.readline().strip()
    sorok= my_file.readlines()
    #print(sorok)
    feldolgoz(sorok)
    my_file.close()


def feldolgoz(sorok):
    i=0
    while i<len(sorok):
        #print(sorok[i].strip())
        sor=sorok[i].strip().split(";")
        #print(sor)
        "példányosítjuk az osztály "
        film=Film(sor)
        filmek_lista.append(film)
        i += 1
    print(filmek_lista)
    print(filmek_lista[1].ev)


#3. Melyik a legrövidebb film címe?
def legrovidebb_film():
    i = 0  # ciklusváltozó
    min_ertek = filmek_lista[0].perc # gyűjtóváltozó
    min_hely = 0
    while i < len(filmek_lista):
        if (filmek_lista[i].perc < min_ertek):
            min_ertek = filmek_lista[i].perc
            min_hely =i

        # elágazás vége
        i += 1  # ciklusváltozó értékét növelem
    return filmek_lista[min_hely].cim



#4. Hány darab legalább 110 perces film van?

def filem_nagyobb_110():
    i = 0
    filmek_szam = 0
    while i < len(filmek_lista):
        if (110<filmek_lista[i].perc):
            filmek_szam += 1
        i += 1
    return filmek_szam

#5. Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből,
# ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű
# színész, akkor azt is tudasd!ž

def film_ajanlo():
    film_cime=[]
    szinesz_neve=input('Kérem adjon meg egy szinészt a kereséshez: ')
    i = 0
    while i < len(filmek_lista):
        if (filmek_lista[i].foszereplo == szinesz_neve):
            film_cime.append(filmek_lista[i].cim)
        i+=1
    if len(film_cime)<=0:
        return 'Nincs ilyen színésszel film '
    else:
        return film_cime

def fileba_iras(eredmeny):
    f=open('feleadat_kiir4',"w",encoding='utf8')
    f.write(str(eredmeny))
    f.close()