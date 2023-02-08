import datetime

#marka=""
#evjarat=0

def beker():
  marka= input('Kérem adja meg az autó márkáját:')
  evjarat=int(input('Kérema daja meg az auto gyártási évét: '))
  return [marka,evjarat]



def kiir(marka,evjarat):
  today = datetime.date.today()
  year=today.year
  if evjarat==year:
    if year<evjarat:
      return print(f"Ez a/az {marka}, friss gyártás")
  elif evjarat<2000:
    return print(f"Ez a/az {marka}, öreg autó")
  elif evjarat<2000<year:
    return print(f"Ez a/az {marka}, átlagos korú")
  else:
    return print(f"A megadott adatot nem felel meg a kritériumnak")