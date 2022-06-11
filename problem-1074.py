N = int(input())

for i in range(N):
    msg = ''
    number = int(input())

    if (number % 2 == 0 and number != 0):
        msg += ' EVEN'
    elif (number != 0):
        msg += 'ODD'
    else:
        msg += ' NULL'
    
    if (number > 0):
        msg += ' POSITIVE'
    elif (number != 0):
        msg += ' NEGATIVE'
    
    print(msg.strip())
