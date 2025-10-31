
def create_board():
    return[" "]*9

def print_board(board):
    print()
    print(f"{board[0]}| {board[1]} | {board[2]}")
    print("----+----+----")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----+----+----")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def valid_moves(board):
    return [i for i, v in enumerate(board) if v ==" "]
def make_move(board,pos,player):
    board[pos]=player
def check_win(board,player):
    wins=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]== board[b]== board[c] ==player for a,b,c in wins)
def check_draw(board):
  return " " not in board

def player_input(board,player):
    moves=valid_moves(board)
    while True:
        try:
            user=input(f"player {player}-choose position (1-9): ").strip()
            if user.lower() in("q","quit","exit"):
                print("exiting game,bye")
                exit()
            pos=int(user)-1
            if pos in moves:
                return pos
            else:
                print("that position isnt avalible try again")
        except ValueError:
            print("please enter a number between 1 and9 (or 'q' to quit)")

def switch_player(player):
    return "0" if player == "X" else "X"

def show_instructions():
    print("tic-tac-toe")