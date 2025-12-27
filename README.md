# 🎯 Number Guessing Game (Python)

An interactive **Number Guessing Game** built using Python. The program randomly generates a number between **1 and 100**, and the player must guess the number using logical hints provided after each attempt.

This project is ideal for **Python beginners** to understand loops, conditionals, user input, and basic game logic.

---

## ✨ Features

* Random number generation using Python's `random` module
* Interactive command-line gameplay
* Smart hints to guide the player (higher/lower)
* Tracks total number of attempts
* Simple, clean, and beginner-friendly code

---

## 🧠 How the Game Works

1. The program generates a random number between **1 and 100**.
2. The user is prompted to guess the number.
3. After each guess:

   * If the guess is **too high**, the program asks for a smaller number.
   * If the guess is **too low**, the program asks for a greater number.
4. The game continues until the correct number is guessed.
5. Once guessed correctly, the program displays:

   * The correct number
   * Total number of attempts taken

---

## 🗂️ Project Structure

```
number-guessing-game/
│
├── main.py        # Core game logic
└── README.md      # Project documentation
```

---

## ▶️ How to Run the Program

### Prerequisites

* Python **3.x** installed on your system

### Steps

1. Clone this repository:

   ```bash
   git clone <your-repository-link>
   ```

2. Navigate to the project directory:

   ```bash
   cd number-guessing-game
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## 🕹️ Sample Output

```
Guess a number: 50
Guess a smaller number

Guess a number: 25
Guess a greater number

Guess a number: 34
You guessed 34 correctly in 3 attempts
```

---

## 📘 Concepts Used

* `random.randint()` for number generation
* `while` loop for continuous guessing
* Conditional statements (`if`, `elif`)
* User input handling
* Basic counters and variables

---

## 🚀 Future Enhancements

* Input validation for non-numeric values
* Difficulty levels (Easy / Medium / Hard)
* Scoreboard or best-attempt tracking
* Replay option without restarting the program
* GUI version using Tkinter or PyGame

---

## 🤝 Contributing

Contributions are welcome. Feel free to:

* Fork the repository
* Create a new branch
* Submit a pull request

---

## 📜 License

This project is open-source and intended for **educational purposes**.

---

### ⭐ If you like this project, consider giving it a star on GitHub!

Happy Coding 🚀
