import pytest
from game_of_life.hello import say_hello


@pytest.mark.parametrize("name", ["John", "Jane", "Jim"])
def test_say_hello(name: str):
    """Test that the say_hello function returns the expected greeting."""
    result = say_hello(name)
    assert result == f"Hello {name}!"
