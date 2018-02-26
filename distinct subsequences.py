
def numDistinct(S, T):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    row = len(S) + 1
    col = len(T) + 1
    dp = [0]*col
    dp[0] = 1
    for i in range(1, row):
        diag = 1
        for j in range(1, col):
            tmp = dp[j]
            if S[i-1] == T[j-1]:
                dp[j] = diag + dp[j]
            diag = tmp
    print(dp[-1])

def test():
    numDistinct("rabbbit","rabbit")

if __name__ == "__main__":
    test()