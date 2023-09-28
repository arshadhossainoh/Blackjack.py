import random
playerIn = True
dealerIn = True
# deck of cards
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'j','Q','K','A','j','Q','K','A','j','Q','K','A','j','Q','K','A']
playerHand = []
dealerHand = []

# deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if card == 'A' and total > 11:
                total += 1
            else:
                total += 11
    return total


# check the winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


# game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f'dealer has {revealDealerHand()} and X')
    print(f'player has {playerHand} for a total of {playerHand}')
    if playerIn:
        stayorHit = input("1:stay or 2:hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)

    if stayorHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"player has {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand}for a total of {total(dealerHand)}")
    print("Blackjack! you win")