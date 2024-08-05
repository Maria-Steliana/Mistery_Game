# Mystery Game: The Mystery of Wilton Manor

## Overview

**The Mystery of Wilton Manor** is an interactive, puzzle-based mystery game built using PyQt6. The game immerses players in a detective story where they need to solve various puzzles to progress through the narrative. The story unfolds across different windows, each representing a new challenge or part of the plot. The game incorporates a timer, and incorrect answers or timeouts lead to different outcomes, adding an element of suspense and urgency to the gameplay.

## Features

- **Interactive Story**: Progress through the game by solving puzzles and uncovering the mystery.
- **Puzzle Challenges**: Each game window presents a different type of puzzle to solve.
- **Timer**: Each puzzle has a time limit, adding to the challenge.
- **Dynamic Storyline**: The game’s narrative evolves based on your actions and puzzle-solving skills.
- **Customizable Content**: All texts, images, and stories are configured through a JSON file, allowing for easy updates and customization.

## Project Structure

Mystery_Game/
│
├── config.json # Configuration file for texts, images, and storylines
├── images/ # Directory containing all game-related images
│   └── (all image files)
├── ui/ # Directory containing .ui files for all the windows
│   └── (all UI files)
├── windows/ # Directory containing Python files for each window in the game
│   └── (individual window files)
├── main.py # Entry point of the application
└── README.md 


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11 installed on your system.
- PyQt6 installed. You can install it via pip:
- open GUI interface in terminal via:

  ```sh
  pip install PyQt6
  pyqt6-tools designer

How to Play

Starting the Game:

Launch the game by running main.py. The main window will appear with the title "The Mystery of Wilton Manor".
Click the "Start" button to begin the game.

Navigating the Game:

Each window presents a part of the story along with a puzzle that you need to solve to progress.
Read the story, solve the puzzle, and interact with the game through the buttons provided.

Timer and Challenges:

Each puzzle has a timer, so think quickly! If you answer incorrectly or time runs out, you'll face different consequences.

Progressing Through the Story:

The story unfolds based on your interactions. Keep solving puzzles to reveal more about the mystery of Wilton Manor.

Customization:

You can easily customize the game's content by editing the config/config.json file. Update the text, story, and image paths to suit your needs.

**IMPORTANT** 

For main.py // main_window.py // first_game_window.py:

- explanations for each line codes are provided to better understand the logic behind;
- for other windows, explanations are provided for the new lines;
- the rest of windows are the same.
