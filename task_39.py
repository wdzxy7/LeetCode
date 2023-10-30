def combinationSum(self, candidates, target):
    res_list = []
    def search(rest,  res_list, path, index):
        if rest == 0:
            res_list.append(path)
            return
        elif rest < 0:
            return
        else:
            for i in range(index, len(candidates)):
                search(rest - candidates[i], res_list, path + [candidates[i]], i)
    search(target, res_list, [], 0)
    return res_list

print(combinationSum(None, [2,3,5], 8))