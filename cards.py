import random

class Player(object):
	"""Creates a player character"""
	def __init__(self, name):
		self.name = name
		self.hand = []
	
	#Gets player name
	def get_name(self):
		return self.name
	
	#Gets player hand
	def get_hand(self):
		return self.hand
		
	#Adds card to player hand
	def add_card(self, card):
		if card is not None:
			self.hand.append(card)
		
	#Plays/discards/burns a card from player hand
	def play_card(self, card):
		c = card
		crd = self.hand[c]
		if c <= len(self.hand) and c >= 0:
			self.hand.remove(crd)
			return crd
		else:
			print("Not in hand.")



class Table(object):
	"""Creates a play table"""
	def __init__(self):
		self.players = {}
		self.discard_pile = {}
		self.discard_pile["Table"] = []
		self.burn_pile = []
	
	#Gets players
	def get_players(self):
		return self.players
	
	#Sets player
	def set_player(self, player):
		nmbr = len(self.players) + 1
		self.players[nmbr] = player
	
	#Gets cards in play/discard pile
	def get_discard(self):
		return self.discard_pile
		
	#Gets cards in burn pile
	def get_burn(self):
		return self.burn_pile
	
	#Plays/discards a card
	def discard(self, player, card):
		p = self.players[player]
		name = p.get_name()
		if name in self.discard_pile:
			self.discard_pile[name].append(card)
		else:
			self.discard_pile[name] = [card]
	
	#Burns a card (Removes from play)
	def burn_card(self, card):
		if card is not None:
			self.burn_pile.append(card)
		else:
			print("No cards")



class Deck(object):
	"""Creates a deck of playing cards"""
	def __init__(self, cards):
		self.cards = cards
		
	#Gets number of cards in deck
	def how_many(self):
		return len(self.cards)
	
	#Gets cards in the deck
	def get_deck(self):
			return self.cards
	
	#Shuffles the deck
	def shuffle(self):
		random.shuffle(self.cards)
	
	#Draws a card from the top of the deck
	def draw_card(self):
		if len(self.cards) > 0:
			return self.cards.pop(0)
		else:
			print("No cards in deck")
	
	#Deals hand(s) from deck
	def deal(self, players, num_cards):
		if num_cards > 0:
			deal_count = num_cards * len(players)
			deal_step = 1
			while deal_count > 0:
				if len(self.cards) > 0:
					players[deal_step].hand.append(self.cards.pop(0))
					deal_count -= 1
					if deal_step < len(players):
						deal_step += 1
					else:
						deal_step = 1
				else:
					print("Not enough cards")
					break
		else:
			print("No cards dealt.")
				


class Card(object):
	"""Creates a playing card"""
	def __init__(self, card):
		self.card = card
		self.face = False
	
	#Gets the card
	def get_card(self):
		if self.face == True:
			return self.card
		else:
			return "Face-down"
	
	#Checks if the card is face-up
	def face_up(self):
		return self.face
		
	#Flips the  card over
	def flip_card(self):
		self.face = not self.face



#Generates a list of card objects
def gen_deck(card_list):
	cards = []
	for c in card_list:
		cards.append(Card(c))
	return Deck(cards)

#Adds player to table
def add_player(table, player):
	table.set_player(Player(player))

#Shows player name
def show_name(table, player):
	plrs = table.get_players()
	if p in plrs:
		print(plrs[p].get_name())
	else:
		print("No player")

#Flips a card in deck
def flip_deck(deck, card):
	d = deck.get_deck()
	c = card - 1
	if card > 0 and card <= len(d):
		d[c].flip_card()
	else:
		print("Out of range")

#Flips all cards in deck
def check_deck(deck):
	d = deck.get_deck()
	i = 1
	for c in d:
		flip_deck(deck, i)
		i += 1

#Shows a card in deck
def show_deck(deck, card):
	d = deck.get_deck()
	c = card - 1
	if card > 0 and card <= len(d):
		print(d[c].get_card())
	else:
		print("Out of range")

#Shows all cards in deck
def print_deck(deck):
	d = deck.get_deck()
	i = 1
	for c in d:
		show_deck(deck, i)
		i += 1

#Deals a deck of cards
def deal_cards(table, deck, num_cards):
	players = table.get_players()
	deck.deal(players, num_cards)

#Flips a card in player hand
def flip_hand(table, player, card):
	p = table.get_players()
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		if card > 0 and card <= len(h):
			c = h[card - 1]
			c.flip_card()
		else:
			print("Out of range")
	else:
		print("Not a player")
		
#Flips all cards in player hand
def check_hand(table, player):
	p = table.get_players()
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		for c in h:
			c.flip_card()
	else:
		print("Not a player")

#Shows a card in player hand
def show_hand(table, player, card):
	p = table.get_players()
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		if card > 0 and card <= len(h):
			print(h[card - 1].get_card())
		else:
			print("Out of range")
	else:
		print("Not a player")

#Shows all cards in player hand
def print_hand(table, player):
	p = table.get_players()
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		for c in h:
			print(c.get_card())
	else:
		print("Not a player")
	
#Plays/Discards from deck
def play_deck(table, deck):
	name_key = "Table"
	table.discard(name_key, deck.draw_card())

#Burns a card from deck
def burn_deck(table, deck):
	table.burn_card(deck.draw_card())
	
#Draws a card from the deck
def draw_deck(table, player):
	p = table.get_players()
	if player > 0 and player <= len(p):
		table.players[player].add_card(deck.draw_card())
	else:
		print("Not a player")

#Plays a card from player hand
def play_hand(table, player, card):
	p = table.get_players()
	c = card - 1
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		if card > 0 and card <= len(h):
			table.discard(player, p[player].play_card(c))
		else:
			print("Out of range")
	else:
		print("Not a player")

#Burns a card from player hand
def burn_hand(table, player, card):
	p = table.get_players()
	if player > 0 and player <= len(p):
		h = p[player].get_hand()
		if card > 0 and card <= len(h):
			c = card - 1
			table.burn_card(p[player].play_card(c))
		else:
			print("Not in range")
	else:
		print("Not a player")
	
	
	
#Create a play table
table = Table()

#Add players
player1 = "Luke"
#player2 = "Jeff"
#player3 = "Jen"

add_player(table, player1)
#add_player(table, player2)
#add_player(table, player3)

#Show player name
#player = 1
#show_name(table, player)

#Build list of cards
card_list = []
nmbrs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["S", "H", "C", "D"]
for n in nmbrs:
		for s in suits:
			card_list.append(n+s)
	
#Create a deck of cards
deck = gen_deck(card_list)

#Shuffle the deck
#deck.shuffle()

#List number of cards in deck
#print(deck.how_many())

#Flip card in deck
#card = 52
#flip_deck(deck, card)

#Flip all cards in deck
#check_deck(deck)

#List card in deck
#card = 1
#show_deck(deck, card)

#List all cards in deck
#print_deck(deck)

#Deal
num_cards = 5
deal_cards(table, deck, num_cards)

#Flip card in player hand
#player = 1
#card = 52
#flip_hand(table, player, card)

#Flip all cards in player hand
player = 1
check_hand(table, player)

#Show card in player hand
#player = 1
#card = 3
#show_hand(table, player, card)

#Show all cards in player hand
player = 1
print_hand(table, player)

#Play/discard from deck
#play_deck(table, deck)

#Burn from deck
#burn_deck(table, deck)

#Draw from deck
#player_number = 1
#draw_deck(table, player_number)

#Play/discard from hand
#player = 1
#card = 1
#play_hand(table, player, card)

#Burn from hand
#player = 1
#card = 2
#burn_hand(table, player, card)
