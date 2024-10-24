from typing import List


def exist(self, board: List[List[str]], word: str) -> bool:
    res_len = len(word)
    high = len(board)
    width = len(board[0])
    def search(x, y, word_len, t_word, move):
        if t_word == word:
            return True
        if word_len >= res_len or not word.startswith(t_word):
            return False
        t = [False for i in range(4)]
        c = -1
        for xi, yj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            c += 1
            if x + xi == high or x + xi < 0 or y + yj == width or y + yj < 0:
                continue
            if move[x + xi][y + yj] is True:
                continue
            move[x + xi][y + yj] = True
            t[c] = search(x + xi, y + yj, word_len + 1, t_word + board[x + xi][y + yj], move)
            move[x + xi][y + yj] = False
        return t[0] or t[1] or t[2] or t[3]


    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != word[0]:
                continue
            moved = [[False for i in range(width)] for j in range(high)]
            moved[i][j] = True
            res = search(i, j, 0, board[i][j], moved)
            if res is True:
                return True
    return False


print(exist(None, [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], 'AAAAAAAAAAAAAAB'))