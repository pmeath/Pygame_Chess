class piece:
	def __init__(piece, colour, location):
		piece.colour = colour
		piece.location = location


class pawn(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
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
		
		
class bishop(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		
class rook(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		
class queen(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		
class king(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		piece.has_moved = False
	def move(direction):
		piece.has_moved = True
		
pieces = []
def populate():
	c = 0
	for c <= 1, c++:
		for x in range(8):
			pieces.append(pawn("white", [x, 2 +c*5]))
		pieces.append(rook("white", [1, 1+c*7]))
		pieces.append(rook("white", [8, 1+c*7]))
		pieces.append(bishop("white", [2, 1+c*7]))
		pieces.append(bishop("white", [7, 1+c*7]))
		pieces.append(knight("white", [3, 1+c*7]))
		pieces.append(knight("white", [6, 1+c*7]))
		pieces.append(queen("white", [4, 1+c*7]))
		pieces.append(king("white", [5, 1+c*7]))
	
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
