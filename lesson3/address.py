class Address:
    def __init__(self, index, city, street, home, flour):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flour = flour

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.home} - {self.flour}"