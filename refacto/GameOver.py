import pygame


pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))


background = pygame.image.load("./assets/bg.webp").convert()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (230, 126, 34)

def Restart():
    # Définition des polices
    title_font = pygame.font.SysFont(None, 72)
    button_font = pygame.font.Font(None, 32)
    screen.blit(background, (0, 0))
    title_text = title_font.render("Game Over", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 125))
    screen.blit(title_text, title_rect)
    quit_button_rect = pygame.Rect(0, 0, 200, 50)
    quit_button_rect.center = (screen_width // 2, screen_height // 2 + 70)
    quit_text = button_font.render("Quitter", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
    pygame.draw.rect(screen, GREEN, quit_button_rect, border_radius=10)
    screen.blit(quit_text, quit_text_rect)
    pygame.display.flip()