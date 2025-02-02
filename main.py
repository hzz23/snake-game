以下是文件 `/snake-game/snake-game/src/main.py` 的内容：

import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()