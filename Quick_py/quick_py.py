


def swap(a,b) :
    temp = a
    a = b
    b = temp


def partition(arr,left,right,pivot) :

    pivotitem = arr[pivot]
    j = left

    for i in range(left+1,right+1) :
        if arr[i] > arr[j] :
            j = j+1
            swap(arr[j],arr[i])
    pivot = j
    swap(arr[left],arr[pivot])






def Quicksort(arr,left,right) :

    pivot = left

    if(right>left) :
        partition(arr,left,right,pivot)
        Quicksort(arr,left,pivot-1)
        Quicksort(arr,pivot+1,right)




if '__name__' == '__main__' :

    list = [1,6,3,10,4,9]

    Quicksort(list,0,list.len-1)

    print(list)
