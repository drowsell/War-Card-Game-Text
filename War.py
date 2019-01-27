# War Card Game
# Dylan Rowsell
# Jan 31, 2018

from random import randint

# List of suits and Special Cards

cardSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
specialCards = ["King", "Queen", "Jack", "Ace"]

# Variable for suit

suitAssign = -1

# List where cards will go.

cards = []

# Each Player's deck.

players = 2
playerOneDeck = []
playerTwoDeck = []
whichDeck = [playerOneDeck, playerTwoDeck]

#playerOneCard = []
#playerTwoCard = []
#whoseCard = [playerOneCard, playerTwoCard]

print("Welcome to WAR.")
print("The text based card game!")
print("How fun!")

for suits in cardSuits:
  
  suitAssign += 1
  cardNumber = 1
  cardName = -1
  
  for numberedCards in range(9):
    cardNumber += 1
    cards.insert(0, (str(cardNumber) + " of " + str(cardSuits[suitAssign])))
  
  for nonNumberdCards in specialCards:
    cardName += 1
    cards.insert(0, (str(specialCards[cardName]) + " of " + str(cardSuits[suitAssign])))
    

#print(cards) # should have all cards
#print(len(cards)) # should be 52

#Sorts the cards into two player decks.

for deckSorting in range(players):
  players -= 1
  if players >= 0:
    for decks in range(26):
      sortedCard = cards[randint(0, (len(cards)-1))]
      whichDeck[players].insert(0, sortedCard)
      cards.remove(sortedCard)
      
#print (len(playerOneDeck)) # should be 26

# The actual game.
# Should keep going until the players are out of cards. 

while len(playerOneDeck) > 0 or len(playerTwoDeck) > 0:

  playerOneCard = (playerOneDeck[randint(0,(len(playerOneDeck)-1))])
  
  answer = 0

  # Ask the player if he wants to redraw.
  # Loop until the player answers yes or no.
  
  while answer == 0:
    answer = input("You pulled up the " + playerOneCard + ". Do you want to re-draw?\n Yes/No :").lower().strip(" !@#$%^&*(),.")
    if answer == "no":
      break
    elif answer == "yes":
      playerOneCard = (playerOneDeck[randint(0,(len(playerOneDeck)-1))])
      print("p1 You drew a " + playerOneCard + ".")
      break
    else:
      print("Invalid input.")
      answer = 0
    
  # Save the name of the card.
  
  playerOneCardName = playerOneCard
  
  # Player two's card is selected
  
  playerTwoCard = (playerTwoDeck[randint(0,(len(playerTwoDeck)-1))])
  print("Player 2 drew a " + playerTwoCard + ".")
  playerTwoCardName = playerTwoCard
  # Find Value of Player One's Card.
  
  if "Ace" in playerOneCard:
    playerOneCard = 14
  elif "King" in playerOneCard:
    playerOneCard = 13
  elif "Queen" in playerOneCard:
    playerOneCard = 12
  elif "Jack" in playerOneCard:
    playerOneCard = 11
  else:
    cardNumber = 10
      
    for number in range(cardNumber):
      cardNumber -= 1
      if str(cardNumber) in str(playerOneCard):
        playerOneCard = cardNumber
      
#  print("player one card value " + str(playerOneCard))

# Find Value of player Two's Card.
  
  if "Ace" in playerTwoCard:
    playerTwoCard = 14
  elif "King" in playerTwoCard:
    playerTwoCard = 13
  elif "Queen" in playerTwoCard:
    playerTwoCard = 12
  elif "Jack" in playerTwoCard:
    playerTwoCard = 11
  else:
    cardNumber = 10
      
    for number in range(cardNumber):
      cardNumber -= 1
      if str(cardNumber) in str(playerTwoCard):
        playerTwoCard = cardNumber
      
#  print("player two card vale " + str(playerTwoCard))


  # If player two's card is less than player one's he will redraw

  if playerOneCard >= playerTwoCard:
    playerTwoCard = (playerTwoDeck[randint(0,(len(playerTwoDeck)-1))]) 
    playerTwoCardName = playerTwoCard
    
    if "Ace" in playerTwoCard:
      playerTwoCard = 14
    elif "King" in playerTwoCard:
      playerTwoCard = 13
    elif "Queen" in playerTwoCard:
      playerTwoCard = 12
    elif "Jack" in playerTwoCard:
      playerTwoCard = 11
    else:
      cardNumber = 10
        
      for number in range(cardNumber):
        cardNumber -= 1
        if str(cardNumber) in str(playerTwoCard):
          playerTwoCard = cardNumber
    
    
    # Whine.
    if playerOneCard > playerTwoCard:
      print("Player 2: I redrew a " + playerTwoCardName + "...")
    
    # Gloat.
    elif playerOneCard < playerTwoCard:
      print("Player 2: Ahaha, I redrew a " + playerTwoCardName + ".")
    
  if playerOneCard > playerTwoCard:
    print("You won!")
    playerOneDeck.insert(randint(0,(len(playerOneDeck)-1)), playerTwoCardName)
    playerTwoDeck.remove(playerTwoCardName)
  elif playerOneCard < playerTwoCard:
    print("You lost!")
    playerTwoDeck.insert(randint(0,(len(playerTwoDeck)-1)), playerOneCardName)
    playerOneDeck.remove(playerOneCardName)
  elif playerOneCard < playerTwoCard:
    print("You tied!")
  
  print("Player 1 deck size: " + str(len(playerOneDeck)))
  print("Player 2 deck size: " + str(len(playerTwoDeck)))




