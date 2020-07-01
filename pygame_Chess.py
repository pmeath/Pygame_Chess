import pygame
from pygame import *
import os
import sys
import pieces.py
def set_dir():
	abspath = os.path.abspath(sys.argv[0])
	dname = os.path.dirname(abspath)
	os.chdir(dname)

# define a main function
def main():
	set_dir()
    # initialize the pygame module
	init()
    # load and set the logo
	logo = image.load("Chess_logo.png")
	display.set_icon(logo)
	display.set_caption("Chess")
    # create a surface on screen
	screen = display.set_mode((600,600), HWSURFACE|DOUBLEBUF)
	bkg = image.load("Chess_board.png")
	screen.blit(transform.scale(bkg, screen.get_size()), (0, 0))
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
