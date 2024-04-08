# Python Clicker

This code is a simple "Cookie Clicker" game implemented in Python using the Pygame library. Here is a brief explanation:

1. Pygame initialization: Pygame is started in order to use its functions and resources to create the game interface.
2. Functions:
    - show_score(): This function displays the player's current score on the screen.
    - autosave(score): This function automatically saves the score to a text file named "saved_score.txt".
    - load_save_score(): This function loads the previously saved score from the file "saved_score.txt".
3. Main game function (main()):
    - Loads the saved score at the start of the game.Starts a main loop that executes the game.Within the loop, events are handled, such as clicking on the window to close the game or clicking on the "cookie" to increase the score.The "cookie" is displayed on the screen and the screen is refreshed.When the player closes the window, the game is over and Pygame closes.
    
The game consists of clicking on the "cookie" (represented by a red circle) to increase the score. The score is automatically saved and loaded each time the game is started.
