def sum_of_intervals(intervals):
    number = []
    maximum = 0
    minimum = 0
    for i in intervals:
        if i[1] > maximum:
            maximum = i[1]
        if i[0] < minimum:
            minimum = i[0]
    for i in range(0, maximum - minimum):
        number.append(0)
    for i in intervals:
        for j in range(i[0]-minimum, i[1]-minimum):
            number[j] = 1   
    return sum(number)