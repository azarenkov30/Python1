class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.material()
        self.sew()
        self.coloring()

    def material(self):
        print('Закупка сырья')

    def sew(self):
        print('Пошив')

    def coloring(self):
        print('Окраска')

class Animal(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'Животное'

class Animation(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'Мультперсонаж'

class Create:
    def creating(self, name, color, type):
        if type == 'Животное':
            return Animal(name, color)
        elif type == 'Мультперсонаж':
            return Animation(name, color)

create = Create()
toy = create.creating('Чебурашка', 'Коричневый', 'Мультперсонаж')