
with open("DE_Sasko_nepovedene_MS.csv", encoding = 'utf-8') as vstup:
   radky = vstup.readlines()

for radek in radky:
    if radek != ";,;;;\n":   
        with open("Sasko.csv", mode='a', encoding = 'utf-8') as vystup:
                vystup.writelines(radek)





