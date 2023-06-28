import pyautogui
import win32gui
import sys
import pygame
import os
from pygame.locals import *

def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x+15, y+14, x1-26-15, y1-146-14))

            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

def draw_circle():
    pos=pygame.mouse.get_pos()
    pygame.draw.circle(screen, pygame.Color(0, 0, 0), pos, 5)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), pos, 4)
    return pos

def draw_line(pos1, pos2):
    pygame.draw.line(screen, pygame.Color(0, 0, 0), pos1, pos2)


im = screenshot('Graphwar')
im.save('war.png')

x = 1000
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = im.width, im.height
screen = pygame.display.set_mode((width, height))
bg_img = pygame.image.load('war.png')
screen.blit(bg_img, (0, 0))
pygame.display.set_caption('death')
prev = None

pos = []
runnning = True
while runnning:
    fpsClock.tick(fps)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            now = draw_circle()
            pos.append(now)
            if prev is not None:
                draw_line(now, prev)
            prev = now
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                pygame.quit()
                runnning = False


print(pos)
print(width)

pos = [(round(i*50/width-25, 2), round((height-j)*30/height-15, 2)) for i, j in pos]
arr = []
for i in range(len(pos)-1):
    x1, y1 = pos[i]

    x2, y2 = pos[i+1]
    arr.append(f'(({y2}-({y1}))/({x2}-({x1})))(0.5)(abs(x-({x1})) - abs(x-({x2})))')
f = '+'.join(arr)
print(pos)

import pyperclip
pyperclip.copy(f)
print(f)