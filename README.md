# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game is a number-guessing challenge where the player tries to find a secret number within a limited number of attempts. However it had a bunch of bugs like incorrect hints, broken resets, and progress not being saved properly.

- [ ] Detail which bugs you found.
 Bugs:
  1) The hints seem to be reversed? for example if the secret is 15 and the user inputs 10 it says "Go LOWER!". And if the input is a higher number such as 20 it says "Go HIGHER!" -> Hints do not work properly. Expectation: the appropriate hint is given t guide the user to the right answer
  2) New game does not reset the score! Expectation: score resets for each new game
  3) New game also does not reset the history, it continues to add on to the history from the last game(s). Expectation: History is reset after every game to only hold the values of the current game
  
- [ ] Explain what fixes you applied.
  I fixed the hint logic in check_guess() so the messages now correctly guide the player (ex: a lower guess shows "Go HIGHER!"). I also ensured the secret number stays same across reruns by initializing it only once in st.session_state, and I reset the score and history so each new game starts fresh.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
