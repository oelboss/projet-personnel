# crée la fonction
# on ajoute un input dans la fonction
def draw_board(spots):
# on remplace la board par une f string
    print ("binevenue dans le super tictactoe!")
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f" |{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f" |{spots[7]}|{spots[8]}|{spots[9]}|")
             
    print(board)