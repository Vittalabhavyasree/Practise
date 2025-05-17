def generate(k,n,curr,ans):
    if(n==0 and len(curr)==k):
        ans.append(curr.copy())
        return
    if(n<0 or len(curr)>k):
        return 
    if(n==0 and len(curr)<k):
        return
    if(len(curr)==0):
        ele=1
    else:
        ele=curr[-1]+1
    for i in range(ele,10):
        curr.append(i)
        generate(k,n-i,curr,ans)
        curr.pop()
def combinationSum3(k,n):
    curr=[]
    ans=[]
    generate(k,n,curr,ans)
    return ans
k=int(input())
n=int(input())
print(combinationSum3(k,n))