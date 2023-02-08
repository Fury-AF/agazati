import feldolgoz
import feldolgoz as f

f.beolvas('film.txt')
print('3. Feladat ')
print(f"\t A legrövidebb film: {feldolgoz.legrovidebb_film()} ")

print('4. Feladat ')
print(f"\t {feldolgoz.filem_nagyobb_110()} db 110 percnél hosszabb film van")

print('5. Feladat ')
print(f"\t A követekző filmeket tudjuk ajánlani a válaszott színésszel {feldolgoz.film_ajanlo()} ")

print('6. Feladat ')
print(f"\t Ki írtuk a 4-feladatot fájba {feldolgoz.fileba_iras()} ")