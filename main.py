#A chess game written in python
#By JohnBobSmith and rm-fr

import rules

board = []

#white pieces below
whiteRook = "WR"
whiteRook1 = "WR"
whiteKnight = "WN"
whiteKnight1 = "WN"
whiteBishop = "WB"
whiteBishop1 = "WB"
whiteKing = "WK"
whiteQueen = "WQ"
whitePawn1 = "WP"
whitePawn2 = "WP"
whitePawn3 = "WP"
whitePawn4 = "WP"
whitePawn5 = "WP"
whitePawn6 = "WP"
whitePawn7 = "WP"
whitePawn8 = "WP"

#Black pieces below
blackRook = "BR"
blackRook1 = "BR"
blackKnight = "BN"
blackKnight1 = "BN"
blackBishop = "BB"
blackBishop1 = "BB"
blackKing = "WK"
blackQueen = "WQ"
blackPawn1 = "BP"
blackPawn2 = "BP"
blackPawn3 = "BP"
blackPawn4 = "BP"
blackPawn5 = "BP"
blackPawn6 = "BP"
blackPawn7 = "BP"
blackPawn8 = "BP"

def init_board():
    for x in range(8):
        board.append(["ES"] * 8)
    
    #White pieces below
    board[0][0] = whiteRook
    board[0][1] = whiteKnight
    board[0][2] = whiteBishop
    board[0][3] = whiteQueen
    board[0][4] = whiteKing
    board[0][5] = whiteBishop1
    board[0][6] = whiteKnight1
    board[0][7] = whiteRook1
    board[1][0] = whitePawn1
    board[1][1] = whitePawn2
    board[1][2] = whitePawn3
    board[1][3] = whitePawn4
    board[1][4] = whitePawn5
    board[1][5] = whitePawn6
    board[1][6] = whitePawn7
    board[1][7] = whitePawn8
    
    #Black pieces below
    board[7][0] = blackRook
    board[7][1] = blackKnight
    board[7][2] = blackBishop
    board[7][3] = blackQueen
    board[7][4] = blackKing
    board[7][5] = blackBishop1
    board[7][6] = blackKnight1
    board[7][7] = blackRook1
    board[6][0] = blackPawn1
    board[6][1] = blackPawn2
    board[6][2] = blackPawn3
    board[6][3] = blackPawn4
    board[6][4] = blackPawn5
    board[6][5] = blackPawn6
    board[6][6] = blackPawn7
    board[6][7] = blackPawn8
        
def print_board():
    for col in board:
        print (" ".join(col))
        
def main():
    init_board()
    print_board()
                
if __name__ == "__main__":
    main()
