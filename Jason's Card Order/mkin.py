#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(10)
    print("Command Tower")
    print("Plains")
    print("War Room")
    print("Evolving Wilds")
    print("Swamp")
    print("Badlands")
    print("Forest")
    print("Island")
    print("Exotic Orchard")
    print("Command Tower")
elif case_num == 1:
    print(10)
    print("War Room")
    print("Exotic Orchard")
    print("Plains")
    print("Island")
    print("Command Tower")
    print("Command Tower")
    print("Evolving Wilds")
    print("Forest")
    print("Badlands")
    print("Swamp")
else:
    # output what should be read in as input by
    # contestant code
    duplicate = ["command tower", "sol ring", "arcane signet"]
    cardList = ["Rakdos Signet", "Ignoble Hierarch", "Assassin's Trophy", "Boros Charm", "Dovin's Veto"
                , "Anguished Unmaking", "Terminate", "Growth Spiral", "Despark", "Izzet Signet"
                , "Dimir Signet", "Orzhov Signet", "Azorius Signet", "Boros Signet", "Talisman of Dominance"
                , "Talisman of Hierarchy", "Talisman of Indulgence", "Talisman of Conviction", "Rhythm of the Wild", "Aura Shards"]
    n = randint(10, 20)
    j = randint(0, 2)
    r1 = randint(0, n//2 - 1)
    r2 = randint(n//2, n - 1)
    print(n)
    i = 0
    while i < n:
        if(i == r1 or i == r2):
            print(duplicate[j])
        else:
            print(cardList[i])
        i += 1
