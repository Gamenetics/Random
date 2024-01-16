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

player_x_vel = player_y_vel = 0
size = 25
player_x = 20
player_y = height-size

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__() 
        self.pos = pygame.math.Vector2(x, y)
        self.move = pygame.math.Vector2()
        try:
            self.image = pygame.image.load('image.png')
        except:
            self.image = pygame.Surface((20, 20))
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(midbottom = (round(self.pos.x), round(self.pos.y)))

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.move.x -= 50
        if pressed[K_RIGHT]:
            self.move.x += 50
        if pressed[K_UP]:
            self.move.y = -1000

        self.pos = self.pos + self.move * time_passed
        self.move.x *= 0.8 # slow down (decrease progressively)
        self.move.y += 5000 * time_passed

        if self.pos.y > 600:
            self.pos.y = 600

        self.rect = self.image.get_rect(midbottom = (round(self.pos.x), round(self.pos.y)))
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.centerx
        if self.rect.right > 800:
            self.rect.right = 800
            self.pos.x = self.rect.centerx

player = Player(player_x, player_y)
clock = pygame.time.Clock()
onground = True
platforms = []
bullet = []
enemy = []

def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+1, pos[1]+1)
    innerSize = ((size[0]-2) * progress, size[1]-2)
    rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
    pygame.draw.rect(surf, healthC, rect)

def createplatform(x,y,width,height, type):
   newplatform = Empty()
   newplatform.x = x
   newplatform.y = y
   newplatform.width = width
   newplatform.height = height
   newplatform.type = type
   platforms.append(newplatform)

def createnewenemy(x,y):
   newenemy = Empty()
   newenemy.posx = x
   newenemy.posy = height-y
   newenemy.attacktimer=random.uniform(300,400)
   newenemy.velx = 0
   newenemy.vely = 0
   newenemy.health = 3
   newenemy.hurt = 0
   enemy.append(newenemy)

def createbullet_p(x,y,right=True, safe=False,vely=0,duration=500,bullettype=""):
   newbullet = Empty()
   newbullet.posx = x
   newbullet.posy = y+size/2
   if right == True:
      newbullet.velx = 4
   else:
      newbullet.velx = -4
   newbullet.vely = vely
   newbullet.duration = duration
   newbullet.safe = safe
   newbullet.type = bullettype
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
createnewenemy(800,450)
for a in levels:
   createplatform(a[0],height-a[1],a[2],a[3],a[4])
#createplatform(300,height-75,80,20)

guncd = 0

def shoot(type,guncd):
    if type == 1 and guncd == 0:
         createbullet_p(player_x-5 if right == False else player_x+5+size,player_y,right,True)
         return 60
    if type == 2 and guncd == 0:
         createbullet_p(player_x-8 if right == False else player_x+8+size,player_y,right,True,-1,75,"shotgun")
         createbullet_p(player_x-8 if right == False else player_x+8+size,player_y,right,True,1,75,"shotgun")
         createbullet_p(player_x-5 if right == False else player_x+5+size,player_y,right,True,0,75,"shotgun")
         createbullet_p(player_x-6 if right == False else player_x+6+size,player_y,right,True,-1/3,75,"shotgun")
         createbullet_p(player_x-6 if right == False else player_x+6+size,player_y,right,True,1/3,75,"shotgun")

         createbullet_p(player_x-4 if right == False else player_x+4+size,player_y,right,True,1/2,75,"shotgun")
         createbullet_p(player_x-4 if right == False else player_x+4+size,player_y,right,True,-1/2,75,"shotgun")
         createbullet_p(player_x-10 if right == False else player_x+10+size,player_y,right,True,-1/4,75,"shotgun")
         createbullet_p(player_x-10 if right == False else player_x+10+size,player_y,right,True,1/4,75,"shotgun")
         createbullet_p(player_x-12 if right == False else player_x+12+size,player_y,right,True,1/5,75,"shotgun")
         createbullet_p(player_x-12 if right == False else player_x+12+size,player_y,right,True,-1/5,75,"shotgun")
         return 240
    return guncd
level = 0

equippedgun = 1
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
            #player_x_vel = -2.5
         if i.key == pygame.K_d:
            right=True
            #player_x_vel = 2.5
         if i.key == pygame.K_LSHIFT:
            player_x_vel *= 2
         if i.key == pygame.K_r:
            player_x= 20
            player_y= height-size
         if i.key == pygame.K_1:
            equippedgun = 1
         if i.key == pygame.K_2:
            equippedgun = 2
         if i.key == pygame.K_e:
            guncd = shoot(equippedgun,guncd)
      keys = pygame.key.get_pressed()
      player_x_vel = (keys[pygame.K_d] - keys[pygame.K_a]) * 2.5  
      if i.type == pygame.MOUSEBUTTONDOWN:
         if i.button == 1:
            guncd = shoot(equippedgun,guncd)

            #elif event.button == 2:
                #print("middle mouse button")
            #elif event.button == 3:
                #print("right mouse button")
            #elif event.button == 4:
             #   print("mouse wheel up")
            #elif event.button == 5:
                #print("mouse wheel down")
     # if i.type == pygame.KEYUP:
        # if i.key == pygame.K_a or i.key == pygame.K_d:
           #player_x_vel = 0
    player_x += player_x_vel
    player_y += player_y_vel
    onground = False
    if player_x+size > width:
       player_x = width-size
    elif player_x < 0:
       player_x = 0

    if player_y+size> height:
       player_y = height-size
    elif player_y < 0-size:
       player_y_vel = 0
    
    if player_y+size == height:
       onground = True
       player_y_vel = 0
    #movement done

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
         pygame.draw.circle(wn, (255,0,0), (x.posx+3 if x.velx > 0 else x.posx-3,x.posy),2)
       else: 
         pygame.draw.circle(wn, (255,255,0), (x.posx,x.posy),4)

    rect = pygame.Rect(player_x,player_y, size, size)

    for x in enemy:
          draw_health_bar(wn , (x.posx-10,x.posy-10), (40,5), (0,0,0), (255,0,0), (0,255,0), x.health/3)
          x.velx = random.uniform(3,-3)/2
          x.vely += 0.25
          x.attacktimer += 1
          if x.attacktimer > 550 and player_y+size/2 >= x.posy >=player_y-size/2:
                x.attacktimer = 0
                createbullet_p(x.posx,x.posy, True if player_x-x.posx >= 0 else False)
          x.posx += x.velx
          x.posy += x.vely
          if x.posx+size> width:
                    x.posx = width-size
          elif x.posx-size < 0:
                    x.posx = 0+size

          if x.posy+size> height:
                    x.posy = height-size
          if x.hurt > 0: 
              pygame.draw.rect(wn, (255,0,0), pygame.Rect(x.posx,x.posy,size,size))
              x.hurt -=1
          else: pygame.draw.rect(wn, (50,150,255), pygame.Rect(x.posx,x.posy,size,size))

    for x in platforms:
        if x.type == "end":
               pygame.draw.rect(wn, (0,200,0), pygame.Rect(x.x, x.y, x.width, x.height))
        elif x.type == "jump":
               pygame.draw.rect(wn, (100,255,100), pygame.Rect(x.x, x.y, x.width, x.height))
        else: pygame.draw.rect(wn, (239,163,55), pygame.Rect(x.x, x.y, x.width, x.height))
        rectplatform = pygame.Rect(x.x,x.y, x.width, x.height)
            #print(x.x,x.y,x.width,x.height,player_x,player_y, x.x+x.width,x.y+x.height)
        collide = rect.colliderect(rectplatform)
        for e in enemy:
            rectenemy = pygame.Rect(e.posx,e.posy, size,size)
            enemycollide = rectenemy.colliderect(rectplatform)
            if enemycollide:
                e.posy = x.y-size
                e.vely = 0
        for b in bullet: 
                rectbullet = pygame.Rect(b.posx,b.posy,3,3)
                bulletcollide = rectbullet.colliderect(rectplatform)
                playercollide = rectbullet.colliderect(rect)
                for e in enemy:
                    rectenemy = pygame.Rect(e.posx,e.posy, size,size)
                    shootenemy = rectenemy.colliderect(rectbullet)
                    
                    if shootenemy and b.safe == True:
                        if b.type == "shotgun": e.health -= 0.25
                        else: e.health -= 1
                        
                        e.hurt= 10
                        bullet.remove(b)
                        e.posx+=b.velx/2
                        if e.health < 1:
                            enemy.remove(e)
                        continue
                if playercollide and b.safe == False:
                    player_x = 20
                    player_y = height-size
                    bullet.remove(b)
                    continue
                if bulletcollide:
                    b.velx *=-1
        if collide:
         if x.y+10 >= player_y+size >=x.y or (x.type=="jump" and x.y+10+x.height/3 >= player_y+size >=x.y):
            onground=True
            player_y = x.y-size
            if x.type == "jump":
                player_y_vel= player_y_vel*-1 - 8
                continue
            if x.type == "end":
               player_x = 20
               player_y = height-size
               level +=1
               platforms = []
               enemy = []
               bullet = []
               if level == 1:
                  levels = [
                           [50,75,80,20,""],
                           [100,150,150,20,""],
                           [150,200,90,20,""],
                           [200,250,150,20,""],
                           [250,300,150,20,""],
                           [200,350,100,25,""],
                           [700,350,100,25,""],
                           [500,300,250,25,""],
                           [400,250,50,20,""],
                           [600,300,50,20,""],
                           [650,500,50,20,""],
                           [700,450,50,20,""],
                           [900,400,50,20,""],
                           [800,350,50,20,""],
                           [500,550,80,40,"end"]
                           ]
                  createnewenemy(500,450)
                  createnewenemy(800,550)
               if level == 2:
                  levels = [
                           [100,80,50,20,""],
                           [200,180,50,20,""],
                           [300,280,50,20,""],
                           [400,380,50,20,""],
                           [500,440,50,20,""],
                           [600,380,50,20,""],
                           [700,280,50,20,""],
                           [800,180,50,20,""],
                           [900,80,50,20,""],
                           [150,130,50,20,""],
                           [250,230,50,20,""],
                           [350,330,50,20,""],
                           [450,4300,50,20,""],
                           [650,330,50,20,""],
                           [750,230,50,20,""],
                           [850,130,50,20,""],
                           [300,100,150,20,""],
                           [500,100,150,20,""],
                           [950,125,50,20,"jump"],
                           [800,550,50,20,"end"]
                           ]
                  createnewenemy(500,450)
                  createnewenemy(800,450)
                  createnewenemy(500,450)
                  createnewenemy(800,450)

               if level == 3:  
                     levels = [
                           [100,80,50,20,""],
                           [200,140,50,20,""],
                           [300,80,50,20,""],
                           [400,140,50,20,""],
                           [500,80,50,20,""],
                           [600,140,50,20,""],
                           [700,80,50,20,""],
                           [800,140,50,20,""],
                           [900,80,50,20,""],

                           [150,210,50,20,""],
                           [250,280,50,20,""],
                           [350,210,50,20,""],
                           [450,280,50,20,""],
                           [550,300,50,20,"jump"],
                           [650,210,50,20,""],
                           [750,280,50,20,""],
                           [850,210,50,20,""],
                           [400,500,50,20,"end"]
                           ]
                     createnewenemy(100,450)
                     createnewenemy(200,450)
                     createnewenemy(300,450)
                     createnewenemy(400,450)
                     createnewenemy(500,450)
                     createnewenemy(600,450)
                     createnewenemy(700,450)
                     createnewenemy(800,450)
                     createnewenemy(850,450)
                     createnewenemy(350,450)
                     createnewenemy(250,450)
                     createnewenemy(550,450)
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