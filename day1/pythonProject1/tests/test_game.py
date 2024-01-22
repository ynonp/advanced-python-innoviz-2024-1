from day3.number_guessing_game import NumberGuessingGame
import io

def test_too_small():
    output = io.StringIO()
    input_iterator = iter([30, 50])
    game = NumberGuessingGame(lambda a, b: 50,
                              lambda prompt: next(input_iterator),
                              output.write)
    game.main()
    assert output.getvalue() == "too small. try againBravo! That's the one"

def test_too_large():
    output = io.StringIO()
    input_iterator = iter([80, 50])
    game = NumberGuessingGame(lambda a, b: 50,
                              lambda prompt: next(input_iterator),
                              output.write)
    game.main()
    assert output.getvalue() == "too large. try againBravo! That's the one"


def test_exact():
    output = io.StringIO()
    input_iterator = iter([50])
    game = NumberGuessingGame(lambda a, b: 50,
                              lambda prompt: next(input_iterator),
                              output.write)
    game.main()
    assert output.getvalue() == "Bravo! That's the one"


def test_long_time_to_guess():
    output = io.StringIO()
    input_iterator = iter([30, 30, 30, 30, 30, 30, 30, 30, 50])
    game = NumberGuessingGame(lambda a, b: 50,
                              lambda prompt: next(input_iterator),
                              output.write)
    game.main()
    assert output.getvalue().endswith("Bravo! That's the one")
    assert output.getvalue().startswith("too small. try again")