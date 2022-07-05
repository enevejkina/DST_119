import numpy as np

number = np.random.randint(1, 101) #guess the number
count = 0
while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100 "))
    if predict_number > number:
        print ('The number should be less')
    elif predict_number < number:
        print ('The number should be bigger')
    else:
        print (f'You are right! This number is {number}, the number of tries is {count}')
        break