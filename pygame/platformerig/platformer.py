import pygame
import pygame.freetype
import random
import math
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.Font(pygame.font.get_default_font(), 25)
pygame.display.set_caption = "Minecart 7"

width = 1000
height = 600
wn = pygame.display.set_mode((width, height))
run = True

right = True
class Empty:
    pass  

player_x = 20
player_y = height/2
player_x_vel = player_y_vel = 0
size = 25

clock = pygame.time.Clock()
onground = True
platforms = []
bullet = []
def createplatform(x,y,width,height, type):
   newplatform = Empty()
   newplatform.x = x
   newplatform.y = y
   newplatform.width = width
   newplatform.height = height
   newplatform.type = type
   platforms.append(newplatform)

def createbullet_p(x,y,right=True):
   newbullet = Empty()
   newbullet.posx = x
   newbullet.posy = y+size/2
   if right == True:
      newbullet.velx = 4
   else:
      newbullet.velx = -4
   newbullet.duration = 500
   bullet.append(newbullet)

levels = [
   [300,75,80,20,""],
   [500,145,150,60,""],
   [400,100,90,30,""],
   [320,205,150,20,""],
   [220,255,150,10,""],
   [100,305,100,5,""],
   [300,355,250,15,""],
   [420,405,50,120,""],
   [520,485,80,40,"end"]
]

for a in levels:
   createplatform(a[0],height-a[1],a[2],a[3],a[4])
#createplatform(300,height-75,80,20)

guncd = 0
level = 0
while run:
    clock.tick(60)
    wn.fill((0, 0 ,0))
    if guncd > 0:
       guncd-=1
    previousx = player_x
    previousy = player_y
    if onground == False:
        player_y_vel += 0.15
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
         run = False
      elif i.type == pygame.KEYDOWN:
         if (i.key == pygame.K_w or i.key == pygame.K_SPACE) and onground == True:
            player_y_vel = -5
            onground = False
         if i.key == pygame.K_a:
            right=False
            player_x_vel = -2.5
         if i.key == pygame.K_d:
            right=True
            player_x_vel = 2.5
         if i.key == pygame.K_LSHIFT:
            player_x_vel *= 2
      if i.type == pygame.MOUSEBUTTONDOWN:
         if i.button == 1:
            if guncd == 0:
               guncd = 60
               createbullet_p(player_x-5 if right == False else player_x+5+size,player_y,right)

            #elif event.button == 2:
                #print("middle mouse button")
            #elif event.button == 3:
                #print("right mouse button")
            #elif event.button == 4:
             #   print("mouse wheel up")
            #elif event.button == 5:
                #print("mouse wheel down")
      if i.type == pygame.KEYUP:
         if i.key == pygame.K_a or i.key == pygame.K_d:
            player_x_vel = 0
    player_x += player_x_vel
    player_y += player_y_vel
    onground = False
    if player_x+size > width:
       player_x = width-size
    elif player_x-size< 0:
       player_x = 0+size

    if player_y+size> height:
       player_y = height-size
    elif player_y-size < 0:
       player_y = 0+size
    
    if player_y+size == height:
       onground = True
       player_y_vel = 0
    #movement done

    for x in bullet:
       x.duration -= 1
       if x.duration < 1:
          bullet.remove(x)
       x.posx += x.velx

       if x.posx > width:
        x.velx *= -1
       elif x.posx < 0:
        x.velx *= -1
       pygame.draw.circle(wn, (255,255,0), (x.posx,x.posy),3)

    rect = pygame.Rect(player_x,player_y, size, size)
    for x in platforms:
       rectplatform = pygame.Rect(x.x,x.y, x.width, x.height)
       #print(x.x,x.y,x.width,x.height,player_x,player_y, x.x+x.width,x.y+x.height)
       collide = rect.colliderect(rectplatform)
       for b in bullet: 
          rectbullet = pygame.Rect(b.posx,b.posy,3,3)
          bulletcollide = rectbullet.colliderect(rectplatform)
          playercollide = rectbullet.colliderect(rect)
          if playercollide:
             player_x_vel+=b.velx/4
             bullet.remove(b)
             continue
          if bulletcollide:
             b.velx *=-1
             
       if x.type == "end":
               pygame.draw.rect(wn, (0,200,0), pygame.Rect(x.x, x.y, x.width, x.height))
       else: pygame.draw.rect(wn, (239,163,55), pygame.Rect(x.x, x.y, x.width, x.height))
               
       pygame.draw.circle(wn, (255,0,0), (player_x,player_y+size),5)
       pygame.draw.circle(wn, (0,255,0), (x.x,x.y+x.height+size),5)
       pygame.draw.circle(wn, (120,255,0), (x.x,x.y+x.height),5)
       pygame.draw.circle(wn, (0,0,255), (x.x+x.width,x.y),5)
       if collide:
         if x.y+10 >= player_y+size >=x.y:
            onground=True
            player_y = x.y-size
            if x.type == "end":
               player_x,player_y = 0,300
               level +=1
               platforms = []
               if level == 1:
                  levels = [
                           [50,75,80,20,""],
                           [100,150,150,20,""],
                           [150,200,90,20,""],
                           [200,250,150,20,""],
                           [250,300,150,20,""],
                           [200,350,100,25,""],
                           [300,300,250,25,""],
                           [400,250,50,20,""],
                           [600,300,50,20,""],
                           [650,500,50,20,""],
                           [700,450,50,20,""],
                           [900,400,50,20,""],
                           [800,350,50,20,""],
                           [500,550,80,40,"end"]
                           ]
               if level == 2:
                  levels = [
                           [50,75,80,20,""],
                           [100,150,150,20,""],
                           [150,200,90,20,""],
                           [200,250,150,20,""],
                           [250,400,150,20,""],
                           [200,250,100,25,""],
                           [300,100,250,25,""],
                           [400,450,50,20,""],
                           [600,500,50,20,""],
                           [650,400,50,20,""],
                           [700,250,50,20,""],
                           [900,400,50,20,""],
                           [800,250,50,20,""],
                           [500,450,80,40,"end"]
                           ]
               for a in levels:
                  createplatform(a[0],height-a[1],a[2],a[3],a[4])
               break
            
         if onground == False:
            player_x = previousx

         if x.x+size >= player_x+size >= x.x and x.y <= player_y <= x.y+height:
            player_x = previousx
            
         elif x.x+x.width-size <= player_x <= x.x+x.width and x.y <= player_y <= x.y+height:
            player_x = previousx
            
         if x.y+x.height+size >= player_y >= x.y+x.height-size:
            player_y = previousy
            player_y_vel = 0
            
    pygame.draw.rect(wn, (0,255,0), pygame.Rect(player_x,player_y,size,size))
    
    if right == True:
      pygame.draw.circle(wn, (255,255,255), (player_x+size/1.25,player_y+size/4), size/5)
      pygame.draw.circle(wn, (0,0,0), (player_x+size/1.25,player_y+size/4), size/10)
      pygame.draw.rect(wn, (100,125,100), pygame.Rect(player_x+size/1.5,player_y+size/2,15,6))
    else:
      pygame.draw.circle(wn, (255,255,255), (player_x+size/4,player_y+size/4), size/5)
      pygame.draw.rect(wn, (100,125,100), pygame.Rect(player_x-size/4,player_y+size/2,15,6))
      pygame.draw.circle(wn, (0,0,0), (player_x+size/4,player_y+size/4), size/10)
    reloadtxt = font.render(f'Gun: {"Ready" if guncd < 1 else "Reloading"}', True, pygame.Color('green' if guncd < 1 else "red"))
    wn.blit(reloadtxt, dest=(0,0))    
    leveltxt = font.render(f'Level {level}', True, pygame.Color('white'))
    wn.blit(leveltxt, dest=(width/2,0))   
    pygame.display.update()