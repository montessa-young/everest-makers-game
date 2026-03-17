class Character:
    def __init__(self, Creature: str, Color: str, Strength: int, Weakness: str, Height:int, Health:int):
        self.Creature = Creature
        self.Color = Color
        self.Strength = Strength
        self.Weakness = Weakness
        self.Height = Height
        self.Health = Health

    def __repr__(self):
        return f"Character(Creature={self.Creature}, Color= {self.Color}, Strength = {self.Strength}, Weakness = {self.Weakness}, Height = {self.Height}, Health = {self.Health})"


# a small roster of snakes the player can choose from
AVAILABLE_CHARACTERS = [{
    "Creature": "Bigfoot",
    "Color": "Brown",
    "Strength": 50,
    "Weakness": "Cheese",
    "Height": 15,
    "Health": 150
},

{
    "Creature": "Yeti",
    "Color": "White",
    "Strength": 100 ,
    "Weakness": "Impatience",
    "Height": 15,
    "Health": 150
},
{
    "Creature": "Sled dogs",
    "Color": "black and white",
    "Strength": 40,
    "Weakness": "fish",
    "Height": 10,
    "Health": 2000
},
{
    "Creature": "Lloyd Christmas",
    "Color": "Tan",
    "Strength": 5,
    "Weakness": "Intellegience",
    "Height": 8,
    "Health": 100
},
{
    "Creature": "Lara Croft",
    "Color": "Black",
    "Strength": 20,
    "Weakness": "Human mortality",
    "Height": 8,
    "Health": 100
},
{
    "Creature": "Ice Minotuar",
    "Color": "Gray and White",
    "Strength": 60,
    "weakness": "Color Red",
    "Height": 15,
    "Health": 200
},
{
    "Creature": "Dragon",
    "Color": "Striking Red",
    "Strength": 200,
    "Weakness": "Fire Sword",
    "Height": 15,
    "Health": 200
},
{
    "Creature": "Python Snake",
    "Color": "Yellow",
    "Strength": 140,
    "Weakness": "Smoke Grenade",
    "Height": 15,
    "Health": 200
},
{
    "Creature": "Vampire",
    "Color": "Dark Grey",
    "Strength": 160,
    "Weakness": "Wooden Cross",
    "Height": 15,
    "Health": 200
}
]







