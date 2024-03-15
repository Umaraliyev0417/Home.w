class Composer:
    count = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)
c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
print(Composer.count)
c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.count)
