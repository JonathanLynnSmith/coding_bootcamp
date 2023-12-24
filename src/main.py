import random
import os

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Function to create a deck of cards
def create_deck():
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    return deck

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            value += 11
            num_aces += 1
        else:
            value += int(rank)

    # Adjust for Aces if needed
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Function to display the player's and dealer's hands
def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    print("\nYour hand:")
    for card in player_hand:
        print(f"  {card[0]} of {card[1]}")
    print(f"Total Value: {calculate_hand_value(player_hand)}")

    print("\nDealer's hand:")
    if reveal_dealer:
        for card in dealer_hand:
            print(f"  {card[0]} of {card[1]}")
        print(f"Total Value: {calculate_hand_value(dealer_hand)}")
    else:
        print(f"  {dealer_hand[0][0]} of {dealer_hand[0][1]}")
        print("  [Hidden Card]")

# Function to check if the player or dealer has blackjack
def has_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to play Blackjack
def play_blackjack():
    while True:
        # Create and shuffle the deck
        deck = create_deck()
        shuffle_deck(deck)

        # Deal initial cards
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Check for player or dealer blackjack
        if has_blackjack(player_hand) or has_blackjack(dealer_hand):
            display_hands(player_hand, dealer_hand, reveal_dealer=True)
            if has_blackjack(player_hand) and has_blackjack(dealer_hand):
                print("It's a tie! Both you and the dealer have Blackjack.")
            elif has_blackjack(player_hand):
                print("Congratulations! You have Blackjack and win.")
            else:
                print("The dealer has Blackjack. You lose.")
            break  # End the game

        # Player's turn
        while calculate_hand_value(player_hand) < 21:
            clear_console()
            display_hands(player_hand, dealer_hand)
            action = input("Do you want to hit or stand? ").lower()
            if action == 'hit':
                player_hand.append(deck.pop())
            elif action == 'stand':
                break
            else:
                print("\nInvalid entry. Please enter 'hit' or 'stand'.")
                input("Press Enter to continue...")
                clear_console()

        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        # Display final hands
        clear_console()
        display_hands(player_hand, dealer_hand, reveal_dealer=True)

        # Determine the winner
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
            print("\nSORRY, YOU LOSE.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("\nYOU WIN!!!")

        # Ask if the player wants to play again
        play_again = input("\nType 'exit' to quit the app, or press Enter to play again: ").lower()
        if play_again == 'exit':
            break  # End the game
        elif play_again != '':
            print("\nInvalid entry. Press Enter to play again.")
        else:
            clear_console()
            # Reset hands and deck for a new game
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]

# Example: Play Blackjack
play_blackjack()
