import pytest

def test_initial_values(sample_Creature):
    """Test initialization of creature attributes"""
    creature = sample_Creature
    assert creature.get_name() == "Dragon"
    assert creature.get_health_points() == 100
    assert creature.get_attack() == 20
    assert creature.get_rewards() == "Golden Treasure"

def test_damage(sample_Creature):
    """Test damage method reduces health correctly"""
    creature = sample_Creature
    creature.damage(10)
    assert creature.get_health_points() == 90

def test_damage_invalid(sample_Creature):
    """Test damage method raises ValueError for invalid input"""
    creature = sample_Creature
    with pytest.raises(ValueError):
        creature.damage(0)

def test_creature_death(sample_Creature):
    """Test creature death behavior when health goes to zero"""
    creature = sample_Creature
    creature.damage(100)
    assert creature.get_health_points() == 0

def test_heal(sample_Creature):
    """Test heal method increases health correctly"""
    creature = sample_Creature
    creature.heal(10)
    assert creature.get_health_points() == 110

def test_heal_invalid(sample_Creature):
    """Test heal method raises ValueError for invalid input"""
    creature = sample_Creature
    with pytest.raises(ValueError):
        creature.heal(-10)

def test_str_representation(sample_Creature):
    """Test the __str__ method for proper formatting"""
    creature = sample_Creature
    assert str(creature) == 
    "Dragon \nHealth: 100 \nAttack Damage: 20 \nRewards to be dropped: Golden Treasure"

def test_repr_representation(sample_Creature):
    """Test the __repr__ method for debugging representation."""
    creature = sample_Creature
    assert repr(creature) == 
    "Creature Name: Dragon \nHealth Points: 100 \nAttack: 20 \nRewards: Golden Treasure"

def test_heal_after_death(sample_Creature):
    """Ensure healing doesn't revive a dead creature"""
    creature = sample_Creature
    creature.damage(100)
    with pytest.raises(ValueError, match="Cannot heal a dead mythical creature"):
        creature.heal(10)