cases = input()
i = 0
cardDictionary = {}
while i < cases:
    card = input()
    if card in cardDictionary:
        print(card)
        break
    cardDictionary[card] = True