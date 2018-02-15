def selfDividingNumbers(left,right):
    answer = []
    for i in range(left,right+1):
        str_i = str(i) 
        if "0" in str_i:
            continue
        checker = True
        for char in str_i:
            if i % int(char) != 0:
                checker = False
        if checker:
            answer.append(i)
    print(answer)
        
def test():
    selfDividingNumbers(1,22)    

if __name__ == "__main__":
    test()