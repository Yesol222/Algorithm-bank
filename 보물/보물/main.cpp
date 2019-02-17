//
//  main.cpp
//  보물
//
//  Created by Yesol on 2019. 1. 16..
//  Copyright © 2019년 Yesol. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {

    int N;
    cin >> N;
    int a[N],b[N],temp[N];
    int n = 0;
    
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    
    for(int i=0;i<N;i++){
        cin >> b[i];
    }
    
    //b의 최솟값은 a의 최댓값과, 최대값은 최솟값과 곱하게 해야 함.
    //b는 순서를 바꿀 수 없음.
    
    

    for(int i=0;i<N;i++){
        cout << temp[i];
    }
    
    
    return 0;
}
