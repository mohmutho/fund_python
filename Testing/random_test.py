import random

def run_guess(guess, answer):
    if 0 < guess < 6:
        if guess == answer:
            print('yor\'re a genius!')
            return True
    else:
        print('hei bodoh, I said 1 ~ 5')
        return False
if __name__ == '__main__':      
    answer = random.randint(1, 5)
    while True:
        try:
            guess = int(input('guess a number 1 ~ 5 : '))
            if run_guess(guess, answer) == True:
                break
        except ValueError:
            print('please enter a number')
            continue