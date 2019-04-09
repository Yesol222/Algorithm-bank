//
//  main.cpp
//  Determine
//
//  Created by Yesol on 2019. 4. 3..
//  Copyright © 2019년 Yesol. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    return 0;
}

void determine(int *arr, int size){
    
    int last - size-1;
    int current = get_parent(last);
    int left;
    int right;
    bool outcome;
    
    while(current >= 0){
        left = current*2+1;
        right = current*2+2;
        
        if(arr[current]<arr[left])
            outcome = 0;
        if(arr[current]<arr[right])
            outcome = 0;
        else
            outcome = 1;
        
    }
    
    
}

int compare(int *arr,int last, int current){
    
    while((current*2))
    left = current*2+1;
    right = current*2+2;
    
    if(arr[current]<arr[left])
        outcome = 0;
    if(arr[current]<arr[right])
        outcome = 0;
    else
        outcome = 1;
}
