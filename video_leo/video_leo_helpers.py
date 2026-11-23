# crée la fonction
# on ajoute un input dans la fonction
def draw_board(spots):
# on remplace la board par une f string
    print ("bienvenue dans le super tictactoe!")
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
             
    print(board)
    
# voir à quel tour on est
def check_turn(turn):
    if turn %2 == 0: return 'O'
    else : return 'X'
    
def check_for_win(spots):
    #vérifier les horizontalers
    if (spots[1] == spots[2] == spots[3]) \
        or(spots[4] == spots[5] == spots[6]) \
        or(spots[7] == spots[8] == spots[9]) :
           return True