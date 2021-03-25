# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import laskenta
import kysymys
import luokat

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
lista = []
while True:

    etunimi = input("Etunimi:")
    sukunimi = input("Sukunimi:")
    paino = kysymys.kysy_liukuluku('Paino (kg):', 30, 350)
    pituus = kysymys.kysy_liukuluku('Pituus (cm):', 100, 300)
    ika = kysymys.kysy_liukuluku('Ikä (v):' , 3, 125)
    sukupuoli = kysymys.kysy_liukuluku('Sukupuoli (Nainen 0, mies 1):' , 0, 1)
    
    if ika > 18:
        tavoitepaino = kysymys.kysy_liukuluku('Tavoitepaino (kg):' , 30, 350)
        aikuinen = luokat.Aikuinen(sukunimi, etunimi, pituus, paino, ika, sukupuoli, tavoitepaino)
        lista.append(aikuinen)
    
    else:
        lapsi = luokat.Lapsi(sukunimi, etunimi, pituus, paino, ika, sukupuoli)
        lista.append(lapsi)
    
    '''# Lasketaan ja tulostetaan painoindeksi
    bmi = laskenta.bmi(paino, pituus) 
    print('Henkilön painoindeksi on:', round(bmi, 1))

    # Lasketaan ja tulostetaan kehon rasvaprosentti
    rasvaprosentti = laskenta.rasvaprosentti(bmi, ika, sukupuoli)
    print('Laskennallinen kehon rasvaprosentti on:', round(rasvaprosentti, 1))'''

    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e)')
    if uusi.upper() == 'E':
        print("listan ensimmäinen henkilö:", lista[0].etunimi, ", listan viiminen henkilö:", lista[len(lista)-1].etunimi)
        break