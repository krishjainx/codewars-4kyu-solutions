def pig_it(text):
    weirdWords = []
    text = text.split()
    for i in text:
        arr = list(i)
        arr.append(arr[0])
        arr.append("ay")
        arr.pop(0)
        weirdWords.append(''.join([str(elem) for elem in arr]))
        
    out = ' '.join([str(elem) for elem in weirdWords])
    return out