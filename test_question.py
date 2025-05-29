# you are given a string S, consisting of lowercase english letters. 
# you can apply this operation to the string S exactly once:
# choose any index i and move the character s[i] to the beginning of the string(deleting it from the original position). 
# find and print the lexicography minimal string that can be obtained after performing this operation. 
def string(S):
    ind=min(range(len(S)),key=lambda i:S[i])
    return S[ind]+S[:ind]+S[ind+1:]
S = input()
print(string(S))  