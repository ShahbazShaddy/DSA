def Partition(arr,start,end):
    x=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1
def QuickSort(arr,start,end):
    if start<end:
        q=Partition(arr,start,end)
        QuickSort(arr,start,q-1)
        QuickSort(arr,q+1,end)
    
arr=[2,4,8,7,1,3,5,51,23,43]
QuickSort(arr,0,len(arr)-1)
print(arr)
        