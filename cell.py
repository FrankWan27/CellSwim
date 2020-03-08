from defs import *
import random
import pygame
from flagella import Flagella

class Cell:
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.flagella = []
        self.energy = START_ENERGY
        self.pos = (GAME_W / 2, GAME_H / 2)
        self.velocity = (0, 0)
        self.radius = 20
        self.alive = True
        self.fitness = 0
        self.randomInit()

    def randomInit(self):
        numFlag = random.randint(0, 8)
        self.radius = random.randint(10, 30)
        for i in range(numFlag):
            self.flagella.append(Flagella(self))

    def move(self):
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

    def update(self, dt):
        if self.alive:
            for flag in self.flagella:
                flag.update(dt)
            self.move()
            self.energy -= self.radius / 200
            if(self.energy < 0):
                self.die()
            else:
                self.draw()

    def draw(self):
        drawColor = (40, int(self.energy / START_ENERGY * 255), 40)
        pygame.draw.circle(self.gameDisplay, drawColor, self.getPos(), (int)(self.radius))
        for flag in self.flagella:
            flag.draw()

    def die(self):
        self.fitness = self.pos[0] - GAME_W / 2
        self.alive = False

    def getPos(self):
        return ((int)(self.pos[0]), (int)(self.pos[1]))

    def getGenome(self):
        genome = []
        #Max 8 flagella
        for i in range(8):
            if i < len(self.flagella):
                genome.append(self.flagella[i].direction)
                genome.append(self.flagella[i].strength)
            else:
                genome.append(Dir.NONE)
                genome.append(0)

        genome.append(self.radius)
        return genome

    def setGenome(self, genome):
        self.reset()
        for i in range(8):
            if genome[i * 2 ] != Dir.NONE:
                newFlag = Flagella(self)
                newFlag.setStats(genome[i * 2], genome[i * 2 + 1])
                self.flagella.append(newFlag)
        print(genome)
        print(genome[16])
        self.radius = genome[16]
    
    def makeChild(self, mom, dad):

        self.setGenome(self.mixGenome(mom.getGenome(), dad.getGenome()))

    def mixGenome(self, a1, a2):
        
        output = []

        for i in range(len(a1)):
            if random.random() < 0.5:
                output.append(a1[i])
            else:
                output.append(a2[i])

        return output


    def reset(self):
        self.energy = START_ENERGY
        self.pos = (GAME_W / 2, GAME_H / 2)
        self.velocity = (0, 0)
        self.radius = 20
        self.alive = True
        self.flagella = []


class Cells():



    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.cells = []
        self.createGeneration()
        self.generation = 0
        self.bestDistance = 0

    def update(self, dt):
        numAlive = 0
        for i in range(len(self.cells)):
            cell = self.cells[i]
            cell.update(dt)
            if cell.alive:
                numAlive += 1
        return numAlive

    def createGeneration(self):
        self.cells = []
        for i in range(POP_SIZE):
            self.cells.append(Cell(self.gameDisplay))

    def evolve(self):
        #get top 10 performers
        best = []

        for i in range(10):
            best.append(self.popBest())

        #Rest of population will be children of top 10
        for i in range(POP_SIZE - 10):
            mom = best[random.randint(0, 9)]
            dad = best[random.randint(0, 9)]
            best.append(self.makeChild(mom, dad))

        self.generation += 1
        print(self.generation)
        self.cells = best

    def popBest(self):
        bestFit = -1
        bestIndex = 0
        for i in range(len(self.cells)):
            if self.cells[i].fitness > bestFit:
                bestIndex = i
                if bestFit > self.bestDistance:
                    self.bestDistance = bestFit
                bestFit = self.cells[i].fitness

        return self.cells.pop(bestIndex)

    def makeChild(self, mom, dad):
        child = Cell(self.gameDisplay)
        child.makeChild(mom, dad)
        return child