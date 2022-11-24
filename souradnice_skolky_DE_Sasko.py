# import modulu geopy
from geopy.geocoders import Nominatim

# načtení the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# otevření souboru
with open('skolky_DE_Sasko_T15.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# vytvoření seznamu z jednoho řádku
jeden_radek = [radek.split('\n') for radek in radky]

# proměnné pro ukládání 
povedene = []
nepovedene = []

# generování souřadnic - povedené se ukládají do jednoho souboru a nepovedené do jiného
for cast_radku in jeden_radek[3:]:
    try:
        # rozdělení řádku na jednotlivé údaje
        cast = cast_radku[0].split(";")
 
        # načtení adresy
        loc = cast[1]
 
        # making an instance of Nominatim class
        geolocator = Nominatim(user_agent="my_request")
 
        #applying geocode method to get the location
        location = geolocator.geocode(loc)
 
        # vypsání adresy a souřadnic (pouze pro kontrolu, že se generují)
        print(location.address)
        print(location.latitude, location.longitude)
        
        # uložení údajů do proměnné povedené
        data = ""
        for casti in cast:
            data+=casti +";"
        povedene.append(data + str(location.latitude) + ";" + str(location.longitude) + "\n")
    except Exception as chyba:
        # uložení údajů do proměnné nepovedené
        data = ""
        for casti in cast:
            data+=casti+";"    
        nepovedene.append(data+"\n")
        pass

# vložení hlavičky u povedených
hlavicka = "NAZEV" + ";" + "ADRESA" + ";" + "KAPACITA" + ";" + "STAT" + ";" + "LATITUDE" + ";" + "LONGITUDE" + "\n"
povedene.insert(0,hlavicka)
#print(povedene)

# uložení povedených do souboru
with open("DE_Sasko_T15_povedene_MS.csv", "w", encoding="utf-8") as vystup:
    vystup.writelines(povedene)

# uložení nepovedených do souboru
with open("DE_Sasko_T15_nepovedene.csv", "w", encoding="utf-8") as soubor:
    soubor.writelines(nepovedene)