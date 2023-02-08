class Film:
    def __init__(self, sor):
        "knosturktor"
        "beállítja a tulajdonságok alapértékeit" \
        "adattagok - osztályok változói"
        self.cim=sor[0]
        self.rendezo=sor[1]
        self.foszereplo=sor[2]
        self.ev=sor[3]
        self.perc=int(sor[4])

    def __str__(self):
        return f"{self.cim},{self.rendezo},{self.foszereplo},{self.ev},{self.perc}"