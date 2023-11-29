import re

def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
    pattern = list(pattern)
    first_index = [match.start() for match in re.finditer(r'' + pattern[0], text)]
    second_index = [match.start() for match in re.finditer(r'' + pattern[1], text)]
    first_len = len(first_index)
    second_len = len(second_index)
    add = max(first_len, second_len)
    if first_len == 0 or second_len == 0:
        return add
    while second_index and second_index[0] < first_index[0]:
        second_len -= 1
        del second_index[0]
    if len(second_index) == 0:
        return add
    while first_index and first_index[-1] > second_index[-1]:
        first_len -= 1
        del first_index[-1]
    if len(first_index) == 0:
        return add
    count = 0
    second_move = 0
    for first in first_index:
        if first <= second_index[second_move]:
            count += second_len - second_move
        else:
            while first > second_index[second_move] and second_move != second_len - 1:
                second_move += 1
            if first <= second_index[second_move]:
                count += second_len - second_move
    if pattern[0] == pattern[1]:
        return count
    return count + add


print(maximumSubsequenceCount(None, '"nyjslyeqlrohtofpusrasrsgisvsxtwokfjfkjkwgrptj"',
                              'il'))