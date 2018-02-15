def roman(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    count = 0
    for i in range(0, len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            count -= roman[s[i]]
        else:
            count += roman[s[i]]
    return count + roman[s[-1]]

def test():
    ans = roman("MCMXCVI")
    print(ans)
    # answer is 1996

if __name__ == "__main__":
    test()