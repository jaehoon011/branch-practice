for i in range(1, 16):
    # Implementation of fizzbuzz
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
