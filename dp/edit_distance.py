def edit_distance(word1: str, word2: str) -> int:
    memo = dict()

    def minimum(src, target):
        key = (src, target)
        if key not in memo:
            if src == target:
                memo[key] = 0
            elif not target:
                memo[key] = len(src)
            elif not src:
                memo[key] = len(target)
            elif src[0] == target[0]:
                memo[key] = minimum(src[1:], target[1:])
            else:
                r = minimum(src[1:], target[1:])
                d = minimum(src[1:], target)
                a = minimum(src, target[1:])
                memo[key] = min(r, d, a) + 1
        return memo[key]
    return minimum(word1, word2)
