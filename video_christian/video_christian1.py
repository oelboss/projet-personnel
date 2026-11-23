from video_christian_helpers import draw_board,check_turn
import os

spots= {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'} 

playing = True
turn=0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("mais t con ou quoi, spot invalid, choisis qqch d'autre" )
        prev_turn=turn
    print("Player" + str((turn % 2)+1)+"'s turn: choisis ton spot ou appuie sur q pour abandonner")
    choice=input()
    prev_turn = turn
    if choice =='q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in ["X", "O"]: #vérifier si le spot est déja utilisé
                turn += 1
                spots[int(choice)] = check_turn(turn) 
                