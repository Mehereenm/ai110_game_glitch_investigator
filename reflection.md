# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first opened the game I saw a page with the title Game Glitch Investigator, which prompted me to "Guess a number between 1 and 100" and displays that there are 8 attempts left. There is a place the Enter my guess and then three options below that: submit guess, new game, and hint. when submitting a guess, if hint is enabled it shows either "Go HIGHER!" or "Go LOWER!" at the bottom and if the guess is correct ballons pop up on screen and a green bar at the bottom states "You already won. Start a new game to play again." 

  Bugs:
  1) The hints seem to be reversed? for example if the secret is 15 and the user inputs 10 it says "Go LOWER!". And if the input is a higher number such as 20 it says "Go HIGHER!" -> Hints do not work properly. Expectation: the appropriate hint is given t guide the user to the right answer
  2) New game does not reset the score! Expectation: score resets for each new game
  3) New game also does not reset the history, it continues to add on to the history from the last game(s). Expectation: History is reset after every game to only hold the values of the current game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
