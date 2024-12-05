import pytest
from creature import Creature

@pytest.fixture
def sample_Creature():
    """Fixture for creating a sample Creature object"""
    return Creature("Dragon", 100, 20, "Golden Treasure")