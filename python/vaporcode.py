def vaporcode(s):
    #your code here
    res = ""
    st = s.replace(" ", "")
    
    for i in st:
        res = res + i.upper() + "  "
    
    res = res.rstrip()
    
    return res