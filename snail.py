def snail(array):
    out = []
    while len(array) > 0:
        out += array[0]
        del array[0]

        if len(array) > 0:
            for i in array:
                out += [i[-1]]
                del i[-1]

            if array[-1]:
                out += array[-1][::-1]
                del array[-1]

            for i in reversed(array):
                out += [i[0]]
                del i[0]

    return out
