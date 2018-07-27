#coding=utf-8
import random
import pygame
import time
from pygame.locals import *
'''
 1.搭建界面，主要完成窗口和背景图的显示
'''
class Base(object):
    def __init__(self, screen, name):
        self.name=name
        #set the window that can show the content
        self.screen=screen

class Plane(Base):
    def __init__(self, screen,name):
        super().__init__(screen,name)
        self.image=pygame.image.load(self.imageName).convert()
        self.bulletList=[]
    def display(self):
        self.screen.blit(self.image, (self.x,self.y))

        needDelItemList=[]
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def fire(self):
        newBullet=PublicBullet(self.x, self.y, self.screen, self.name)
        self.bulletList.append(newBullet)

class HeroPlane(Plane):

    def __init__(self, screen,name):
        self.x=230
        self.y=600
        self.imageName="./picture/hero.gif"
        super().__init__(screen,name)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

class EnemyPlane(Plane):
    def __init__(self,screen,name):
        self.x=0
        self.y=0
        self.imageName="./picture/enemy-1.gif"

        super().__init__(screen,name)
        self.direction="right"

    def move(self):
        if self.direction=='right':
            self.x+=2
        elif self.direction=="left":
            self.x-=2

        if self.x>480-50:
            self.direction="left"
        elif self.x<0:
            self.direction="right"

    def fire(self):
        num=random.randint(1,100)
        if num==88:
            super().fire()

class PublicBullet(Base):
    def __init__(self,x,y,screen, planeName):
        super().__init__(screen,planeName)

        if self.name=="hero":
           self.x=x+40
           self.y=y-20
           imageName="./picture/bullet-3.gif"

        elif self.name=="enemy":
            self.x=x+30
            self.y=y+30
            imageName="./picture/bullet-1.gif"
        self.image=pygame.image.load(imageName).convert()
    def move(self):
        if self.name=="hero":
            self.y-=2
        elif self.name=="enemy":
            self.y+=2
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y>800 or self.y<0:
            return True
        else:
            return False

if __name__ =="__main__":

    # 1 创建窗口
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2 创建一个背景图片
    background = pygame.image.load("./picture/background.png").convert()

    # 3 创建一个飞机对象
    heroPlane =HeroPlane(screen,"hero")

    #4 创建一个敌人飞机
    enemyPlane=EnemyPlane(screen,"enemy")

    #5 把背景图放到窗口显示
    while True:
        screen.blit(background, (0, 0))

        heroPlane.display()

        enemyPlane.move()
        enemyPlane.fire()
        enemyPlane.display()

        # 判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                    # 控制飞机让其向左移动
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    print("space")
                    heroPlane.fire()

        time.sleep(0.01)
        pygame.display.update()

