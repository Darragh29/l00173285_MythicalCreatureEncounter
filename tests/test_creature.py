import pytest
from creature import Creature

@pytest.fixture
def sampleCreature():
    """Fixture for creating a sample Creature object"""
    return Creature("Dragon", 100, 20, "Golden Treasure")

def testInitialValues(sampleCreature):
    """Test initialization of creature attributes"""
    assert sampleCreature.getName() == "Dragon"
    assert sampleCreature.getHealthPoints() == 100
    assert sampleCreature.getAttack() == 20
    assert sampleCreature.getRewards() == "Golden Treasure"

def testDamage(sampleCreature):
    """Test damage method reduces health correctly"""
    sampleCreature.damage(10)
    assert sampleCreature.getHealthPoints() == 90

def testDamageInvalid(sampleCreature):
    """Test damage method raises ValueError for invalid input"""
    with pytest.raises(ValueError):
        sampleCreature.damage(0)

def testCreatureDeath(sampleCreature):
    """Test creature death behavior when health goes to zero"""
    sampleCreature.damage(100)
    assert sampleCreature.getHealthPoints() == 0

def testHeal(sampleCreature):
    """Test heal method increases health correctly"""
    sampleCreature.heal(10)
    assert sampleCreature.getHealthPoints() == 110

def testHealInvalid(sampleCreature):
    """Test heal method raises ValueError for invalid input"""
    with pytest.raises(ValueError):
        sampleCreature.heal(-10)

def testStrRepresentation(sampleCreature):
    """Test the __str__ method for proper formatting"""
    assert str(sampleCreature) == "Dragon \nHealth: 100 \nAttack Damage: 20 \nRewards to be dropped: Golden Treasure"

def testReprRepresentation(sampleCreature):
    """Test the __repr__ method for debugging representation."""
    assert repr(sampleCreature) == "Creature Name: Dragon \nHealth Points: 100 \nAttack: 20 \nRewards: Golden Treasure"

def testHealAfterDeath(sampleCreature):
    """Ensure healing doesn't revive a dead creature"""
    sampleCreature.damage(100)
    
    with pytest.raises(ValueError, match="Cannot heal a dead mythical creature"):
        sampleCreature.heal(10)

