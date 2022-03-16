def xo(s):
    numberOfOs = len([i for i in s.lower() if i == "o"])
    numberOfXs = len([i for i in s.lower() if i == "x"])

    if numberOfOs == numberOfXs:
        return True
    else:
        return False

