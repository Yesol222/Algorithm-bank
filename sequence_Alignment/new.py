#finding shortest path considering panlaty
import numpy as np

    
def matrix(x,y) :

    n = len(x)
    m = len(y)

    newList = [0 for i in range(n-1)]
    panalty = [0 for i in range(n-1)]

    #n by m 행렬을 위해 numpy로 opt 정의 
    opt = np.zeros((n,m))

    #초기 행렬 정의, n행 m열의 원소를 채움 
    if x[n-1] == y[m-1] :
        opt[n-1][m-1] = 0
    else :
        opt[n-1][m-1] = 2
    #행렬을 모두 채우기 위해 n행과 m열을 채운다. 모두 갭과 만나므로 2씩 증가 
    for j in range(m-2,-1,-1) :
            opt[n-1][j] = opt[n-1][j+1] + 2
    
    for i in range(n-2,-1,-1) :
            opt[i][m-1] = opt[i+1][m-1] + 2         
    #위,아래,대각선으로 가는 시퀀스 중에 최소인 값을 저장하면서 모든 행렬을 채움 
    for j in range(m-2,-1,-1):
        for i in range(n-2,-1,-1):
            if x[i] == y[j] :
                d = opt[i+1][j+1]
            else :
                d = opt[i+1][j+1] + 1
            opt[i][j] = min(d,opt[i+1][j]+2,opt[i][j+1]+2)
    #첫번째 시퀀스와 최소로 매치 시키기 위한 새로운 시퀀스 값을 newList에 저장, 초기값은 y의 첫 원소.
    newList[0] = y[0]
    #최소 시퀀스를 찾기 위해 다시 0,0부터 n,m까지 검사하며 패널티와 newList 값을 채움. 
    i = 0
    j = 0
    while i < n-1 :
        if x[i+1] == y[j+1] :    
            if opt[i][j] == opt[i+1][j+1] :
                panalty[i] = 0
                newList[i] = y[j]
                i = i+1
                j = j+1
            elif opt[i][j] == opt[i+1][j+1] + 1 :
                panalty[i] = 1
                newList[i] = y[j]
                i = i+1
                j = j+1
        elif x[i+1] == y[j] and opt[i+1][j] < opt[i+1][j+1]  :
            panalty[i] = 2
            newList[i] = '-'
            i = i+1
        else :
            if opt[i][j] == opt[i+1][j+1] :
                panalty[i] = 0
                newList[i] = y[j]
                i = i+1
                j = j+1
            elif opt[i][j] == opt[i+1][j+1] + 1 :
                panalty[i] = 1
                newList[i] = y[j]
                i = i+1
                j = j+1
    print(opt)
    print(x[0:n-1])
    print(newList)
    print(panalty)
    print("Sequence penalty score =",sum(panalty))

if __name__ == "__main__":

    f = open("sequence.txt",'r')

    indatas = f.readlines()

    f.close()

    x = list()
    y = list()

    #첫번째 줄의 시퀀스를 x에, 두번째 줄은 y에 저장 후 마지막에 각  '-'를 추가 
    for l in range(0,11) :
        if indatas[0][l] == '\n' :
            x.append('-')
            break
        else :
            x.append(indatas[0][l])

    for l in range(0,9) :
        if indatas[1][l] == '\n' :
            y.append('-')
            break
        else :
            y.append(indatas[1][l])

    print(x)
    print(y)
    matrix(x,y)
