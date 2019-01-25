# animal classes
class Animal:
    feed_state = 'hungry'

    def __init__(self, name, voice_type, weight):
        self.name = name
        self.voice_type = voice_type
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def feed(self):
        self.feed_state = 'full'
        return '{} is feeded'.format(self.name)

    def voice(self):
        print(self.voice_type)


class Goose(Animal):
    eggs_state = 'full'

    def collect_eggs(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} goose'.format(self.name))


class Cow(Animal):
    milk_state = 'full'

    def milking(self):
        self.milk_state = 'empty'
        print('Cow {} was milked'.format(self.name))


class Sheep(Animal):
    wool_state = 'full'

    def shear(self):
        self.wool_state = 'empty'
        print('Sheep {} was sheared'.format(self.name))


class Chicken(Animal):
    eggs_state = 'full'

    def collect_eggs(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} chicken'.format(self.name))


class Goat(Animal):
    milk_state = 'full'

    def milking(self):
        self.milk_state = 'empty'
        print('Goat {} was milked'.format(self.name))


class Duck(Animal):
    eggs_state = 'full'

    def collect_eggs(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} duck'.format(self.name))

# animal instances


grey_goose = Goose('Серый', 'га-га-га', 12)
white_goose = Goose('Белый', 'га-га-га', 14)
cow = Cow('Манька', 'мууу', 104)
rammy_sheep = Sheep('Барашек', 'бееее', 52)
cyrly_sheep = Sheep('Кудрявый', 'бееее', 56)
goat_horns = Goat('Рога', 'мееее', 47)
goat_hoofs = Goat('Копыта', 'мееее', 43)
mallard_duck = Duck('Кряква', 'кря-кря', 16)


# feed all animals

all_animals = [grey_goose, white_goose, cow, rammy_sheep, cyrly_sheep, goat_horns, goat_hoofs, mallard_duck]

for animal in all_animals:
    print(animal.feed())

# some action with each animal

grey_goose.collect_eggs()
white_goose.collect_eggs()
cow.milking()
rammy_sheep.shear()
cyrly_sheep.shear()
goat_horns.milking()
goat_hoofs.milking()
mallard_duck.collect_eggs()

# total animals weight


def get_total_animals_weight():

    total_weight = 0

    for animal in all_animals:
        total_weight += animal.weight

    return total_weight


print('Total animals weight is {}'.format(get_total_animals_weight()))

# the heaviest animal


def get_heaviest_animal_name():
    heaviest_animal = all_animals[0]

    for animal_inst in all_animals:
        if heaviest_animal < animal_inst:
            heaviest_animal = animal_inst

    return heaviest_animal.name


print('The heaviest animal is {}'.format(get_heaviest_animal_name()))
