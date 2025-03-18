class Smartphone:
    def __init__(self, mark, model, user_number):
        self.mark = mark
        self.model = model
        self.user_number = user_number

    def __str__(self):
        return f'{self.mark} - {self.model}. {self.user_number}'
