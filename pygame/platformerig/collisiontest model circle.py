import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))
radius = 25
rect = pygame.Rect(125-radius, 125-radius, radius*2, radius*2)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()
    collide = rect.collidepoint(point)
    color = (255, 0, 0) if collide else (255, 255, 255)

    window.fill(0)
    pygame.draw.circle(window, color, rect.center,radius)
    pygame.display.flip()

pygame.quit()
exit()