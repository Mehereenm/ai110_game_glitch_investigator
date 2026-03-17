from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_when_guess_lower_than_secret_str():
    # Test hint when secret is str and guess is lower (bug was hints reversed)
    outcome, message = check_guess(10, "15")
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message

def test_hint_when_guess_higher_than_secret_str():
    # Test hint when secret is str and guess is higher
    outcome, message = check_guess(20, "15")
    assert outcome == "Too High"
    assert "Go LOWER!" in message
