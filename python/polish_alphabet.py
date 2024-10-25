def correct_polish_letters(st): 
    # your code here
    res = ""
    dic = {"ą": "a", "ć": "c", "ę": "e", "ł":"l", "ń": "n", 
           "ó": "o", "ś":"s", "ź": "z", "ż": "z"}
    for i in st:
        if i in dic.keys():
            res = res + dic[i]
        else: 
            res = res + i
    return res