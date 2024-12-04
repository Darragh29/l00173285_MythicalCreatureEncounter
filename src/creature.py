# Mythical Creature class
# Represents a creature in a creature encounter with a name, health points, biome, rewards
class Creature:
    def __init__(self, name, health_points, attack, rewards):
        self.name = name
        self.health_points = health_points
        self.attack = attack
        self.rewards = rewards

    def __str__(self):
        return f"Creature Name: {self.name} \nHealth Points: {self.health_points} \nBiome: {self.attack} \nRewards: {self.rewards}"

    def __repr__(self):
        return f"Creature Name: {self.name} \nHealth Points: {self.health_points} \nBiome: {self.attack} \nRewards: {self.rewards}"