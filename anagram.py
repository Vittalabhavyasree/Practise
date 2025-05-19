def is_anagram(s,t):
    return sorted(s) == sorted(t)
s=input()
t=input()
print(is_anagram(s,t))