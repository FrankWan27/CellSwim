import pygame
import sys
import os
from cell import Cells
from defs import *

# PyInstaller adds this attribute
if getattr(sys, 'frozen', False):
    # Running in a bundle
    CurrentPath = sys._MEIPASS
else:
    # Running in normal Python environment
    CurrentPath = os.path.dirname(__file__)

def startSimulation():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Cell Swim')
    
    runloop = True
    clock = pygame.time.Clock()
    dt = 0
    gameTime = 0

    cells = Cells(gameDisplay)

    while runloop:    
        gameDisplay.fill(LIGHT_BLUE)

        dt = clock.tick(FPS)
        gameTime += dt    
        #Break loop if we quit
        runloop = handleInput()

        if(cells.update(dt) <= 0):
            cells.evolve()

        showDebug(gameDisplay, dt, gameTime, cells)

        pygame.display.update()

    pygame.display.quit()
    pygame.quit()

def showLabel(gameDisplay, data, text, x, y):
    font = pygame.font.Font(os.path.join(CurrentPath, 'fonts/abel.ttf'), 20)
    label = font.render('{} {}'.format(text, data), 1, (40,40,250))
    gameDisplay.blit(label, (x, y))
    return y + 20

def showDebug(gameDisplay, dt, gameTime, cells):
    xOffset = GAME_W + 10
    yOffset = 2
    yOffset = showLabel(gameDisplay, round(1000/dt, 2), 'FPS: ', xOffset, yOffset)
    yOffset = showLabel(gameDisplay, round(gameTime/1000, 2),'Game Time: ', xOffset, yOffset)
    yOffset = showLabel(gameDisplay, cells.generation, 'Current Generation: ', xOffset, yOffset)
    yOffset = showLabel(gameDisplay, cells.bestDistance, 'Best Distance: ', xOffset, yOffset)


#Handle keyboard input
def handleInput():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return False
    return True

if __name__== "__main__":
    startSimulation()