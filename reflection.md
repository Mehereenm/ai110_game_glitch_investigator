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

I used GitHub Copilot as my AI tool for this project

One correct AI suggestion was when Copilot helped identify and fix the reversed hints bug in the "check_guess" function and suggested swapping the hint messages so that "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!" (since it was reversed before). I verified the result by running the Streamlit app, and guessing numbers below and above the secret to confirm that the hints properly reflected the secret and guided the player towards the correct answer. For example, guessing 10 when the secret is 15 showed "Go HIGHER!", and guessing 20 showed "Go LOWER!"

One incorrect or misleading AI suggestion occurred when Copilot suggested tests that didn’t match what the function actually returns. It checked for a single value like "Win", but the function returns two things (outcome, message), not just a string. This caused test failures that didn't reflect the actual code behavior. I verified this by running the existing tests, which failed with assertion errors, and then corrected the tests to check both outcome and message.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I did both manual playtesting and automated testing to figure out if it was fixed. For the hint reversal, I ran the Streamlit app, guessed numbers above and below a given secret from the Developer Debug Info section, and confirmed that the hint text now correctly guides me toward the secret.

One pytest test I ran was test_hint_when_guess_lower_than_secret_str, which asserts that when the secret is passed as a string (an edge case caused by the app’s logic) and the guess is lower, the function returns "Too Low" and the message includes "Go HIGHER!". The test passed after the fix, confirming the hint logic works correctly even when the secret is a string.

AI helped me design the tests by suggesting the exact edge case to cover (secret stored as a string on even attempts) and how to assert both the outcome and the hint message, which made the test more precise and reliable.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because the app restarted every time you interacted with it. Each time it restarted, it picked a new random number instead of keeping the same one. Since it didn’t save the number anywhere, every click or input reset it, making it hard to win.

Imagine the app is like a video game level that restarts from scratch every time you press a button or type something, that's a "rerun," where all the code runs again. Session state is like a save file that remembers important data (like your score or the secret number) between these restarts, so the game feels continuous instead of resetting everything. (When I was trying to understand it, the AI helped me understand with a example like this, which I found really helpful so I would also explain it using video games as an exmaple)

The change I made to give the game a stable secret number was adding a check if "secret" not in st.session_state before setting it to a random value. This ensures that it's only generated once per game session instead of after every click!

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Just getting comfotable working along side AI as a partner. Keeping in mind the phrase "work smarter not harder", AI is now everywhere so it's better getting comfortable in using it to help me understand and tackle problems rather than being stranger with it.

One thing I would do differently is the way I ask it questions, for example giving it details and contexts on what my code is doing wrong verses what it should be doing. It gives the AI a better guideline of what I want to achieve.

It shows that AI can be used as a partner in writing or understanding code
