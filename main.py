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
blackKing = "BK"
blackQueen = "BQ"
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
        
init_board()
print_board()
                
def move_piece(piece_to_move):
    '''
    This function will actually find and then move
    the found piece. Does not move the piece
    currently. 
    '''
    print "Enter the co-ordinate where you would"
    print "Like to move your piece to"
    print "Enter row"
    userPositionRow = int(raw_input(">> "))
    print "Enter col"
    userPositionCol = int(raw_input(">> "))
    
    userPositionRow -= 1
    userPositionCol -= 1
    
    board[userPositionRow][userPositionCol] = piece_to_move
    print_board()
    
                
def select_piece():
    '''
    Lets the user select a piece. Contains the
    menu that the user is presented with. 
    '''
    while True:
        try:
            print "Enter the row of where your piece is"
            userPositionRow = int(raw_input(">> "))
            print "Enter the column of where your piece is"
            userPositionCol = int(raw_input(">> "))
            
            userPositionRow -= 1
            userPositionCol -= 1
            
            if userPositionRow < 0 or userPositionRow > 7 or userPositionCol < 0 or userPositionCol > 7:
                print "Error, your number is to big or small. Try again"
                continue
            else:
                piece = board[userPositionRow][userPositionCol]
                if piece == "ES":
                    print "Ooops, thats an empty space! Try again"
                    continue
                else:
                    board[userPositionRow][userPositionCol] = "ES"
                    break
        except ValueError:
            print "Oops, something went wrong...try again!"
            
    
    print "You selected the %s at %s:%s" % (piece, userPositionRow, userPositionCol)
    move_piece(piece)
                
        
def main():
    print "Welcome to the pre-alpha version of chess!"
    print "The game will ask you to select a piece."
    print "Simply enter the INTEGER co-ordinates of where you would like to move the piece"
    print "The top left corner is 1,1 and the bottom right corner is 8,8"
    print "Have fun testing this pre-alpha version of chess!"
    select_piece()
                
if __name__ == "__main__":
    main()
