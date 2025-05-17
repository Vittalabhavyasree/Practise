def generate(ind,curr_str,o,c,ans,n):
    if(o>n):
        return
    if(ind==2*n and o==c):    # Fix: 2*n instead of 2**n and use 'and' not '&'
        ans.append(curr_str)
        return
    generate(ind+1,curr_str+"(",o+1,c,ans,n)
    if(o>c):
        generate(ind+1,curr_str+")",o,c+1,ans,n)

def generateParenthesis(n):
    ind=0
    o=0
    c=0
    curr_str=""
    ans=[]
    generate(ind,curr_str,o,c,ans,n)    # Fix: move this line inside the function
    return ans    # Fix: indent properly
n=int(input())
print(generateParenthesis(n))
