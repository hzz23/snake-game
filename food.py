class Food:
    def __init__(self, width, height):
        self.position = self.spawn(width, height)

    def spawn(self, width, height):
        import random
        x = random.randint(0, (width // 10) - 1) * 10
        y = random.randint(0, (height // 10) - 1) * 10
        return (x, y)