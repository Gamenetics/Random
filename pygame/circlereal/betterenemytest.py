import pygame
import pygame.freetype
import random
import math
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.Font(pygame.font.get_default_font(), 10)
background = pygame.image.load('./grid.jpg')
background_size = background.get_size()
background_rect = background.get_rect()

w,h = 1000,600
x = 0
y = 0

class Empty:
    pass  

x1 = 0
y1 = -h

pygame.display.set_caption = "Minecart 7"

width = 1000
height = 600
wn = pygame.display.set_mode((width, height))
run = True

player_x = width/2
player_y = height/2
player_x_vel = player_y_vel = 0
size = 15

lol = 255
#food limit
foodlimit = 50
#food x:y key dictionary
food = {}
totalfood= 0
enemy = []
totalenemy=0
bullet = []
player = []
totalplayer=0
#new food function
def createnewfood():
   new_x = random.uniform(5,995)
   new_y = random.uniform(5,595)
   while player_x-15 < new_x < player_x+size+15 and player_y-15 < new_y < player_y +size+15:
      new_x = random.uniform(5,995)
      new_y = random.uniform(5,595)
   food[new_x] = new_y

def createnewenemy():
   new_x = random.uniform(5,995)
   new_y = random.uniform(5,595)
   while player_x-25 < new_x < player_x+size+25 and player_y-25 < new_y < player_y +size+25:
      new_x = random.uniform(5,995)
      new_y = random.uniform(5,595)
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
   newbullet.duration = 1000
   bullet.append(newbullet)
def createnewplayer():
   new_x = random.uniform(5,995)
   new_y = random.uniform(5,595)
   while player_x-25 < new_x < player_x+size+25 and player_y-25 < new_y < player_y +size+25:
      new_x = random.uniform(5,995)
      new_y = random.uniform(5,595)
   newplayer = Empty()
   newplayer.posx = new_x
   newplayer.posy = new_y
   newplayer.movement=40
   newplayer.size = 15
   newplayer.velx = 0
   newplayer.vely = 0
   player.append(newplayer)
while run:
    wn.blit(background,(0,0))

    for i in pygame.event.get():
      if i.type == pygame.QUIT:
         run = False
      elif i.type == pygame.KEYDOWN:
         if i.key == pygame.K_w:
            player_y_vel = -0.5
         if i.key == pygame.K_s:
            player_y_vel = 0.5
         if i.key == pygame.K_a:
            player_x_vel = -0.5
         if i.key == pygame.K_d:
            player_x_vel = 0.5
      if i.type == pygame.KEYUP:
         if i.key == pygame.K_w or i.key == pygame.K_s:
            player_y_vel = 0
         if i.key == pygame.K_a or i.key == pygame.K_d:
            player_x_vel = 0
    player_x += player_x_vel
    player_y += player_y_vel
    if player_x +size > width:
       player_x = width - size
    elif player_x -size < 0:
       player_x = 0 +size

    if player_y +size > height:
       player_y = height - size
    elif player_y -size< 0:
       player_y = 0+size
    
    #eatfood
    for x in list(food):
       if player_x-size-2.5 < x < player_x +size+2.5 and player_y-size-2.5 < food[x] < player_y +size+2.5:
          size+=1
          totalfood-=1
          del food[x]
          continue
       else:
         for c in player:
            if c.posx-c.size-2.5 < x < c.posx +size+2.5 and c.posy-size-2.5 < food[x] < c.posy + c.size+2.5:
               c.size+=1
               totalfood-=1
               del food[x]
               break
   
    for x in enemy:
       if player_x-size-7.5 < x.posx < player_x +size+7.5 and player_y-size-7.5 < x.posy < player_y +size+7.5:
          size-=10
          totalenemy-=1
          enemy.remove(x)
          continue
    for x in bullet:
       if player_x-size-2.5 < x.posx < player_x +size+2.5 and player_y-size-2.5 < x.posy < player_y +size+2.5:
          size-=3
          bullet.remove(x)
          continue
    
    if size > 600 or size < 1:
      run = False
    #stuff
    if totalfood < 150:
       totalfood+=1
       createnewfood()
    if totalenemy < 3:
       totalenemy+=1
       createnewenemy()
    if totalplayer < 3:
       totalplayer+=1
       createnewplayer()


    pygame.draw.circle(wn, (0,lol,0), (player_x,player_y), size)
    for x in food:
       pygame.draw.circle(wn, (random.uniform(0,200),random.uniform(0,200),random.uniform(0,200)), (x,food[x]), 5)
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
       if x.posx> width:
            x.posx = width
       elif x.posx < 0:
            x.posx = 0

       if x.posy> height:
            x.posy = height
       elif x.posy< 0:
            x.posy = 0
       pygame.draw.circle(wn, (255,0,0), (x.posx,x.posy), 15)

    for x in player:
       x.movement += 1
       if x.movement > 175:
          x.movement = 0
          x.velx,x.vely = random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)
       x.posx += x.velx
       x.posy += x.vely
       if x.posx + x.size> width:
            x.posx = width-x.size
       elif x.posx - x.size< 0:
            x.posx = 0+x.size

       if x.posy + x.size> height:
            x.posy = height-x.size
       elif x.posy - x.size< 0:
            x.posy = 0+x.size
       pygame.draw.circle(wn, (0,255,0), (x.posx,x.posy), x.size)

    for x in bullet:
       x.duration -= 1
       if x.duration < 1:
          bullet.remove(x)
       x.posx += x.velx/2
       x.posy += x.vely/2
       if x.posx > width:
        x.velx *= -1
       elif x.posx < 0:
        x.velx *= -1

       if x.posy > height:
          x.vely *= -1
       elif x.posy < 0:
          x.vely *= -1
       pygame.draw.circle(wn, (255,255,0), (x.posx,x.posy),5)
    #eyeballs
    if player_x_vel == 0 and player_y_vel == 0 or player_x_vel == 0 and player_y_vel < 0:
       pygame.draw.circle(wn, (255,255,255), (player_x-size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x+size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/2,player_y-size/2.5), size/10)
    if player_x_vel == 0 and player_y_vel > 0:
       pygame.draw.circle(wn, (255,255,255), (player_x-size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x+size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/2,player_y+size/2.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/2,player_y+size/2.5), size/10)
    if player_x_vel > 0 and player_y_vel == 0:
       pygame.draw.circle(wn, (255,255,255), (player_x+size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x+size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/2,player_y+size/2.5), size/10)
    if player_x_vel < 0 and player_y_vel == 0:
       pygame.draw.circle(wn, (255,255,255), (player_x-size/2,player_y-size/2.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x-size/2,player_y+size/2.5), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/2,player_y-size/2.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/2,player_y+size/2.5), size/10)
    #diagonals
    if player_x_vel < 0 and player_y_vel < 0:
       pygame.draw.circle(wn, (255,255,255), (player_x-size/4,player_y-size/1.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x-size/1.5,player_y-size/4), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/4,player_y-size/1.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/1.5,player_y-size/4), size/10)
    if player_x_vel > 0 and player_y_vel > 0:
       pygame.draw.circle(wn, (255,255,255), (player_x+size/4,player_y+size/1.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x+size/1.5,player_y+size/4), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/4,player_y+size/1.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/1.5,player_y+size/4), size/10)
    if player_x_vel > 0 and player_y_vel < 0:
       pygame.draw.circle(wn, (255,255,255), (player_x+size/4,player_y-size/1.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x+size/1.5,player_y-size/4), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/4,player_y-size/1.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x+size/1.5,player_y-size/4), size/10)
    if player_x_vel < 0 and player_y_vel > 0:
       pygame.draw.circle(wn, (255,255,255), (player_x-size/4,player_y+size/1.5), size/5)
       pygame.draw.circle(wn, (255,255,255), (player_x-size/1.5,player_y+size/4), size/5)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/4,player_y+size/1.5), size/10)
       pygame.draw.circle(wn, (0,0,0), (player_x-size/1.5,player_y+size/4), size/10)
    

    text_surface = font.render(f'{size}', True, pygame.Color('orange'))
    wn.blit(text_surface, dest=(player_x,player_y+size+5))
    
    pygame.display.update()