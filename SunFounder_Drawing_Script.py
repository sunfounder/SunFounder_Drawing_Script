'''
**********************************************************************
* Filename    : SunFounder_Drawing.py
* Description : A simple draw on screen script base on pygame
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : support@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-10-10    New release
**********************************************************************
'''
import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()
display_res = pygame.display.Info()
screen=pygame.display.set_mode((display_res.current_w, display_res.current_h), FULLSCREEN | NOFRAME, 32)
#screen=pygame.display.set_mode((320, 240), NOFRAME, 32)

# Change The Line Width Here!
LINE_WIDTH = 10


WHITE   = (200,	200, 190)
BLACK   = ( 39,  40,  34)
RED	    = (249,  38, 114)
ORANGE  = (253, 151,  31)
YELLOW  = (255, 231, 146)
GREEN   = (166, 226,  46)
CYAN    = ( 39, 239, 239)
BLUE    = ( 39,  39, 239)
PURPLE  = (153, 100, 239)

GRID = (display_res.current_w/8, display_res.current_h/9)

DRAW_BAR_RECT    = Rect(0, 0, display_res.current_w - GRID[0], display_res.current_h)
TOOL_BAR_RECT    = Rect(DRAW_BAR_RECT.width, 0, display_res.current_w, display_res.current_h)
BUTTON_RECT      = Rect(0, 0, GRID[0]*0.9, GRID[1]*0.9)
EXIT_BUTTON_RECT = BUTTON_RECT.copy()
RED_RECT         = BUTTON_RECT.copy()
ORANGE_RECT      = BUTTON_RECT.copy()
YELLOW_RECT      = BUTTON_RECT.copy()
GREEN_RECT       = BUTTON_RECT.copy()
CYAN_RECT        = BUTTON_RECT.copy()
BLUE_RECT        = BUTTON_RECT.copy()
PURPLE_RECT      = BUTTON_RECT.copy()
CLEAR_RECT       = BUTTON_RECT.copy()

EXIT_BUTTON_RECT.center = ((display_res.current_w-(GRID[0]/2)), ((GRID[1]/2) + (GRID[1] * 0)))
RED_RECT.center         = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 1))
ORANGE_RECT.center      = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 2))
YELLOW_RECT.center      = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 3))
GREEN_RECT.center       = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 4))
CYAN_RECT.center        = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 5))
BLUE_RECT.center        = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 6))
PURPLE_RECT.center      = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 7))
CLEAR_RECT.center       = (EXIT_BUTTON_RECT.centerx, (GRID[1]/2) + (GRID[1] * 8))

def draw_line(color, start_pos, end_pos):
	#pygame.draw.aaline(screen, color, start_pos, end_pos, 1)

	pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
	pygame.draw.circle(screen, color, end_pos, LINE_WIDTH/2)

def setup():
	screen.set_clip((0, 0, display_res.current_w, display_res.current_h))
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, EXIT_BUTTON_RECT, 5)
	pygame.draw.line(screen, WHITE, EXIT_BUTTON_RECT.topleft, EXIT_BUTTON_RECT.bottomright, 5)
	pygame.draw.line(screen, WHITE, EXIT_BUTTON_RECT.topright, EXIT_BUTTON_RECT.bottomleft, 5)
	pygame.draw.ellipse(screen, RED, RED_RECT, 0)
	pygame.draw.ellipse(screen, ORANGE, ORANGE_RECT, 0)
	pygame.draw.ellipse(screen, YELLOW, YELLOW_RECT, 0)
	pygame.draw.ellipse(screen, GREEN, GREEN_RECT, 0)
	pygame.draw.ellipse(screen, CYAN, CYAN_RECT, 0)
	pygame.draw.ellipse(screen, BLUE, BLUE_RECT, 0)
	pygame.draw.ellipse(screen, PURPLE, PURPLE_RECT, 0)
	pygame.draw.ellipse(screen, WHITE, CLEAR_RECT, 0)
	pygame.display.update()
	screen.set_clip(DRAW_BAR_RECT)
	screen.fill(WHITE)
	pygame.display.update()

def main():
	Draw = False
	current_color = CYAN
	pos = (0, 0)
	last_pos = (0, 0)
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				start_point = pygame.mouse.get_pos()
				pygame.draw.circle(screen, current_color, start_point, LINE_WIDTH/2)
				Draw = True
			if event.type == MOUSEBUTTONUP:
				Draw = False
				pos = pygame.mouse.get_pos()

		if Draw:
			if pos != last_pos and TOOL_BAR_RECT.collidepoint(pos):
				if EXIT_BUTTON_RECT.collidepoint(pos):
					exit()
				elif RED_RECT.collidepoint(pos):
					current_color = RED
				elif ORANGE_RECT.collidepoint(pos):
					current_color = ORANGE
				elif YELLOW_RECT.collidepoint(pos):
					current_color = YELLOW
				elif GREEN_RECT.collidepoint(pos):
					current_color = GREEN
				elif CYAN_RECT.collidepoint(pos):
					current_color = CYAN
				elif BLUE_RECT.collidepoint(pos):
					current_color = BLUE
				elif PURPLE_RECT.collidepoint(pos):
					current_color = PURPLE
				elif CLEAR_RECT.collidepoint(pos):
					screen.fill(WHITE)
				last_pos = pos
			else:
				end_point = pygame.mouse.get_pos()
				draw_line(current_color, start_point, end_point)
				start_point = end_point
	 
			pygame.display.update()

if __name__ == '__main__':
	setup()
	main()