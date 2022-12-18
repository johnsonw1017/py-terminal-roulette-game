# roulette - Python Terminal Application Documentation
## Introduction
This application simulates the classic casino of Roulette. The game involves betting chips on board with numbers ranging from 0 to 36. The player can choose to bet on a single number or a group of numbers. Each round, the roulette wheel spins and a number is selected (0 to 36). If you have betted on the selected number, you will receive a payout of chips. The purpose of this application is for people to enjoy this game without any monetary commitment. The terminal application was developed on Python version 3.9.6. The code structure follows the Model-View_Controller (MVC) pattern where:

- Model: storage of the game state in variables of different data structures
- Controller: update of the game state through the use of created functions
- View: player's viewpoint of the game which involves the prompts and messages shown to the players.

## Installation Guide
In order to access the source code and perform other development activities, please download Python 3 using this [guide](https://wsvincent.com/install-python/).

### Installing on MacOS
Since this application was developed on MacOS, the created roulette.exe file can only be executed on MacOS.

1. Download the zip file from the roulette [repository](https://github.com/johnsonw1017/roulette), by clicking on the green "Code" button then "Download ZIP.
2. Once the folder is unzipped, ctrl-click on the roulette Unix Executable file then click "Open". The game should open in default terminal on the computer.

### Installing on Windows

1. Download the zip file from the roulette [repository](https://github.com/johnsonw1017/roulette), by clicking on the green "Code" button then "Download ZIP.
2. Once the folder is unzipped, the roulette.py can be converted to an executable file on cmd by following this [guide](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/).
3. Open the created .exe file.

## Features
### 1. Game Loop
This feature relates to the function main_loop() which runs the View section of the game (i.e. what the player see). This involves regulating the player interactions like providing the gameplay prompts and responding to the player inputs. The game is broken down into the following phases:

- **Introduction**: welcomes the player to the game, shows the roulette board and provide the key user commands for game support.
- **Betting stage**: in this phase, the players would be prompted with 2 questions, what position would they like to bet their chips and how many chip they like to place at the position they selected. These prompts would be played on a loop until the player enters the command "done", then the wheel spin stage begins.
- **Wheel spin stage**: a number is randomly selected between 0 and 36 and displayed on the player's screen. Functions (the "Controller") would then calculate the total winnings the player receives and update the game state variables (Model), the players would be informed on the result of their chip stack after the spin.
- **End of game**: the betting stage and the wheel spin stage would play on a loop until either one of two conditions, the player decide to quit or they run out of chips. A message would be played to thank the player for playing the game.

### 2. Betting Phase


### 3. Wheel Spin Phase


### 4. Game Support


## Implementation Plan - Feature Checklists
### 1. Game Loop


### 2. Betting Phase


### 3. Wheel Spin Phase


### 4. Game Support
