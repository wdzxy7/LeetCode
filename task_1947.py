def maxCompatibilitySum(self, students, mentors):
    compat = []
    for stu in students:
        com = []
        for men in mentors:
            s = 0
            for i,z in zip(stu, men):
                if i == z:
                    s += 1
            com.append(s)
        compat.append(com)
    f = {(0, '')}
    for com in compat:
        g = set()
        for i in range(len(com)):
            for s in f:
                t_i = str(i)
                if t_i not in s[1]:
                    t = com[i] + s[0]
                    t_i = s[1] + t_i
                    g.add((t, t_i))
        f = g
    f = sorted(f, key=lambda x:x[0])
    return f[-1][0]

print(maxCompatibilitySum(None, [[1,1,0],[1,0,1],[0,0,1]], [[1,0,0],[0,0,1],[1,1,0]]))