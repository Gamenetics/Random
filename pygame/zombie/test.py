import pygame
import pygame.freetype
import random
import math
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.Font(pygame.font.get_default_font(), 25)
background = pygame.image.load('./grid.jpg')
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
player_x_vel = player_y_vel = 0
size = 15
health = 3

enemy = []
totalenemy=0
bullet = []

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

def createbullet_p(x,y,safe=False,spread=0,duration=500,bullettype=""):
   newbullet = Empty()
   mouse_x, mouse_y = pygame.mouse.get_pos()
   angle = math.atan2(mouse_y-y,(mouse_x-x))
   newbullet.velx = 4*math.cos(angle) 
   newbullet.vely = 4*math.sin(angle)
   newbullet.posx = x
   newbullet.posy = y
   newbullet.duration = duration
   newbullet.safe = safe
   newbullet.type = bullettype
   if bullettype=="shotgun":
    print(newbullet.velx,newbullet.vely)
    if newbullet.velx > 0: newbullet.vely*= spread
    else: newbullet.velx *= spread
    if newbullet.vely > 0: newbullet.velx*= spread
    else: newbullet.vely *= spread
    print("e",newbullet.velx,newbullet.vely)
   bullet.append(newbullet)

guncd = 0
def shoot(type,guncd):
    if type == 1 and guncd == 0:
         createbullet_p(player_x,player_y,True)
         return 60
    if type == 2 and guncd == 0:
         createbullet_p(player_x,player_y,True,1,75,"shotgun")
         createbullet_p(player_x,player_y,True,1,75,"shotgun")
         createbullet_p(player_x,player_y,True,0,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/3,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/3,75,"shotgun")

         createbullet_p(player_x,player_y,True,1/2,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/2,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/4,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/4,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/5,75,"shotgun")
         createbullet_p(player_x,player_y,True,1/5,75,"shotgun")
         return 240
    return guncd

equippedgun = 1
while run:
    time_passed = clock.tick(60)/3
    clock.tick(60)
    wn.blit(background,(0,0))
    if guncd > 0: guncd -=1
    
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
         run = False
      elif i.type == pygame.KEYDOWN:
         if i.key == pygame.K_1:
            equippedgun = 1
         if i.key == pygame.K_2:
            equippedgun = 2
         if i.key == pygame.K_3:
            equippedgun = 3
         if i.key == pygame.K_LSHIFT:
            print("yay")
      keys = pygame.key.get_pressed()
      player_x_vel = (keys[pygame.K_d] - keys[pygame.K_a]) * 0.5  
      player_y_vel = (keys[pygame.K_s] - keys[pygame.K_w]) * 0.5  
      if i.type == pygame.MOUSEBUTTONDOWN:
         if i.button == 1:
            guncd = shoot(equippedgun,guncd)
    player_x += player_x_vel * time_passed
    player_y += player_y_vel * time_passed
    if player_x+size> width:
       player_x = width-size
    elif player_x-size < 0:
       player_x = 0+size

    if player_y+size > height:
       player_y = height-size
    elif player_y-size < 0:
       player_y = 0+size
   
    for x in enemy:
       if player_x-size-7.5 < x.posx < player_x +size+7.5 and player_y-size-7.5 < x.posy < player_y +size+7.5:
          size-=10
          totalenemy-=1
          enemy.remove(x)
          continue
       
    for x in bullet:
       x.duration -= 1
       if x.duration < 1:
          bullet.remove(x)
       x.posx += x.velx
       x.posy += x.vely

       if x.posx > width:
        x.velx *= -1
       elif x.posx < 0:
        x.velx *= -1

       if x.posy > height:
            x.vely *= -1
       elif x.posy < 0:
            x.vely *= -1
       if x.type == "shotgun": 
         pygame.draw.circle(wn, (255,255,0), (x.posx,x.posy),2)
         pygame.draw.circle(wn, (255,0,0), (x.posx+x.velx+x.vely/2,x.posy+x.vely+x.vely/2),2)
       else: 
         pygame.draw.circle(wn, (255,255,0), (x.posx,x.posy),4)
    if totalenemy < 3:
       totalenemy+=1
       createnewenemy()


    pygame.draw.circle(wn, (0,255,0), (player_x,player_y), size)
    for x in enemy:
       x.movement += 1
       if x.movement > 75:
          x.movement = 0
          x.velx,x.vely = random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)
       x.posx += x.velx
       x.posy += x.vely
       if x.posx > width:
            x.posx = width
       elif x.posx < 0:
            x.posx = 0

       if x.posy > height:
            x.posy = height
       elif x.posy < 0:
            x.posy = 0
       pygame.draw.circle(wn, (255,0,0), (x.posx,x.posy), 15)
    for x in bullet:
       x.duration -= 1
       if x.duration < 1:
          bullet.remove(x)
       x.posx += x.velx
       x.posy += x.vely
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

    reloadtxt = font.render(f'Gun: {"Ready" if guncd < 1 else "Reloading"}', True, pygame.Color('green' if guncd < 1 else "red"))
    wn.blit(reloadtxt, dest=(0,0))    
    pygame.display.flip()