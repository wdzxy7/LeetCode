def hIndex(self, citations):
    citations.sort(reverse=True)
    length = len(citations)
    h = 0
    i = 0
    while i < length and citations[i] > h:
        h += 1
        i += 1
    return h

print(hIndex(None, [3,0,6,1,5]))