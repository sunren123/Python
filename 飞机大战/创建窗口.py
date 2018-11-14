import pygame
from plane_sprites import *

# from 飞机大战.plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480,700))

#绘制图像 1加载数据 2biit绘制图形 3 update更新
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

#制作英雄飞机
hero =pygame.image.load("./images/me1.png")

screen.blit(hero,(200,500))

#可以绘制之后，统一update
pygame.display.update()

#创建时钟
clock =pygame.time.Clock()
i =0

#英雄飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)



#创建敌机
enemy = GameSprite("./images/enemy1.png")
#创建敌机组
enemy_group = pygame.sprite.Group(enemy)
#游戏循环，游戏正式开始
while True:
    #可以指定时钟在内部的执行频率
    clock.tick(60)

    #获取事件
    for event in pygame.event.get():
        #判断事件是否退出
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()


    #修改飞机位置
    hero_rect.y -=1
    #判断飞机的位置
    if hero_rect.y<=0:
        hero_rect.y=700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    #让敌机调用俩个方法
    enemy_group.update()
    enemy_group.draw(screen)




    pygame.display.update()




pygame.quit()