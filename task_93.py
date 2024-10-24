from typing import List


def restoreIpAddresses(self, s: str) -> List[str]:
    res = []
    l = len(s)
    def search(index, now):
        nonlocal res
        if len(now) > 4:
            return
        if index == l and len(now) == 4:
            res.append('.'.join(now))
        for i in range(index, min(index + 3, l)):
            t_ip = s[index: i + 1]
            if (i + 1 - index > 1 and t_ip.startswith('0')) or int(t_ip) > 255:
                return
            now.append(t_ip)
            search(i + 1, now)
            now.pop()

    search(0, [])
    return res


print(restoreIpAddresses(None, '25525511135'))