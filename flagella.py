from defs import *
import random
import pygame


class Flagella:
    def __init__(self, body):
        self.state = State.IDLE
        self.body = body
        self.ticker = 0
        self.randomInit()

    def randomInit(self):
        self.direction = random.choice(list(Dir))
        self.strength = random.random() * 0.2
        self.reset()

    def update(self, dt):
        if self.state == State.ACTIVE:
            self.body.velocity = (self.body.velocity[0] + self.direction.value[0] * self.strength, self.body.velocity[1] + self.direction.value[1] * self.strength)
            self.body.energy -= self.strength

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
        endPos = ((int)(self.body.pos[0] - self.direction.value[0] * self.strength * 500), (int)(self.body.pos[1] - self.direction.value[1] * self.strength * 500))
        if self.state == State.ACTIVE:
            drawColor = LIGHT_GREEN
        else:
            drawColor = LIGHT_ORANGE
        pygame.draw.line(self.body.gameDisplay, drawColor, startPos, endPos, 4)

    def reset(self):
        self.interval = self.genTimeInterval()
        self.duration = self.genTimeInterval()


    def setStats(self, direction, strength):
        self.direction = direction
        self.strength = strength
        self.reset()


