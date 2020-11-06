class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_name(self):
        name = str(self.value) + " de " + self.color

        if self.value == 11:
            name = "Valet de " + self.color
        elif self.value == 12:
            name = "Dame de " + self.color
        elif self.value == 13:
            name = "Roi de " + self.color
        elif self.value == 1:
            name = "As de " + self.color

        return name

    def get_value(self):
       return self.value

    def get_color(self):
        return self.color