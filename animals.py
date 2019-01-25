class Animal:
    def __init__(self, name, voice_type):
        self.name = name
        self.voice_type = voice_type

    feed_state = 'hungry'

    def feed(self):
        self.feed_state = 'full'
        print('{} is feeded'.format(self.name))

    def voice(self):
        print(self.voice_type)

class Goose(Animal):
    def collect_eggs(self):
        print('Eggs were collected from {} goose'.format(self.name))


class Cow(Animal):
    def milking(self):
        print('Cow {} was milked'.format(self.name))


class Sheep(Animal):
    def shear(self):
        print('Sheep {} was sheared'.format(self.name))


class Chicken(Animal):
    def collect_eggs(self):
        print('Eggs were collected from {} chicken'.format(self.name))


class Goat(Animal):
    def milking(self):
        print('Goat {} was milked'.format(self.name))


class Duck(Animal):
    def collect_eggs(self):
        print('Eggs were collected from {} duck'.format(self.name))



grey_goose = Goose('Серый', 'га-га-га')
white_goose = Goose('Белый', 'га-га-га')
cow = Cow('Манька', 'мууу')
rammy_sheep = Sheep('Барашек', 'бееее')
cyrly_sheep = Sheep('Кудрявый', 'бееее')
goat_horns = Goat('Рога', 'мееее')
goat_hoofs = Goat('Копыта', 'мееее')
mallard_duck = Duck('Кряква', 'кря-кря')


# feed 













