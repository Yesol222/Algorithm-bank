//
//  main.cpp
//  퀵소트
//
//  Created by Yesol on 2019. 2. 17..
//  Copyright © 2019년 Yesol. All rights reserved.
//

#include <iostream>

using namespace std;
void swap(int n,int m){
    int temp = n;
    n = m;
    m  = temp;
}
int partition(int a[],int start,int end){
    int pivot = a[start];
    int left = start+1;
    int right = end;
    
    while(left<right){
        while(left<a[pivot]){
            left++;
        }
        while(right>a[pivot]){
            right--;
        }
        swap(left,right);
        a[pivot] = left+1;
    }
    return left;
}

void QuickSort(int a[],int left,int right){
    
    if(left<right){
        int q = partition(a,left,right);
        QuickSort(a, left, q-1);
        QuickSort(a,q+1,right);
    }
    
}

int main(int argc, const char * argv[]) {

    int a[]= {4,1,6,8,9,5};
    QuickSort(a,0,5);
    
    for(int i=0;i<6;i++){
        cout << a[i] << endl;
    }
    return 0;
}
