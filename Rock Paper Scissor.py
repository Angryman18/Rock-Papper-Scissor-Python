import random

win_counter = lost_counter = tied_counter = round_counter = 0 # variable to calculate win, loss , tie
w = l = t = 0 # this will track the continous win or loss or tie

def flow(x, r, data, user, win_condition): # if continous win or loss or tie this will flow the program
    if x == 'win_flow':
        while True:
            r = random.choice(data)
            if (r, data[user-1]) not in win_condition:
                return r
    elif x == 'lost_flow':
        while True:
            r = random.choice(data)
            if (r, data[user-1]) in win_condition or (r == data[user-1]):
                return r
    elif x == 'tie_flow':
        while True:
            r = random.choice(data)
            if r != data[user-1]:
                return r

def percentage(counter):
    return f'{round((counter*100)/(win_counter+lost_counter+tied_counter), 2)}%'

def game():
    global win_counter, lost_counter, tied_counter, round_counter, w, t, l
    data = ['rock','paper','scissor']
    r = random.choice(data)
    win_condition = [('rock', 'paper'), ('paper', 'scissor'), ('scissor', 'rock')] # win condition

    try:
        user = int(input('Rock, Paper, Scissor? Type 1, 2, 3: '))
        while user > 3:
            print('Please Enter a Valid Input Between 1 to 3:')
            game()
    except:
        print('Please Enter a Valid Input Between 1 to 3:')
        game()

    if w == 3: # lets not user win or loss or tie for 3 continous times 
        w = 0
        r = flow('win_flow', r, data, user, win_condition)
    elif l == 3:
        l = 0
        r = flow('lost_flow', r, data, user, win_condition)
    elif t == 3:
        t = 0
        r = flow('tie_flow', r, data, user, win_condition)
    
    # we have restrict the tied flow between 26-33 otherwise it will stick close to 33-34
    if round_counter > 20 and round((tied_counter*100)/(win_counter+lost_counter+tied_counter), 2) > random.uniform(26,33):
        r = flow('tie_flow', r, data, user, win_condition)

    if (r, data[user-1]) in win_condition:
        win_counter += 1
        round_counter += 1
        print(f'\n\t*Congrats! You win!\n\tYou Choosed: {data[user-1]}, Computer Choosed: {r}\n\t[Rounds: {round_counter}], You won: {win_counter}, Computer won: {lost_counter}, Game Tied: {tied_counter}')
        w += 1
        t = l = 0

    elif r == data[user-1]:
        tied_counter += 1
        round_counter += 1
        print(f'\n\t-Game Tied-\n\tYou Choosed: {data[user-1]}, Computer Choosed: {r}\n\t[Rounds: {round_counter}], You won: {win_counter}, Computer won: {lost_counter}, Game Tied: {tied_counter}')
        t += 1
        w = l = 0

    else:
        lost_counter += 1
        round_counter += 1
        print(f'\n\tOps! You Lost!\n\tYou Choosed: {data[user-1]}, Computer Choosed: {r}\n\t[Rounds: {round_counter}], You won: {win_counter}, Computer won: {lost_counter}, Game Tied: {tied_counter}')
        l += 1
        w = t = 0

    pop_up = input('Want to play again? ')
    if type(pop_up) != int and pop_up.lower() in ('y', 'yes'):
        game()
    else:
        print(f'Win Rate: {percentage(win_counter)} \nLost Rate: {percentage(lost_counter)} \nTied Rate: {percentage(tied_counter)}')
        quit()
game()
