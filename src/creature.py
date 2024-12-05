# Mythical Creature class
# Represents a creature in a creature encounter with a name, health points, attack damage, and rewards to be dropped
class Creature:
    """
    Represents a creature in a mythical creature encounter with a name, health points, attack damage, and rewards to be dropped.
    
    Attributes:
        name (str): The name of the creature
        healthPoints (int): The health points of the creature
        attack (int): The attack damage of the creature
        rewards (str): The rewards to be dropped by the creature upon death
    """

    def __init__(self, name, healthPoints, attack, rewards):
        """
        Initializes the Creature object with the given attribute

        Args:
            name (str): The name of the creature
            healthPoints (int): The initial health points of the creature
            attack (int): The attack damage of the creature
            rewards (str): The rewards the creature will drop
        """
        self.name = name
        self.healthPoints = healthPoints
        self.attack = attack
        self.rewards = rewards

    def __str__(self):
        """
        Returns a string representation of the creature, including name, health, attack, and rewards

        Returns:
            str: String representation of the creature
        """
        return f"{self.name} \nHealth: {self.healthPoints} \nAttack Damage: {self.attack} \nRewards to be dropped: {self.rewards}"

    def __repr__(self):
        """
        Returns a detailed string representation of the creature for debugging

        Returns:
            str: Detailed string representation of the creature
        """
        return f"Creature Name: {self.name} \nHealth Points: {self.healthPoints} \nAttack: {self.attack} \nRewards: {self.rewards}"

    def getName(self):
        """
        Returns the name of the creature

        Returns:
            str: The name of the creature
        """
        return self.name
    
    def getHealthPoints(self):
        """
        Returns the health points of the creature

        Returns:
            int: The health points of the creature
        """
        return self.healthPoints
    
    def getAttack(self):
        """
        Returns the attack damage of the creature

        Returns:
            int: The attack damage of the creature
        """
        return self.attack
    
    def getRewards(self):
        """
        Returns the rewards to be dropped by the creature

        Returns:
            str: The rewards to be dropped
        """
        return self.rewards
    
    def damage(self, damage):
        """
        Applies damage to the creature, reducing its health points

        Args:
            damage (int): The amount of damage to be applied

        Raises:
            ValueError: If the damage is less than or equal to 0

        Returns:
            int: The updated health points of the creature
        """
        if damage <= 0:
            raise ValueError("Damage must be greater than 0")
        self.healthPoints -= damage

        if self.healthPoints <= 0:
            print(f"{self.name} has died!")
            print(f"{self.name} has dropped {self.rewards}")
            self.healthPoints = 0
            return
        print(f"{self.name} took {damage} damage!")
    
    def heal(self, amount):
        """
        Heals the creature increasing its health points

        Args:
            amount (int): The amount to heal

        Raises:
            ValueError: If the heal amount is less than or equal to 0

        Returns:
            int: The updated health points of the creature
        """
        if self.healthPoints <= 0:
            raise ValueError("Cannot heal a dead mythical creature")
        if amount <= 0:
            raise ValueError("Heal amount must be greater than 0")
        self.healthPoints += amount
        print(f"{self.name} healed for {amount} health!")

