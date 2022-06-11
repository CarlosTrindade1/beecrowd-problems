qtd = int(input())
if (qtd != 0):
    expression = input()
count = 1

while(qtd != 0):

    numbers = list(map(int, expression.replace('+', ' ').replace('-', ' ').split()))
    operators = []
    result = 0

    for i in range(len(expression)):
        if (expression[i] == '+'):
            operators.append('+')
        elif (expression[i] == '-'):
            operators.append('-')


    while(len(operators) > 0):
        
        if (operators[0] == '+'):
            result = numbers[0] + numbers[1]
        elif (operators[0] == '-'):
            result = numbers[0] - numbers[1]
        
        numbers[0] = result
        
        del(numbers[1])
        del(operators[0])
    
    print('Teste %i' %(count))
    print(result)
    print()

    count += 1

    qtd = int(input())

    if (qtd != 0):   
        expression = input()