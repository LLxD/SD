class Food:
    def __init__(self, name, time_to_be_prepared_in_minutes, client_name, quantity=1):
        plural = "s" if quantity > 1 else ""
        self.name = name + plural
        self.time_to_be_prepared_in_minutes = quantity * time_to_be_prepared_in_minutes
        self.client_name = client_name
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} {self.name} - {self.time_to_be_prepared_in_minutes} minutos - {self.client_name}"


class Sandwich(Food):
    def __init__(self, client_name, quantity):
        super().__init__("Sanduíche", 5, client_name, quantity)


class Drink(Food):
    def __init__(self, client_name, quantity):
        super().__init__("Bebida", 2, client_name, quantity)


class ReadyMeal(Food):
    def __init__(self, client_name, quantity):
        super().__init__("Prato Pronto", 15, client_name, quantity)


class Dessert(Food):
    def __init__(self, client_name, quantity):
        super().__init__("Sobremesa", 3, client_name, quantity)
