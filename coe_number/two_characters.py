from itertools import combinations
def two_characters(s):
    max_len = 0
    for c1, c2 in combinations(set(s), 2):
        res = [c for c in s if c == c1 or c == c2]
        if all(res[i] != res[i+1] for i in range(len(res)-1)):
            max_len = max(max_len, len(res))
    return max_len