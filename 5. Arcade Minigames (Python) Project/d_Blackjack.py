import random

# Deck Parameters
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
single_deck = 4 * cards
decks_used = 6
game_deck = []
deck_size = len(single_deck) * decks_used
player_account_bal = 0
bet = 0

# Default Player and Dealer Hand Parameters:
player_hand = []
dealer_hand = []
player_hand_value = 0
dealer_hand_value = 0

# Sets initial account balance
def set_account_bal():
    global player_account_bal
    while True: 
        try:
            initial_account_size = int(input( 'Please input your total chip amount! (Enter a value between 10000 and 100000)\n'))    
            if 10000 <= initial_account_size <= 100000:
                player_account_bal += initial_account_size
                print('\nSystem: You have a balance of ${}. Let\'s begin!\n'.format(player_account_bal))
                break
            else:
                print('\nError: Only amounts between 10000 and 100000 are accepted!\n')
        except ValueError:
            print('\nError: Please enter a valid integer!\n')

# Betting function
def place_bet():
    while True:
        try:
            bet_amount = int(input('Place your bet: (Enter a value between 0 and {}.)\n'.format(player_account_bal)))
            if 0 < bet_amount <= player_account_bal:
                return bet_amount
            else:
                print('\nError: Please enter a valid bet within your account balance!\n')
        except ValueError:
            print('\nError: Please enter a valid integer bet amount!\n')


# Shuffling current deck
def shuffle_deck(current_deck):
    random.shuffle(current_deck)

# Dealing hands from current deck
def deal(current_deck):
    for i in range(2):
        player_hand.append(current_deck.pop())
        dealer_hand.append(current_deck.pop())
        
    print("\nPlayer hand: ", player_hand)
    print("Dealer hand: ", [dealer_hand[0], 'Hidden'], '\n')

# Determining Card Values
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# Evaluate Hands - Algorithm to determine the highest possible hand, accounting for flexibility of Aces carrying 1 or 12
def evaluate_hand(hand):
    hand_value = 0
    aces_count = 0

    for card in hand:
        hand_value += card_value(card)
        if card == 'A':
            aces_count += 1

    possible_values = [hand_value]

    for i in range(aces_count):
        hand_value -= 10
        possible_values.append(hand_value)

    valid_values = [value for value in possible_values if value <= 21]

    return max(valid_values) if valid_values else min(possible_values)

# Player Turn: Hit - draws a card from the deck and adds it to the player's hand
def hit():
    player_hand.append(game_deck.pop())
    print('\nPlayer\'s Hand:', player_hand)

# Reveals the dealer's hidden card and draws until dealer has a score >= 17, the dealer then stands automatically
def reveal_dealer_hand():
    dealer_turn_text = '\n\033[4m\033[3mDealer\'s Turn\033[0m'
    print(dealer_turn_text)

    print("Dealer\'s hand: ", dealer_hand)
    dealer_hand_value = evaluate_hand(dealer_hand)
    print('The dealer\'s hand has a score of:', dealer_hand_value, '\n')

    while dealer_hand_value < 17 and player_hand_value <= 21 and len(player_hand) < 5:
        print('Dealer draws...')
        dealer_hand.append(game_deck.pop())
        print("Dealer hand: ", dealer_hand)
        dealer_hand_value = evaluate_hand(dealer_hand)
        print('The dealer\'s hand has a score of:', dealer_hand_value, '\n')

# Tabulates game results, accounting for various win/loss combinations and their wager multipliers
def game_results(): 
    global player_account_bal
    you_win = 'Congratulations, you win!\n'
    you_win_blackjack = 'Blackjack! You win!\n'
    you_lose = 'Sorry, you lose.\n'
    you_bust = 'You have busted. Sorry, you lose.\n'
    tie = 'It\'s a tie!\n'
    if len(player_hand) == 5 and player_hand_value < 21:
        player_account_bal += 2 * bet
        print(you_win)
    else:
        if player_hand_value > 21:
            print(you_bust)
        elif player_hand_value == 21 and len(player_hand) == 2 and dealer_hand_value != 21:
            player_account_bal += 2.5 * bet
            print(you_win_blackjack)
        elif player_hand_value == dealer_hand_value:
            player_account_bal += bet
            print(tie)
        elif dealer_hand_value > 21: 
            player_account_bal += 2 * bet
            print(you_win)
        elif player_hand_value < dealer_hand_value:
            print(you_lose)
        elif player_hand_value > dealer_hand_value:
            player_account_bal += 2 * bet
            print(you_win)
    
# Resets current hand and value
def reset_current_game():
    global player_hand, dealer_hand, player_hand_value, dealer_hand_value
    player_hand = []
    dealer_hand = []
    player_hand_value = 0
    dealer_hand_value = 0

# Checks if current deck has depleted to threshold for reset (set at 0.33 of the original deck's size)
def deck_count():
    global game_deck
    if len(game_deck) <= (0.33 * deck_size):
        print('\n', '-' * 25, 'Shuffling deck', '-' * 25, '\n')
        game_deck = single_deck * decks_used
        shuffle_deck(game_deck)

# Restarts the current game and deals for a new round - deck remains shuffled since initialisation
def restart_game():
    global player_hand, dealer_hand, player_hand_value, dealer_hand_value
    reset_current_game()
    deal(game_deck)

    player_hand_value = evaluate_hand(player_hand)
    print('Your hand has a score of:', player_hand_value, '\n') 

    while player_hand_value < 21 and len(player_hand) < 5: #Player turn - Hit or Stand if player hand has a value of less than 21 and less than 5 cards
            player_turn_text = '\033[4m\033[3mPlayer\'s Turn\033[0m'
            print(player_turn_text)
            action = input('Would you like to hit or stand? (hit / stand)\n')
            if action.lower() == 'hit':
                hit()
                player_hand_value = evaluate_hand(player_hand)
                print('Your hand has a score of:', player_hand_value, '\n') 
            elif action.lower() == 'stand':
                break
            else:
                print('\nPlease try again. (hit / stand)\n')
    
    reveal_dealer_hand()

    dealer_hand_value = evaluate_hand(dealer_hand)
    player_hand_value = evaluate_hand(player_hand) # Re-evaluates hands for generating results
    
    game_results()
    deck_count()


# Game flow
def main(): 
    global game_deck, deck_size, player_account_bal, bet
    print('\nLet\'s play blackjack!\n')
    
    set_account_bal()
            
    game_deck = single_deck * decks_used
    shuffle_deck(game_deck)
    
    while True:
        if player_account_bal > 0:
            bet = place_bet()
            player_account_bal -= bet

            restart_game()

            print('Your account balance is ${}.\n'.format(player_account_bal))

            while True:
                choice = input('Another round? (yes / no)\n') 
                if choice.lower() == 'yes':
                    print('\n', '-' * 25, 'New Round', '-' * 25, '\n')
                    print('Your account balance is ${}.\n'.format(player_account_bal))
                    break
                elif choice.lower() == 'no':
                    print('\nThank you for playing!')
                    return
                elif choice.lower() not in ['yes', 'no']:
                    print('Please try again!\n')
        else: 
            set_account_bal()
