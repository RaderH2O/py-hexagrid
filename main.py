import pygame
from pygame.locals import *
from math import cos, sin, tan, pi, sqrt

pygame.init()

radius = 4 # the radius of the circle that the hexagon is in

WIDTH = 1024
HEIGHT = 720

win = pygame.display.set_mode((WIDTH, HEIGHT))
running = True # shows if the application is running or not

def d2r(degree): # degree to radian
    return degree/180 * pi

def draw_hexagon(win, x, y, r, color=(255, 255, 255)):
    pygame.draw.line(win, color, (x+r*cos(d2r(0)), y-r*sin(d2r(0))), (x+r*cos(d2r(60)), y-r*sin(d2r(60))))
    pygame.draw.line(win, color, (x+r*cos(d2r(60)), y-r*sin(d2r(60))), (x-r*cos(d2r(60)), y-r*sin(d2r(60))))
    pygame.draw.line(win, color, (x-r*cos(d2r(60)), y-r*sin(d2r(60))), (x-r*cos(d2r(0)), y-r*sin(d2r(0))))
    pygame.draw.line(win, color, (x-r*cos(d2r(0)), y-r*sin(d2r(0))), (x-r*cos(d2r(60)), y+r*sin(d2r(60))))
    pygame.draw.line(win, color, (x-r*cos(d2r(60)), y+r*sin(d2r(60))), (x+r*cos(d2r(60)), y+r*sin(d2r(60))))
    pygame.draw.line(win, color, (x+r*cos(d2r(60)), y+r*sin(d2r(60))), (x+r*cos(d2r(0)), y-r*sin(d2r(0))))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for y in range(HEIGHT//(radius)):
        for x in range(WIDTH//(2*radius)):
            draw_hexagon(win, x*3*radius, y*2*(radius - radius/2*tan(d2r(15))) + (radius - radius/2 * tan(d2r(15))), radius)
            draw_hexagon(win, x*3*radius + 3*radius/2, y*2*(radius - radius/2*tan(d2r(15))), radius)
    pygame.display.update()
    win.fill((0,0,0))

pygame.quit()