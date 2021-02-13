import random
import json
class Enemy():
    def __init__(self,health,attack,armor):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.death_phrase = "Аааа,сссука.."

class Seller():
    def __init__(self):
        with open("catalog.json") as f:
            self.catalog = json.load(f)

class Player():
    def __init__(self,health,attack,armor):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.potion = 3
        self.death_phrase = "Ну пиздааа,не заролял..."
        self.money = 0