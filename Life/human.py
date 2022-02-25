class Human:
    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name, age=0, energy=100):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"{self.name} is {self.age} years old with {self.energy} energy."

    def eat(self, amount):
        potential_energy = self.energy + amount

        if potential_energy >= Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
            return potential_energy - Human.MAX_ENERGY
        else:
            self.energy = potential_energy
            return self.energy - Human.MAX_ENERGY

    def grow(self):
        self.age += 1

    def move(self, distance):
        potential_energy = self.energy - distance

        if potential_energy >= Human.MOVE_ENERGY:
            self.energy = potential_energy
            return True
        else:
            return False

    def reproduce(self):
        potential_energy = self.energy - Human.REPRODUCE_ENERGY

        if potential_energy >= Human.REPRODUCE_ENERGY:
            self.energy = potential_energy
            return True
        else:
            return False
