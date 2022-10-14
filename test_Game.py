from Game import your
from Game import computer
from Game import logic
from Game import game

def test_your():
    pass

def test_computer():
    assert(computer() == "paper" or computer() == "scissor" or computer() == "rock")

def test_logic():
    assert(logic("scissor", "scissor") == 0)
    assert(logic("scissor", "paper") == 1)
    assert(logic("scissor", "rock") == 0)

    assert(logic("paper", "scissor") == 0)
    assert(logic("paper", "paper") == 0)
    assert(logic("paper", "rock") == 1)

    assert(logic("rock", "scissor") == 1)
    assert(logic("rock", "paper") == 0)
    assert(logic("rock", "rock") == 0)


def test_game():
    pass