import string

def name_value(my_list):
    st  = string.ascii_lowercase
    numbers = []
    res = []
    for i in my_list:
        n = 0
        for j in i:
            if j in st:
                n += st.index(j) + 1
        numbers.append(n)
    
    for i in range(len(numbers)):
        res.append(numbers[i]*(i+1))
    return res
print(name_value(["abc", "abc abc"]))