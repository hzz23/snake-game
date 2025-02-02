class Game:
    def __init__(self):
        self.snake = None
        self.food = None
        self.score = 0
        self.is_running = True

    def run(self):
        while self.is_running:
            self.handle_input()
            self.update()
            self.draw()
            self.check_collision()

    def handle_input(self):
        pass  # 处理用户输入

    def update(self):
        pass  # 更新游戏状态

    def draw(self):
        pass  # 绘制游戏元素

    def check_collision(self):
        pass  # 检查碰撞