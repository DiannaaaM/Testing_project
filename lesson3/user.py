class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'

    def __str__(self):
        return self.full_name

    def ret_first_name(self):
        return self.first_name

    def ret_last_name(self):
        return self.last_name
