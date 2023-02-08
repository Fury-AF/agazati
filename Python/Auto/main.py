import bevezetes as bv
import sorozat as s
import beolvas as b
#bv.beker()
#eredmeny=bv.beker()
#bv.kiir(eredmeny[0],eredmeny[1])
nyero_szamok=s.lottoszamok(5)
#print(nyero_szamok)
#print(s.kiir2(nyero_szamok,'-'))
#eredm=s.kiir(nyero_szamok,';')
#print(nyero_szamok)
#print(eredm)
#print(f" A nyerő számok elválasztva:\n \t {s.kiir(nyero_szamok,';')}")
#print(f"Az egyjegyűek száma: \n \t{s.egyjegyu(nyero_szamok)}")
#s.konzol_kiir('E',s.egyjegyu(nyero_szamok))
#s.file_kiir(s.egyjegyu(nyero_szamok))
b.beolvas('auto.txt')
b.flott()
b.legfiatalab_auto()
