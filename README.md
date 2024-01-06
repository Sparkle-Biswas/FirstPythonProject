#
# CS 177 - Project3.py
# Sparkle Biswas
# Ruhani Sansoya
# Following CS 177 Coding Standards and Guidelines
#
# DESCRIPTION OF THE GAME
# In this game, the user has to guess a 5 letter word
# You get 10 wrong guesses, after that you lose the game
#
#
# We were required to add three compulsary features:
# 1) The HINT button. We created a hint button on the control panel which would only be functional went
#       the game panel is open. Once you click on the hint button, it will eliminate three random characters
#       but it will cost them two guesses as 2 Polygons from the Block P will fall.
# 2) The second feature is that at the end of each game, display an Entry box object in the GAME PANEL Graphics
#       window along with a label to prompt the user to enter their name. The player’s game statistics
#       (name, number of rounds and final score) should be added to the scores.txt datafile. The initial
#       file is provided with the Project 3 assignment on Blackboard and your program must support the file
#       in that format. No changes to the format of the scores.txt datafile are allowed.
# 3) The third feature we had to add was the high scores window. We modified the CONTROL PANEL Graphics window
#       to include a new Rectangle labeled HIGH SCORES. A click on this control opens a new Graphics window that
#       displays the top 7 scores from the scores.txt file in a “scrolling” animation.  When the HIGH SCORES
#       Graphics window is opened, it stays open until it is clicked.
#
# We were required to create three Custom Creative Features:
# 1) The first feature we created were the four themes. We made four buttons on the control panel. These buttons
#       are used to buy the theme as well as apply the themes to the game panel. A certain number of boilerbucks
#       (game currency) are mentioned on these buttons(ex: 100 BOILERBUCKS) and once you have the particular amount of boilerbucks
#       you can click on the button to buy it. You have to click on the bought theme button again to apply the theme to
#       the game panel. You can only use one theme for each round.You can apply the theme even in the middle of the round.
#       Even after losing a game you retain  the themes you have bought.
#       Each theme changes the background color of the game panel as well as the letter circles and golden rectangles 
#       after being clicked.if statements check for clicks on the theme button, allowing the player to buy only if they have enough
#       boilerbucks and allowing the application of the theme only if the game panel is open and none of the other themes have been
#       applied for that round.We have created graphics like icicles, fish, grass, clouds, etc. using for loops.
#       We have made winning and losing animations using loops and decision statments. Some animations include,icicles falling 
#       one by one,fish swimming across the window, balloons floating and poping, clouds moving and a sun moving into the screen,etc.
#       
# 2) The second feature we created is the boilerbucks.They can be considered the game's currency. 
#       We made a BOILERBUCKS button at the bottom of the control panel.The player starts with 50 boilerbucks. The player can
#       bet 5 boilerbucks in each round by clicking on the BOILERBUCKS button. This button can be clicked at the beginning of a
#       a round or during the game play however, you cannot click on the button after you have won/lost the round. If you win the
#       round after you bet 5 boilerbucks you win 10 X (length of the word) boilerbucks. Ex: If the secret word is HOME you can win
#       40 boilerbucks. You also win 2 boilerbucks after winning every round(even without betting) so that you don't run out of
#       boilerbucks. You will retain your boilerbucks even after you lose an entire game. You have to remember to click on the
#       BOILERBUCKS button for every round, you can click on it even after you have started guessing. This feature includes decision
#       statements to check for clicks. The amount of boilerbucks you currently have is shown on the BOILERBUCKS button and contiously
#       updated after winning and betting.
#
# 3) The third feature we made is the 'WHAT ARE BOILERBUCKS?' button on the control panel. On clicking this button it will open a new window.
#       This window gives instructions on how to use boilerbucks and is user-interactive. It asks the user to click on the window and
#       buttons to learn how to use the boilerbucks and how to spend them. There is a CLOSE button on the window at all times which can be
#       clicked anytime to close this window. This window also closes with all the other windows when the QUIT button on the control
#       panel is clicked. This feature uses decision statements to check for clicks on the window and accordingly draws and undraws graphic
#       objects. We suggest that the player click on this button before playing the game to get a better idea of how boilerbucks work.
#
#
