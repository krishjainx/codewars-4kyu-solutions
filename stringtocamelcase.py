def to_camel_case(text):
    #your code here
    textArray = list(text)
    for i in range(len(textArray)-1):
        if textArray[i] == "-" or textArray[i] == "_":
            textArray[i] = textArray[i+1].upper()
            textArray[i+1] = ""
    
    out = [i for i in textArray if i != ""]
    return "".join(out)

print(to_camel_case("the-stealth-warrior"))