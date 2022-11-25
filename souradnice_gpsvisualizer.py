with open("Sasko_geo.csv", encoding = 'utf-8') as vstup:
   radky = vstup.readlines()

radky=[radek.split(';') for radek in radky]

latitude = [radek[0] for radek in radky]
longitude = [radek[1] for radek in radky]
nazev = [radek[2] for radek in radky]
adresa = [radek[3] for radek in radky]
kapacita = [radek[4] for radek in radky]

znak=0
Sasko_hotovo=[]

for radek in radky:
   Sasko_radek = nazev[znak]+";"+ adresa[znak]+";"+ kapacita[znak]+";;"+latitude[znak]+";"+ longitude[znak] +"\n"
   Sasko_hotovo.append(Sasko_radek)
   znak+=1

with open("DE_Sasko_souradnice_MS_hotovo.csv", mode = 'a', encoding = 'utf-8') as vystup:
   vystup.writelines(Sasko_hotovo)
