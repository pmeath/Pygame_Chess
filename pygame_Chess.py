import pygame
from pygame import *
import os
import sys
from pieces import *


def set_dir():
    abspath = os.path.abspath(sys.argv[0])
    dname = os.path.dirname(abspath)
    os.chdir(dname)


screen = display.set_mode((600, 600), HWSURFACE | DOUBLEBUF)
tile_size = (int(screen.get_size()[0] / 8), int((screen.get_size()[1] / 8)))

white_pawn_img = transform.scale(image.load("white_pawn.png"), tile_size)
white_knight_img = transform.scale(image.load("white_knight.png"), tile_size)
white_bishop_img = transform.scale(image.load("white_bishop.png"), tile_size)
white_rook_img = transform.scale(image.load("white_rook.png"), tile_size)
white_queen_img = transform.scale(image.load("white_queen.png"), tile_size)
white_king_img = transform.scale(image.load("white_king.png"), tile_size)
black_pawn_img = transform.scale(image.load("black_pawn.png"), tile_size)
black_knight_img = transform.scale(image.load("black_knight.png"), tile_size)
black_bishop_img = transform.scale(image.load("black_bishop.png"), tile_size)
black_rook_img = transform.scale(image.load("black_rook.png"), tile_size)
black_queen_img = transform.scale(image.load("black_queen.png"), tile_size)
black_king_img = transform.scale(image.load("black_king.png"), tile_size)
marker_img = transform.scale(image.load("marker.png"), tile_size)


def draw_pieces():
    for i in pieces:
        screen.blit(i.img[i.colour], (i.location[0] * tile_size[0], i.location[1] * tile_size[1]))


def right_click(position):
    click_location = (((position[0]//tile_size[0])*tile_size[0], (position[1]//tile_size[1])*tile_size[1]))
    screen.blit(marker_img, click_location)
    display.flip()


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
            if event.type == pygame.MOUSEBUTTONUP:
                position = mouse.get_pos()
                if event.button == 3:
                    right_click(position)

            if event.type == QUIT:
                # change the value to False, to exit the main loop
                running = False




# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
