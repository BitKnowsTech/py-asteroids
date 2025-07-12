import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    print("Starting Asteroids!")
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0,0,0))
        #begin drawing

        updateable.update(dt)
        
        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                return
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
        
        for d in drawable:
            d.draw(screen)
        
        #end drawing
        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000


if __name__ == "__main__":
    main()
