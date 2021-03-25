class SaaAsema:
    def __init__(self, nimi, tyyppi, sijainti):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.sijainti = sijainti 

class SaaHavainto:
    def __init__(self, paivamaara: str, lampotila, tnopeus, tsuunta, pilvisyys, nakyvyys):
        self.paivamaara = paivamaara
        self.lampotila = str(lampotila) + "c"
        self.tnopeus = tnopeus
        self.tsuunta = tsuunta
        self.pilvisyys = pilvisyys
        self.nakyvyys = nakyvyys

    def mmh(self):
        mailit = self.tnopeus * 0.62
        return mailit

    def mphkm(self):
        kilometrit = self.tnopeus * 1.60934
        return str(kilometrit) + "km/h"
    
    def solmutkm(self):
        kilometrit = self.tnopeus * 1.852
        return str(kilometrit) + "km/h"

    def mskmh(self):
        kilometrit = self.tnopeus * 3.6
        return str(kilometrit) + "km/h"


plimplom = SaaAsema("Plimplom", "Rannikkoasema", "Chicago")
plopplop = SaaAsema("Plopplop", "Lentokenttä", "New York")

fasfas = SaaHavainto("23.03", 25, 120, 320, 3/8, 2)

print("Säähavainto ilmeni", fasfas.paivamaara + ", lämpötila oli", fasfas.lampotila, "\nTuulennopeus oli tuolloin", str(fasfas.tnopeus) + "m/s ja suunta", fasfas.tsuunta, "astetta")
print(str(fasfas.tnopeus) + "m/s kilometreinä on", fasfas.mskmh() + ". Pilvisyys oli", fasfas.pilvisyys, "ja näkyvyys", fasfas.nakyvyys)

print(fasfas.mphkm())
print(fasfas.solmutkm())