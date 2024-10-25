def solution(s):
    res = ""
    for i in s:
        if i.isupper():
            res = res + " " + i
        else:
            res = res + i
            
    return res