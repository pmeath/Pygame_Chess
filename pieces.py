from pygame_Chess import *


class Piece:
    def __init__(self, colour, location):
        self.colour = colour
        self.location = location


class Pawn(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_pawn_img, white_pawn_img)
        self.has_moved = False

    def can_move(self, destination):
        if ((destination[0] - self.location[0]) == 0) & ((destination[1] - self.location[1]) == 1 - (2 * self.colour)):
            self.has_moved = True
            return True
        elif (self.has_moved == False) & ((destination[0] - self.location[0]) == 0) & ((destination[1] - self.location[1]) == 2 - (4 * self.colour)):
            self.has_moved = True
            return True
        else:
            return False

    def take(self, direction):
        Piece.location[1] += 1
        Piece.location[0] += direction
        Piece.has_moved = True


class Knight(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_knight_img, white_knight_img)

    def can_move(self, destination):
        if (abs(destination[0] - self.location[0]) == 2) & (abs(destination[1] - self.location[1]) == 1):
            return True
        elif (abs(destination[0] - self.location[0]) == 1) & (abs(destination[1] - self.location[1]) == 2):
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_bishop_img, white_bishop_img)

    def can_move(self, destination):
        if abs(destination[0] - self.location[0]) == abs(destination[1] - self.location[1]):
            return True
        else:
            return False


class Rook(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_rook_img, white_rook_img)

    def can_move(self, destination):
        if (destination[0] == self.location[0]) | (destination[1] == self.location[1]):
            return True
        else:
            return False


class Queen(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_queen_img, white_queen_img)

    def can_move(self, destination):
        if ((destination[0] == self.location[0]) | (destination[1] == self.location[1])) | (abs(destination[0] - self.location[0]) == abs(destination[1] - self.location[1])):
            return True
        else:
            return False


class King(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_king_img, white_king_img)
        self.has_moved = False

    def can_move(self, destination):

        if (abs(destination[0] - self.location[0]) <= 1) & (abs(destination[1] - self.location[1]) <= 1):
            Piece.has_moved = True
            return True
        else:
            return False


null_piece = Piece(-1, [-1, -1])
active_piece = null_piece
pieces = []


def populate():
    c = 0   # black is 0 and white is 1
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
