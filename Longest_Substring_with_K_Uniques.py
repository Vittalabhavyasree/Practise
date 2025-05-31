# brute force approach
'''def longest(s,k):
    n=len(s)
    if(n==1):
        return 1
    dup=sorted(s)
    if(dup[0]==dup[n-1]):
        return -1
    if(len(set(dup))<k):
        return -1
    maxLen=0
    for i in range(0,n):
        hash_set=set()
        for j in range(i,n):
            hash_set.add(s[j])
            if(len(hash_set)>k):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
s=input()
k=int(input())
print(longest(s,k))'''

# sliding window approach
def longestKSubstr(s, k):
    n=len(s)
    if(n==1):
        return 1
    dup=sorted(s)
    if(dup[0]==dup[n-1]):
        return -1
    if(len(set(dup))<k):
        return -1
    left=0
    right=0
    maxLen=0
    d={}
    while(right<n):
        if(s[right] in d):
            d[s[right]]+=1
        else:
            d[s[right]]=1
        if(len(d)>k):
            while(len(d)>k):
                d[s[left]]-=1
                if(d[s[left]]==0):
                    del d[s[left]]
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
s=input()
k=int(input())
print(longestKSubstr(s, k))