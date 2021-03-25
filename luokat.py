# Tässä modulissa määritellään luokat painonhallintasovellukseen

# Modulien ja kirjastojen lataukset
import laskenta

# Henkilö-luokka

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, sukunimi, etunimi, pituus, paino, ika, sukupuoli):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        #bmi = self.paino / (self.pituus / 100) ** 2
        bmi = laskenta.bmi(self.paino, self.pituus)
        print("Painoindeksisi on", bmi)



class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii 
    Henkilo-luokan ominaisuudet ja metodit"""
    def __init__(self, sukunimi, etunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(sukunimi, etunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino

    def rasvaprosentti(self):
        bmi = laskenta.bmi(self.paino, self.pituus)
        rasvaprosentti = laskenta.rasvaprosentti(bmi, self.ika, self.sukupuoli)
        return rasvaprosentti


class Lapsi(Henkilo):
    """Aliluokka lapselle, perii 
    Henkilo-luokan ominaisuudet ja metodit"""
    def __init__(self, sukunimi, etunimi, pituus, paino, ika, sukupuoli):
        super().__init__(sukunimi, etunimi, pituus, paino, ika, sukupuoli)

    def rasvaprosentti(self):
        bmi = laskenta.bmi(self.paino, self.pituus)
        rasvaprosentti = laskenta.rasvaprosentti(bmi, self.ika, self.sukupuoli)
        return rasvaprosentti


if __name__ == "__main__":
    jormaW = Henkilo("Wuorio", "Jorma", 185, 98, 35, 1)
    #print("Paino", jormaW.paino)
    #jormaW.painoindeksi()

    jormaW2 = Aikuinen("Wuorio", "Jorma", 185, 98, 35, 1, 85)
    print("Painoindeksi on", jormaW2.etunimi)
    print("Jorman rasvaprosentti on", round(jormaW2.rasvaprosentti(), 2))
