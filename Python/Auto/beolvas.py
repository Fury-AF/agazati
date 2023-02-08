from autom import Auto
autok_lista=[]
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
        sor=sorok[i].strip().split("$")
        #print(sor)
        "példányosítjuk az osztály "
        auto=Auto(sor)
        autok_lista.append(auto)
        i += 1

def flott():
    return print(len(autok_lista))

def legfiatalab_auto():
        i = 0  # ciklusváltozó
        min_ertek = autok_lista[0].gyartasi_dt  # gyűjtóváltozó
        min_hely = 0
        while i < len(autok_lista):
            if (autok_lista[i].gyartasi_dt < min_ertek):
                min_ertek = autok_lista[i].gyartasi_dt
                min_hely = i

            # elágazás vége
            i += 1  # ciklusváltozó értékét növelem
        return print(f"A legöregebb autó: {autok_lista[min_hely].marka}, ({autok_lista[min_hely].gyartasi_dt})")