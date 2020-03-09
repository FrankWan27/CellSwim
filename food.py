from defs import *
import random
import pygame

class Food:
    def __init__(self, gameDisplay, x, y, r):
        self.gameDisplay = gameDisplay
        self.pos = (x, y)
        self.radius = r
        self.velocity = (random.random() * 0.01, random.random() * 0.01)
        self.alive = True

    def update(self, dt, cells):
        #float around
        self.pos = (self.pos[0] + self.velocity[0] * dt, self.pos[1] + self.velocity[1] * dt)
        self.bounceWall()
        self.checkCollision(cells)
        self.draw()

    def draw(self):
        pygame.draw.circle(self.gameDisplay, pygame.Color('black'), self.getPos(), (int)(self.radius) + 1)
        pygame.draw.circle(self.gameDisplay, LIGHT_GREEN, self.getPos(), (int)(self.radius))

    def getPos(self):
        return ((int)(self.pos[0]), (int)(self.pos[1]))


    def checkCollision(self, cells):
        for cell in cells.cells:
            if getDistance(cell.pos, self.pos) <= self.radius + cell.radius:
                self.alive = False
                cell.foodEaten += 1
                cell.energy = START_ENERGY * self.radius / MAX_FOOD_SIZE
                break

    def bounceWall(self):
        if self.pos[0] < 0 or self.pos[0] >= GAME_W:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.pos[1] < 0 or self.pos[1] >= GAME_H:
            self.velocity = (self.velocity[0], -self.velocity[1])

class Foods:

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.reset()

    def spawnFood(self):
        x = random.random() * GAME_W
        y=random.random() * GAME_H
        r=random.random() * MAX_FOOD_SIZE
        self.foods.append(Food(self.gameDisplay, x, y, r))

    def update(self, dt, cells):
        for food in self.foods:
            food.update(dt, cells)

        self.foods = [food for food in self.foods if food.alive]



        if len(self.foods) <= 20:
            self.spawnFood()

    def reset(self):
        self.foods = []
        while(len(self.foods) <= 50):
            self.spawnFood()