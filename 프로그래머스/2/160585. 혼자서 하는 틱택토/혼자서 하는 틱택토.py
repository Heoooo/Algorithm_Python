def check(board, k):
    #가로 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == k:
            return True
    #세로확인
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == k:
            return True
    #왼쪽 대각선
    if board[0][0] == board[1][1] == board[2][2] == k:
        return True
    #오른쪽 대각선
    if board[0][2] == board[1][1] == board[2][0] == k:
        return True
    return False
    

def solution(board):
    white = 0
    black = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                black += 1
            elif board[i][j] == 'X':
                white += 1
    if not((white + 1 == black) or (white == black)):
        return 0
    black_win = check(board, 'O')
    white_win = check(board, 'X')
    if black_win and black != white+1:
        return 0
    if white_win and black_win:
        return 0
    if white_win and not white == black:
        return 0
    return 1