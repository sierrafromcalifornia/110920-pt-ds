import numpy as np
np.random.seed(2021)

def flip(prob = [.5, .5]):
    return np.random.choice(['HEADS', 'TAILS'], p=prob)
    
def roll(number=6):
    return np.random.choice(list(range(1, number+1)))
    
    
    
class DrawAMarble():
    
    def __init__(self, replace=False):
        self.replace = replace
        self.marbles = ['yellow', 'yellow', 'green', 'green','blue', 'blue', 'red']
        self.draw_count = 0
    
    def draw(self):
        marble = np.random.choice(self.marbles)
        self.draw_count += 1
        self.marbles[self.draw_count] = marble
        if not self.replace:
            self.marbles.remove(marble)
            
        return marble
            