from abc import ABC, abstractmethod

# abstract base animal class


class Animal(ABC):
    feed_state = 'hungry'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def collect(self):
        pass

# animals inheritance    
    

class Goose(Animal):
    eggs_state = 'full'
    voice_type = 'га-га-га'

    def feed(self):
        self.feed_state = 'full'
        print('Goose {} now is full'.format(self.name))

    def collect(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} goose'.format(self.name))

    def voice(self):
        print(self.voice_type)


class Cow(Animal):
    milk_state = 'full'
    voice_type = 'мууу'

    def feed(self):
        self.feed_state = 'full'
        print('Cow {} now is full'.format(self.name))

    def collect(self):
        self.milk_state = 'empty'
        print('Cow {} was milked'.format(self.name))

    def voice(self):
        print(self.voice_type)


class Sheep(Animal):
    wool_state = 'full'
    voice_type = 'бееее'

    def feed(self):
        self.feed_state = 'full'
        print('Sheep {} now is full'.format(self.name))

    def collect(self):
        self.wool_state = 'empty'
        print('Sheep {} was sheared'.format(self.name))

    def voice(self):
        print(self.voice_type)


class Chicken(Animal):
    eggs_state = 'full'
    voice_type = 'ко-ко-ко'

    def feed(self):
        self.feed_state = 'full'
        print('Chicken {} now is full'.format(self.name))

    def collect(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} chicken'.format(self.name))

    def voice(self):
        print(self.voice_type)


class Goat(Animal):
    milk_state = 'full'
    voice_type = 'мееее'

    def feed(self):
        self.feed_state = 'full'
        print('Goat {} now is full'.format(self.name))

    def collect(self):
        self.milk_state = 'empty'
        print('Goat {} was milked'.format(self.name))

    def voice(self):
        print(self.voice_type)


class Duck(Animal):
    eggs_state = 'full'
    voice_type = 'кря-кря'

    def feed(self):
        self.feed_state = 'full'
        print('Duck {} now is full'.format(self.name))

    def collect(self):
        self.eggs_state = 'empty'
        print('Eggs were collected from {} duck'.format(self.name))

    def voice(self):
        print(self.voice_type)

# animal instances


grey_goose = Goose('Серый', 12)
white_goose = Goose('Белый', 14)
cow = Cow('Манька', 104)
rammy_sheep = Sheep('Барашек', 52)
cyrly_sheep = Sheep('Кудрявый', 56)
coco_chicken = Chicken('Ко-ко', 10)
kukareku_chicken = Chicken('Кукареку', 9)
goat_horns = Goat('Рога', 47)
goat_hoofs = Goat('Копыта', 43)
mallard_duck = Duck('Кряква', 16)


# animals list

animal_list = [
    grey_goose,
    white_goose,
    cow,
    rammy_sheep,
    cyrly_sheep,
    coco_chicken,
    kukareku_chicken,
    goat_horns,
    goat_hoofs,
    mallard_duck
]


# feed all animals

for animal in animal_list:
    animal.feed()

# collect something from each animal

for animal in animal_list:
    animal.collect()


# total animals weight
total_animals_weight = sum(animal.weight for animal in animal_list)
print('Total animals weight is {}'.format(total_animals_weight))

# the heaviest animal
heaviest_animal_name = max(animal_list, key=lambda animal: animal.weight)
print('The heaviest animal is {}'.format(heaviest_animal_name.name))
