//
//  main.cpp
//  거품정렬
//
//  Created by Yesol on 2019. 1. 12..
//  Copyright © 2019년 Yesol. All rights reserved.
//

#include <iostream>

using namespace std;
int main()
{
    int N = 5;
    int i, j, temp;
    int data[] = { 5, 3, 7, 9, 1 };
    // Bubble Sort
    for (i = 0; i < N; i++) {
        for (j = 0; j < N-(i+1); j++) {
            if (data[j] > data[j+1]) {
                temp = data[j+1];
                data[j+1] = data[j];
                data[j] = temp;
                }
            }
        }
    for(int n=0;n<N;n++){
        cout << data[n] << endl;
    }
    
    }

