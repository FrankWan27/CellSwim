from defs import *
import random
import pygame

bg = pygame.image.load('flagella.png')


class Flagella:
    def __init__(self, body):
        self.state = State.IDLE
        self.body = body
        self.ticker = 0
        self.randomInit()

    def randomInit(self):
        self.direction = random.choice(list(Dir))
        self.strength = 0.00001 + random.random() * 0.00001 * self.body.radius
        self.reset()

    def update(self, dt):
        if self.state == State.ACTIVE:
            self.body.velocity = (self.body.velocity[0] + self.direction.value[0] * self.strength * dt, self.body.velocity[1] + self.direction.value[1] * self.strength * dt)
            self.body.energy -= self.strength * 0.2 * dt

        self.ticker += dt
        if self.state == State.ACTIVE and self.ticker >= self.duration:
            self.state = State.IDLE
            self.duration = self.genTimeInterval()
            self.ticker = 0
        elif self.state == State.IDLE and self.ticker >= self.interval:
            self.state = State.ACTIVE
            self.interval = self.genTimeInterval()
            self.ticker = 0

    def genTimeInterval(self):
        return random.random() * 1000 + 100

    def draw(self):
        startPos = self.body.getPos()
        #endPos = ((int)(self.body.pos[0] - self.direction.value[0] * self.strength * 500), (int)(self.body.pos[1] - self.direction.value[1] * self.strength * 500))
        if self.state == State.ACTIVE:
            self.img = pygame.transform.flip(self.img, True, False)
        #else:
            #drawColor = LIGHT_ORANGE

        #pygame.draw.arc(self.body.gameDisplay, (255,255,255), rect, 0, PI/ 2, 2)
        newImg = pygame.transform.rotate(self.img, dirToDegree(self.direction))
        #newImg = self.img
        imgRect = newImg.get_rect()
        imgRect.centerx = self.body.getPos()[0]
        imgRect.centery = self.body.getPos()[1]
        self.body.gameDisplay.blit(newImg, imgRect)


    def reset(self):
        self.interval = self.genTimeInterval()
        self.duration = self.genTimeInterval()
        self.img = pygame.transform.scale(bg, ((int)(300000 * self.strength), (int)(self.strength * 600000)))


    def setStats(self, direction, strength):
        self.direction = direction
        self.strength = strength
        self.reset()


