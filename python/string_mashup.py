def solve(a,b):
    res = []
    c = 0
    for i in b:
        c = a.count(i)
        res.append(c)
    return res