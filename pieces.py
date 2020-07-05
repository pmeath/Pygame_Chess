from pygame_Chess import *

class piece:
	def __init__(piece, colour, location):
		piece.colour = colour
		piece.location = location


class pawn(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = pawn_img
		piece.has_moved = False

	def first_move():
		piece.location[1] += 2
		piece.has_moved = True
	#def promote():

	def move():
		piece.location[1] += 1
		piece.has_moved = True
		if (location[1] == 8):
			piece.promote
	def take(direction):
		piece.location[1] += 1
		piece.location[0] += direction
		piece.has_moved = True
		
class knight(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = knight_img
		
class bishop(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = bishop_img
		
class rook(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = rook_img
		
class queen(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = queen_img
		
class king(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.img = king_img
		piece.has_moved = False
	def move(direction):
		piece.has_moved = True
		
pieces = []
def populate():
	c = 0
	for c in range(2):
		for x in range(8):
			pieces.append(pawn(c, [x, 1 + c*5]))
		pieces.append(rook(c, [0, c*7]))
		pieces.append(rook(c, [7, c*7]))
		pieces.append(bishop(c, [2, c*7]))
		pieces.append(bishop(c, [5, c*7]))
		pieces.append(knight(c, [1, c*7]))
		pieces.append(knight(c, [6, c*7]))
		pieces.append(queen(c, [3, c*7]))
		pieces.append(king(c, [4, c*7]))
	
#	for x in range(8):
#		pieces.append(pawn("black", [x, 7]))
#	pieces.append(rook("black", [1, 8]))
#	pieces.append(rook("black", [8, 8]))
#	pieces.append(bishop("black", [2, 8]))
#	pieces.append(bishop("black", [7, 8]))
#	pieces.append(knight("black", [3, 8]))
#	pieces.append(knight("black", [6, 8]))
#	pieces.append(queen("black", [4, 8]))
#	pieces.append(king("black", [5, 8]))
