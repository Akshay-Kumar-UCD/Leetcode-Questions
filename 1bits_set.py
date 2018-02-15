"""
class Solution(object):
    def countPrimeSetBits(self, L, R):
        def isPrime2(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3,int(n**0.5)+1,2):   # only odd numbers
                if n%i==0:
                    return False    
            return True
        prime_counter = 0
        count = 0
        ran = False
        for i in range(L,R+1):
            bin_i = bin(i)
            if "1" in bin_i:
                ran = True
                count = bin_i.count("1")
            if ran:
                if isPrime2(count):
                    prime_counter += 1
        return prime_counter
"""