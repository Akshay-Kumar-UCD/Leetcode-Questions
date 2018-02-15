def pgen(op,close,s):
    if op == 0 and close == 0:
        print(s)
    if op > close:
        return "done"
    if op > 0:
        pgen(op-1,close,s + "(")
    if close > 0:
        pgen(op,close-1,s+")")
    
def test(x):
    pgen(x,x,"")

if __name__ == "__main__":
    test(3)


"""

class Solution(object):
    def generateParenthesis(self, n):
        def pgen(op,close,s,ans):
            if op == 0 and close == 0:
                ans.append(s)
            if op > close:
                return -1
            if op > 0:
                pgen(op-1,close,s+"(",ans)
            if close > 0:
                pgen(op,close-1,s+")",ans)
        
        ans = []
        pgen(n,n,"",ans)
        return ans

"""