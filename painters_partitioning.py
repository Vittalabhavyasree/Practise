def findLargestMinDistance(arr: list ,m: int) -> int:
    def canWePaint(maxBoards,arr):
        no_of_boards_painted=arr[0]
        painters=1
        for boards in range(1,len(arr)):
            if(arr[boards]+no_of_boards_painted<=maxBoards):
                no_of_boards_painted+=arr[boards]
            else:
                no_of_boards_painted=arr[boards]
                boards+=1
        return boards
    if(m>len(arr)):
        return -1
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        maxBoards=(low+high)//2
        if(canWePaint(maxBoards,arr)<=m):
            high=maxBoards-1
        else:
            low=maxBoards+1
    return low
arr=list(map(int, input().split()))
m=int(input())
print(findLargestMinDistance(arr,m))