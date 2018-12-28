# Write a function that determines whether a string is a valid guess in a Boggle board,
#  as per the rules of Boggle. A Boggle board is a 2D array of individual characters, e.g.:
# [ ["I","L","A","W"],
#   ["B","N","G","E"],
#   ["I","U","A","O"],
#   ["A","S","R","L"] ]
# Valid guesses are strings which can be formed by connecting adjacent cells
# (horizontally, vertically, or diagonally) without re-using any previously used cells.

# For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses,
#  while "BUNGIE", "BINS", and "SINUS" would not.

# Your function should take two arguments (a 2D array and a string) and return true or false
#  depending on whether the string is found in the array as per Boggle rules.


# Test cases will provide various array and string sizes
# (squared arrays up to 150x150 and strings up to 150 uppercase letters).
# You do not have to check whether the string is a real word or not, only if it's a valid guess.
def find_word(board, word):
    starts = []
    first_m = first_n = 0
    for m in range(len(board)):
        for n in range(len(board[0])):
            if board[m][n] == word[0]:
                starts.append((m, n))
                i = 1
                flag = find_char(board, word, i, m, n)
                if flag:
                    return flag
    return False


def find_char(board, word, i, m, n):
    if i > len(word) - 1:
        return True
    char = word[i]
    flag = False
    if index2value(board, m - 1, n) == char and not flag:
        new_board = mark(board, m - 1, n)
        flag = find_char(new_board, word, i + 1, m - 1, n)
    if index2value(board, m + 1, n) == char and not flag:
        new_board = mark(board, m + 1, n)
        flag = find_char(new_board, word, i + 1, m + 1, n)
    if index2value(board, m, n - 1) == char and not flag:
        new_board = mark(board, m, n - 1)
        flag = find_char(new_board, word, i + 1, m, n - 1)
    if index2value(board, m, n + 1) == char and not flag:
        new_board = mark(board, m, n + 1)
        flag = find_char(new_board, word, i + 1, m, n + 1)
    if index2value(board, m + 1, n + 1) == char and not flag:
        new_board = mark(board, m + 1, n + 1)
        flag = find_char(new_board, word, i + 1, m + 1, n + 1)
    if index2value(board, m - 1, n + 1) == char and not flag:
        new_board = mark(board, m - 1, n + 1)
        flag = find_char(new_board, word, i + 1, m - 1, n + 1)
    if index2value(board, m - 1, n - 1) == char and not flag:
        new_board = mark(board, m - 1, n - 1)
        flag = find_char(new_board, word, i + 1, m - 1, n - 1)
    if index2value(board, m + 1, n - 1) == char and not flag:
        new_board = mark(board, m + 1, n - 1)
        flag = find_char(new_board, word, i + 1, m + 1, n - 1)
    return flag


import copy


def mark(board, m, n):
    tmp = copy.deepcopy(board)
    tmp[m][n] = None
    return tmp


def index2value(board, m, n):
    if (m >= 0) and (m < len(board)) and (n >= 0) and (n < len(board[0])):
        return board[m][n]
    return False


testBoard = [["E", "A", "R", "A"], ["N", "L", "E", "C"], ["I", "A", "I", "S"],
             ["B", "Y", "O", "R"]]

print(find_word(testBoard, "C"))
print(find_word(testBoard, "EAR"))
print(find_word(testBoard, "EARS"))
print(find_word(testBoard, "CEREAL"))
