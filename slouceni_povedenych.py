# otevření souboru T3
with open('DE_Sasko_T3_povedene_MS.csv', encoding='utf-8') as vstup:
    T3 = vstup.readlines()

# otevření souboru T4
with open('DE_Sasko_T4_povedene_MS.csv', encoding='utf-8') as vstup:
    T4 = vstup.readlines()

# otevření souboru T5
with open('DE_Sasko_T5_povedene_MS.csv', encoding='utf-8') as vstup:
    T5 = vstup.readlines()

# otevření souboru T6
with open('DE_Sasko_T6_povedene_MS.csv', encoding='utf-8') as vstup:
    T6 = vstup.readlines()

# otevření souboru T7
with open('DE_Sasko_T7_povedene_MS.csv', encoding='utf-8') as vstup:
    T7 = vstup.readlines()

# otevření souboru T8
with open('DE_Sasko_T8_povedene_MS.csv', encoding='utf-8') as vstup:
    T8 = vstup.readlines()

# otevření souboru T9
with open('DE_Sasko_T9_povedene_MS.csv', encoding='utf-8') as vstup:
    T9 = vstup.readlines()

# otevření souboru T10
with open('DE_Sasko_T10_povedene_MS.csv', encoding='utf-8') as vstup:
    T10 = vstup.readlines()

# otevření souboru T11
with open('DE_Sasko_T11_povedene_MS.csv', encoding='utf-8') as vstup:
    T11 = vstup.readlines()

# otevření souboru T12
with open('DE_Sasko_T12_povedene_MS.csv', encoding='utf-8') as vstup:
    T12 = vstup.readlines()

# otevření souboru T13
with open('DE_Sasko_T13_povedene_MS.csv', encoding='utf-8') as vstup:
    T13 = vstup.readlines()

# otevření souboru T14
with open('DE_Sasko_T14_povedene_MS.csv', encoding='utf-8') as vstup:
    T14 = vstup.readlines()

# otevření souboru T15
with open('DE_Sasko_T15_povedene_MS.csv', encoding='utf-8') as vstup:
    T15 = vstup.readlines()

vse = T3 + T4[1:] + T5[1:] + T6[1:] + T7[1:] + T8[1:] + T9[1:] + T10[1:] + T11[1:] + T12[1:] + T13[1:] + T14[1:] + T15[1:]

# uložení do souboru
with open('DE_Sasko_souradnice_MS.csv', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(vse)