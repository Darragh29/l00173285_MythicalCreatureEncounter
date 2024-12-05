import pytest
from creature import Creature

def testInitialValues(sample_Creature):
    """Test initialization of creature attributes"""
    creature = sample_Creature
    assert creature.getName() == "Dragon"
    assert creature.getHealthPoints() == 100
    assert creature.getAttack() == 20
    assert creature.getRewards() == "Golden Treasure"

def testDamage(sample_Creature):
    """Test damage method reduces health correctly"""
    creature = sample_Creature
    creature.damage(10)
    assert creature.getHealthPoints() == 90

def testDamageInvalid(sample_Creature):
    """Test damage method raises ValueError for invalid input"""
    creature = sample_Creature
    with pytest.raises(ValueError):
        creature.damage(0)

def testCreatureDeath(sample_Creature):
    """Test creature death behavior when health goes to zero"""
    creature = sample_Creature
    creature.damage(100)
    assert creature.getHealthPoints() == 0

def testHeal(sample_Creature):
    """Test heal method increases health correctly"""
    creature = sample_Creature
    creature.heal(10)
    assert creature.getHealthPoints() == 110

def testHealInvalid(sample_Creature):
    """Test heal method raises ValueError for invalid input"""
    creature = sample_Creature
    with pytest.raises(ValueError):
        creature.heal(-10)

def testStrRepresentation(sample_Creature):
    """Test the __str__ method for proper formatting"""
    creature = sample_Creature
    assert str(creature) == "Dragon \nHealth: 100 \nAttack Damage: 20 \nRewards to be dropped: Golden Treasure"

def testReprRepresentation(sample_Creature):
    """Test the __repr__ method for debugging representation."""
    creature = sample_Creature
    assert repr(creature) == "Creature Name: Dragon \nHealth Points: 100 \nAttack: 20 \nRewards: Golden Treasure"

def testHealAfterDeath(sample_Creature):
    """Ensure healing doesn't revive a dead creature"""
    creature = sample_Creature
    creature.damage(100)
    
    with pytest.raises(ValueError, match="Cannot heal a dead mythical creature"):
        creature.heal(10)

