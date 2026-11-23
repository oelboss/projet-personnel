#import de la fonction draw_board, check_turn et check_for_win dans le main
from video_leo_helpers import draw_board, check_turn, check_for_win
# ne pas toujours dessiner la board à chaque tour
import os

#utilisation du dico
spots = {1 : '1', 2 : '2' , 3: '3' , 4 : '4' , 5: '5', 6 : '6', 7 : '7' , 8: '8', 9:'9'}

#interaction avec while
playing = True
# vérifizer si la partie est finie
complete = false
#initialisation des tours
turn = 0
#tour précédent
prev_turn= -1

while playing:
    # reset le screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #si un tour invalide est joué, signaler au joueur
    if prev_turn == turn:
        print ("Emplacement invalide sélectionné, veuillez en choisir un nouveau")
    prev_turn = turn
    print ("tour du joueur " + str((turn%2) +1) + ": choisis ton emplacement ou presse 'q' pout quitter")
    #recevoir l'input des joueurs
    choice = input()
    if choice =="q":
        playing = False
    
        turn +=1
        spots[int(choice)] = check_turn(turn)
    #regarder si le jpoueur a mis un nombre de 1 à 9
    elif str.isdigit(choice) and int(choice) in spots :
        #regarder si l'emplacement a déjà été choisi
        if not spots[int(choice)] in {'x', '0'}:
            #si l'input est valide, on update la board
            turn+=1
            spots[int(choice)] = check_turn(turn)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False
    
#on imprime les résultats en dehors du loop
#on imprime la board une dernière fois
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# 15 min 30 de la vidéo