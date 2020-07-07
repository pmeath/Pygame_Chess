from pygame_Chess import *


class Piece:
    def __init__(self, colour, location):
        self.colour = colour
        self.location = location


class Pawn(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_pawn_img, black_pawn_img)
        self.has_moved = False

    def first_move(self):
        self.location[1] += 2
        self.has_moved = True

    # def promote():

    def move(self):
        self.location[1] += 1
        self.has_moved = True
        if self.location[1] == 8:
            self.promote

    def take(self, direction):
        Piece.location[1] += 1
        Piece.location[0] += direction
        Piece.has_moved = True


class Knight(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_knight_img, black_knight_img)


class Bishop(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_bishop_img, black_bishop_img)


class Rook(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_rook_img, black_rook_img)


class Queen(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_queen_img, black_queen_img)


class King(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (white_king_img, black_king_img)
        self.has_moved = False

    def move(self, direction):
        Piece.has_moved = True


pieces = []


def populate():
    c = 0
    for c in range(2):
        for x in range(8):
            pieces.append(Pawn(c, [x, 1 + c * 5]))
        pieces.append(Rook(c, [0, c * 7]))
        pieces.append(Rook(c, [7, c * 7]))
        pieces.append(Bishop(c, [2, c * 7]))
        pieces.append(Bishop(c, [5, c * 7]))
        pieces.append(Knight(c, [1, c * 7]))
        pieces.append(Knight(c, [6, c * 7]))
        pieces.append(Queen(c, [3, c * 7]))
        pieces.append(King(c, [4, c * 7]))
