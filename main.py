import pygame
import CharacterAll
import Enemy

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()


fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon,(800, 500))

pacman = CharacterAll.Character(250, 350,50,50,5,"hero.png")

enemy = Enemy.Enemy(350, 350,50,50,1,"cyborg.png", 100, 200, 300, 300)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pacman.move()
    enemy.move()
    window.fill((0,153,0))
    window.blit(fon,(0,0))
    pacman.render(window)
    enemy.render(window)
    pygame.display.flip()
    fps.tick(60)