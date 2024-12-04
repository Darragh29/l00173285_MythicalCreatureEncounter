# Mythical Creature class
# Represents a creature in a creature encounter with a name, health points, attack damage, and rewards to be dropped
class Creature:
    def __init__(self, name, healthPoints, attack, rewards):
        self.name = name
        self.healthPoints = healthPoints
        self.attack = attack
        self.rewards = rewards

    def __str__(self):
        return f"{self.name} \nHealth: {self.healthPoints} \nAttack Damage: {self.attack} \nRewards to be dropped: {self.rewards}"

    def __repr__(self):
        return f"Creature Name: {self.name} \nHealth Points: {self.healthPoints} \nAttack: {self.attack} \nRewards: {self.rewards}"
    
    def damage(self, damage):
        if damage <= 0:
            raise ValueError("Damage must be greater than 0")
        self.healthPoints -= damage

        if self.healthPoints <= 0:
            print(f"{self.name} has died!")
            print(f"{self.name} has dropped {self.rewards}")
            return
        print(f"{self.name} took {damage} damage!")
    
    def heal(self, amount):
        if amount <= 0:
            raise ValueError("Heal amount must be greater than 0")
        self.health_points += amount
        print(f"{self.name} healed for {amount} health!")