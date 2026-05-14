# Password Guessing Game

A simple Python terminal game where the player guesses a secret password based on difficulty level.

## Features

- Easy, Medium, and Hard difficulty modes
- Random password generation
- Hint system
- Attempt counter
- Beginner-friendly Python project

---

## Technologies Used

- Python
- Random module

---

## How to Run

1. Clone the repository

```bash
git clone <your-repo-link>
```

2. Open the project folder

```bash
cd password-guessing-game
```

3. Run the program

```bash
python main.py
```

---

## Game Rules

- Choose a difficulty level:
  - easy
  - medium
  - hard

- Guess the hidden password.
- After every wrong guess, you receive a hint:
  - Correct letters in the correct position are shown
  - Wrong letters are replaced with `_`

Example:

```text
Secret Word: python
Your Guess: pexxxx

Hint: p_____
```

---

## Example Gameplay

```text
Welcome to the password guessing game.
Choose a difficulty level: easy, medium, hard

Enter difficulty level: medium

Guess the secret password

Enter your guess: bottle
Hint: __tt__

Enter your guess: python
Congratulations! You guessed it in 2 attempts.
```

---

## Project Structure

```text
password-guessing-game/
│
├── main.py
└── README.md
```

---

## Future Improvements

- Add score system
- Add timer
- Add multiplayer mode
- Store high scores
- GUI version using Tkinter or PyQt
- Difficulty-based attempt limits