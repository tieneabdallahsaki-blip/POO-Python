class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_surface(self):
        self.x * self.y
        print(f"La surface est S = {(self.x * self.y)}")

R = Rectangle(9, 6)
R.calc_surface()