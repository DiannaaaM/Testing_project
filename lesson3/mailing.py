from lesson3.address import Address


class Malling:
    def __init__(self, to_address: Address, from_address: Address, coast: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.coast = coast
        self.track = track

    def __str__(self):
        return f'Sending {self.track} from {self.from_address} in {self.to_address}. Coast is {self.coast} rub'