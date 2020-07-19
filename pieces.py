from pygame_Chess import *


class Piece:
    def __init__(self, colour, location):
        self.colour = colour
        self.location = location

    def check_path(self, start, end):
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]
        if x2 - x1 < 0:
            dx = -1
        elif x2 - x1 > 0:
            dx = 1
        else:
            dx = 0

        if y2 - y1 < 0:
            dy = -1
        elif y2 - y1 > 0:
            dy = 1
        else:
            dy = 0

        if dx != 0:
            y = y1
            for x in range(x1 + dx, x2, dx):
                y += dy
                for i in pieces:
                    if i.location == [x, y]:
                        return False
        elif dy != 0:
            x = x1
            for y in range(y1 + dy, y2, dy):
                x += dx
                for i in pieces:
                    if i.location == [x, y]:
                        return False

        return True

    can_jump = False


class Pawn(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_pawn_img, white_pawn_img)
        self.has_moved = False

    def can_move(self, destination):
        if (destination[0] - self.location[0]) != 0:
            return False
        elif (destination[1] - self.location[1]) == 1 - (2 * self.colour):
            self.has_moved = True
            return True
        elif (self.has_moved is False) & ((destination[1] - self.location[1]) == 2 - (4 * self.colour)):
            if super().check_path(self.location, destination):
                self.has_moved = True
                return True
            else:
                return False
        else:
            return False

    def can_take(self, destination):
        if ((destination[1] - self.location[1]) == 1 - (2 * self.colour)) & (
                abs(destination[0] - self.location[0]) == 1):
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, colour, location):
        self.can_jump = True
        super().__init__(colour, location)
        self.img = (black_knight_img, white_knight_img)

    def can_move(self, destination):
        if (abs(destination[0] - self.location[0]) == 2) & (abs(destination[1] - self.location[1]) == 1):
            return True
        elif (abs(destination[0] - self.location[0]) == 1) & (abs(destination[1] - self.location[1]) == 2):
            return True
        else:
            return False

    def can_take(self, destination):
        return self.can_move(destination)


class Bishop(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_bishop_img, white_bishop_img)

    def can_move(self, destination):
        if abs(destination[0] - self.location[0]) != abs(destination[1] - self.location[1]):
            return super().check_path(self.location, destination)
        else:
            return False

    def can_take(self, destination):
        return self.can_move(destination)


class Rook(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_rook_img, white_rook_img)

    def can_move(self, destination):
        if (destination[0] == self.location[0]) | (destination[1] == self.location[1]):
            return super().check_path(self.location, destination)
        else:
            return False

    def can_take(self, destination):
        return self.can_move(destination)


class Queen(Piece):
    def __init__(self, colour, location):
        super().__init__(colour, location)
        self.img = (black_queen_img, white_queen_img)

    def can_move(self, destination):
        if ((destination[0] == self.location[0]) | (destination[1] == self.location[1])) | (
                abs(destination[0] - self.location[0]) == abs(destination[1] - self.location[1])):
            return super().check_path(self.location, destination)
        else:
            return False

    def can_take(self, destination):
        return self.can_move(destination)


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

    def can_take(self, destination):
        return self.can_move(destination)


null_piece = Piece(-1, [-1, -1])
active_piece = null_piece
pieces = []


def populate():
    c = 0  # black is 0 and white is 1
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
