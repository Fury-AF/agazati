
class Auto:
    def __init__(self, sor):
        "knosturktor"
        "beállítja a tulajdonságok alapértékeit" \
        "adattagok - osztályok változói"
        self.marka=sor[0]
        self.gyartasi_dt=sor[1]


    def __str__(self):
        return f"{self.marka},{self.gyartasi_dt}"