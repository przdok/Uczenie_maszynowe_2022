class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area}\nNumber of rooms: {self.rooms}\nPrice:\
             {self.price}\nAddress: {self.address}\n"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}Plot: {self.plot}\n\n"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}Floor number: {self.floor}\n\n"


H = House("24m2", 3, 100000, "Downing Street 4, 43-000 Katowice", 250)
F = Flat("24m2", 3, 100000, "Downing Street 4, 43-000 Katowice", 4)

print(H.__str__() + F.__str__())
