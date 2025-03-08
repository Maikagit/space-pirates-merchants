#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Space Pirates and Merchants
Un jeu 2D de vaisseaux spatiaux où les joueurs peuvent être pirates ou marchands.
"""

import os
import sys
import pygame

# Initialiser Pygame
pygame.init()
pygame.mixer.init()  # Pour le son
pygame.font.init()  # Pour le texte

# Constantes
TITLE = "Space Pirates and Merchants"
WIDTH, HEIGHT = 1200, 800
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Fonction pour charger les assets
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join('assets', 'images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print(f"Impossible de charger l'image: {name}")
        raise SystemExit(message)
    
    image = image.convert_alpha()
    if scale != 1:
        image_size = image.get_size()
        image = pygame.transform.scale(image, (int(image_size[0] * scale), int(image_size[1] * scale)))
    
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    
    return image, image.get_rect()

# Classes de base (à déplacer dans des modules séparés plus tard)
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file):
        super().__init__()
        try:
            self.image, self.rect = load_image(image_file)
        except:
            # Image temporaire si l'asset n'est pas disponible
            self.image = pygame.Surface((50, 30))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
        
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0
        self.speedy = 0
        self.rotation = 0
        self.rotation_speed = 3
        self.acceleration = 0.2
        self.max_speed = 5
        self.original_image = self.image.copy()
    
    def update(self):
        # Mettre à jour la rotation
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Mettre à jour la position
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Empêcher de sortir de l'écran
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def rotate(self, direction):
        self.rotation += direction * self.rotation_speed
        self.rotation %= 360
    
    def accelerate(self):
        # Calculer l'accélération en fonction de l'angle
        angle_rad = pygame.math.Vector2(1, 0).rotate(-self.rotation).normalize()
        self.speedx += angle_rad.x * self.acceleration
        self.speedy += angle_rad.y * self.acceleration
        
        # Limiter la vitesse maximale
        speed = pygame.math.Vector2(self.speedx, self.speedy).length()
        if speed > self.max_speed:
            scale = self.max_speed / speed
            self.speedx *= scale
            self.speedy *= scale
    
    def decelerate(self):
        # Réduire progressivement la vitesse
        if abs(self.speedx) > 0.1:
            self.speedx *= 0.95
        else:
            self.speedx = 0
        
        if abs(self.speedy) > 0.1:
            self.speedy *= 0.95
        else:
            self.speedy = 0

class PlayerShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y, "player_ship.png")
        self.shoot_delay = 250  # Délai entre les tirs en millisecondes
        self.last_shot = pygame.time.get_ticks()
        self.health = 100
        self.money = 1000
        self.cargo = {}
        self.cargo_capacity = 10
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            # Créer un projectile (sera implémenté plus tard)
            return True
        return False

# Classe principale du jeu
class Game:
    def __init__(self):
        self.running = True
        self.game_over = False
        self.paused = False
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        
        # Créer le joueur
        self.player = PlayerShip(WIDTH // 2, HEIGHT // 2)
        self.all_sprites.add(self.player)
        self.players.add(self.player)
        
        # État du jeu
        self.score = 0
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
        
        # Contrôles continus
        if not self.paused and not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                self.player.rotate(1)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.rotate(-1)
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                self.player.accelerate()
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.decelerate()
    
    def update(self):
        if not self.paused and not self.game_over:
            self.all_sprites.update()
            
            # Vérifier les collisions (à implémenter plus tard)
    
    def draw(self):
        # Dessiner le fond
        screen.fill(BLACK)
        
        # Dessiner les étoiles (à implémenter plus tard)
        
        # Dessiner tous les sprites
        self.all_sprites.draw(screen)
        
        # Afficher le score, la santé, etc.
        self.draw_hud()
        
        # Afficher les écrans de pause ou de game over
        if self.paused:
            self.draw_pause_screen()
        elif self.game_over:
            self.draw_game_over_screen()
        
        # Mettre à jour l'affichage
        pygame.display.flip()
    
    def draw_hud(self):
        # À implémenter plus tard
        font = pygame.font.SysFont('Arial', 24)
        health_text = font.render(f"Santé: {self.player.health}", True, WHITE)
        money_text = font.render(f"Crédits: {self.player.money}", True, WHITE)
        
        screen.blit(health_text, (10, 10))
        screen.blit(money_text, (10, 40))
    
    def draw_pause_screen(self):
        # À implémenter plus tard
        font = pygame.font.SysFont('Arial', 48)
        text = font.render("PAUSE", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    
    def draw_game_over_screen(self):
        # À implémenter plus tard
        font = pygame.font.SysFont('Arial', 48)
        text = font.render("GAME OVER", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    
    def run(self):
        while self.running:
            clock.tick(FPS)
            self.process_events()
            self.update()
            self.draw()

# Point d'entrée principal
if __name__ == "__main__":
    # Démarrer le jeu
    game = Game()
    game.run()
    
    # Quitter proprement
    pygame.quit()
    sys.exit()
