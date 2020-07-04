import pygame
from pygame import *
import os
import sys
from piece_objects import *

print(os.getcwd())
def set_dir():
	abspath = os.path.abspath(sys.argv[0])
	dname = os.path.dirname(abspath)
	os.chdir(dname)
	
	
def draw_pieces():
	img = image.load("white_pawn.png")
	for i in pieces:
		screen.blit(transform.scale(img, (i.location[0], i.location[1]))
		print(str(i))

screen = display.set_mode((600,600), HWSURFACE|DOUBLEBUF)

tile_size = (screen.get_size()[0]/8, screen.get_size()[1]/8)
print(tile_size)

def main():
    # initialize the pygame module
	init()
    # load and set the logo
	logo = image.load("Chess_logo.png")
	display.set_icon(logo)
	display.set_caption("Chess")
    # create a surface on screen
	
	bkg = image.load("Chess_board.png")
	screen.blit(transform.scale(bkg, screen.get_size()), (0, 0))
	populate()
	draw_pieces()
	display.flip()

	# define a variable to control the main loop
	running = True

    # main loop
	while running:
		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == QUIT:
				# change the value to False, to exit the main loop
				running = False
			
				
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
