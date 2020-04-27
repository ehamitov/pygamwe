import pygame
import random
import os
import sys
import time
from enum import Enum
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((800, 600))
background_image = pygame.image.load("background1.jpg")
shoot_sound = pygame.mixer.Sound("crash.wav")
life1=3
life2=3
FPS = 30
clock = pygame.time.Clock()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Times new roman', 32)

def scores (x,y):
    res = font.render('life:  ' + str(life1), True, (255, 255, 0)) #draw text on a new Surf
    screen.blit(res, (x,y))

def scores1 (x,y):
    res = font.render('life:  ' + str(life2), True, (255, 0, 255)) #draw text on a new Surf
    screen.blit(res, (x,y))

def end(Life1,life2):
    myfont = pygame.font.SysFont('arial', 32)
    ending1 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    ending1_1 = myfont.render('P1 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    ending2 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    ending1_2 = myfont.render('P2 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    if life1==0:
        background_image = pygame.image.load('ground1.jpg')
        screen.blit(background_image,(0,0))
        screen.blit(ending2,(350, 200))
        screen.blit(ending1_2,(450, 300))
    if life2==0:
        background_image = pygame.image.load('ground1.jpg')
        screen.blit(background_image,(0,0))
        screen.blit(ending1,(350, 200))
        screen.blit(ending1_1,(450, 300))
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    STOP = 5

class Tank:
    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN, d_stop=pygame.K_RALT):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 40
        self.direction = Direction.STOP
        self.life = 3

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN,
                    d_stop: Direction.STOP}

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,(self.x, self.y, self.width, self.width))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 4)
        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (self.x - int(self.width / 2), self.y + int(self.width / 2)), 4)
        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 4)
        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)
        if self.direction == Direction.STOP:
            if lastMoveOfTank1 == "right":
                pygame.draw.line(screen, tank1.color, (tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)), (tank1.x + tank1.width + int(tank1.width / 2), tank1.y + int(tank1.width / 2)), 4)
            if lastMoveOfTank1 == "left":
                pygame.draw.line(screen, tank1.color, (tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)), (tank1.x - int(tank1.width / 2), tank1.y + int(tank1.width / 2)), 4)
            if lastMoveOfTank1 == "up":
                pygame.draw.line(screen, tank1.color, (tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)), (tank1.x + int(tank1.width / 2), tank1.y - int(tank1.width / 2)), 4)
            if lastMoveOfTank1 == "down":
                pygame.draw.line(screen, tank1.color, (tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)), (tank1.x + int(tank1.width / 2), tank1.y + tank1.width + int(tank1.width / 2)), 4)

            if lastMoveOfTank2 == "right":
                pygame.draw.line(screen, tank2.color, (tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)), (tank2.x + tank2.width + int(tank2.width / 2), tank2.y + int(tank2.width / 2)), 4)
            if lastMoveOfTank2 == "left":
                pygame.draw.line(screen, tank2.color, (tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)), (tank2.x - int(tank2.width / 2), tank2.y + int(tank2.width / 2)), 4)
            if lastMoveOfTank2 == "up":
                pygame.draw.line(screen, tank2.color, (tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)), (tank2.x + int(tank2.width / 2), tank2.y - int(tank2.width / 2)), 4)
            if lastMoveOfTank2 == "down":
                pygame.draw.line(screen, tank2.color, (tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)), (tank2.x + int(tank2.width / 2), tank2.y + tank2.width + int(tank2.width / 2)), 4)


    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.speed0 = self.speed
            self.x -= self.speed0
        if self.direction == Direction.RIGHT: 
            self.speed0 = self.speed
            self.x += self.speed0
        if self.direction == Direction.UP: 
            self.speed0 = self.speed
            self.y -= self.speed0
        if self.direction == Direction.DOWN: 
            self.speed0 = self.speed
            self.y += self.speed0
        if self.direction == Direction.STOP:
            self.speed0 = 0
        self.draw()

class snaryad():  
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 10 

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def edge1():
    if tank1.x > 800:
        tank1.x = 0
        tank1.x += tank1.speed
    if tank1.x < 0:
        tank1.x = 800
        tank1.x += tank1.speed
    if tank1.y > 600:
        tank1.y = 0
        tank1.y += tank1.speed
    if tank1.y < 0:
        tank1.y = 600
        tank1.y += tank1.speed

def edge2():
    if tank2.x > 800:
        tank2.x = 0
        tank2.x += tank2.speed
    if tank2.x < 0:
        tank2.x = 800
        tank2.x += tank2.speed
    if tank2.y > 600:
        tank2.y = 0
        tank2.y += tank2.speed
    if tank2.y < 0:
        tank2.y = 600
        tank2.y += tank2.speed
bullets1 = []
bullets2 = []


lastMoveOfTank1 = "left"
lastMoveOfTank2 = "right"

move1 = "RIGHT"
move2 = "RIGHT"

tank1 = Tank(540, 280, 4, (255, 123, 100))
tank2 = Tank(220, 280, 4, (100, 230, 40), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)

tanks = [tank1, tank2]

mainloop = True
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if event.key == pygame.K_RETURN:
                shoot_sound.play()
                if len(bullets1) == 0:
                    if lastMoveOfTank1 == "right":
                        bullets1.append(snaryad(tank1.x + tank1.width + int(tank1.width / 2), tank1.y + int(tank1.width / 2), 5, (255, 123, 100)))
                        move1 = "RIGHT"
                    if lastMoveOfTank1 == "left":
                        bullets1.append(snaryad(tank1.x - tank1.width + int(tank1.width / 2), tank1.y + int(tank1.width / 2), 5, (255, 123, 100)))
                        move1 = "LEFT"
                    if lastMoveOfTank1 == "up": 
                        bullets1.append(snaryad(tank1.x + int(tank1.width / 2), tank1.y - int(tank1.width / 2), 5, (255, 123, 100)))
                        move1 = "UP"
                    if lastMoveOfTank1 == "down":
                        bullets1.append(snaryad(tank1.x + int(tank1.width / 2), tank1.y + tank1.width + int(tank1.width / 2), 5, (255, 123, 100)))
                        move1 = "DOWN"
                
            if event.key == pygame.K_SPACE:
                shoot_sound.play()    
                if len(bullets2) == 0: 
                    if lastMoveOfTank2 == "right":
                        bullets2.append(snaryad(tank2.x + tank2.width + int(tank2.width / 2), tank2.y + int(tank2.width / 2), 5, (255, 123, 100)))
                        move2 = "RIGHT"
                    if lastMoveOfTank2 == "left":
                        bullets2.append(snaryad(tank2.x - tank2.width + int(tank2.width / 2), tank2.y + int(tank2.width / 2), 5, (255, 123, 100)))
                        move2 = "LEFT"
                    if lastMoveOfTank2 == "up": 
                        bullets2.append(snaryad(tank2.x + int(tank2.width / 2), tank2.y - int(tank2.width / 2), 5, (255, 123, 100)))
                        move2 = "UP"
                    if lastMoveOfTank2 == "down":
                        bullets2.append(snaryad(tank2.x + int(tank2.width / 2), tank2.y + tank2.width + int(tank2.width / 2), 5, (255, 123, 100)))
                        move2 = "DOWN"

            for tank in tanks: 
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
    
    if tank1.direction == Direction.LEFT:
        lastMoveOfTank1 = "left"
    if tank1.direction == Direction.RIGHT:
        lastMoveOfTank1 = "right"
    if tank1.direction == Direction.UP:
        lastMoveOfTank1 = "up"
    if tank1.direction == Direction.DOWN:
        lastMoveOfTank1 = "down"

    if tank2.direction == Direction.LEFT:
        lastMoveOfTank2 = "left"
    if tank2.direction == Direction.RIGHT:
        lastMoveOfTank2 = "right"
    if tank2.direction == Direction.UP:
        lastMoveOfTank2 = "up"
    if tank2.direction == Direction.DOWN:
        lastMoveOfTank2 = "down"
    
    for bullet in bullets1:
        if bullet.x > 0 and bullet.x < 800 and bullet.y > 0 and bullet.y < 600:
            if move1 == "RIGHT":
                bullet.x += bullet.vel
            if move1 == "LEFT":
                bullet.x -= bullet.vel
            if move1 == "UP":
                bullet.y -= bullet.vel
            if move1 == "DOWN":
                bullet.y += bullet.vel
        else:
             bullets1.pop(bullets1.index(bullet))

    for bullet in bullets2:
        if bullet.x > 0 and bullet.x < 800 and bullet.y > 0 and bullet.y < 600:
            if move2 == "RIGHT":
                bullet.x += bullet.vel
            if move2 == "LEFT":
                bullet.x -= bullet.vel
            if move2 == "UP":
                bullet.y -= bullet.vel
            if move2 == "DOWN":
                bullet.y += bullet.vel
        else:
            bullets2.pop(bullets2.index(bullet))
    
    for bullet in bullets1 :
        if bullet.y >= tank2.y and bullet.y <= tank2.y + tank2.width and bullet.x >= tank2.x and bullet.x <= tank2.x + tank2.width :
            bullets1.pop(bullets1.index(bullet))
            life2 -= 1
            tank2.x,tank2.y = random.randint(20, 770), random.randint(20, 570)
        

    for bullet in bullets2 :
        if bullet.y >= tank1.y and bullet.y <= tank1.y + tank1.width and bullet.x >= tank1.x and bullet.x <= tank1.x + tank1.width :
            bullets2.pop(bullets2.index(bullet))
            life1 -= 1
            tank1.x,tank1.y = random.randint(20, 770), random.randint(20, 570)


    screen.blit(background_image, (0, 0))
    pygame.display.set_caption('TANKs DUEL')
    edge1()
    edge2()
    for tank in tanks:
        tank.move()
    for bullet in bullets1:
        bullet.draw(screen)
    for bullet in bullets2:
        bullet.draw(screen)
    end(life1,life2)
    clock.tick(FPS)
    scores(650,30)
    scores1(50,30)
    pygame.display.flip()


pygame.quit()