def count_positives_sum_negatives(arr):
    c = 0 
    s = 0
    for num in arr:
        if num >0:
            c +=1
        else:
            s+= num
    if arr == []:
        return []
    return [c,s]