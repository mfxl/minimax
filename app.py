from minimax import find_best_move
from tictactoe import TTTPiece, TTTBoard
from os import system

system("cls")
new_game = 'y'
while new_game == 'y':
    is_machine_player = True if input("Human vs. Machine? (y/n) ") == "y" else False
    b = TTTBoard()  # initialize empty board
    print(" ", b)
    while b.is_win == False and b.is_draw == False:
        print(f"It's {b.turn} turn")
        if is_machine_player and b.turn == TTTPiece.O:
            m = find_best_move(b)
        else:
            m = 20
            while m not in b.legal_moves:
                m = int(input("Insert new Position: "))
                if m not in b.legal_moves:
                    print("This Position is illegal. Pleaes try again.")
        b = b.move(m)
        b = TTTBoard(b.position, b.turn)
        system("cls")
        if b.is_win:
            print(f"Game Over. {b.turn.opposite} wins")
        elif b.is_draw:
            print(f"Game Over. Draw!")
        print(" ", b)
    new_game = input("A new round? [y/n]: ")
    system("cls")