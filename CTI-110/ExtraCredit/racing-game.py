import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 200:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH - 200:
            self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200, SCREEN_WIDTH - 250)
        self.rect.y = -50
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def draw_road():
    # Road background
    pygame.draw.rect(SCREEN, GRAY, (200, 0, SCREEN_WIDTH - 400, SCREEN_HEIGHT))
    
    # Road borders
    pygame.draw.line(SCREEN, WHITE, (200, 0), (200, SCREEN_HEIGHT), 5)
    pygame.draw.line(SCREEN, WHITE, (SCREEN_WIDTH - 200, 0), (SCREEN_WIDTH - 200, SCREEN_HEIGHT), 5)
    
    # Road center line
    for y in range(0, SCREEN_HEIGHT, 100):
        pygame.draw.line(SCREEN, WHITE, (SCREEN_WIDTH // 2, y), (SCREEN_WIDTH // 2, y + 50), 5)

def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    player = Car()
    all_sprites.add(player)

    # Game variables
    score = 0
    spawn_timer = 0
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer > 60:  # Adjust for difficulty
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacles.add(obstacle)
            spawn_timer = 0

        # Update
        all_sprites.update()

        # Collision detection
        hits = pygame.sprite.spritecollide(player, obstacles, False)
        if hits:
            running = False

        # Increment score
        score += 1

        # Draw
        SCREEN.fill(GREEN)  # Background color
        draw_road()
        all_sprites.draw(SCREEN)

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(score_text, (10, 10))

        # Refresh display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    # Game over screen
    SCREEN.fill(BLACK)
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    SCREEN.blit(game_over_text, text_rect)
    pygame.display.flip()

    # Wait before closing
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == "__main__":
    main()
