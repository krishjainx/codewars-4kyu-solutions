def high_and_low(numbers):
    
    arrayOfNumbers = [int(n) for n in numbers.split()]

    arrayOfNumbers.sort()
    
    out = str(arrayOfNumbers[-1]) + " " + str(arrayOfNumbers[0])
    
    return out


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))