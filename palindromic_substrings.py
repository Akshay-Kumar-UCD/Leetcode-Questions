def countSubstrings(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                ans += 1
    return ans


def test():
    answer = countSubstrings("aaa")
    print(answer)

if __name__ == "__main__":
    test()