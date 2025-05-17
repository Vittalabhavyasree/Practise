#sum of alphabets according to their position
'''s=input()
sum=0
for i in s:
    sum+=ord(i)-96
print(sum)
#vowels in capitals without using uppercase'''
'''s=input()
v='aeiou'
res=""
for i in s:
    if(i in v):
        res+=chr(ord(i)-32)
    else:
        res+=i
print(res)'''

#small to capital , capital to small
'''s=input()
v='aeiouAEIOU'
res=""
for i in s:
    if(97<=ord(i)<=123):
        res+=chr(ord(i)-32)
    else:
        res+=chr(ord(i)+32)
print(res)'''

#need to change
'''s=input()
res=""
for i in s:
    if('a'<=i<='z'):
        res+=chr(ord(i)-32)
    else:
        res+=chr(ord(i)+32)
print(res)'''

#pair two strings if there is not pair captalize the letter
'''s=input()
t=input()
i=0
res=""
while(i<len(s) and i<len(t)):
    res+=(s[i]+t[i])
    i+=1
while(i<len(s)):
    res+=chr(ord(s[i])-32)
    i+=1
while(i<len(t)):
    res+=chr(ord(t[i])-32)
    i+=1
print(res)'''

# finding a sub string in a string by using membership operator
'''s=input() 
t=input()
res=''
if(len(s)>len(t)):
    res+=s+s
    if(t in res):
        print("true")
    else:
        print("false")'''

# "IS" operator is used to compare to memory space
'''a=5
b=5
print(b is a)
print(id(a))
print(id(b))'''

# printing the letters according to the before mentionrd number like 3a=aaa
'''str="3a4b6c"
res=""
for i in range(0,len(str),2):
    res+=int(str[i]) * str[i+1]
print(res)'''

# 31a4b111c
'''str="31a4b111c"
res=""
num=""
for i in str:
    if i.isdigit():
        num += i
    else:
        res += int(num) * i
        num=""
print(res)'''

# 31ab1c
str="31abc1h"
res=""
num=""
alp=""
i=0
while(i<len(str)):
    while str[i].isdigit():
        num += str[i]
        i+=1
    while i<len(str) and str[i].isalpha():
        alp+=str[i]
        i+=1
    res+=int(num)*alp 
    num=alp=""
print(res)