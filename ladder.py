import random

t = int(input())

# Function to get ladder and snake start and end position
def get_extremes(objs):
    start = [int(i.split(',')[0]) for i in objs]
    end = [int(i.split(',')[1]) for i in objs]
    return start, end


# Function to get Dice face number using cummulative probability concept
def get_die_number(die_probs, prob):
    pos = 0
    prob_cum = 0.
    while prob_cum < prob:
        prob_cum += die_probs[pos]
        pos += 1
    return pos if pos > 0 else 1


for _ in range(t):
    probs = list(map(float, input().split(',')))   # To get probability of each turn
    input()  # Ladder and Snake count

    ladders = input().split()
    ladder_start, ladder_end = get_extremes(ladders)    # To find ladder start and end position
    
    
    snakes = input().split()
    snake_start, snake_end = get_extremes(snakes)      # To find snake start and end position
    
    win_runs = []

    for i in range(5000):    # 5000 simulation
        runs = 0          # Run count 
        pos = 1           # Position count
        
        while runs < 1000 and pos != 100:
            
            runs += 1           # Increment  run count
            
            die_prob = random.uniform(0, 1)      # Obtaining probability between 0 and 1
            
            die_number = get_die_number(probs, die_prob)    # Get die number
            
            # Check if positon + die number is not greater then 100 
            if pos + die_number > 100:
                continue
                
            # Increasing position on chess board 
            pos += die_number
            
            # Check if positon is on ladder base
            if pos in ladder_start:
                index = ladder_start.index(pos)
                pos = ladder_end[index]  # Climb the ladder
              
            # Check if positon is on Snake mouth
            elif pos in snake_start:
                index = snake_start.index(pos)
                pos = snake_end[index]  # To snake's tail

        if pos == 100:
            win_runs.append(runs)       # Append win count number
            
    print(sum(win_runs) // len(win_runs))   # Average of the win numbers for these 5000 games
