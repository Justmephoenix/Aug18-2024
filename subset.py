def subsetFind(arr,subset,index):
    print(*subset)
    for i in range(index,len(arr)):
        subset.append(arr[i])
        
        subsetFind(arr,subset,i+1)
        subset.pop(-1)
    return
        



def subset(arr):
    subset=[]
    index=0
    subsetFind(arr,subset,index)


arr=[1,2,3]
subset(arr)