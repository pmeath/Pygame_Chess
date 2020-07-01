class piece:
	def __init__(piece, colour, location):
		piece.colour = colour
		piece.location = location

class pawn(piece):
	def __init__(piece, colour, location):
		super().__init__(colour, location)
		
	def move():
		location[1] += 1
	def first_move():
		location[1] += 2
		
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
		
def populate():

	for(x in range(8)):
		"pawn"+x = pawn("white", (x, 2))	
	rook1 = rook("white", (1, 1))
	rook2 = rook("white", (8, 1))
	bishop1 = bishop("white", (2, 1))
	bishop2 = bishop("white", (7, 1))
	knight1 = knight("white", (3, 1))
	knight2 = knight("white", (6, 1))
	queen = queen("white", (4, 1))
	king = king("white", (5, 1))
