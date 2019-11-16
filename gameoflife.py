import pygame
import random
pygame.init()
population =[]
new_population =[]
sumof=0
clock = pygame.time.Clock()
state =0
neighbor = 0
window = pygame.display.set_mode((800,500))
pygame.display.set_caption("Game of Life!")
window.fill((255,255,255))
windowopen = True
for i in range(9):
    individual_population =[]
    for j in range(15):
        y = random.randint(0,1)
        individual_population.append(y)
    population.append(individual_population)

def countneighbor(grid,x,y):
    summ = 0
    for i in range(-1,2):
        for j in range(-1,2):
            col = (x+i+9) %9
            row = (y+j+15) %15
            summ+=grid[col][row]
    
    summ-=grid[x][y]
    return summ
new_population = population

print(population)

while windowopen:
   
    for i in range(9):
        for j in range(15):
            if population[i][j] == 0:
                pygame.draw.rect(window,(0,0,0),[20+(j*50),20+(i*50),50,50],1)
            else:
                pygame.draw.rect(window,(0,0,0),[20+(j*50),20+(i*50),50,50])
    
    pygame.display.update()
    clock.tick(5)    
    for i in range(9):
        for j in range(15):
            state = population[i][j]
            neighbor = countneighbor(population,i,j)

            if state == 0 and neighbor ==3:
                new_population[i][j]=1
            elif state==1 and (neighbor<2 or neighbor>3):
                new_population[i][j]=0
            else:
                new_population[i][j]=state

    population=new_population

        
    window.fill((255,255,255))            
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            windowopen = False
    
    pygame.display.update()