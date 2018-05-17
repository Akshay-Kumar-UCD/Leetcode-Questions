def shiftZero(input):
    i = j = len(input)-1
    while i > -1 and j > -1:
        if input[i] != 0 and input[j] == 0:
            dummy = input[i]
            input[i] = input[j]
            input[j] = dummy
            i -= 1
            j -= 1
        if input[i] == 0:
            i -= 1
        if input[j] != 0:
            j -= 1

input = [-2,10,0,55,-10,0,0,4,0]
print("Before: ", input)
shiftZero(input)
print("After: ", input)