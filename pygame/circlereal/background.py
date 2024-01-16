import pygame
import pygame.freetype
import random
import math
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.Font(pygame.font.get_default_font(), 20)
background = pygame.image.load('./grid2.jpg')

clock = pygame.time.Clock()

class Empty:
    pass  

pygame.display.set_caption = "Minecart 7"

width = 1000
height = 600
wn = pygame.display.set_mode((width, height))
run = True

player_x = width/2
player_y = height/2
worldxv = worldyv = worldx = worldy = player_x_vel = player_y_vel = 0
size = 15

#food limit
foodlimit = 50
#food x:y key dictionary
food = {}
totalfood= 0
enemy = []
totalenemy=0
bullet = []
#new food function
def createnewfood():
   new_x = random.uniform(5,1995)
   new_y = random.uniform(5,1995)
   while player_x-15 < new_x < player_x+size+15 and player_y-15 < new_y < player_y +size+15:
      new_x = random.uniform(5,1995)
      new_y = random.uniform(5,1995)
   food[new_x] = new_y

def createnewenemy():
   new_x = random.uniform(5,1995)
   new_y = random.uniform(5,1995)
   while player_x-25 < new_x < player_x+size+25 and player_y-25 < new_y < player_y +size+25:
      new_x = random.uniform(5,1995)
      new_y = random.uniform(5,1995)
   newenemy = Empty()
   newenemy.posx = new_x
   newenemy.posy = new_y
   newenemy.attacktimer=0
   newenemy.movement=40
   newenemy.velx = 0
   newenemy.vely = 0
   enemy.append(newenemy)
def createbullet_p(x,y):
   newbullet = Empty()
   newbullet.posx = x
   newbullet.posy = y
   newbullet.velx = (player_x-x)/150
   newbullet.vely = (player_y-y)/150
   bullet.append(newbullet)

world = pygame.Surface((2000,2000)) # Create Map Surface
while run:
    wn.fill((0,0,0))
    world.blit(background,(0,0))
    clock.tick(60)
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
         run = False
      elif i.type == pygame.KEYDOWN:
         if i.key == pygame.K_w or i.key == pygame.K_UP:
            player_y_vel = -1.75
            worldyv =1.75
         if i.key == pygame.K_s or i.key == pygame.K_DOWN:
            player_y_vel = 1.75
            worldyv =-1.75
         if i.key == pygame.K_a or i.key == pygame.K_LEFT:
            player_x_vel = -1.75
            worldxv =1.75
         if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
            player_x_vel = 1.75
            worldxv=-1.75      
      if i.type == pygame.KEYUP:
         if i.key == pygame.K_w or i.key == pygame.K_s or i.key == pygame.K_UP or i.key == pygame.K_DOWN:
            player_y_vel = 0
            worldyv=0
         if i.key == pygame.K_a or i.key == pygame.K_d or i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
            player_x_vel = 0
            worldxv=0
    #
    lastworldx,lastworldy = worldx,worldy
    worldx += worldxv
    player_x += player_x_vel
    worldy += worldyv
    player_y += player_y_vel
    if player_x+size > 2000:
       player_x = 2000-size
       worldx = lastworldx
    elif player_x-size < 0:
       player_x = 0+size
       worldx = lastworldx
      
    if player_y+size > 2000:
       player_y = 2000-size
       worldy = lastworldy
    elif player_y-size < 0:
       player_y = 0+size
       worldy = lastworldy
      
    for x in list(food):
       #print(player_x,x,player_y,food[x])
       pygame.draw.circle(world, (25,25,255), (x, food[x]),6)
       if player_x-size-2.5 < x < player_x +size+2.5 and player_y-size-2.5 < food[x] < player_y +size+2.5:
          size+=1
          totalfood-=1
          del food[x]
          continue
   
    for x in enemy:
       if player_x-size-7.5 < x.posx < player_x +size+7.5 and player_y-size-7.5 < x.posy < player_y +size+7.5:
          size-=10
          totalenemy-=1
          enemy.remove(x)
          continue
    for x in bullet:
       if player_x-size-2.5 < x.posx < player_x +size+2.5 and player_y-size-2.5 < x.posy < player_y +size+2.5:
          size-=2
          bullet.remove(x)
          continue
    
    if size > 600 or size < 1:
      run = False
    #stuff
    if totalfood < 250:
       totalfood+=1
       createnewfood()
    if totalenemy < 15:
       totalenemy+=1
       createnewenemy()
   
    
    for x in food:
       pygame.draw.circle(world, (random.uniform(0,200),random.uniform(0,200),random.uniform(0,200)), (x,food[x]), 5)
    for x in enemy:
       x.attacktimer += 1
       x.movement += 1
       if x.attacktimer > 400:
          x.attacktimer = 0
          createbullet_p(x.posx,x.posy)
       if x.movement > 75:
          x.movement = 0
          x.velx,x.vely = random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)
       x.posx += x.velx
       x.posy += x.vely
       pygame.draw.circle(world, (255,0,0), (x.posx,x.posy), 15)
    for x in bullet:
       x.posx += x.velx/4
       x.posy += x.vely/4
       pygame.draw.circle(world, (255,255,0), (x.posx,x.posy),5)
    #eyeballs
    pygame.draw.circle(world, (0,255,0), (player_x,player_y), size)
    
    if player_x_vel == 0 and player_y_vel == 0 or player_x_vel == 0 and player_y_vel < 0:
       pygame.draw.circle(world, (255,255,255), (player_x-size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x+size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x-size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x+size/2,player_y-size/2.5), size/10)
    if player_x_vel == 0 and player_y_vel > 0:
       pygame.draw.circle(world, (255,255,255), (player_x-size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x+size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x-size/2,player_y+size/2.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x+size/2,player_y+size/2.5), size/10)
    if player_x_vel > 0 and player_y_vel == 0:
       pygame.draw.circle(world, (255,255,255), (player_x+size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x+size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x+size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x+size/2,player_y+size/2.5), size/10)
    if player_x_vel < 0 and player_y_vel == 0:
       pygame.draw.circle(world, (255,255,255), (player_x-size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x-size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x-size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x-size/2,player_y+size/2.5), size/10)
    #diagonals
    if player_x_vel < 0 and player_y_vel < 0:
       pygame.draw.circle(world, (255,255,255), (player_x-size/4,player_y-size/1.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x-size/1.5,player_y-size/4), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x-size/4,player_y-size/1.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x-size/1.5,player_y-size/4), size/10)
    if player_x_vel > 0 and player_y_vel > 0:
       pygame.draw.circle(world, (255,255,255), (player_x+size/4,player_y+size/1.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x+size/1.5,player_y+size/4), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x+size/4,player_y+size/1.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x+size/1.5,player_y+size/4), size/10)
    if player_x_vel > 0 and player_y_vel < 0:
       pygame.draw.circle(world, (255,255,255), (player_x+size/4,player_y-size/1.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x+size/1.5,player_y-size/4), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x+size/4,player_y-size/1.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x+size/1.5,player_y-size/4), size/10)
    if player_x_vel < 0 and player_y_vel > 0:
       pygame.draw.circle(world, (255,255,255), (player_x-size/4,player_y+size/1.5), size/5)
       pygame.draw.circle(world, (255,255,255), (player_x-size/1.5,player_y+size/4), size/5)
       pygame.draw.circle(world, (0,0,0), (player_x-size/4,player_y+size/1.5), size/10)
       pygame.draw.circle(world, (0,0,0), (player_x-size/1.5,player_y+size/4), size/10)
    
    
    wn.blit(world, (worldx,worldy))
    text_surface = font.render(f'{size} ({worldx}|{worldy}) ({player_x}|{player_y})', True, pygame.Color('orange'))
    wn.blit(text_surface, dest=(0,0))    
    pygame.display.flip()