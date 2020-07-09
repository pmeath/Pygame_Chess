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

board = image.load("Chess_board.png")
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
select_img = transform.scale(image.load("selected.png"), tile_size)


def draw_pieces():
    screen.blit(transform.scale(board, screen.get_size()), (0, 0))
    for i in pieces:
        screen.blit(i.img[i.colour], (i.location[0] * tile_size[0], i.location[1] * tile_size[1]))


def right_click(position):
    click_location = ((position[0] // tile_size[0]) * tile_size[0], (position[1] // tile_size[1]) * tile_size[1])
    draw_pieces()
    screen.blit(marker_img, click_location)
    display.flip()





def left_click(position):
    tile_clicked = [(position[0] // tile_size[0]), (position[1] // tile_size[1])]
    click_location = (tile_clicked[0] * tile_size[0], tile_clicked[1] * tile_size[1])
    global pieces
    for i in pieces:
        if i.location == tile_clicked:
            global active_piece
            if i == active_piece:
                active_piece = null_piece
                draw_pieces()
                display.flip()
            elif i.colour == active_piece.colour:
                draw_pieces()
                screen.blit(select_img, click_location)
                display.flip()
                active_piece = i
            elif i.colour + active_piece.colour == 1:
                pieces.remove(i)
                active_piece.location = tile_clicked
                draw_pieces()
                display.flip()
            else:
                draw_pieces()
                screen.blit(select_img, click_location)
                display.flip()
                active_piece = i
            return
    print(null_piece)
    if active_piece != null_piece:
        active_piece.location = tile_clicked
        draw_pieces()
        display.flip()
        active_piece = null_piece


def main():
    # initialize the pygame module
    init()
    # load and set the logo
    logo = image.load("Chess_logo.png")
    display.set_icon(logo)
    display.set_caption("Chess")
    # create a surface on screen

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
                if event.button == 1:
                    left_click(position)
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
