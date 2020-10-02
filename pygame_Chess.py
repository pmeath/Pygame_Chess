import pygame
from pygame import *
from pieces import *

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
    global previous_moves
    global active_piece
    for i in pieces:
        if i.location == tile_clicked:
            if active_piece == 0:  # select the piece
                draw_pieces()
                screen.blit(select_img, click_location)
                display.flip()
                active_piece = i
            elif i == active_piece:  # deselect the piece
                active_piece = 0
                draw_pieces()
                display.flip()
            elif i.colour == active_piece.colour:  # change selected piece.
                draw_pieces()
                screen.blit(select_img, click_location)
                display.flip()
                active_piece = i
            else:  # capture a piece
                if active_piece.can_take(tile_clicked):
                    previous_moves.append((active_piece, active_piece.location, i))
                    pieces.remove(i)
                    active_piece.location = tile_clicked

                if isinstance(active_piece, Pawn):
                    if active_piece.promotion(1):
                        pieces.remove(active_piece)

                draw_pieces()
                display.flip()
                active_piece = 0

            return
    if active_piece:  # move to an empty square
        if active_piece.can_move(tile_clicked):
            previous_moves.append((active_piece, active_piece.location))
            active_piece.location = tile_clicked
            if isinstance(active_piece, Pawn):
                if active_piece.promotion(1):
                    pieces.remove(active_piece)



        elif isinstance(active_piece, Pawn):    # en passant
            pawn = active_piece.en_passant(tile_clicked)
            if pawn:
                for l in pieces:
                    if l.location == pawn.location:
                        previous_moves.append((active_piece, active_piece.location, l))
                        pieces.remove(l)
                        break
                active_piece.location = tile_clicked

        elif isinstance(active_piece, King):  # castling
            rook = active_piece.castle(tile_clicked)
            if rook:
                previous_moves.append((active_piece, active_piece.location, rook, rook.location))
                active_piece.has_moved = True
                rook.has_moved = True
                if rook.location[0]:
                    rook.location[0] = 5  # right
                    active_piece.location[0] = 6
                else:
                    rook.location[0] = 3  # left
                    active_piece.location[0] = 2

        draw_pieces()
        display.flip()
        active_piece = 0


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
