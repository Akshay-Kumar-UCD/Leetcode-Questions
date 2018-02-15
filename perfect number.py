import math
def checkPerfectNumber(num):
    count = 0
    if num < 0 or num == 0: return False
    num_sqrt = int(math.sqrt(num))
    count = sum(i + num // i for i in range(1,num_sqrt+1) if not num % i)
    if num == num_sqrt ** 2: count -= num_sqrt
    return count - num == num
        
def test():
    answer = checkPerfectNumber(6)    
    print(answer)

if __name__ == "__main__":
    test()