//
//  main.cpp
//  힙정렬
//
//  Created by Yesol on 2019. 1. 14..
//  Copyright © 2019년 Yesol. All rights reserved.
//

#include <iostream>

using namespace std;

void heapify(int a[], int size, int mid){
    int parent = mid;
    int left = parent*2+1;
    int right = parent*2+2;
    int largest = parent;
    int temp;
    
    if(left<size&&a[left]>a[parent]){
        largest = left;
    }
    if(right<size&&a[right]>a[parent]){
        largest = right;
    }
    if(parent!=largest){
        temp = a[largest];
        a[largest] = a[parent];
        a[parent] = temp;
        heapify(a, size, largest);
}
    
}

void build_max_heap(int a[],int size){
    int mid = size/2-1;
    for(mid;mid>=0;mid--){
        heapify(a,size,mid);
    }
}

void heapSort(int a[],int size){
    build_max_heap(a, size);
    //last 노드와 root 노드를 바꿔서 힙을 하나씩 없애는 과정이 필요.
    int temp = 0;
    for(int i=size-1;i>0;i--){
        temp = a[0];
        a[0] = a[i];
        a[i] = temp;
        heapify(a,i,0);
    }
}
int main(int argc, const char * argv[]) {
    
    int a[5] = {5,1,6,4,2};
    heapSort(a,5);
    for(int i=0;i<5;i++){
        cout << a[i] << endl;
    }
    return 0;
}
