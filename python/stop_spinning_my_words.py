def spin_words(sentence):
    # Your code goes here
    
    l = [i[::-1] if len(i)>=5 else i for i in sentence.split()]
    return " ".join(l)