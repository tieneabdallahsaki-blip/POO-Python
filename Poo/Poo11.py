class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimetre(self):
        return 2 * (self.width + self.length)

    def surface(self):
        return self.width * self.length

    def afficher(self):
        print(f"Perimetre = {self.perimetre()}")
        print(f"Surface = {self.surface()}")

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

rec = Rectangle(8, 3)
rec.afficher()