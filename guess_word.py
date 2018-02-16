class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        list_guess = []
        for char in guess:
            list_guess.append(char.encode("utf-8"))
        for a,b in zip(secret,guess):
            if a == b:
                A += 1
            if a in list_guess:
                B += 1
                list_guess.remove(a)
        B -= A
        answer = str(A) + "A" + str(B) + "B"
        return answer