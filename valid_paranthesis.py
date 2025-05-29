def isValid(s):
    stack=[]
    for ele in s:
        if(ele=="([{"):
            stack.append(ele)
        else:
            if(len(stack)==0):
                return False
            x=stack.pop()
            if(x=="(" and ele==")" or x=="[" and ele=="]" or x=="{" and ele=="}"):
                continue
            else:
                return False
    return len(stack)==0
s=input()
print(isValid(s))