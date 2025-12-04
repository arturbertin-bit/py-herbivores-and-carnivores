class Animal:
    alive = []

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden is False:
                herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
