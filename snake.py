class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # 初始方向向右

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()  # 移除尾部

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)  # 在尾部添加一个新的身体部分

    def reset(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # 重置方向为向右