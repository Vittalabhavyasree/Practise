s=input()
vowel="aeiouAEIOU"
v=0
for i in s:
    if(i in vowel):
        v+=1
print(v)