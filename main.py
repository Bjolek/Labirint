import pygame
import CharacterAll
import Enemy
import GoldEnemy
from Wall import wall

pygame.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()


fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon,(800, 500))

pacman = CharacterAll.Character(250, 350,50,50,5,"hero.png")

enemy = Enemy.Enemy(250, 350,50,50,1,"cyborg.png", 100, 200, 300, 300)

gold = GoldEnemy.Gold(50, 50, 75,  75, "treasure.png")

game = True

walls = []
walls.append(wall(220, 40, 100, 20,(255, 255, 0)))
walls.append(wall(247, 48, 5, 100, (255, 255, 0)))


while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pacman.move()
    enemy.move()
    window.fill((0,153,0))
    window.blit(fon,(0,0))
    pacman.render(window)
    enemy.render(window)
    gold.render(window)
    for Wall in walls:
        Wall.render(window)
    pygame.display.flip()
    fps.tick(60)