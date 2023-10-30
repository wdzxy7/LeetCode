def combinationSum2(self, candidates, target):
    candidates = sorted(candidates)
    if sum(candidates) < target:
        return []
    res_list = []
    used = []
    def search(res, path, index, rest):
        if rest == 0:
            res.append(tuple(path))
            used.append(path[0])
            return
        elif rest < 0:
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] not in used:
                    search(res, path + [candidates[i]], i + 1, rest - candidates[i])
    search(res_list, [], 0, target)
    res_list = set(res_list)
    return [list(i) for i in res_list]

print(combinationSum2(None, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))