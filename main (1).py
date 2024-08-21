

import random

class Hayvan:
    def __init__(self, x, y, cinsiyet):
        self.x = x
        self.y = y
        self.cinsiyet = cinsiyet

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.x = max(0, min(self.x, 499))
        self.y = max(0, min(self.y, 499))

    def distance_to(self, diger_hayvan):
        return ((self.x - diger_hayvan.x) ** 2 + (self.y - diger_hayvan.y) ** 2) ** 0.5

class Koyun(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 2

class İnek(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 2

class TavukHoroz(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 1

class Kurt(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 3

class Aslan(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 4

class Avci(Hayvan):
    def __init__(self, x, y, cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.value = 1

def Hayvan_olustur():
    hayvanlar = []

    for _ in range(15):
        hayvanlar.append(Koyun(random.randint(0, 499), random.randint(0, 499), "erkek"))
        hayvanlar.append(Koyun(random.randint(0, 499), random.randint(0, 499), "disi"))

    for _ in range(5):
        hayvanlar.append(İnek(random.randint(0, 499), random.randint(0, 499), "erkek"))
        hayvanlar.append(İnek(random.randint(0, 499), random.randint(0, 499), "disi"))

    for _ in range(10):
        hayvanlar.append(TavukHoroz(random.randint(0, 499), random.randint(0, 499), "erkek"))
        hayvanlar.append(TavukHoroz(random.randint(0, 499), random.randint(0, 499), "disi"))

    for _ in range(5):
        hayvanlar.append(Kurt(random.randint(0, 499), random.randint(0, 499), "erkek"))
        hayvanlar.append(Kurt(random.randint(0, 499), random.randint(0, 499), "disi"))

    for _ in range(4):
        hayvanlar.append(Aslan(random.randint(0, 499), random.randint(0, 499), "erkek"))
        hayvanlar.append(Aslan(random.randint(0, 499), random.randint(0, 499), "disi"))

    hayvanlar.append(Avci(random.randint(0, 499), random.randint(0, 499), "erkek"))

    return hayvanlar

def main():
    hayvanlar = Hayvan_olustur()

    for _ in range(1000):
        for hayvan in hayvanlar:
            hayvan.move()

        for hayvan in hayvanlar:
            if isinstance(hayvan, Kurt):
                for diger_hayvan in hayvanlar:
                    if isinstance(diger_hayvan, (Koyun, TavukHoroz)) and hayvan.distance_to(diger_hayvan) <= 4:
                        hayvanlar.remove(diger_hayvan)
            elif isinstance(hayvan, Aslan):
                for diger_hayvan in hayvanlar:
                    if isinstance(diger_hayvan, (İnek, Koyun)) and hayvan.distance_to(diger_hayvan) <= 5:
                        hayvanlar.remove(diger_hayvan)
            elif isinstance(hayvan, Avci):
                for diger_hayvan in hayvanlar:
                    if hayvan.distance_to(diger_hayvan) <= 8 and not isinstance(diger_hayvan, Avci):
                        hayvanlar.remove(diger_hayvan)

    Koyunlar = sum(1 for hayvan in hayvanlar if isinstance(hayvan, Koyun))
    İnekler = sum(1 for hayvan in hayvanlar if isinstance(hayvan, İnek))
    TavukHorozlar = sum(1 for hayvan in hayvanlar if isinstance(hayvan, TavukHoroz))
    Kurtlar = sum(1 for hayvan in hayvanlar if isinstance(hayvan, Kurt))
    Aslanlar = sum(1 for hayvan in hayvanlar if isinstance(hayvan, Aslan))
    TekAvci = sum(1 for hayvan in hayvanlar if isinstance(hayvan, Avci))

    print("Toplam koyun sayisi:", Koyunlar)
    print("Toplam inek sayisi:", İnekler)
    print("Toplam tavukHoroz sayisi:", TavukHorozlar)
    print("Toplam kurt sayisi:", Kurtlar)
    print("Toplam aslan sayisi:", Aslanlar)
    print("Toplam avci sayisi:", TekAvci)

if __name__ == "__main__":
    main()
