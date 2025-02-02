def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def load_image(file_path):
    import pygame
    image = pygame.image.load(file_path)
    return image.convert_alpha()