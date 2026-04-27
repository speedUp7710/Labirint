import math
import sys
import pygame

from classes.AnimSprite import AnimSprite
from classes.Enemy import Enemy
from classes.Maze import Maze
from classes.Player import Player

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('www/music/music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

sound_death = pygame.mixer.Sound('www/music/death1.mp3')
sound_death.set_volume(0.3)
SCREEN_W, SCREEN_H = 700, 500
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Лабиринт")

background = pygame.transform.scale(pygame.image.load("www/img/image.webp"), (SCREEN_W, SCREEN_H))

player = Player("www/img/player.png", 169, 256, anim_speed=0.04, speed=2)
player.change_size_factor(0.1)
player.reset()

coin = AnimSprite("www/img/coin.png", 36, 32, 1)
coin.rect.topleft = (55, 465)


enemy1 = Enemy('www/img/enemy.png', speed=3, start_pos=(618, 275), end_pos=(82, 275))
enemy2 = Enemy('www/img/enemy.png', speed=3, start_pos=(474, 421), end_pos=(474, 377))
enemy3 = Enemy('www/img/enemy.png', speed=3, start_pos=(175, 426), end_pos=(175, 377))

for enemy in [enemy1, enemy2, enemy3]:
    enemy.change_size(100, 50)

enemies = pygame.sprite.Group(enemy1, enemy2, enemy3) #Это проблема типизации PyCharm/VSCode. Pygame имеет устаревшие type hints. Бла бла бла, я все четка сделал, ошибку пишет, тк студия навичек, а я нет!11!


wall_img = pygame.image.load("www/img/wall_square.png")
maze = Maze(wall_img, size=50, screen_width=SCREEN_W, screen_height=SCREEN_H)

clock = pygame.time.Clock()
FPS = 60



while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event.pos)


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player.rect.top > 0:
        player.rect.y -= player.speed
    if keys[pygame.K_s] and player.rect.bottom < SCREEN_H:
        player.rect.y += player.speed
    if keys[pygame.K_a] and player.rect.left > 0:
        player.rect.x -= player.speed
        player.flip(True, False)
    if keys[pygame.K_d] and player.rect.right < SCREEN_W:
        player.rect.x += player.speed
        player.flip(False, False)

    #Обновление координат
    player.update()
    enemies.update()
    coin.update()


    if pygame.sprite.spritecollideany(player, enemies) or maze.collide(player):
        sound_death.play()
        player.reset()

    #Рисование blit-ами
    window.blit(background, (0, 0))
    window.blit(coin.image, coin.rect)
    maze.draw(window)
    window.blit(player.image, player.rect)
    enemies.draw(window)

    pygame.display.flip()


