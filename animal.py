class Animal(object):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def prnt(self):
        return f"{self.species} на ім'я {self.name}, вік {self.age} років."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed

    def __str__(self):
        return f"Собака породи {self.breed} на ім'я {self.name}, вік {self.age} років."

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Кіт")
        self.breed = breed

    def __str__(self):
        return f"Кіт породи {self.breed} на ім'я {self.name}, вік {self.age} років."

dog = Dog("Боб", 12, "Бульдог")
cat = Cat("Мурчик", 7, "Немає")

print(cat)
print(dog)
