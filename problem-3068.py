farm = list(map(int, input().split()))
qtd = int(input())

countTest = 1

while(farm[0] != 0 and farm[1] != 0 and farm[2] != 0 and farm[3 != 0]):
    count = 0

    for i in range(qtd):
        coordsMeteor = list(map(int, input().split()))
        
        if (
            farm[0] <= coordsMeteor[0] and coordsMeteor[0] <= farm[2] and
            farm[3] <= coordsMeteor[1] and coordsMeteor[1] <= farm[1]
        ):
            count += 1
    
    print('Teste %i' %(countTest))
    print(count)

    countTest += 1

    farm = list(map(int, input().split()))
    if (farm[0] != 0 and farm[1] != 0 and farm[2] != 0 and farm[3] != 0):
        qtd = int(input())


    
