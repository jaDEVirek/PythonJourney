import itertools

## Basic variables
suits = ["spades", "clubs","hearts","diamonds"]
ranks = ['A', 'J', 'Q', 'K']

ranks.extend([str(i).zfill(1) for i in range(2,11)])
cards = []


# print('Your card is: ' + rank + ' of ' + suit)

for result  in itertools.product(suits,ranks): print(result[0] + result[1])



# suits.append('snakes')

