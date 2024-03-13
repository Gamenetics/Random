import pygame
import random

pygame.init()

pygame.display.set_caption = "Genshin Impact 2"

gadget_pair = 1
gadget_pair = int(input("Enter your choice for gadget pair: "))


ballcolor = (0, 0 ,225)
wallcolor = (255, 0 ,0)
width, height = 1000, 600
size = 15
b_x, b_y = width/2 - size, height/2 - size
bx_vel, by_vel = 0.7,0.7

db_x, db_y = width/2 - size, height/2 - size
dbx_vel, dby_vel = 0.7,0.7

paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = height/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, width - (100 - paddle_width/2)
left_vel = right_vel = 0

wn = pygame.display.set_mode((width, height))
run = True
direction =[0,1]
angle = [0, 1, 2]

left_gadget = right_gadget = 0
left_gadget_re = right_gadget_re = 5

while run:
    wn.fill((0, 0 ,0))
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
         run = False
      elif i.type == pygame.KEYDOWN:
         if i.key == pygame.K_UP:
            right_vel = -0.9
         if i.key == pygame.K_DOWN:
            right_vel = 0.9
         if i.key == pygame.K_RIGHT and right_gadget_re > 0:
            right_gadget = 1
         if i.key == pygame.K_LEFT and right_gadget_re > 0:
            right_gadget = 2
         if i.key == pygame.K_d and left_gadget_re > 0:
            left_gadget = 1
         if i.key == pygame.K_a and left_gadget_re > 0:
            left_gadget = 2
         if i.key == pygame.K_w:
            left_vel = -0.9
         if i.key == pygame.K_s:
            left_vel = 0.9
      if i.type == pygame.KEYUP:
            right_vel = 0
            left_vel = 0

    if b_y <= 0+size or b_y >= height - size: by_vel *=-1
    if db_y <= 0+size or db_y >= height - size: dby_vel *=-1
    if b_x >= width - size: 
       b_x, b_y = width/2 - size, height/2 - size
       db_x, db_y = width/2 - size, height/2 - size
       dir = random.choice(direction)
       ang = random.choice(angle)
       if dir == 0:
          if ang == 0:
            
             by_vel, bx_vel = -1.4, 0.7
             dby_vel, dbx_vel = -1.4, 0.7
          if ang == 1:
             by_vel, bx_vel = -0.7, 0.7
             dby_vel, dbx_vel = -0.7, 0.7
          if ang == 3:
             by_vel, bx_vel = -0.7, 1.4
             dby_vel, dbx_vel = -0.7, 1.4
       if dir == 1:
          if ang == 0:
             by_vel, bx_vel = 1.4, 0.7
             dby_vel, dbx_vel = 1.4, 0.7
          if ang == 1:
             by_vel, bx_vel = 0.7, 0.7
             dby_vel, dbx_vel = 0.7, 0.7
          if ang == 3:
             by_vel, bx_vel = 0.7, 1.4
             dby_vel, dbx_vel = 0.7, 1.4
       bx_vel *=-1
       dbx_vel *=-1
    if b_x <= 0 + size: 
       b_x, b_y = width/2 - size, height/2 - size
       db_x, db_y = width/2 - size, height/2 - size
       dir = random.choice(direction)
       ang = random.choice(angle)
       if dir == 0:
          if ang == 0:
             by_vel, bx_vel = -1.4, 0.7
             dby_vel, dbx_vel = -1.4, 0.7
          if ang == 1:
             by_vel, bx_vel = -0.7, 0.7
             dby_vel, dbx_vel = -0.7, 0.7
          if ang == 3:
             by_vel, bx_vel = -0.7, 1.4
             dby_vel, dbx_vel = -0.7, 1.4
       if dir == 1:
          if ang == 0:
             by_vel, bx_vel = 1.4, 0.7
             dby_vel, dbx_vel = 1.4, 0.7
          if ang == 1:
             by_vel, bx_vel = 0.7, 0.7
             dby_vel, dbx_vel = 0.7, 0.7
          if ang == 3:
             by_vel, bx_vel = 0.7, 1.4
             dby_vel, dbx_vel = 0.7, 1.4
       bx_vel *=-1
       dbx_vel *=-1

    b_x += bx_vel
    b_y += by_vel
    db_x += dbx_vel
    db_y += dby_vel
    left_paddle_y += left_vel
    right_paddle_y += right_vel
    if left_paddle_y >= height - paddle_height: 
       left_paddle_y = height - paddle_height
    if left_paddle_y <= 0: 
       left_paddle_y = 0
    if right_paddle_y >= height - paddle_height: 
       right_paddle_y = height - paddle_height
    if right_paddle_y <= 0: 
       right_paddle_y = 0
    
    if gadget_pair == 1: 
       if left_gadget == 1 and left_paddle_x <= b_x <= left_paddle_x + paddle_width:
         if left_paddle_y <= b_y <= left_paddle_y + paddle_height:
            b_x = left_paddle_x + paddle_width
            bx_vel *= -3.5
            dbx_vel *= -3.5
            left_gadget = 0
            left_gadget_re -= 1
       elif left_gadget == 2:
            left_paddle_y = b_y
            left_gadget = 0
            left_gadget_re -= 1 
       elif left_gadget == 3 and left_paddle_x <= b_x <= left_paddle_x + paddle_width:
         if left_paddle_y <= b_y <= left_paddle_y + paddle_height:
            b_x = left_paddle_x + paddle_width
            bx_vel *= -3.5
            dbx_vel *= -3.5
            left_gadget = 0
            left_gadget_re -= 1

    if right_gadget == 1 and right_paddle_x <= b_x <= right_paddle_x + paddle_width:
       if right_paddle_y <= b_y <= right_paddle_y + paddle_height:
          b_x = right_paddle_x + paddle_width
          bx_vel *= -3.5
          right_gadget = 0
          right_gadget_re -= 1
    elif right_gadget == 2:
       right_paddle_y = b_y
       right_gadget = 0
       right_gadget_re -= 1
    elif right_gadget == 3 and right_paddle_x <= b_x <= right_paddle_x + paddle_width:
       if right_paddle_y <= b_y <= right_paddle_y + paddle_height:
          b_x = right_paddle_x + paddle_width
          bx_vel *= -3.5
          right_gadget = 0
          right_gadget_re -= 1
    elif gadget_pair == 2:
      if left_gadget == 1 and left_paddle_y <= b_y <= left_paddle_y + paddle_height:
          b_x = left_paddle_x + paddle_width
          bx_vel *= -1
          db_x = left_paddle_x + paddle_width
          dbx_vel *= -1
          dby_vel *= -1
          left_gadget = 0
          left_gadget_re -= 1
      elif right_gadget == 1 and right_paddle_x <= b_x <= right_paddle_x + paddle_width:
         if right_paddle_y <= b_y <= right_paddle_y + paddle_height:
            b_x = right_paddle_x
            bx_vel *= -1
            db_x = right_paddle_x
            dbx_vel *= -1
            dby_vel *= -2
            right_gadget = 0
            right_gadget_re -= 1
         
    if left_paddle_x <= b_x <= left_paddle_x + paddle_width:
       if left_paddle_y <= b_y <= left_paddle_y + paddle_height:
          b_x = left_paddle_x + paddle_width
          bx_vel *= -1
          db_x = left_paddle_x + paddle_width
          dbx_vel *= -1

    if right_paddle_x <= b_x <= right_paddle_x + paddle_width:
       if right_paddle_y <= b_y <= right_paddle_y + paddle_height:
          b_x = right_paddle_x
          bx_vel *= -1
          db_x = right_paddle_x
          dbx_vel *= -1
    font = pygame.font.SysFont('callibri', 32)
    pygame.draw.circle(wn, ballcolor, (b_x,b_y), size)
    pygame.draw.rect(wn, wallcolor, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, wallcolor, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.draw.circle(wn, ballcolor, (db_x,db_y), size)

    if left_gadget == 1:
       pygame.draw.circle(wn, (255,255,255), (left_paddle_x + 10, left_paddle_y +10), 4)
    if right_gadget == 1:
       pygame.draw.circle(wn, (255,255,255), (right_paddle_x + 10, right_paddle_y +10), 4)
    pygame.display.update()