import numpy as np
def random_predict(number:int=1) -> int:
    """Random guess of number

    Args:
        number (int, optional): Secret number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #supposed number
        if number == predict_number:
            break # quit the game
    return (count)
print (f'Number of tries:{random_predict()}') 

def score_game(random_predict) -> int:
    """Mean number of tries for 1000 iterations

    Args:
        random_predict ([type]): function of guessing

    Returns:
        int: mean number of tries
    """
    count_ls = [] #list for fixing number of tries
    np.random.seed (1) # fix the seed 
    random_array = np.random.randint(1, 101, size=(1000)) # we guess the list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) #calculate the mean number of tries
    print (f'Your algorithm guesses the number for {score} tries')
    return (score)

if __name__ == '__main__':
    score_game(random_predict)
