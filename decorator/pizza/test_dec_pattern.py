from abc import abstractmethod
from typing import Protocol


class Pizza(Protocol):
    description: str

    def get_dectiption(self) -> str: ...

    def cost(self) -> float: ...


class BasicPizza(Pizza):
    description: str = "Basic Pizza"

    def get_dectiption(self) -> str:
        return self.description

    def cost(self) -> float:
        return 5.0


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        self.pizza = pizza

    @abstractmethod
    def get_dectiption(self) -> str:
        raise NotImplementedError


class Cheese(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_dectiption(self):
        return self.pizza.get_dectiption() + ", Cheese"

    def cost(self) -> float:
        return self.pizza.cost() + 0.5


if __name__ == "__main__":
    piz: Pizza = BasicPizza()
    cheesePiz = Cheese(piz)
    print(cheesePiz.get_dectiption(), " COST: ", cheesePiz.cost())
