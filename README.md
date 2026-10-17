# 🎮 Hangman Game in Python - CodeAlpha intership project
# Made by Samarth B.tech AIML 2nd year
## 📌 Project Description

Hangman is a simple, text-based word-guessing game developed using Python. In this game, the computer randomly selects a word from a predefined list, and the player must guess the word one letter at a time.

The player gets a maximum of 6 incorrect guesses to identify the secret word. The game ends when the player guesses the word correctly or runs out of attempts.

This project demonstrates basic Python programming concepts, including loops, conditional statements, lists, strings, user input, and the "random" module.

## ✨ Features

- 🎯 Random selection of a secret word.
- 🔤 Guess the word one letter at a time.
- ❤️ Maximum of 6 incorrect guesses.
- 📝 Displays the current word with hidden letters.
- 📋 Tracks previously guessed letters.
- ✅ Validates user input.
- 🚫 Prevents duplicate guesses.
- 🏆 Displays a winning message when the word is guessed correctly.
- ❌ Reveals the secret word if the player loses.

## 🛠️ Technologies Used

- Programming Language: Python
- Module: "random"
- Concepts: Loops, conditional statements, lists, strings, functions, and input validation.

## 📂 Project Structure

Hangman-Game/
│
├── hangman.py       # Main Python game file
└── README.md        # Project documentation

## 🚀 Getting Started

Prerequisites

Install Python 3 on your computer.

Check your Python installation by running:

python --version

Installation

1. Clone this repository:
   
   git clone <your-repository-url>

2. Navigate to the project directory:
   
   cd Hangman-Game

3. Run the Python file:
   
   python hangman.py
   
   If your system uses "python3", run:
   
   python3 hangman.py

## 🎮 How to Play

1. Run the program.
2. The computer randomly selects a secret word.
3. Enter one letter when prompted.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses reduce your remaining attempts.
6. Avoid guessing the same letter more than once.
7. Guess all the letters before you run out of attempts to win!

Example Gameplay

=== Welcome to Hangman! ===

Word: _ _ _ _ _ _
Incorrect guesses remaining: 6
Guessed letters: None
Guess a letter: p

Good job! 'p' is in the word.

Word: p _ _ _ _ _
Incorrect guesses remaining: 6
Guessed letters: p
Guess a letter: z

Sorry, 'z' is not in the word.

Note: The displayed word and gameplay depend on the randomly selected secret word.

## 📚 Learning Outcomes

Through this project, I learned how to:

- Use Python's "random.choice()" function.
- Work with lists and strings.
- Implement "while" loops and "for" loops.
- Apply "if-else" conditions.
- Accept and validate user input.
- Track game progress using variables and lists.
- Implement win and loss conditions.

## 🔮 Future Improvements

- Add more words and different difficulty levels.
- Display a visual hangman after incorrect guesses.
- Allow players to restart the game.
- Add score tracking.
- Provide hints to help players guess the word.

## 👨‍💻 Author

Samarth
B.Tech — 2nd Year
Artificial Intelligence and Machine Learning (AIML)

## 🏢 Internship

Code Alpha Internship

This project was created as part of my learning and development journey in Python programming.

## 📄 License

This project is intended for educational and learning purposes. You may modify and improve it for personal practice.
