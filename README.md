Generování souřadnic

    soubor: souradnice_skolky_DE_Sasko.py
    
    vstup: skolky_DE_Sasko_T3.csv (soubory T3 až T15, tzn. postupně celkem 13 souborů)
    
    výstup: DE_Sasko_T3_povedene_MS.csv, DE_Sasko_T3_nepovedene.csv (soubory T3 až T15, celkem 26 souborů)
		
Sloučení povedených

    soubor: slouceni_povedenych.py
    
    vstup: DE_Sasko_T3_povedene_MS.csv - soubory T3-T15, celkem 12 souborů
    
    výstup: DE_Sasko_souradnice.py

		
Sloučení nepovedených

    soubor: slouceni_nepovedenych.py

    vstup: DE_Sasko_T3_nepovedene.csv - soubory T3-T15, celkem 12 souborů

    výstup: DE_Sasko_nepovedene_MS.csv

Přečištění nepovedených

    soubor: Sasko_radky.py
    
    vstup: DE_Sasko_nepovedene_MS.csv
    
    výstup: Sasko.csv

Souřadnice z gpsvisualizer.com

    soubor: Sasko_sloupce.py
    
    vstup: Sasko_geo.csv
    
    výstup: DE_Sasko_souradnice_MS_hotovo.csv
