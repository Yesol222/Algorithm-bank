

def merge(arr,left,mid,right) :

    i = left
    j = mid+1
    k = left

    temp = list()

    while(i<=mid and j<=right) :
        if arr[i] <= arr[j] :
            temp[k] == arr[i]
            i = i+1
        else :
            temp[k] == arr[j]
            j = j+1
        k = k + 1

    if i > mid :
        l = j
        for j in range(j,right+1) :
            temp[k] == arr[l]
            k = k+1
    else :
        l = i
        for l in range(i,range+1) :
            temp[k] == arr[l]


    for m in range(left,right+1) :
        arr[m] = temp[m]






def mergeSort(arr,left,right) :

    mid = (left+right)/2

    if(left<right):
        mergeSort(arr,left,mid-1)
        mergeSort(arr,mid+1,left)
        merge(arr,left,mid,right)


if '__name__' == 'main' :

    arr = [10,12,5,24,6,1]

    mergeSort(arr,0,arr.size()-1)

    print(arr)
