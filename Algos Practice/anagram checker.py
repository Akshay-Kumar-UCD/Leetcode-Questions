# program checks if two strings are anagrams

def anagramChecker(s1,s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

s1 = "hello"
s2 = "olleh"

ans = anagramChecker(s1,s2)
print(ans)

s1 = "wrong"
s2 = "right"

ans = anagramChecker(s1,s2)
print(ans)